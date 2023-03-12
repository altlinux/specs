# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: cppcheck
Version: 2.10.2
Release: alt1

Summary: A tool for static C/C++ code analysis
License: GPLv3
Group: Development/Tools

Url: https://github.com/danmar/cppcheck
# Source-url: https://github.com/danmar/cppcheck/archive/%version.tar.gz
Source: %name-%version.tar

Patch2: cppcheck-1.78-norebuild.patch
Patch4: cppcheck-1.72-test_32.patch
Patch8: cppcheck-2.2-translations.patch
Patch10: cppcheck-2.8-kate.patch

BuildRequires: gcc-c++
BuildRequires: qt5-base-devel qt5-tools-devel qt5-charts-devel
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: docbook-style-xsl libpcre-devel xsltproc
BuildRequires: libtinyxml2-devel
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-cmake

%add_python3_req_skip cppcheckdata misra_9 cppcheck

%description
Static analysis of C/C++ code. Checks for: memory leaks, mismatching
allocation-deallocation, buffer overrun, and many more. The goal is
0%% false positives.

%package gui
Summary: Qt version of %name, %summary
Group: Development/Tools
Requires: %name = %EVR
Requires: icon-theme-hicolor

%description gui
%summary

%prep
%setup

%__subst 's|/usr/share/sgml/docbook/stylesheet/xsl/nwalsh/manpages/docbook.xsl|/usr/share/xml/docbook/xsl-stylesheets/manpages/docbook.xsl|' \
 Makefile man/cppcheck.1.xml tools/dmake.cpp

%patch2 -p1

%ifnarch x86_64
%patch4 -p1
%endif

%patch8 -p1
%patch10 -p1

