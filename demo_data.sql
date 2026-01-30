-- Clear existing data
TRUNCATE TABLE vacancyskill, cvskill, vacancy, cv CASCADE;

-- ==========================================
-- VACANCIES
-- ==========================================

-- 1. Senior Python Backend Developer (FinTech)
INSERT INTO vacancy (id, title, description, category, salary_range, location, status, created_at)
VALUES (
    'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
    'Senior Python Backend Developer',
    'We are a leading FinTech startup looking for a Senior Backend Engineer to help us build our next-generation payment processing engine. You will design and implement high-performance, scalable APIs and work closely with our data science team.',
    'Backend',
    '$120,000 - $160,000',
    'Remote (US/EU)',
    'Open',
    NOW()
);

-- 2. Frontend React Engineer (E-commerce)
INSERT INTO vacancy (id, title, description, category, salary_range, location, status, created_at)
VALUES (
    'b1eebc99-9c0b-4ef8-bb6d-6bb9bd380b22',
    'Frontend React Engineer',
    'Join our fast-paced E-commerce team. We need a specialist in React and TypeScript to modernize our customer-facing storefront. Experience with Next.js and Tailwind CSS is a huge plus.',
    'Frontend',
    '$90,000 - $130,000',
    'New York, NY',
    'Open',
    NOW()
);

-- 3. Lead Data Scientist (AI/ML)
INSERT INTO vacancy (id, title, description, category, salary_range, location, status, created_at)
VALUES (
    'c2eebc99-9c0b-4ef8-bb6d-6bb9bd380c33',
    'Lead Data Scientist',
    'We are seeking a Lead Data Scientist to drive our predictive modeling initiatives. You should have deep expertise in NLP, Python (Pandas, Scikit-learn), and deploying models to production.',
    'DataScience',
    '$150,000 - $200,000',
    'San Francisco, CA',
    'Open',
    NOW()
);

-- 4. DevOps Engineer (Cloud Infrastructure)
INSERT INTO vacancy (id, title, description, category, salary_range, location, status, created_at)
VALUES (
    'd3eebc99-9c0b-4ef8-bb6d-6bb9bd380d44',
    'Mid-Level DevOps Engineer',
    'Help us maintain our cloud infrastructure on AWS. You will be responsible for CI/CD pipelines, container orchestration with Kubernetes, and monitoring system health.',
    'DevOps',
    '$100,000 - $140,000',
    'Berlin, Germany',
    'Open',
    NOW()
);

-- ==========================================
-- VACANCY SKILLS
-- ==========================================

