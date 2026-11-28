Name: cowrie
Version: 3.1.3
Release: alt1
Summary: SSH and Telnet honeypot

License: BSD-3-Clause AND LicenseRef-FoxIO-1.1
Group: Networking/Other
URL: https://github.com/cowrie/cowrie
# Source-url: https://github.com/cowrie/cowrie/archive/refs/tags/v%{version}.tar.gz
Source: %name-%version.tar
Source1: cowrie.service
Source2: cowrie.sysusers
Source3: cowrie.logrotate
Source4: cowrie.cfg
Source5: README.ALT
Patch0: cowrie-external-auth.patch

BuildArch: noarch
AutoProv: yes,nopython3
# An emulated executable payload, never executed by the service or host.
%add_verify_elf_skiplist %python3_sitelibdir/cowrie/data/arch/*
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
# Build the emulated x86-64 payload on every build host architecture.
BuildRequires: llvm lld

# Disabled output plugins must not pull database/cloud clients into the service.
%add_python3_req_skip csirtgsdk pyes MySQLdb txmongo libvirt rethinkdb
%add_python3_req_skip botocore slackclient influxdb aiokafka geoip2
%add_python3_req_skip hpfeeds pika psycopg2 redis splunklib tftpy
%add_python3_req_skip botocore.exceptions botocore.session elasticsearch
%add_python3_req_skip hpfeeds.twisted influxdb.exceptions mysql.connector oci
%add_python3_req_skip pika.adapters.twisted_connection prometheus_client psutil pymisp
%add_python3_req_skip rethinkdb.errors slack txmongo.connection txredisapi
%add_python3_req_skip wokkel wokkel.client wokkel.xmppim

%description
Cowrie is a medium to high interaction SSH and Telnet honeypot designed to
log brute force attacks and shell interaction performed by attackers.

%prep
%setup
%patch0 -p1
# Distribution versions replace the upstream lock file constraints.
sed -i 's/==/>=/g' pyproject.toml
# Optional integrations are not installed by default.
sed -i '/^\[project.optional-dependencies\]/,/^\[tool.isort\]/{ /^\[tool.isort\]/!d; }' pyproject.toml
# Unused upstream JA4 command-line tools have standalone-only imports.
rm src/cowrie/vendor/ja4/ja4.py src/cowrie/vendor/ja4/ja4h.py src/cowrie/vendor/ja4/ja4x.py
# Never ship the prebuilt, cross-architecture dummy executables.
find src/cowrie/data/arch -maxdepth 1 -type f -delete
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
sed 's/^;;;/#/' src/cowrie/data/arch/src/nop.asm > nop.s
llvm-mc --triple=x86_64-pc-linux-gnu --filetype=obj -o nop.o nop.s
ld.lld -m elf_x86_64 --strip-all -o src/cowrie/data/arch/linux-x64-lsb nop.o
chmod 0644 src/cowrie/data/arch/linux-x64-lsb
%pyproject_build

%install
%pyproject_install
# Avoid clashing with the independent asciinema terminal recorder.
mv %buildroot%_bindir/asciinema %buildroot%_bindir/cowrie-asciinema
install -D -m 0644 %SOURCE1 %buildroot%_unitdir/cowrie.service
install -D -m 0644 %SOURCE2 %buildroot%_sysusersdir/cowrie.conf
install -D -m 0644 %SOURCE3 %buildroot%_sysconfdir/logrotate.d/cowrie
install -d %buildroot%_sysconfdir/cowrie
install -m 0644 %SOURCE4 %buildroot%_sysconfdir/cowrie/cowrie.cfg
install -m 0644 src/cowrie/data/etc/userdb.example %buildroot%_sysconfdir/cowrie/userdb.txt
install -d %buildroot%_datadir/cowrie
cp -a src/cowrie/data/fs.pickle src/cowrie/data/txtcmds %buildroot%_datadir/cowrie/
install -m 0644 src/cowrie/data/etc/cowrie.cfg.dist %buildroot%_datadir/cowrie/
install -m 0644 %SOURCE5 README.ALT
# Honeyfs file contents have been embedded in fs.pickle since Cowrie 3.x.
# Extract the original bytes for administrator overrides without host paths.
python3 - <<'PYHONEY'
import pickle
from pathlib import Path
root = Path('%buildroot%_datadir/cowrie/honeyfs')
root.mkdir()
def extract(node, parent):
    path = parent / node[0] if node[0] else parent
    if node[1] == 1:
        for child in node[7]:
            extract(child, path)
    elif node[1] == 2 and isinstance(node[7], bytes) and node[7]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(node[7])
with open('src/cowrie/data/fs.pickle', 'rb') as stream:
    tree = pickle.load(stream)
for node in tree[7]:
    extract(node, root)
PYHONEY
install -d %buildroot/var/lib/cowrie/downloads %buildroot/var/lib/cowrie/tty %buildroot/var/lib/cowrie/keys
install -d %buildroot/var/log/cowrie
cp -a %buildroot%_datadir/cowrie/fs.pickle %buildroot/var/lib/cowrie/
cp -a %buildroot%_datadir/cowrie/honeyfs %buildroot/var/lib/cowrie/
rm -rf %buildroot%python3_sitelibdir/cowrie/test

%pre
%sysusers_create_package cowrie %SOURCE2

%post
%post_service cowrie

%preun
%preun_service cowrie

%files
%doc README.ALT LICENSE.rst LICENSES README.rst
%_bindir/cowrie
%_bindir/fsctl
%_bindir/cowrie-asciinema
%_bindir/createfs
%_bindir/dumpfs
%_bindir/playlog
%python3_sitelibdir/cowrie/
%python3_sitelibdir/backend_pool/
%python3_sitelibdir/cowrie-*.dist-info/
%python3_sitelibdir/twisted/plugins/cowrie_plugin.py
%python3_sitelibdir/twisted/plugins/__pycache__/cowrie_plugin.*
%_unitdir/cowrie.service
%_sysusersdir/cowrie.conf
%_sysconfdir/logrotate.d/cowrie
%dir %_sysconfdir/cowrie
%config(noreplace) %_sysconfdir/cowrie/cowrie.cfg
%config(noreplace) %_sysconfdir/cowrie/userdb.txt
%_datadir/cowrie/
%dir %attr(0750,cowrie,cowrie) /var/lib/cowrie
%dir %attr(0750,cowrie,cowrie) /var/lib/cowrie/downloads
%dir %attr(0750,cowrie,cowrie) /var/lib/cowrie/tty
%dir %attr(0750,cowrie,cowrie) /var/lib/cowrie/keys
%dir %attr(0750,cowrie,cowrie) /var/log/cowrie
%config(noreplace) %attr(0640,cowrie,cowrie) /var/lib/cowrie/fs.pickle
%config(noreplace) %attr(-,cowrie,cowrie) /var/lib/cowrie/honeyfs/

%changelog
* Fri Nov 27 2026 Vitaly Lipatov <lav@altlinux.ru> 3.1.3-alt1
- initial build for ALT Sisyphus

