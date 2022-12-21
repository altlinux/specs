Name: torrust-tracker
Version: 2.3.1
Release: alt1

Summary: Lightweight BitTorrent tracker
License: AGPL-3.0
Group: Networking/File transfer
Url: https://github.com/torrust/torrust-tracker.git

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc libsqlite3-devel libssl-devel
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
sed -ri '/^aquatic_udp_protocol/ s,git\s+=\s+\S+,path = "vendor/aquatic_udp_protocol",' Cargo.toml
%endif

%build
export CARGO_HOME=${PWD}/cargo
cargo build --release

%install
install -pm0755 -D target/release/torrust-tracker %buildroot%_sbindir/torrust-tracker
install -pm0644 -D torrust-tracker.service %buildroot%_unitdir/torrust-tracker.service
mkdir -p %buildroot%_localstatedir/torrust
touch %buildroot%_localstatedir/torrust/data.db
cd %buildroot%_localstatedir/torrust && ../../../usr/sbin/torrust-tracker ||:

%pre
/usr/sbin/groupadd -r -f _torrust &>/dev/null ||:
/usr/sbin/useradd -r -g _torrust -d /var/lib/torrust -s /dev/null \
    -c "torrust bittorrent tracker" -M -n _torrust &>/dev/null ||:

%files
%doc LICENSE README*
%_unitdir/torrust-tracker.service
%_sbindir/torrust-tracker
%dir %attr(0770,root,_torrust) %_localstatedir/torrust
%config(noreplace) %attr(0660,_torrust,_torrust) %_localstatedir/torrust/config.toml
%ghost %attr(0660,_torrust,_torrust) %_localstatedir/torrust/data.db

%changelog
* Wed Dec 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.1-alt1
- 2.3.1 released

* Thu May 12 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.0-alt1
- 2.3.0 released

* Tue Mar 22 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt1
- initial
