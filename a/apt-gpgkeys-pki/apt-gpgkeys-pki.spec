Name: apt-gpgkeys-pki
Version: 0.1
Release: alt1

Summary: APT PKI for external GnuPG keys
License: GPL-2.0-or-later
Group: System/Configuration/Other
URL: https://altlinux.space/ALTLinux/apt-gpgkeys-pki.git

BuildArch: noarch

%define aptconf apt-gpgkeys.conf
%define utilname apt-gpgkeys
%define filetrigger apt-gpgkeys.filetrigger

Source: %name-%version.tar

BuildPreReq: gnupg, libshell
Requires: alt-gpgkeys

%description
The APT Public Key Infrastructure for external GnuPG keys.

%prep
%setup -q

%install
%define aptconfdir %_sysconfdir/apt/apt.conf.d
mkdir -p %buildroot%aptconfdir
install -pm644 %aptconf \
	%buildroot%aptconfdir/

%define aptgpgdir %_sysconfdir/pki/apt-gpg
mkdir -p %buildroot%aptgpgdir/{sources,blacklist,extracted}
touch %buildroot%aptgpgdir/extracted/{gpg.conf,pubring.gpg,secring.gpg}

%define aptgpgdatadir %_datadir/pki/apt-gpg
mkdir -p %buildroot%aptgpgdatadir/{sources,blacklist}

mkdir -p %buildroot%_rpmlibdir
install -pm644 %filetrigger \
	%buildroot%_rpmlibdir/

mkdir -p %buildroot%_bindir
install -pm755 %utilname \
	%buildroot%_bindir/

%define _unpackaged_files_terminate_build 1

%post
# Initial extracted apt gpgkeys after install or upgrade.
%utilname update

%files
%aptconfdir/%aptconf
%dir %aptgpgdir/
%dir %aptgpgdir/*
%ghost %aptgpgdir/extracted/*
%dir %aptgpgdatadir/
%dir %aptgpgdatadir/*
%_bindir/%utilname
%_rpmlibdir/%filetrigger

%changelog
* Fri Oct 10 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.1-alt1
- Initial APT PKI for external GnuPG keys.

