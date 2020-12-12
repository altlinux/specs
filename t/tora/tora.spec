Name: tora
Version: 3.2
Release: alt6.git1a03ec3d
Summary: TOra is an open-source multi-platform database management GUI
License: GPL
Group: Databases
Url: https://github.com/tora-tool/tora/wiki

ExclusiveArch: %ix86 x86_64

# https://github.com/tora-tool/tora.git
Source: %name-%version.tar
Source2: %name.png

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ postgresql-devel boost-devel libferrisloki-devel
BuildRequires: qt5-base-devel qt5-tools-devel libqscintilla2-qt5-devel

%description
TOra is a Toolkit for Oracle which aims to help the DBA or
developer of database applications. Features PL/SQL debugger,
SQL worksheet with syntax highlighting, DB browser and a full
set of DBA tools. TOra also includes support for MySQL and Postgres.

%prep
%setup

%build
%cmake_insource \
	-DWANT_INTERNAL_QSCINTILLA=OFF \
	-DWANT_INTERNAL_LOKI=OFF \
	-DENABLE_ORACLE=0 \
	-DLOKI_LIBRARY="$(pkg-config --variable=libdir ferrisloki)/libferrisloki.so" \
	-DLOKI_INCLUDE_DIR="$(pkg-config --variable=includedir ferrisloki)/FerrisLoki"

%make_build

%install
%makeinstall_std
mkdir -p %buildroot/{%_liconsdir,%_desktopdir}

install -pm 644 %SOURCE2 %buildroot%_liconsdir/%name.png
install -pm 644 src/tora.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc AUTHORS ChangeLog COPYING* copyright.txt ISSUES README README.md 
%_bindir/*
%_datadir/%name-%version
%_liconsdir/*
%_desktopdir/*

%changelog
* Sat Dec 12 2020 Andrey Sokolov <keremet@altlinux.ru> 3.2-alt6.git1a03ec3d
- Updated to v3.2-292-g1a03ec3d (closes: 39434)

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 3.2-alt5
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 3.2-alt4
- NMU: remove %ubt from release

* Fri Sep 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2-alt3%ubt
- Fixed build with new Qt.

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2-alt2%ubt
- Rebuilt with qscintilla2 2.10.1.

* Wed Oct 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2-alt1%ubt
- Updated to upstream version 3.2.

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4-alt1.svn4502.2
- Rebuilt with qscintilla2 2.9

* Sat Nov 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4-alt1.svn4502.1
- Rebuilt with new qscintilla2

* Sat Dec 22 2012 Andrew Clark <andyc@altlinux.ru> 2.1.4-alt1.svn4502
- version update to 2.1.4-alt1.svn4502

* Fri Dec 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4-alt1.svn4398.1
- Rebuilt with new qscintilla2

* Wed Aug 29 2012 Andrew Clark <andyc@altlinux.ru> 2.1.4-alt1.svn4398
- version update to 2.1.4-alt1.svn4398

* Mon Apr 30 2012 Andrew Clark <andyc@altlinux.ru> 2.1.3-alt2.svn4289
- version update to 2.1.3-alt2.svn4289

* Sun Feb 19 2012 Andrew Clark <andyc@altlinux.ru> 2.1.3-alt2.svn4238
- version update to 2.1.3-alt2.svn4238

* Mon Jan 2 2012 Andrew Clark <andyc@altlinux.ru> 2.1.3-alt2.svn4200
- buildreq

* Sat Dec 31 2011 Andrew Clark <andyc@altlinux.ru> 2.1.3-alt1.svn4200
- version update to 2.1.3-alt1.svn4200

* Sun Nov 13 2011 Andrew Clark <andyc@altlinux.ru> 2.1.3-alt1.svn4135
- version update to 2.1.3-alt1.svn4135

* Sun Sep 4 2011 Andrew Clark <andyc@altlinux.ru> 2.1.3-alt1.svn4045
- version update to 2.1.3-alt1.svn4045

* Wed Aug 17 2011 Andrew Clark <andyc@altlinux.ru> 2.1.3-alt1.svn4036
- version update to 2.1.3-alt1.svn4036

* Sun Jul 24 2011 Andrew Clark <andyc@altlinux.ru> 2.1.3-alt1.svn4005
- version update to 2.1.3-alt1.svn4005

* Sun Jul 24 2011 Andrew Clark <andyc@altlinux.ru> 2.1.3-alt1.svn3997
- version update to 2.1.3-alt1.svn3997
- desktop file and icon file added

* Thu Jun 9 2011 Andrew Clark <andyc@altlinux.ru> 2.1.3-alt1.svn3971
- initial build for ALT.

