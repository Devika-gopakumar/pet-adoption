-- Sample queries demonstrating JOINs and aggregation on the pet_adoption schema

-- 1. List all available pets along with their donor's details
SELECT p.pet_id, p.pet_species, p.pet_breed, d.donor_name, d.donor_phone
FROM Pet p
JOIN Donor d ON p.donor_id = d.donor_id
WHERE p.available = 1;

-- 2. List all adopters along with the details of the pet they adopted
SELECT a.adopter_name, a.adopter_phone, p.pet_species, p.pet_breed
FROM Adopter a
JOIN Pet p ON a.pet_id = p.pet_id;

-- 3. List each donor along with the total number of pets they've donated
SELECT d.donor_name, COUNT(p.pet_id) AS pets_donated
FROM Donor d
LEFT JOIN Pet p ON d.donor_id = p.donor_id
GROUP BY d.donor_id, d.donor_name;

-- 4. Full chain: adopter -> pet -> original donor, for every adopted pet
SELECT a.adopter_name, p.pet_species, p.pet_breed, d.donor_name
FROM Adopter a
JOIN Pet p ON a.pet_id = p.pet_id
JOIN Donor d ON p.donor_id = d.donor_id;

-- 5. Species that have never been adopted (still available)
SELECT DISTINCT pet_species
FROM Pet
WHERE available = 1;
