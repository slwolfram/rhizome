CREATE PROCEDURE `QRY_ROOTS` 
()
BEGIN
	SELECT * from rhizome.root r
	join rhizome.shoot s
	on r.shoot_sk=s.shoot_id;
END
