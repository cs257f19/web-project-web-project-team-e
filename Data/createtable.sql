DROP TABLE IF EXISTS ksdata;
CREATE TABLE ksdata (
  id real,
  projectname text,
  category text,
  main_category text,
  currency text,
  projectyear real,
  deadline date,
  goal real,
  total_days real,
  pledged real,
  state text,
  backers real,
  country text,
  usd_pledged_real real,
  usd_goal_real real
);
