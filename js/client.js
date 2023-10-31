const movableBlock = document.querySelector('.movable-block');
let isMoving = false;

movableBlock.addEventListener('mousedown', (event) => {
    isMoving = true;
    const offsetX = event.clientX - movableBlock.getBoundingClientRect().left;
    const offsetY = event.clientY - movableBlock.getBoundingClientRect().top;

    document.addEventListener('mousemove', moveBlock);

    document.addEventListener('mouseup', () => {
        isMoving = false;
        document.removeEventListener('mousemove', moveBlock);
    });

    function moveBlock(event) {
        if (isMoving) {
            movableBlock.style.left = event.clientX - offsetX + 'px';
            movableBlock.style.top = event.clientY - offsetY + 'px';
        }
    }
});
