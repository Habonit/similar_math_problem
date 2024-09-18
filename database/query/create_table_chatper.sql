-- chapter 테이블을 생성합니다. 
CREATE TABLE smp.chapter (
    id INT AUTO_INCREMENT PRIMARY KEY,
    학교 VARCHAR(50) NOT NULL,
    학년 INT NOT NULL,
    학기 INT NOT NULL,
    대단원명 VARCHAR(255) NOT NULL,
    소단원명 VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

