function startjs() {
    inpform();
}


function inpform() {
    
    function xdate(x) {
        var date = $("#id_date_"+x).val();
        regex = new RegExp("^([0-9]{2})\\.([0-9]{2})\\.([1-2][0-9]{3})$");


        if(date === 'NaN.NaN.NaN' || date === '') { 
            date = ''
        } else {
            if(regex.test(date) === false){
                var date = new Date(date);    
                const option = { year: 'numeric', month: 'numeric', day: 'numeric' }        
                date = date.toLocaleDateString(undefined, option);                
            }else{
                pass
            }
        }
        return date;
    }
    
    $("#id_date_birt").val(xdate('birt'));
    $("#id_date_deat").val(xdate('deat'));
    $("#id_date_fune").val(xdate('fune'));
   
}