-- Skills for Senior Python Backend (a0eebc99...)
INSERT INTO vacancyskill (name, vacancy_id) VALUES
('Python', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'),
('Django', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'),
('PostgreSQL', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'),
('Docker', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'),
('Redis', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11');

-- Skills for Frontend React Engineer (b1eebc99...)
INSERT INTO vacancyskill (name, vacancy_id) VALUES
('React', 'b1eebc99-9c0b-4ef8-bb6d-6bb9bd380b22'),
('TypeScript', 'b1eebc99-9c0b-4ef8-bb6d-6bb9bd380b22'),
('Next.js', 'b1eebc99-9c0b-4ef8-bb6d-6bb9bd380b22'),
('Tailwind CSS', 'b1eebc99-9c0b-4ef8-bb6d-6bb9bd380b22'),
('Redux', 'b1eebc99-9c0b-4ef8-bb6d-6bb9bd380b22');

-- Skills for Lead Data Scientist (c2eebc99...)
INSERT INTO vacancyskill (name, vacancy_id) VALUES
('Python', 'c2eebc99-9c0b-4ef8-bb6d-6bb9bd380c33'),
('Machine Learning', 'c2eebc99-9c0b-4ef8-bb6d-6bb9bd380c33'),
('NLP', 'c2eebc99-9c0b-4ef8-bb6d-6bb9bd380c33'),
('TensorFlow', 'c2eebc99-9c0b-4ef8-bb6d-6bb9bd380c33'),
('SQL', 'c2eebc99-9c0b-4ef8-bb6d-6bb9bd380c33');

-- Skills for DevOps Engineer (d3eebc99...)
INSERT INTO vacancyskill (name, vacancy_id) VALUES
('AWS', 'd3eebc99-9c0b-4ef8-bb6d-6bb9bd380d44'),
('Kubernetes', 'd3eebc99-9c0b-4ef8-bb6d-6bb9bd380d44'),
('Terraform', 'd3eebc99-9c0b-4ef8-bb6d-6bb9bd380d44'),
('Jenkins', 'd3eebc99-9c0b-4ef8-bb6d-6bb9bd380d44'),
('Linux', 'd3eebc99-9c0b-4ef8-bb6d-6bb9bd380d44');


-- ==========================================
-- CVs (CANDIDATES)
-- ==========================================

-- 1. Alice Pythonista (Perfect match for Backend)
INSERT INTO cv (id, full_name, email, summary, experience_level, created_at)
VALUES (
    '11111111-1111-1111-1111-111111111111',
    'Alice Pythonista',
    'alice@example.com',
    'Senior Backend Developer with 7 years of experience building scalable systems. Expert in Python, Django, and database optimization. Passionate about clean code and architecture.',
    'Senior',
    NOW()
);

-- 2. Bob Frontender (Good match for Frontend)
INSERT INTO cv (id, full_name, email, summary, experience_level, created_at)
VALUES (
    '22222222-2222-2222-2222-222222222222',
    'Bob Frontender',
    'bob@example.com',
    'Creative Frontend Developer specializing in React ecosystems. I love creating smooth user interfaces and have strong TypeScript skills. Previously worked at a digital agency.',
    'Mid',
    NOW()
);

-- 3. Charlie Data (Perfect match for Data Science)
INSERT INTO cv (id, full_name, email, summary, experience_level, created_at)
VALUES (
    '33333333-3333-3333-3333-333333333333',
    'Charlie Data',
    'charlie@example.com',
    'Lead Data Scientist with a PhD in Computational Linguistics. Proven track record of deploying NLP models that increased revenue by 20%. Strong leader and mentor.',
    'Lead',
    NOW()
);

-- 4. Dave DevOps (Good match for DevOps)
INSERT INTO cv (id, full_name, email, summary, experience_level, created_at)
VALUES (
    '44444444-4444-4444-4444-444444444444',
    'Dave DevOps',
    'dave@example.com',
    'Reliable DevOps Engineer focused on automation and stability. Experienced in migrating legacy systems to AWS and implementing GitOps workflows.',
    'Mid',
    NOW()
);

-- 5. Eve Fullstack (Decent match for Backend & Frontend)
INSERT INTO cv (id, full_name, email, summary, experience_level, created_at)
VALUES (
    '55555555-5555-5555-5555-555555555555',
    'Eve Fullstack',
    'eve@example.com',
    'Fullstack Developer comfortable with both Python backends and React frontends. I enjoy working on the entire product lifecycle from database design to UI implementation.',
    'Senior',
    NOW()
);

-- 6. Frank Junior (Junior, low match for senior roles)
INSERT INTO cv (id, full_name, email, summary, experience_level, created_at)
VALUES (
    '66666666-6666-6666-6666-666666666666',
    'Frank Junior',
    'frank@example.com',
    'Recent Computer Science graduate eager to learn. I have done several university projects using Python and Java. Quick learner and hard worker.',
    'Junior',
    NOW()
);

-- ==========================================
-- CV SKILLS
-- ==========================================

-- Alice (Backend Expert) - Highly Verified
INSERT INTO cvskill (name, is_verified, cv_id) VALUES
('Python', true, '11111111-1111-1111-1111-111111111111'),
('Django', true, '11111111-1111-1111-1111-111111111111'),
('PostgreSQL', true, '11111111-1111-1111-1111-111111111111'),
('Redis', false, '11111111-1111-1111-1111-111111111111'),
('System Design', true, '11111111-1111-1111-1111-111111111111');

-- Bob (Frontend)
INSERT INTO cvskill (name, is_verified, cv_id) VALUES
('React', true, '22222222-2222-2222-2222-222222222222'),
('JavaScript', true, '22222222-2222-2222-2222-222222222222'),
('TypeScript', false, '22222222-2222-2222-2222-222222222222'),
('CSS', true, '22222222-2222-2222-2222-222222222222');

-- Charlie (Data Science Lead)
INSERT INTO cvskill (name, is_verified, cv_id) VALUES
('Python', true, '33333333-3333-3333-3333-333333333333'),
('Machine Learning', true, '33333333-3333-3333-3333-333333333333'),
('NLP', true, '33333333-3333-3333-3333-333333333333'),
('TensorFlow', false, '33333333-3333-3333-3333-333333333333'),
('Leadership', true, '33333333-3333-3333-3333-333333333333');

-- Dave (DevOps)
INSERT INTO cvskill (name, is_verified, cv_id) VALUES
('AWS', true, '44444444-4444-4444-4444-444444444444'),
('Linux', true, '44444444-4444-4444-4444-444444444444'),
('Docker', true, '44444444-4444-4444-4444-444444444444'),
('Kubernetes', false, '44444444-4444-4444-4444-444444444444');

-- Eve (Fullstack)
INSERT INTO cvskill (name, is_verified, cv_id) VALUES
('Python', true, '55555555-5555-5555-5555-555555555555'),
('React', true, '55555555-5555-5555-5555-555555555555'),
('FastAPI', false, '55555555-5555-5555-5555-555555555555'),
('SQL', true, '55555555-5555-5555-5555-555555555555');

-- Frank (Junior)
INSERT INTO cvskill (name, is_verified, cv_id) VALUES
('Python', false, '66666666-6666-6666-6666-666666666666'),
('Java', false, '66666666-6666-6666-6666-666666666666'),
('HTML', true, '66666666-6666-6666-6666-666666666666');
