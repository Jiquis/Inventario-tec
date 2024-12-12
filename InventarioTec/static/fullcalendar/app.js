//var modal = new bootstrap.Modal(document.getElementById("newissuemodal"));

document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      headerToolbar: {
        left: "prev, next, today",
        center: "title",
        right: "dayGridMonth, timeGridWeek, listWeek"
      },
      events: [
        {% for issue in issues %}
         {
            title: "{{issue.tarea_name}}",
            start: "{{issue.tarea_btime | date: 'Y-m-d'}}",
            end: "{{issue.tarea_etime | date: 'Y-m-d'}}",
          },
        {% endfor%}
      ]
    });
    calendar.render();
  });