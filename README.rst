=================================================================
ElectrumX-Dime - Reimplementation of electrum-server for Dimecoin
=================================================================

  :Licence: MIT
  :Language: Python (>= 3.7)
  :Author: Dimecoin Developers; Original author Neil Booth

This project is a fork of `kyuupichan/electrumx <https://github.com/kyuupichan/electrumx>`_.
The original author dropped support for Bitcoin, which we intend to keep.

ElectrumX-Dime allows users to run their own Electrum server. It connects to your
full node and indexes the blockchain, allowing efficient querying of history of
arbitrary addresses. The server can be exposed publicly, and joined to the public network
of servers via peer discovery. As of May 2020, a significant chunk of the public
Electrum server network runs ElectrumX.

Adding a new coin
=================
- Add an ansible setup script inside provisioning/tasks
- Add parameters inside lib/coins.py

Credits
=======
- `Dashboard by @Mirobit <https://github.com/Mirobit/electrumx-dashboard>`_.'

Documentation
=============
See `readthedocs <https://electrumx-docs.dimecoinnetwork.com/>`_.

