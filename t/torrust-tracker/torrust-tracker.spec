Name: torrust-tracker
Version: 3.0.0
Release: alt1

Summary: Lightweight BitTorrent tracker
License: AGPL-3.0
Group: Networking/File transfer
Url: https://github.com/torrust/torrust-tracker.git

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc libsqlite3-devel libssl-devel perl(IPC/Cmd.pm)
ExcludeArch: ppc64le

%description
%summary

%prep
%setup
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 vendor
%else
tar xf %SOURCE1
%endif

%build
export CARGO_HOME=${PWD}/cargo
cargo build --offline --release

%install
export CARGO_HOME=${PWD}/cargo
cargo install --force --root %buildroot%_prefix --path . --no-track
rm -v %buildroot%_bindir/{profiling,e2e_tests_runner,tracker_checker}

install -pm0644 -D torrust.sysconfig %buildroot%_sysconfdir/sysconfig/torrust
install -pm0644 -D torrust-tracker.service %buildroot%_unitdir/torrust-tracker.service
install -pm0644 -D share/default/config/tracker.container.sqlite3.toml %buildroot%_sysconfdir/torrust/tracker.toml
sed -i 's,tracker/database/sqlite3.db,data.db,' %buildroot%_sysconfdir/torrust/tracker.toml

mkdir -p %buildroot%_localstatedir/torrust
touch %buildroot%_localstatedir/torrust/data.db

%pre
/usr/sbin/groupadd -r -f _torrust &>/dev/null ||:
/usr/sbin/useradd -r -g _torrust -d /var/lib/torrust -s /dev/null \
    -c "torrust bittorrent tracker" -M -n _torrust &>/dev/null ||:

%files
%doc LICENSE README* share/default/config

%attr(0640,root,_torrust) %config(noreplace) %_sysconfdir/torrust/tracker.toml
%config(noreplace) %_sysconfdir/sysconfig/torrust

%_unitdir/torrust-tracker.service

%_bindir/torrust-tracker
%_bindir/http_health_check
%_bindir/http_tracker_client
%_bindir/udp_tracker_client

%dir %attr(0770,root,_torrust) %_localstatedir/torrust
%ghost %attr(0660,_torrust,_torrust) %_localstatedir/torrust/data.db

%changelog
* Thu Oct 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.0-alt1
- 3.0.0 released

* Wed Dec 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.1-alt1
- 2.3.1 released

* Thu May 12 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.0-alt1
- 2.3.0 released

* Tue Mar 22 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt1
- initial
