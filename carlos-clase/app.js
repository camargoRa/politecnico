import mongoose from 'mongoose';
import express from 'express';
import dotenv from 'dotenv';
import Estudiante from './models/estudiante.js';
dotenv.config({ override: true });

const app = express();
const PORT = process.env.PORT || 4000;

app.use(express.json());

async function conectarMongo() {
    try {
        await mongoose.connect(process.env.MONGO_URI);
        console.log('Conexion exitosa a Mongodb');
    } catch (err) {
        console.error('Error al conectarse:', err.message);
    }
}
conectarMongo();

app.get('/', (req, res) => {
    res.send('Servidor Atlas funcionando correctamente');
});

app.post('/registro', async (req, res) => {
    try {
        console.log('POST recibido en /registro con body:', req.body);
        const nuevoEstudiante = new Estudiante(req.body);
        const resultado = await nuevoEstudiante.save()

        res.status(201).json({
            mensaje: "Estudiante registrado correctamente",
            estudiante: resultado
        });

    } catch (err) {
        res.status(500).send('Error al registrar: ' + err.message);
    }
});

app.get('/listar', async (req,res) => {
    try {
        const lista = await Estudiante.find();
        res.json(lista);
    } catch (err) {
        res.status(500).send('Error Al listar ' + err.message)
    }
});
app.delete('/eliminar/:id', async (req, res) => {
    try{
        const eliminado = await Estudiante.findByIdAndDelete(req.params.id);
        if (!eliminado) return res.status(404).json({mensaje: 'Estudiante no encontrado'});
        res.json({mensaje: 'Estudiante eliminado correctamente'})
    } catch (err){
        res.status(500).json({mensaje: 'Error al eliminar', err})
    }
})

app.put('/actualizar/:id', async (req, res) => {
    try {
        const { id } = req.params;   // ← el ID viene de la URL
        const { nombre, edad, ciudad } = req.body;

        const actualizado = await Estudiante.findByIdAndUpdate(
            id,
            { nombre, edad, ciudad },
            { new: true } // devuelve los datos actualizados
        );

        if (!actualizado) {
            return res.status(404).json({ mensaje: 'Estudiante no encontrado' });
        }

        res.json({
            mensaje: "Estudiante actualizado correctamente",
            estudiante: actualizado
        });

    } catch (error) {
        res.status(500).json({ mensaje: 'Error al actualizar', error: error.message });
    }
});

app.get('/buscar/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const buscar = await Estudiante.findById(id);
        if (!buscar){
            return res.status(400).json({mensaje: 'EStudiante no encontrado'});
        }
        res.json({
            mensaje: "Estudiante Encontrado Correctamente",
            estudiante : buscar
        })
    } catch (error) {
    res.status(500).json({ mensaje: 'Error al actualizar', error: error.message });
    }
}) ;

app.listen(PORT, () => {
    console.log(`Servidor corriendo en puerto http://localhost:${PORT}`);
});
