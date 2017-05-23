<!DOCTYPE html>
<html>
<head>
	<title>Compare</title>
	<link rel="stylesheet" type="text/css" href="bootstrap.css">
	<link rel="stylesheet" type="text/css" href="style.css">

	<?php
		$t = $_GET['t'];
		$o = $_GET['o'];
		$l = $_GET['l'];
		$clf1 = $_GET['clf1'];
		$clf2 = $_GET['clf2'];

		$tw_viral_file = file($clf1 . "/twitter_viral_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$tw_popular_file = file($clf1 . "/twitter_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$tw_viral_and_popular_file = file($clf1 . "/twitter_viral_and_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);

		$yt_viral_file = file($clf1 . "/youtube_viral_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$yt_popular_file = file($clf1 . "/youtube_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$yt_viral_and_popular_file = file($clf1 . "/youtube_viral_and_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);

		$bo_viral_file = file($clf1 . "/both_viral_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$bo_popular_file = file($clf1 . "/both_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$bo_viral_and_popular_file = file($clf1 . "/both_viral_and_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);

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

		$tw_viral_file = file($clf2 . "/twitter_viral_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$tw_popular_file = file($clf2 . "/twitter_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$tw_viral_and_popular_file = file($clf2 . "/twitter_viral_and_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);

		$yt_viral_file = file($clf2 . "/youtube_viral_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$yt_popular_file = file($clf2 . "/youtube_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$yt_viral_and_popular_file = file($clf2 . "/youtube_viral_and_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);

		$bo_viral_file = file($clf2 . "/both_viral_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$bo_popular_file = file($clf2 . "/both_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);
		$bo_viral_and_popular_file = file($clf2 . "/both_viral_and_popular_".$t.$o.$l.".eva",FILE_IGNORE_NEW_LINES);

		$twitter_viral_all_old2	= explode("\t",$tw_viral_file[0]);
		$twitter_viral_baseline_old2 = explode("\t",$tw_viral_file[1]);
		$twitter_viral_all_recent2	= explode("\t",$tw_viral_file[2]);
		$twitter_viral_baseline_recent2	 = explode("\t",$tw_viral_file[3]);
		$twitter_viral_f1_score2 = explode("\t",$tw_viral_file[4]);

		$twitter_popular_all_old2	= explode("\t",$tw_popular_file[0]);
		$twitter_popular_baseline_old2 = explode("\t",$tw_popular_file[1]);
		$twitter_popular_all_recent2	= explode("\t",$tw_popular_file[2]);
		$twitter_popular_baseline_recent2	 = explode("\t",$tw_popular_file[3]);
		$twitter_popular_f1_score2 = explode("\t",$tw_popular_file[4]);

		$twitter_viral_and_popular_all_old2	= explode("\t",$tw_viral_and_popular_file[0]);
		$twitter_viral_and_popular_baseline_old2 = explode("\t",$tw_viral_and_popular_file[1]);
		$twitter_viral_and_popular_all_recent2	= explode("\t",$tw_viral_and_popular_file[2]);
		$twitter_viral_and_popular_baseline_recent2	 = explode("\t",$tw_viral_and_popular_file[3]);
		$twitter_viral_and_popular_f1_score2 = explode("\t",$tw_viral_and_popular_file[4]);

		$youtube_viral_all_old2	= explode("\t",$yt_viral_file[0]);
		$youtube_viral_baseline_old2 = explode("\t",$yt_viral_file[1]);
		$youtube_viral_all_recent2	= explode("\t",$yt_viral_file[2]);
		$youtube_viral_baseline_recent2	 = explode("\t",$yt_viral_file[3]);
		$youtube_viral_f1_score2 = explode("\t",$yt_viral_file[4]);

		$youtube_popular_all_old2	= explode("\t",$yt_popular_file[0]);
		$youtube_popular_baseline_old2 = explode("\t",$yt_popular_file[1]);
		$youtube_popular_all_recent2	= explode("\t",$yt_popular_file[2]);
		$youtube_popular_baseline_recent2	 = explode("\t",$yt_popular_file[3]);
		$youtube_popular_f1_score2 = explode("\t",$yt_popular_file[4]);

		$youtube_viral_and_popular_all_old2	= explode("\t",$yt_viral_and_popular_file[0]);
		$youtube_viral_and_popular_baseline_old2 = explode("\t",$yt_viral_and_popular_file[1]);
		$youtube_viral_and_popular_all_recent2	= explode("\t",$yt_viral_and_popular_file[2]);
		$youtube_viral_and_popular_baseline_recent2	 = explode("\t",$yt_viral_and_popular_file[3]);
		$youtube_viral_and_popular_f1_score2 = explode("\t",$yt_viral_and_popular_file[4]);

		$both_viral_all_old2	= explode("\t",$bo_viral_file[0]);
		$both_viral_baseline_old2 = explode("\t",$bo_viral_file[1]);
		$both_viral_all_recent2	= explode("\t",$bo_viral_file[2]);
		$both_viral_baseline_recent2	 = explode("\t",$bo_viral_file[3]);
		$both_viral_f1_score2 = explode("\t",$bo_viral_file[4]);

		$both_popular_all_old2	= explode("\t",$bo_popular_file[0]);
		$both_popular_baseline_old2 = explode("\t",$bo_popular_file[1]);
		$both_popular_all_recent2	= explode("\t",$bo_popular_file[2]);
		$both_popular_baseline_recent2	 = explode("\t",$bo_popular_file[3]);
		$both_popular_f1_score2 = explode("\t",$bo_popular_file[4]);

		$both_viral_and_popular_all_old2	= explode("\t",$bo_viral_and_popular_file[0]);
		$both_viral_and_popular_baseline_old2 = explode("\t",$bo_viral_and_popular_file[1]);
		$both_viral_and_popular_all_recent2	= explode("\t",$bo_viral_and_popular_file[2]);
		$both_viral_and_popular_baseline_recent2	 = explode("\t",$bo_viral_and_popular_file[3]);
		$both_viral_and_popular_f1_score2 = explode("\t",$bo_viral_and_popular_file[4]);
			
	?>

</head>
<body>

<div class="container wrapper">

	<h3 class="title">
		Algorithm Comparison
	</h3>

	<form action="compare.php" method="GET">

	<div class="row">
		<div class="col-md-4">
			<div class = "title">
				Select Training Window
			</div>

			<select class="form-control" name="t">
			  <option>1</option>
			  <option>2</option>
			  <option>3</option>
			  <option>7</option>
			</select>
		</div>

		<div class="col-md-4">
			<div class = "title">
				Select Offset
			</div>

			<select class="form-control" name="o">
			  <option>0</option>
			  <option>1</option>
			  <option>2</option>
			  <option>3</option>
			  <option>7</option>
			</select>
		</div>

		<div class="col-md-4">
			<div class = "title">
				Select Labeling Window
			</div>

			<select class="form-control" name="l">
			  <option>1</option>
			  <option>2</option>
			  <option>3</option>
			  <option>7</option>
			</select>
		</div>
	</div>

	<div class="row">
	  <div class="col-md-4">
	  	<h4>Select First Algorithm</h4>
	  	<select class="form-control" name="clf1">
		  		<option>LogisticRegression</option>
				<option>SVM - LinearSVC</option>
				<option>K Nearest Neighbours</option>
				<option>Decision Tree</option>
				<option>Random Forest</option>
				<option>Extra Trees</option>
				<option>Bagging Decision Tree</option>
				<option>Gradient Boosting Decision Tree</option>
				<option>AdaBoost Decision Tree</option>
				<option>Voting - AdaBoostGradientBoosting DT</option>
				<option>Voting - ABGBLR</option>
				<option>BaggingGBDT</option>
		</select>
	  </div>

	  <div class="col-md-4">
	  	<h4>Select Second Algorithm</h4>
	  	<select class="form-control" name="clf2">
		  		<option>LogisticRegression</option>
				<option>SVM - LinearSVC</option>
				<option>K Nearest Neighbours</option>
				<option>Decision Tree</option>
				<option>Random Forest</option>
				<option>Extra Trees</option>
				<option>Bagging Decision Tree</option>
				<option>Gradient Boosting Decision Tree</option>
				<option>AdaBoost Decision Tree</option>
				<option>Voting - AdaBoostGradientBoosting DT</option>
				<option>Voting - ABGBLR</option>
				<option>BaggingGBDT</option>
		</select>
	  </div>

	  <div class="col-md-4">
	  		<input class="btn btn-default myBut " type="submit" value="Generate Comparison">
	  </div>

	  

		
	</div>

	</form>

	<div class="row">
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Twitter Viral - <br><?= $clf1 ?></th>
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
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Twitter Viral - <br><?= $clf2 ?></th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?=$twitter_viral_f1_score2[1]?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?=$twitter_viral_all_old2[1]?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?=$twitter_viral_all_recent2[1]?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?=$twitter_viral_baseline_old2[1]?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?=$twitter_viral_baseline_recent2[1]?></td>
	  		</tr>

		</table>
	  </div>
	  <div class="col-md-4 title">
	  	<table class="table table-hover">
	  		<tr>
			    <th>Better Performance</th>
			    <br>
			</tr>
			
				<?php
					if($twitter_viral_f1_score2[1]>= $twitter_viral_f1_score[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>
			
			<tr>
			    
				<?php
					if( $twitter_viral_all_old2[1]>= $twitter_viral_all_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $twitter_viral_all_recent2[1]>= $twitter_viral_all_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $twitter_viral_baseline_old2[1]>= $twitter_viral_baseline_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $twitter_viral_baseline_recent2[1]>= $twitter_viral_baseline_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>
			 
		</table>
	  </div>
	</div>

	<div class="row">
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Twitter Popular - <br><?= $clf1 ?></th>
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
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Twitter Popular - <br><?= $clf2 ?></th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?=$twitter_popular_f1_score2[1]?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $twitter_popular_all_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $twitter_popular_all_recent2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $twitter_popular_baseline_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $twitter_popular_baseline_recent2[1] ?></td>
	  		</tr>

		</table>
	  </div>
	  <div class="col-md-4 title">
	  	<table class="table table-hover">
	  		<tr>
			    <th>Better Performance</th>
			    <br>
			</tr>
			
				<?php
					if($twitter_popular_f1_score2[1]>= $twitter_popular_f1_score[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>
			
			<tr>
			    
				<?php
					if( $twitter_popular_all_old2[1]>= $twitter_popular_all_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $twitter_popular_all_recent2[1]>= $twitter_popular_all_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $twitter_popular_baseline_old2[1]>= $twitter_popular_baseline_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $twitter_popular_baseline_recent2[1]>= $twitter_popular_baseline_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>
			 
		</table>
	  </div>
	</div>

	<div class="row">
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Twitter Viral and Popular - <br><?= $clf1 ?></th>
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
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Twitter Viral and Popular - <br><?= $clf2 ?></th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?= $twitter_viral_and_popular_f1_score2[1]?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $twitter_viral_and_popular_all_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $twitter_viral_and_popular_all_recent2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $twitter_viral_and_popular_baseline_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $twitter_viral_and_popular_baseline_recent2[1] ?></td>
	  		</tr>

		</table>
	  </div>
	  <div class="col-md-4 title">
	  	<table class="table table-hover">
	  		<tr>
			    <th>Better Performance</th>
			    <br>
			</tr>
			
				<?php
					if($twitter_viral_and_popular_f1_score2[1]>= $twitter_viral_and_popular_f1_score[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>
			
			<tr>
			    
				<?php
					if( $twitter_viral_and_popular_all_old2[1]>= $twitter_viral_and_popular_all_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $twitter_viral_and_popular_all_recent2[1]>= $twitter_viral_and_popular_all_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $twitter_viral_and_popular_baseline_old2[1]>= $twitter_viral_and_popular_baseline_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $twitter_viral_and_popular_baseline_recent2[1]>= $twitter_viral_and_popular_baseline_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>
			 
		</table>
	  </div>
	</div>

	<div class="row">
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Youtube Viral - <br><?= $clf1 ?></th>
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
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Youtube Viral - <br><?= $clf2 ?></th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?= $youtube_viral_f1_score2[1] ?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $youtube_viral_all_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $youtube_viral_all_recent2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $youtube_viral_baseline_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $youtube_viral_baseline_recent2[1] ?></td>
	  		</tr>

		</table>
	  </div>
	  <div class="col-md-4 title">
	  	<table class="table table-hover">
	  		<tr>
			    <th>Better Performance</th>
			    <br>
			</tr>
			
				<?php
					if($youtube_viral_f1_score2[1]>= $youtube_viral_f1_score[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>
			
			<tr>
			    
				<?php
					if( $youtube_viral_all_old2[1]>= $youtube_viral_all_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $youtube_viral_all_recent2[1]>= $youtube_viral_all_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $youtube_viral_baseline_old2[1]>= $youtube_viral_baseline_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $youtube_viral_baseline_recent2[1]>= $youtube_viral_baseline_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>
			 
		</table>
	  </div>
	</div>

	<div class="row">
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Youtube Popular - <br><?= $clf1 ?></th>
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
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Youtube Popular - <br><?= $clf2 ?></th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?= $youtube_popular_f1_score2[1] ?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $youtube_popular_all_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $youtube_popular_all_recent2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $youtube_popular_baseline_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $youtube_popular_baseline_recent2[1] ?></td>
	  		</tr>

		</table>
	  </div>
	  <div class="col-md-4 title">
	  	<table class="table table-hover">
	  		<tr>
			    <th>Better Performance</th>
			    <br>
			</tr>
			
				<?php
					if($youtube_popular_f1_score2[1]>= $youtube_popular_f1_score[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>
			
			<tr>
			    
				<?php
					if( $youtube_popular_all_old2[1]>= $youtube_popular_all_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $youtube_popular_all_recent2[1]>= $youtube_popular_all_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $youtube_popular_baseline_old2[1]>= $youtube_popular_baseline_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $youtube_popular_baseline_recent2[1]>= $youtube_popular_baseline_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>
			 
		</table>
	  </div>
	</div>

	<div class="row">
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Youtube Viral and Popular - <br><?= $clf1 ?></th>
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
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Youtube Viral and Popular - <br><?= $clf2 ?></th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?= $youtube_viral_and_popular_f1_score2[1] ?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $youtube_viral_and_popular_all_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $youtube_viral_and_popular_all_recent2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $youtube_viral_and_popular_baseline_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $youtube_viral_and_popular_baseline_recent2[1] ?></td>
	  		</tr>

		</table>
	  </div>
	  <div class="col-md-4 title">
	  	<table class="table table-hover">
	  		<tr>
			    <th>Better Performance</th>
			    <br>
			</tr>
			
				<?php
					if($youtube_viral_and_popular_f1_score2[1]>= $youtube_viral_and_popular_f1_score[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>
			
			<tr>
			    
				<?php
					if( $youtube_viral_and_popular_all_old2[1]>= $youtube_viral_and_popular_all_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $youtube_viral_and_popular_all_recent2[1]>= $youtube_viral_and_popular_all_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $youtube_viral_and_popular_baseline_old2[1]>= $youtube_viral_and_popular_baseline_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $youtube_viral_and_popular_baseline_recent2[1]>= $youtube_viral_and_popular_baseline_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>
			 
		</table>
	  </div>
	</div>

	<div class="row">
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Both Viral - <br><?= $clf1 ?></th>
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
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Both Viral - <br><?= $clf2 ?></th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?= $both_viral_f1_score2[0] ?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $both_viral_all_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $both_viral_all_recent2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $both_viral_baseline_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $both_viral_baseline_recent2[1] ?></td>
	  		</tr>

		</table>
	  </div>
	  <div class="col-md-4 title">
	  	<table class="table table-hover">
	  		<tr>
			    <th>Better Performance</th>
			    <br>
			</tr>
			
				<?php
					if($both_viral_f1_score2[1]>= $both_viral_f1_score[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>
			
			<tr>
			    
				<?php
					if( $both_viral_all_old2[1]>= $both_viral_all_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $both_viral_all_recent2[1]>= $both_viral_all_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $both_viral_baseline_old2[1]>= $both_viral_baseline_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $both_viral_baseline_recent2[1]>= $both_viral_baseline_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>
			 
		</table>
	  </div>
	</div>

	<div class="row">
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Both Popular - <br><?= $clf1 ?></th>
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
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Both Popular - <br><?= $clf2 ?></th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?= $both_popular_f1_score2[1] ?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $both_popular_all_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $both_popular_all_recent2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $both_popular_baseline_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $both_popular_baseline_recent2[1] ?></td>
	  		</tr>

		</table>
	  </div>
	  <div class="col-md-4 title">
	  	<table class="table table-hover">
	  		<tr>
			    <th>Better Performance</th>
			    <br>
			</tr>
			
				<?php
					if($both_popular_f1_score2[1]>= $both_popular_f1_score[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>
			
			<tr>
			    
				<?php
					if( $both_popular_all_old2[1]>= $both_popular_all_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $both_popular_all_recent2[1]>= $both_popular_all_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $both_popular_baseline_old2[1]>= $both_popular_baseline_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $both_popular_baseline_recent2[1]>= $both_popular_baseline_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>
			 
		</table>
	  </div>
	</div>

	<div class="row">
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Both Viral and Popular - <br><?= $clf1 ?></th>
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
	  <div class="col-md-4 title">
	  	<table class="table table-hover">

	  		<tr>
			    <th>Both Viral and Popular - <br><?= $clf2 ?></th>
			    <th>Value</th>
			</tr>

			<tr>
			    <td>F1 Score</td>
			    <td><?= $both_viral_and_popular_f1_score2[1] ?></td>
	  		</tr>
			 
			 <tr>
			    <td>All Features Old - AUC</td>
			    <td><?= $both_viral_and_popular_all_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>All Features Recent - AUC</td>
			    <td><?= $both_viral_and_popular_all_recent2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Old - AUC</td>
			    <td><?= $both_viral_and_popular_baseline_old2[1] ?></td>
	  		</tr>

	  		<tr>
			    <td>Baseline Features Recent - AUC</td>
			    <td><?= $both_viral_and_popular_baseline_recent2[1] ?></td>
	  		</tr>

		</table>
	  </div>
	  <div class="col-md-4 title">
	  	<table class="table table-hover">
	  		<tr>
			    <th>Better Performance</th>
			    <br>
			</tr>
			
				<?php
					if($both_viral_and_popular_f1_score2[1]>= $both_viral_and_popular_f1_score[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>
			
			<tr>
			    
				<?php
					if( $both_viral_and_popular_all_old2[1]>= $both_viral_and_popular_all_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $both_viral_and_popular_all_recent2[1]>= $both_viral_and_popular_all_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $both_viral_and_popular_baseline_old2[1]>= $both_viral_and_popular_baseline_old[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>

			<tr>
			    
			    <?php
					if( $both_viral_and_popular_baseline_recent2[1]>= $both_viral_and_popular_baseline_recent[1]){ ?>
						<tr class="clf2">
							<td class="clf2"><?=$clf2?></td>
						</tr>
					<?php
					}else{ ?>
						<tr>
							<td><?=$clf1?></td>
						</tr>					
				<?php } ?>

			</tr>
			 
		</table>
	  </div>
	</div>

</div>

</body>
</html>