$(document).ready(function() {
    $('.card').each(function() {
        const $currentCard = $(this);
        let hiddenInputValue = $currentCard.find('input[type="hidden"]').val();

        switch (hiddenInputValue) {
        case 'Electrónicos o Digitales':
            $currentCard.addClass('text-white bg-primary');
            break;
        case 'Narrativa':
            $currentCard.addClass('text-white bg-secondary');
            break;
        case 'Poesía':
            $currentCard.addClass('text-white bg-success');
            break;
        case 'Dramaturgia':
            $currentCard.addClass('text-white bg-danger');
            break;
        case 'Ensayo':
            $currentCard.addClass('text-white bg-warning');
            break;
        case 'No-Ficción':
            $currentCard.addClass('text-white bg-info');
            break;
        case 'Diccionario/Enciclopedia':
            $currentCard.addClass('bg-light');
            break;
        case 'Glosario':
            $currentCard.addClass('text-white bg-dark');
            break;
        case 'Atlas/Mapas':
            $currentCard.addClass('border-primary');
            break;
        case 'Gran Formato':
            $currentCard.addClass('border-secondary');
            break;
        case 'Cómics, libros álbum y novelas gráficas':
            $currentCard.addClass('border-success');
            break;
        case 'Ciencia y tecnología':
            $currentCard.addClass('border-danger');
            break;
        case 'Historia':
            $currentCard.addClass('border-warning');
            break;
        case 'Biografías y Memorias':
            $currentCard.addClass('border-info');
            break;
        case 'Libros de texto':
            $currentCard.addClass('border-light');
            break;
        case 'Libros técnicos o especializados':
            $currentCard.addClass('border-dark');
            break;
        case 'Manuales y libros prácticos':
            $currentCard.addClass('text-white border-primary');
            break;
        case 'Autoayuda':
            $currentCard.addClass('text-white border-secondary');
            break;
        case 'Religiosos o sagrados':
            $currentCard.addClass('text-white border-success');
            break;
        case 'Libros infantiles':
            $currentCard.addClass('text-white border-danger');
            break;
        default:
            $currentCard.addClass('text-white bg-primary border-primary');
        }
    });
});