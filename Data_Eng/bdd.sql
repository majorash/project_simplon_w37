SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

-- --------------------------------------------------------
-- Table structure for table images
-- --------------------------------------------------------

CREATE TABLE IF NOT EXISTS images (
  id_img char(5) NOT NULL,
  time_upld timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  user smallint(5) unsigned DEFAULT NULL,
  category char(15) DEFAULT NULL,
  url char(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8_unicode_ci;

-- --------------------------------------------------------
-- Table structure for table users
-- --------------------------------------------------------

CREATE TABLE IF NOT EXISTS users (
  id_usr smallint(5) unsigned NOT NULL,
  email varchar(100) NOT NULL,
  password char(64) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8_unicode_ci;

--
-- Indexes for table images
--
ALTER TABLE images
  ADD PRIMARY KEY (id_img);

--
-- Indexes for table users
--
ALTER TABLE users
  ADD PRIMARY KEY (id_usr);
--
-- FK for table images
--

ALTER TABLE images
ADD FOREIGN KEY (user) REFERENCES users(id_usr);

--
-- AUTO_INCREMENT for table users
--
ALTER TABLE users
  MODIFY id_usr smallint(5) unsigned NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table images
--
ALTER TABLE images
  MODIFY id_img smallint(5) unsigned NOT NULL AUTO_INCREMENT;
