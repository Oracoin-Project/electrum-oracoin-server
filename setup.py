from setuptools import setup

setup(
    name="electrum-oracoin-server",
    version="1.0",
    scripts=['run_electrum_oracoin_server.py','electrum-oracoin-server'],
    install_requires=['plyvel','jsonrpclib', 'ltc_scrypt' , 'irc >= 11, <=14.0'],
    package_dir={
        'electrumoracoinserver':'src'
        },
    py_modules=[
        'electrumoracoinserver.__init__',
        'electrumoracoinserver.utils',
        'electrumoracoinserver.storage',
        'electrumoracoinserver.deserialize',
        'electrumoracoinserver.networks',
        'electrumoracoinserver.blockchain_processor',
        'electrumoracoinserver.server_processor',
        'electrumoracoinserver.processor',
        'electrumoracoinserver.version',
        'electrumoracoinserver.ircthread',
        'electrumoracoinserver.stratum_tcp',
        'electrumoracoinserver.stratum_http'
    ],
    description="Oracoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.deg",
    maintainer="oracoin",
    maintainer_email="support@oracoin.org",
    license="GNU Affero GPLv3",
    url="https://github.com/Oracoin-Project/electrum-oracoin-server/",
    long_description="""Server for the Lightweight Oracoin Wallet"""
)
