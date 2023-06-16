
//fungsi buat upload and

function uploadFiles() {
    var files = document.getElementById('file_upload').files;
    if(files.length==0){
        alert("Please first choose or drop any file(s)...");
        return;
    }
    var filenames="";
    for(var i=0;i<files.length;i++){
        filenames+=files[i].name+"\n";
    }
    alert("Selected file(s) :\n____________________\n"+filenames);
}
