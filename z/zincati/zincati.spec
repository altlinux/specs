%define zincati_user    zincati
%define zincati_group   zincati

%define zincati_confdir1 %_libexecdir/%name/config.d/
%define zincati_confdir2 %_sysconfdir/%name/config.d/
%define zincati_dbus_systemd /usr/share/dbus-1/system.d/

%define zincati_bindir %{_prefix}/libexec/

Name:     zincati
Version:  0.0.22
Release:  alt1

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
if getent passwd zincati 
then
    userdel zincati
fi
if getent group zincati 
then
    groupdel zincati
fi
%_sbindir/useradd -c 'Zincati user for auto-updates' -M %name

%install
install -Dm 755 target/%_arch-unknown-linux-gnu/release/%name %buildroot/%zincati_bindir/%name
mkdir -p %buildroot{%zincati_confdir1,%zincati_confdir2,%zincati_dbus_systemd,%_unitdir}
install dist/config.d/* %buildroot%zincati_confdir1
install -Dm 444 dist/systemd/system/zincati.service %buildroot%_unitdir
install -Dm 755 dist/tmpfiles.d/zincati.conf  %buildroot%_tmpfilesdir/zincati.conf
install dist/dbus-1/system.d/org.coreos.zincati.conf %buildroot%zincati_dbus_systemd
install -Dm 755 alt-ostree %buildroot%_bindir/alt-ostree
ln -s alt-ostree %buildroot%_bindir/rpm-ostree

%files
%zincati_bindir/*
%_bindir/*
%zincati_confdir1/*
%zincati_dbus_systemd/*
%_unitdir/*
%_tmpfilesdir/*

%dir
%zincati_confdir2
%doc *.md

%changelog
* Fri Sep 03 2021 Andrey Sokolov <keremet@altlinux.org> 0.0.22-alt1
- Init
