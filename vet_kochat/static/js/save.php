<?php
	include 'database.php';
	$pets_pet_serial=$_POST['pets_pet_serial'];
	$pets_members_member_serial=$_POST['pets_members_member_serial'];
	$diag_date=$_POST['diag_date'];
	$diag_time=$_POST['diag_time'];
	$diag_ds_name=$_POST['diag_ds_name'];
	$sql = "INSERT INTO `expect_diagnoses` (`pets_pet_serial`, `pets_members_member_serial`, `diag_date`, `diag_time`, `diag_ds_name`) VALUES ('$pets_pet_serial','$pets_members_member_serial','$diag_date','$diag_time','$diag_ds_name')";
	if (mysqli_query($conn, $sql)) {
		echo json_encode(array("statusCode"=>200));
	}
	else {
		echo json_encode(array("statusCode"=>201));
	}
	mysqli_close($conn);
?>
