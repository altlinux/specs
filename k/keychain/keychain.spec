Name: keychain
Version: 2.6.8
Release: alt1
Summary: agent manager for OpenSSH, ssh.com, Sun SSH, and GnuPG
Packager: Kirill Maslinsky <kirill@altlinux.org>
Url: http://www.gentoo.org/proj/en/keychain/index.xml
Source0: %name-%version.tar.bz2
License: GPL v2
Group: Networking/Remote access
BuildArch: noarch

%description
Keychain is a manager for OpenSSH, ssh.com, Sun SSH and GnuPG agents.
It acts as a front-end to the agents, allowing you to easily have one
long-running agent process per system, rather than per login session.
This dramatically reduces the number of times you need to enter your
passphrase from once per new login session to once every time your
local machine is rebooted.

%prep
%setup -q

%build
%install
mkdir -p %buildroot/%_bindir %buildroot/%_man1dir
install -m0755 keychain %buildroot/%_bindir/keychain
install -m0644 keychain.1 %buildroot/%_man1dir

%files
%_bindir/keychain
%doc %_man1dir/*
%doc ChangeLog COPYING keychain.pod README

%changelog
* Tue Aug 28 2007 Kirill Maslinsky <kirill@altlinux.org> 2.6.8-alt1
- Initial build for Sisyphus
	(based on rpm package by Aron Griffis)

