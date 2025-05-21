-- Create papers table
CREATE TABLE ageing_papers (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  paper_id TEXT UNIQUE NOT NULL,
  title TEXT,
  doi TEXT,
  abstract TEXT,
  source TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Create claims table
CREATE TABLE claims (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  paper_id TEXT REFERENCES papers(paper_id),
  intervention TEXT,
  mechanism TEXT,
  effect TEXT,
  species TEXT,
  support_direction TEXT CHECK (support_direction IN ('Supports', 'Contradicts', 'Neutral'))
);