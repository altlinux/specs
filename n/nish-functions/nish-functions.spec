Name: nish-functions
Version: 1.01
Release: alt4

Summary: Shell functions collection featuring isolated namespace
License: Public domain
Group: Development/Other
BuildArch: noarch
Packager: Fr. Br. George <george@altlinux.ru>

Source: %name-%version.tar

%description
Namespace-isolated shell functions (NISh-functions) is a posix shell
functions collection for reusing in shell scripts. It based on strong
namespace separation policy, self-documentation and ugly shell hacking.
No bash/zsh/whatever extension used. Runs on Linux and (losely) FreeBSD.

%prep
%setup

%build
%make LIBEXEC=lib

%install
%makeinstall DESTDIR=%buildroot LIBEXEC=lib

%files
%doc README
%_bindir/*
%dir %_libexecdir/nish
%_libexecdir/nish/*

%changelog
* Tue Nov 08 2011 Fr. Br. George <george@altlinux.ru> 1.01-alt4
- Uscan is used for download/rename

* Thu Jul 28 2011 Fr. Br. George <george@altlinux.ru> 1.01-alt3
- Bugfix and workflow adaptation

* Mon Jul 04 2011 Fr. Br. George <george@altlinux.ru> 1.01-alt2
Fix incomplete installation error

* Tue Jun 14 2011 Fr. Br. George <george@altlinux.ru> 1.01-alt1
- Debian uscan is used
- Xautomation module added
- Help and digest subsystes improved
- Additional functions and bugfixes

* Fri Sep 24 2010 Fr. Br. George <george@altlinux.ru> 0.6-alt1
- XTerm and ascii modules separated
- Autobuild module and uscan.pl added

* Fri Apr 10 2009 Fr. Br. George <george@altlinux.ru> 0.5.1-alt2
- Tab echoing compatibility
- IPCalc dependency avoid

* Sat Mar 21 2009 Fr. Br. George <george@altlinux.ru> 0.5.1-alt1
- Version up

* Thu Dec 18 2008 Fr. Br. George <george@altlinux.ru> 0.5-alt1
- Initial release

