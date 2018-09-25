%define skeldir %_sysconfdir/skel
%define skelfile .screenrc

Name: etcskel-screenrc
Version: 20180925
Release: alt1
BuildArch: noarch
BuildRequires: etcskel

Summary: GNU screen configuration for new users
Group: System/Configuration/Other
License: GPL

Source: %name-%version.tar.xz

%description
Default %summary

%prep
%setup

%install
%__install -d %buildroot%skeldir
%__install %skelfile %buildroot%skeldir/

%files
%config(noreplace) %_sysconfdir/skel/%skelfile

%changelog
* Tue Sep 25 2018 Gremlin from Kremlin <gremlin@altlinux.ru> 20180925-alt1
- disabled hardstatus (avoid TIOCSTI-related issues)
- reduced shelltitle length down to 1 symbol
- added more useful settings with detailed comments

* Tue Apr 20 2010 Mykola Grechukh <gns@altlinux.ru> 20100420-alt1
- first build
