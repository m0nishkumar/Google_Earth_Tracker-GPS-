<!DOCTYPE html>
<html>
      
<head>
    <title>
        How to call PHP function
        on the click of a Button ?
    </title>
</head>
  
<body style="text-align:center;">
      
  
    <?php

        if(isset($_POST['button1'])) {
            $command = escapeshellcmd('python osrunning.py');
            $output = shell_exec($command);
        }

    ?>
      
    <form method="post">
        <input type="submit" name="button1"
                value="LocationTracker"/>
          
    </form>
</head>
  
</html>