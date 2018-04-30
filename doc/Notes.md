# 3rd party Utils

* Using SQLite studio for sqlite exploration and tables definition
* using pytest for help with tests


# Personal notes

pos chain: no mining, no tx fee - marginal cost = 0
(chain can be pruned to reduce storage)
no tx fee = service messages are free and can be mandatory in every block

no tx spam: only mn can send tx. only jurors can send specific messages.
spammy mn are visible and can be voted down. bad behavior penalizes the actor.
tx from a mn can also be throttled anyway, to avoid unvoluntary spam (bug?) 

No incentive in cheating: no bis, no direct advantage. Actions logged by everyone, will be seen and recorded.


Code for light tests only, can launch with only partial tests/checks, and update later on.
Can prepare a roadmap with the MN evolution

- firsts mn deployments
- relaxed checks, first data collection (goal: check for PoS stability, nothing breaks if it fails)
- first notation criterions, nodes evaluation
- bad actors penalization
- checks and notation improvements


Should "catching up" masternodes also verify the timeslots for each round (then they need the mn list for each round)
or can we skip this test? If we only ask masternodes (that are veryfied by each other) then no need?
Get full round in one go.
ask one and check signature on 3 others?
find consensus on N well noted mn, then fetch full data from any and recheck signature matches. 
keep a table with only signatures of previous rounds.
for sir 0, use whole prev_round hash instead of last blocks? (= hash of all the blocks hashes)

for past rounds, fetch one round in a single go.
get round total hash and # of sources from peers, take the biggest from our peers, fetch from him.
check on receive. if he lied, issue a tx and ignore him for a while.
add a message for that. 


# TODO

Auto-update/restart when code update
or specific message


Check time > slot begin + delta not to send block too fast


When receiving a block, if last calculation of forger was not in that slot, refresh.

btc messages use:
- magic number to resync failed stream
- checksum in header
Both are easy to add with little overhead. reserve space for them in protobuff structure, even if not enforced at start.

DONE.
See network number + checksum and b58encoding in btc
https://en.bitcoin.it/wiki/File:PubKeyToAddr.png