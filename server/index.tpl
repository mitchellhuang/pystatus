<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>PyStatus</title>
    <style media="screen" type="text/css">
    body {
        margin: 35px 0px;
        padding: 0px;
        text-align: center;
        background-color: #FFFFFF;
        font-family: Helvetica, Arial, sans-serif;
    }
    #wrapper {
        width: 500px;
        height: 100%;
        margin: 0px auto;
        text-align: left;
    }
    .main {
        margin-top: 10px;
        margin-bottom: 10px;
        padding: 10px;
        border-style: groove;
        border-width: 1px;
        width: 100%;
        height: 100px;
    }
    .load {
        float: left;
    }
    .info {
        float: right;
        width: 90%;
    }

    </style>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js" type="text/javascript"></script>
    <script type="text/javascript">
    $(document).ready(function() {
        %for client in clients:
        $.getJSON("/status/{{client}}", function(data) {
            $("#{{client}} .info .hostname").html(data.hostname);
            $("#{{client}} .load").html("<img src='check.gif' alt='done' />");
        });
        %end
    });
    </script>
</head>
<body>
    <div id="logo">PyStatus 1.0</div>
    <div id="wrapper">
        %for client in clients:
        <div id="{{client}}" class="main">
            <div class="load">
                <img src="/load.gif" alt="loading" />
            </div>
            <div class="info">
                <div class="hostname">
                    Loading...
                </div>
            </div>
        </div>
        <p></p>
        %end
    </div>
</body>
</html>