document.addEventListener('DOMContentLoaded', function () {
    const paginationLinks = document.querySelectorAll('.pagination-link');
    const coursesContainer = document.getElementById('courses-container');

    paginationLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const page = this.dataset.page;

            fetch(`?page=${page}`, {
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(data => {
                const parser = new DOMParser();
                const htmlDoc = parser.parseFromString(data, 'text/html');
                const newCourses = htmlDoc.querySelector('#courses-container').innerHTML;
                const newPagination = htmlDoc.querySelector('#pagination').innerHTML;

                coursesContainer.innerHTML = newCourses;
                document.getElementById('pagination').innerHTML = newPagination;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});
