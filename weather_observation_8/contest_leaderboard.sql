SELECT h.hacker_id, h.name, SUM(max_scores.max_score) AS total_score
FROM hackers h
JOIN (
    SELECT s.hacker_id, s.challenge_id, MAX(s.score) AS max_score
    FROM submissions s
    GROUP BY s.hacker_id, s.challenge_id
) max_scores
ON h.hacker_id = max_scores.hacker_id
GROUP BY h.hacker_id, h.name
HAVING total_score > 0
ORDER BY total_score DESC, h.hacker_id;
