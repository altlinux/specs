%define _unpackaged_files_terminate_build 1

Name: lcov
Version: 1.10
Release: alt1

Summary: A graphical GCOV front-end
Group: Development/Tools
License: GPL
URL: http://ltp.sourceforge.net/coverage/lcov.php

Source: http://downloads.sourceforge.net/ltp/lcov-%version.tar.gz
Patch: lcov-1.10-fc-gcc-47-unreachable.patch

BuildArch: noarch
Requires: gcc-common perl-GD

%description
LCOV is a graphical front-end for GCC's coverage testing tool gcov.
It collects gcov data for multiple source files and creates HTML pages
containing the source code annotated with coverage information. It also
adds overview pages for easy navigation within the file structure.

%prep
%setup
%patch -p1

%install
%make install PREFIX=%buildroot

%files
%_bindir/gendesc
%_bindir/genhtml
%_bindir/geninfo
%_bindir/genpng
%_bindir/%name
%_man1dir/gendesc.1.*
%_man1dir/genhtml.1.*
%_man1dir/geninfo.1.*
%_man1dir/genpng.1.*
%_man1dir/%name.1.*
%_man5dir/lcovrc.5.*
%config(noreplace) %_sysconfdir/lcovrc
%doc README CHANGES

%changelog
* Tue Apr 09 2013 Yuri N. Sedunov <aris@altlinux.org> 1.10-alt1
- 1.9.10

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

