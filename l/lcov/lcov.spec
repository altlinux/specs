# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lcov
Version: 1.9
Release: alt1

Summary: A graphical GCOV front-end
License: GPL
Group: Development/Tools
Url: http://ltp.sourceforge.net/coverage/lcov.php
Packager: Slava Semushin <php-coder@altlinux.ru>

Source: http://downloads.sourceforge.net/ltp/lcov-%version.tar.gz
Patch1: lcov-alt-src-findreq_hints.patch
BuildArch: noarch

BuildRequires: perl-GD

%description
LCOV is a graphical front-end for GCC's coverage testing tool gcov. It
collects gcov data for multiple source files and creates HTML pages
containing the source code annotated with coverage information. It
also adds overview pages for easy navigation within the file
structure.

%prep
%setup
%patch1 -p2

%install
%makeinstall_std PREFIX=%buildroot

%files
%doc README CHANGES
%_bindir/*
%_man1dir/*
%_man5dir/*
%_sysconfdir/lcovrc

%changelog
* Sat Dec 04 2010 Slava Semushin <php-coder@altlinux.ru> 1.9-alt1
- Updated to 1.9

* Sun Jul 25 2010 Slava Semushin <php-coder@altlinux.ru> 1.8-alt1
- Updated to 1.8

* Mon Oct 19 2009 Slava Semushin <php-coder@altlinux.ru> 1.7-alt2
- Added dependency to perl-GD which required by genpng (LP: #452352)

* Thu Feb 05 2009 Slava Semushin <php-coder@altlinux.ru> 1.7-alt1
- Initial build for ALT Linux Sisyphus

* Wed Aug 13 2008 Peter Oberparleiter (Peter.Oberparleiter@de.ibm.com)
- changed description + summary text
* Mon Aug 20 2007 Peter Oberparleiter (Peter.Oberparleiter@de.ibm.com)
- fixed "Copyright" tag
* Mon Jul 14 2003 Peter Oberparleiter (Peter.Oberparleiter@de.ibm.com)
- removed variables for version/release to support source rpm building
- added initial rm command in install section
* Mon Apr 7 2003 Peter Oberparleiter (Peter.Oberparleiter@de.ibm.com)
- implemented variables for version/release
* Fri Oct 8 2002 Peter Oberparleiter (Peter.Oberparleiter@de.ibm.com)
- created initial spec file
