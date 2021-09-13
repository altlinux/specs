%define zincati_user         zincati
%define zincati_group        %zincati_user
%define zincati_home         %_localstatedir/%zincati_user

%define zincati_confdir1     %_libexecdir/%name/config.d/
%define zincati_confdir2     %_sysconfdir/%name/config.d/
%define zincati_dbus_systemd /usr/share/dbus-1/system.d/

%define zincati_bindir       %{_prefix}/libexec/

Name:     zincati
Version:  0.0.22
Release:  alt3

Summary:  An auto-update agent for Fedora CoreOS hosts.
License:  Apache-2.0
Group:    Development/Tools
Url:      https://github.com/coreos/zincati

Packager: Alexey Kostarev <kaf@altlinux.org>

Source:   %name-%version.tar
Patch1:   %name-%version-%release.patch

ExclusiveArch: x86_64 aarch64

BuildRequires: rust-cargo openssl-devel  
BuildRequires: /proc

%description
%summary

%prep
%setup
%patch1 -p1

%build
export RUSTFLAGS="-g"
cargo build \
   --release \
   %{?_smp_mflags} \
   --offline \
   --target %_arch-unknown-linux-gnu

%pre
groupadd -r -f %zincati_group >/dev/null 2>&1 ||:
useradd -g %zincati_group -G root,wheel -c 'Zincati user for auto-updates' -M -d %zincati_home -s /dev/null -r -l %zincati_user >/dev/null 2>&1 ||:

%install
install -Dm 755 target/%_arch-unknown-linux-gnu/release/%name %buildroot/%zincati_bindir/%name
mkdir -p %buildroot{%zincati_confdir1,%zincati_confdir2,%zincati_dbus_systemd,%_unitdir}
install dist/config.d/* %buildroot%zincati_confdir1
install -Dm 444 dist/systemd/system/zincati.service %buildroot%_unitdir
install -Dm 755 dist/tmpfiles.d/zincati.conf  %buildroot%_tmpfilesdir/zincati.conf
install dist/dbus-1/system.d/org.coreos.zincati.conf %buildroot%zincati_dbus_systemd
install -Dm 755 alt-ostree %buildroot%_bindir/alt-ostree
ln -s alt-ostree %buildroot%_bindir/rpm-ostree
install -d -m 0755 %buildroot%zincati_home

%files
%zincati_bindir/*
%_bindir/*
%zincati_confdir1/*
%zincati_dbus_systemd/*
%_unitdir/*
%_tmpfilesdir/*
%attr(-,%zincati_user,%zincati_group) %dir %zincati_home

%dir
%zincati_confdir2
%doc *.md

%changelog
* Mon Sep 13 2021 Andrey Sokolov <keremet@altlinux.org> 0.0.22-alt3
- Fix zincati user adding

* Fri Sep 10 2021 Andrey Sokolov <keremet@altlinux.org> 0.0.22-alt2
- Fix zincati user adding

* Fri Sep 03 2021 Andrey Sokolov <keremet@altlinux.org> 0.0.22-alt1
- Init
