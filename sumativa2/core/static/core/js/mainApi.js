async function mostrarPosters(elementoHTML) {
    const options = {
        method: 'GET',
        headers: {
            accept: 'application/json',
            Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNTA1MzE4MTZkMWU1ZGY0OGMzZWNlMzMwNTQ1MzM0NSIsInN1YiI6IjY2MjkxOWRmMTc2YTk0MDE3ZjgzNjM3MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.VLTYur3Ut34FSJWM_JmQigT2z72C_le5acTHO2d717Q'
        }
    };

    try {
        const response = await fetch('https://api.themoviedb.org/3/movie/popular?language=en-US&page=1', options);

        if (!response.ok) {
            throw new Error("Error al consumir la API:", response.status);
        }

        const datos = await response.json();

        let html = "";
        for (const pelicula of datos.results) {
            const titulo = pelicula.title;
            const imagen = pelicula.poster_path ? `https://image.tmdb.org/t/p/w300${pelicula.poster_path}` : "imagen-no-disponible.jpg";

            html += `
                <div class="col-3 gap-10 ">
                    <div class="col">
                        <img src="${imagen}" class="card-img-top" alt="${titulo}">
                    </div>
                    <div class="">
                        <div class="card-body  text-center">
                            <h5 class="card-title"> ${titulo}</h5>
                        </div>
                    </div>
                </div>
            `;
        }

        elementoHTML.innerHTML = html;
    } catch (error) {
        console.error("Error al obtener los datos:", error);
    }
}

mostrarPosters(document.getElementById('postersMovies'));


