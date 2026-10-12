
CREATE DATABASE IF NOT EXISTS lost_found_db;

-- Select database
USE lost_found_db;




CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    password_hash VARCHAR(255) NOT NULL,
    profile_image VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE lost_items (
    lost_item_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    item_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    description TEXT,
    location VARCHAR(255),
    lost_date DATE,
    image_url VARCHAR(255),
    status VARCHAR(30) DEFAULT 'Lost',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);


-- =========================
-- 3. FOUND ITEMS TABLE
-- =========================

CREATE TABLE found_items (
    found_item_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    item_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    description TEXT,
    location VARCHAR(255),
    found_date DATE,
    image_url VARCHAR(255),
    status VARCHAR(30) DEFAULT 'Found',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);


-- =========================
-- 4. CLAIMS TABLE
-- =========================

CREATE TABLE claims (
    claim_id INT AUTO_INCREMENT PRIMARY KEY,

    lost_item_id INT,
    found_item_id INT,
    claimant_id INT NOT NULL,

    proof_text TEXT,
    claim_status VARCHAR(30) DEFAULT 'Pending',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (lost_item_id)
        REFERENCES lost_items(lost_item_id)
        ON DELETE CASCADE,

    FOREIGN KEY (found_item_id)
        REFERENCES found_items(found_item_id)
        ON DELETE CASCADE,

    FOREIGN KEY (claimant_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);


-- =========================
-- 5. MESSAGES TABLE
-- =========================

CREATE TABLE messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,

    sender_id INT NOT NULL,
    receiver_id INT NOT NULL,

    claim_id INT,

    message_text TEXT NOT NULL,

    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (sender_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE,

    FOREIGN KEY (receiver_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE,

    FOREIGN KEY (claim_id)
        REFERENCES claims(claim_id)
        ON DELETE CASCADE
);