<!DOCTYPE html>
<html>
<head>
	<title>Results</title>
	<link rel="stylesheet" type="text/css" href="bootstrap.css">
	<link rel="stylesheet" type="text/css" href="style.css">

	<?php
		$clf = $_GET['classifier'];
		$t = $_GET['t'];
		$o = $_GET['o'];
		$l = $_GET['l'];

		$tw_viral_file = file($clf. "/twitter_viral_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$tw_popular_file = file($clf . "/twitter_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$tw_viral_and_popular_file = file($clf. "/twitter_viral_and_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);

		$yt_viral_file = file($clf. "/youtube_viral_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$yt_popular_file = file($clf. "/youtube_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$yt_viral_and_popular_file = file($clf. "/youtube_viral_and_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);

		$bo_viral_file = file($clf. "/both_viral_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$bo_popular_file = file($clf. "/both_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$bo_viral_and_popular_file = file($clf. "/both_viral_and_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);

		$twitter_viral_all_old	= explode("\t",$tw_viral_file[0]);
		$twitter_viral_baseline_old = explode("\t",$tw_viral_file[1]);
		$twitter_viral_all_recent	= explode("\t",$tw_viral_file[2]);
		$twitter_viral_baseline_recent	 = explode("\t",$tw_viral_file[3]);
		$twitter_viral_f1_score = explode("\t",$tw_viral_file[4]);

		$twitter_popular_all_old	= explode("\t",$tw_popular_file[0]);
		$twitter_popular_baseline_old = explode("\t",$tw_popular_file[1]);
		$twitter_popular_all_recent	= explode("\t",$tw_popular_file[2]);
		$twitter_popular_baseline_recent	 = explode("\t",$tw_popular_file[3]);
		$twitter_popular_f1_score = explode("\t",$tw_popular_file[4]);

		$twitter_viral_and_popular_all_old	= explode("\t",$tw_viral_and_popular_file[0]);
		$twitter_viral_and_popular_baseline_old = explode("\t",$tw_viral_and_popular_file[1]);
		$twitter_viral_and_popular_all_recent	= explode("\t",$tw_viral_and_popular_file[2]);
		$twitter_viral_and_popular_baseline_recent	 = explode("\t",$tw_viral_and_popular_file[3]);
		$twitter_viral_and_popular_f1_score = explode("\t",$tw_viral_and_popular_file[4]);

		$youtube_viral_all_old	= explode("\t",$yt_viral_file[0]);
		$youtube_viral_baseline_old = explode("\t",$yt_viral_file[1]);
		$youtube_viral_all_recent	= explode("\t",$yt_viral_file[2]);
		$youtube_viral_baseline_recent	 = explode("\t",$yt_viral_file[3]);
		$youtube_viral_f1_score = explode("\t",$yt_viral_file[4]);

		$youtube_popular_all_old	= explode("\t",$yt_popular_file[0]);
		$youtube_popular_baseline_old = explode("\t",$yt_popular_file[1]);
		$youtube_popular_all_recent	= explode("\t",$yt_popular_file[2]);
		$youtube_popular_baseline_recent	 = explode("\t",$yt_popular_file[3]);
		$youtube_popular_f1_score = explode("\t",$yt_popular_file[4]);

		$youtube_viral_and_popular_all_old	= explode("\t",$yt_viral_and_popular_file[0]);
		$youtube_viral_and_popular_baseline_old = explode("\t",$yt_viral_and_popular_file[1]);
		$youtube_viral_and_popular_all_recent	= explode("\t",$yt_viral_and_popular_file[2]);
		$youtube_viral_and_popular_baseline_recent	 = explode("\t",$yt_viral_and_popular_file[3]);
		$youtube_viral_and_popular_f1_score = explode("\t",$yt_viral_and_popular_file[4]);

		$both_viral_all_old	= explode("\t",$bo_viral_file[0]);
		$both_viral_baseline_old = explode("\t",$bo_viral_file[1]);
		$both_viral_all_recent	= explode("\t",$bo_viral_file[2]);
		$both_viral_baseline_recent	 = explode("\t",$bo_viral_file[3]);
		$both_viral_f1_score = explode("\t",$bo_viral_file[4]);

		$both_popular_all_old	= explode("\t",$bo_popular_file[0]);
		$both_popular_baseline_old = explode("\t",$bo_popular_file[1]);
		$both_popular_all_recent	= explode("\t",$bo_popular_file[2]);
		$both_popular_baseline_recent	 = explode("\t",$bo_popular_file[3]);
		$both_popular_f1_score = explode("\t",$bo_popular_file[4]);

		$both_viral_and_popular_all_old	= explode("\t",$bo_viral_and_popular_file[0]);
		$both_viral_and_popular_baseline_old = explode("\t",$bo_viral_and_popular_file[1]);
		$both_viral_and_popular_all_recent	= explode("\t",$bo_viral_and_popular_file[2]);
		$both_viral_and_popular_baseline_recent	 = explode("\t",$bo_viral_and_popular_file[3]);
		$both_viral_and_popular_f1_score = explode("\t",$bo_viral_and_popular_file[4]);
	?>
</head>
<body>

<div class="container">
	<div class="row">
	  <div class="col-md-4">
	  	<img src="<?= $clf?>/viral_twitter_features_<?= $t?><?= $o?><?= $l?>.png"  class="myImg">
	  </div>

	  <div class="col-md-4">
	  	<img src="<?= $clf?>/popular_twitter_features_<?= $t?><?= $o?><?= $l?>.png" class="myImg">	
	  </div>

	  <div class="col-md-4">
	  	<img src="<?= $clf?>/popular-viral_twitter_features_<?= $t?><?= $o?><?= $l?>.png" class="myImg">
	  </div>
	</div>
</div>

<div class="container">
	<div class="row">
	  <div class="col-md-4">
	  	<img src="<?= $clf?>/viral_youtube_features_<?= $t?><?= $o?><?= $l?>.png" class="myImg">
	  </div>

	  <div class="col-md-4">
	  	<img src="<?= $clf?>/popular_youtube_features_<?= $t?><?= $o?><?= $l?>.png" class="myImg">	
	  </div>

	  <div class="col-md-4">
	  	<img src="<?= $clf?>/popular-viral_youtube_features_<?= $t?><?= $o?><?= $l?>.png" class="myImg">
	  </div>
	</div>
</div>

<div class="container">
	<div class="row">
	  <div class="col-md-4">
	  	<img src="<?= $clf?>/viral_both_features_<?= $t?><?= $o?><?= $l?>.png" class="myImg">
	  </div>

	  <div class="col-md-4">
	  	<img src="<?= $clf?>/popular_both_features_<?= $t?><?= $o?><?= $l?>.png" class="myImg">	
	  </div>

	  <div class="col-md-4">
	  	<img src="<?= $clf?>/popular-viral_both_features_<?= $t?><?= $o?><?= $l?>.png" class="myImg">
	  </div>
	</div>
</div>

<div class="container">
	<div class="row">
	  <div class="col-md-4">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Twitter Viral</th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?= $twitter_viral_f1_score[1]?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?=$twitter_viral_all_old[1]?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?=$twitter_viral_all_recent[1]?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?=$twitter_viral_baseline_old[1]?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?=$twitter_viral_baseline_recent[1]?></td>
	  		</tr>

		</table>
	  </div>

	  <div class="col-md-4">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Twitter Popular</th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?=$twitter_popular_f1_score[1]?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $twitter_popular_all_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $twitter_popular_all_recent[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $twitter_popular_baseline_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $twitter_popular_baseline_recent[1] ?></td>
	  		</tr>

		</table>
	  </div>

	  <div class="col-md-4">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Twitter Viral and Popular</th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?= $twitter_viral_and_popular_f1_score[1]?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $twitter_viral_and_popular_all_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $twitter_viral_and_popular_all_recent[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $twitter_viral_and_popular_baseline_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $twitter_viral_and_popular_baseline_recent[1] ?></td>
	  		</tr>

		</table>
	  </div>
	</div>
</div>

<div class="container">
	<div class="row">
	  <div class="col-md-4">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Youtube Viral</th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?= $youtube_viral_f1_score[1] ?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $youtube_viral_all_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $youtube_viral_all_recent[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $youtube_viral_baseline_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $youtube_viral_baseline_recent[1] ?></td>
	  		</tr>

		</table>
	  </div>

	  <div class="col-md-4">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Youtube Popular</th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?= $youtube_popular_f1_score[1] ?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $youtube_popular_all_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $youtube_popular_all_recent[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $youtube_popular_baseline_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $youtube_popular_baseline_recent[1] ?></td>
	  		</tr>

		</table>
	  </div>

	  <div class="col-md-4">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Youtube Viral and Popular</th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?= $youtube_viral_and_popular_f1_score[1] ?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $youtube_viral_and_popular_all_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $youtube_viral_and_popular_all_recent[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $youtube_viral_and_popular_baseline_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $youtube_viral_and_popular_baseline_recent[1] ?></td>
	  		</tr>

		</table>
	  </div>
	</div>
</div>

<div class="container">
	<div class="row">
	  <div class="col-md-4">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Both Viral</th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?= $both_viral_f1_score[1] ?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $both_viral_all_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $both_viral_all_recent[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $both_viral_baseline_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $both_viral_baseline_recent[1] ?></td>
	  		</tr>

		</table>
	  </div>

	  <div class="col-md-4">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Both Popular</th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?= $both_popular_f1_score[1] ?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $both_popular_all_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $both_popular_all_recent[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $both_popular_baseline_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $both_popular_baseline_recent[1] ?></td>
	  		</tr>

		</table>	
	  </div>

	  <div class="col-md-4">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Both Viral and Popular</th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?= $both_viral_and_popular_f1_score[1] ?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $both_viral_and_popular_all_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $both_viral_and_popular_all_recent[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $both_viral_and_popular_baseline_old[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $both_viral_and_popular_baseline_recent[1] ?></td>
	  		</tr>

		</table>
	  </div>
	</div>
</div>


</body>
</html>