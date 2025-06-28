SELECT h.hacker_id, h.name
FROM Hackers h
JOIN (
    SELECT s.hacker_id, s.challenge_id
    FROM Submissions s
    JOIN Challenges c ON s.challenge_id = c.challenge_id
    JOIN Difficulty d ON c.difficulty_level = d.difficulty_level
    GROUP BY s.hacker_id, s.challenge_id, d.score
    HAVING MAX(s.score) = d.score
) t
ON h.hacker_id = t.hacker_id
GROUP BY h.hacker_id, h.name
HAVING COUNT(t.challenge_id) > 1
ORDER BY COUNT(t.challenge_id) DESC, h.hacker_id;
