Name: lcov
Version: 1.12
Release: alt1

Summary: LTP GCOV extension code coverage tool
Group: Development/Tools
License: GPLv2+
URL: http://ltp.sourceforge.net/coverage/lcov.php
BuildArch: noarch

# https://github.com/linux-test-project/lcov.git
# git://git.altlinux.org/gears/l/lcov.git
Source: %name-%version-%release.tar

Requires: gcc-common perl-GD

%define _unpackaged_files_terminate_build 1

%description
LCOV is an extension of GCOV, a GNU tool which provides information
about what parts of a program are actually executed (i.e. "covered")
while running a particular test case.  The extension consists of a set
of PERL scripts which build on the textual GCOV output to implement
HTML based output and support for large projects.

%prep
%setup -n %name-%version-%release
cat > .version <<EOF
VERSION=%version
RELEASE=%release
FULL=%version
EOF

%install
make install PREFIX=%buildroot

%files
%_bindir/*
%_man1dir/*
%_man5dir/*
%config(noreplace) %_sysconfdir/lcovrc

%changelog
* Wed Feb 03 2016 Dmitry V. Levin <ldv@altlinux.org> 1.12-alt1
- 1.10 -> v1.12-1-g79e9f28.

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
