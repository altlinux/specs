Name:		netinst-overlays
Version:	0.02
Release:	alt1
License:	BSD
Summary:	Managing ALT Linux netinst-style ISO patches
Group:		System/Configuration/Networking
BuildArch:	noarch
Source:		%name-%version.tar

%description
A set of server and client scripts for managing
ALT Linux netinst-style filesystem patches.

%prep
%setup

%install
install -d %buildroot%_bindir
install overlays-* %buildroot%_bindir/

%files
%_bindir/*

%changelog
* Tue Jan 30 2018 Arseny Maslennikov <arseny@altlinux.org> 0.02-alt1
- Added dependency on libshell(shell-getopt).
- Added some configuration command-line options.
- Scripts now act properly if the distro uses systemd.
- Config file can now be stored in root's $XDG_CONFIG_HOME.

* Thu Mar 20 2014 Fr. Br. George <george@altlinux.ru> 0.01-alt1
- Initial build as RPM