%__subst 's|/usr/bin/env python.*$|%__python3|' htmlreport/{cppcheck-htmlreport,*.py} addons/*.py tools/*.py

%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -name '*.cpp' -o -name '*.hpp' -o -name '*.c' -o -name '*.h' |
	xargs -r sed -ri 's,^\xEF\xBB\xBF,,'
%endif

# Make sure bundled tinyxml2 is not used
#rm -r externals/tinyxml2



%build
%cmake \
	-G'Unix Makefiles' \
	-DCMAKE_BUILD_TYPE=Release \
	-DUSE_MATCHCOMPILER:BOOL=ON \
	-DHAVE_RULES:BOOL=ON \
	-DBUILD_GUI:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DBUILD_TESTS:BOOL=ON \
	-DFILESDIR=%{_datadir}/Cppcheck \
	-DPCRE_INCLUDE="%_includedir/pcre" \
	%nil

%cmake_build

%make man

# Generate html documentation
for N in man/*.docbook; do
  xsltproc -o ${N%%.docbook}.html \
	/usr/share/xml/docbook/xsl-stylesheets/xhtml/docbook.xsl $N
done

%install
%cmakeinstall_std

install -pD -m 644 %name.1 %buildroot%_man1dir/%name.1

# Install htmlreport
install -pD -m 755 htmlreport/cppcheck-htmlreport %buildroot%_bindir/cppcheck-htmlreport
# Restore execute permission of python files
grep -l "#\!%__python3" %buildroot%_datadir/Cppcheck/addons/*.py | xargs chmod +x

%check
#cmake_build --target check

%files
%doc readme.txt man/*.html
%_bindir/%name
%_bindir/%name-htmlreport
%_man1dir/%name.1*
%dir %_datadir/Cppcheck/
%_datadir/Cppcheck/addons/
%_datadir/Cppcheck/cfg/
%_datadir/Cppcheck/platforms/

%files gui
%doc gui/help/manual.html
%_bindir/%name-gui
%_datadir/Cppcheck/lang
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*

%changelog
* Sun Mar 12 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2.10.2-alt1
- New Version

* Sun Feb 12 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2.10.0-alt1
- New Version

* Mon Jan 23 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2.9.3-alt1
- Vesion 2.9.3

* Sat Oct 01 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2.9.0-alt1
- Vesion 2.9

* Mon Aug 01 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2.8.2-alt1
- Version 2.8.2

* Sun May 22 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2.8-alt2
- Add cppcheck-2.8-kate.patch

* Sat May 21 2022 Andrew A. Vasilyev <andy@altlinux.org> 2.8-alt1
- 2.8

* Mon Apr 18 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2.7.5-alt1
- 2.7.5

* Fri Mar 25 2022 Andrew A. Vasilyev <andy@altlinux.org> 2.7.4-alt1
- 2.7.4

* Mon Mar 21 2022 Andrew A. Vasilyev <andy@altlinux.org> 2.7.3-alt1
- 2.7.3

* Sat Mar 12 2022 Andrew A. Vasilyev <andy@altlinux.org> 2.7.1-alt1
- 2.7.1

* Sat Feb 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 2.7-alt1
- 2.7

* Fri Dec 17 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.6.3-alt1
- 2.6.3

* Tue Nov 23 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.6.2-alt1
- 2.6.2

* Mon Oct 25 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.6.1-alt1
- 2.6.1

* Thu Oct 07 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.6-alt1
- 2.6

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 2.2-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu Oct 08 2020 Anton Farygin <rider@altlinux.ru> 2.2-alt1
- 2.2
- cleanup spec

* Sat Jan 25 2020 Vitaly Lipatov <lav@altlinux.ru> 1.90-alt1
- NMU: new version 1.90 (with rpmrb script)
- cleanup build, switch to python3

* Sat Aug 31 2019 Michael Shigorin <mike@altlinux.org> 1.88-alt2
- E2K: strip UTF-8 BOM for lcc < 1.24

* Wed Aug 07 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.88-alt1
- Updated to upstream version 1.88.

* Thu Jan 25 2018 Hihin Ruslan <ruslandh@altlinux.ru> 1.82-alt1_git_de7aa8f.1
- Fix cppcheck-1.82-appPath.patch

* Thu Jan 18 2018 Hihin Ruslan <ruslandh@altlinux.ru> 1.82-alt1_git_de7aa8f
- Update from git commit  de7aa8f5134a4b666ce642f3108ae3121f77905b

* Sun Aug 20 2017 Hihin Ruslan <ruslandh@altlinux.ru> 1.80-alt1
- Version 1.80

* Sat May 27 2017 Hihin Ruslan <ruslandh@altlinux.ru> 1.79-alt1.1
- Version 1.79

* Fri May 19 2017 Fr. Br. George <george@altlinux.ru> 1.79-alt1
- Autobuild version bump to 1.79

* Thu Apr 27 2017 Hihin Ruslan <ruslandh@altlinux.ru> 1.78-alt1
- Version 1.78

* Wed Mar 08 2017 Hihin Ruslan <ruslandh@altlinux.ru> 1.77-alt1
- Version 1.77

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 1.76.1-alt1
- Autobuild version bump to 1.76.1

* Tue Oct 18 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.76-alt1.1
- Version 1.76.1

* Sun Oct 09 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.76-alt1
- Version 1.76

* Sat Aug 13 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.75-alt1
- Version 1.75

* Wed Jul 20 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.74-alt1.3eef
- Update from  git://github.com/danmar/cppcheck.git

* Sat Jun 11 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.74-alt1
- Version 1.74

* Thu Feb 25 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.72-alt1
- Version 1.72

* Sat Nov 21 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.71-alt2
- Fix Version in help

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 1.71-alt1
- Autobuild version bump to 1.71

* Sun Nov 01 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.70-alt1
- Version 1.70

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 1.69-alt1
- Autobuild version bump to 1.69

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 1.68-alt1
- Autobuild version bump to 1.68

* Tue Nov 25 2014 Fr. Br. George <george@altlinux.ru> 1.67-alt1
- Autobuild version bump to 1.67
- Package config file
- Build Qt GUI and package separately

* Wed May 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.65-alt1
- Version 1.65

* Mon Nov 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.62-alt1
- Version 1.62

* Tue Jun 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.60.1-alt1
- Version 1.60.1

* Fri Feb 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.58-alt1
- Version 1.58

* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.55-alt1
- Version 1.55

* Sat Sep 17 2011 Slava Semushin <php-coder@altlinux.ru> 1.50-alt1
- Updated to 1.50

* Fri May 06 2011 Slava Semushin <php-coder@altlinux.ru> 1.48-alt1
- Updated to 1.48
- I not maintain this package any more

* Thu Feb 10 2011 Slava Semushin <php-coder@altlinux.ru> 1.47-alt1
- Updated to 1.47

* Wed Dec 29 2010 Slava Semushin <php-coder@altlinux.ru> 1.46.1-alt1
- Updated to 1.46.1

* Sat Oct 30 2010 Slava Semushin <php-coder@altlinux.ru> 1.45-alt1
- Updated to 1.45

* Fri Jul 16 2010 Slava Semushin <php-coder@altlinux.ru> 1.44-alt1
- Updated to 1.44

* Mon May 10 2010 Slava Semushin <php-coder@altlinux.ru> 1.43-alt1
- Updated to 1.43

* Thu Mar 11 2010 Slava Semushin <php-coder@altlinux.ru> 1.42-alt1
- Updated to 1.42

* Sun Jan 17 2010 Slava Semushin <php-coder@altlinux.ru> 1.40-alt1
- Updated to 1.40

* Sat Dec 12 2009 Slava Semushin <php-coder@altlinux.ru> 1.39-alt1
- Updated to 1.39
- Include manual.html to documentation

* Sat Oct 31 2009 Slava Semushin <php-coder@altlinux.ru> 1.38-alt1
- Updated to 1.38
- Moved "make test" to %%check section

* Wed Sep 23 2009 Slava Semushin <php-coder@altlinux.ru> 1.37-alt1
- Updated to 1.37

* Sun Aug 16 2009 Slava Semushin <php-coder@altlinux.ru> 1.35-alt1
- Updated to 1.35

* Sun Jul 12 2009 Slava Semushin <php-coder@altlinux.ru> 1.34-alt1
- Updated to 1.34

* Wed Jun 10 2009 Slava Semushin <php-coder@altlinux.ru> 1.33-alt1
- Updated to 1.33
- Run test suite during build

* Mon May 11 2009 Slava Semushin <php-coder@altlinux.ru> 1.32-alt1
- Updated to 1.32

* Tue May 05 2009 Slava Semushin <php-coder@altlinux.ru> 1.31-alt1
- Initial build for ALT Linux


