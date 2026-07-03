%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: atinout
Version: 0.9.1.0.15.g4013
Release: alt2

Summary: A command line tool for interation with AT modem

Group: System/Kernel and hardware
License: GPLv3+
Url: https://atinout.sourceforge.net/index.html
#Vcs0: git://git.code.sf.net/p/atinout/code
Vcs: https://github.com/beralt/atinout

Source: %name-%version.tar

BuildRequires: ronn groff-base

%description
This program will read a file (or stdin) containing a list of AT
commands. Each command will be send to the modem, and all the response
for the command will be output to file (or stdout).

%prep
%setup

%build
%make_build atinout.1 all

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/%name.1*
%doc Changelog README FAQ

%changelog
* Fri Jul 03 2026 Andrew Savchenko <bircoph@altlinux.org> 0.9.1.0.15.g4013-alt2
- Fix ftbfs

* Sat Dec 07 2024 Andrew Savchenko <bircoph@altlinux.org> 0.9.1.0.15.g4013-alt1
- Initial version.
