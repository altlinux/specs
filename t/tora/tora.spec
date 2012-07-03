%define origname tora
Name: tora
Version: 2.1.3
Release: alt2.svn4289
Summary: TOra is an open-source multi-platform database management GUI
License: GPL
Group: Databases
Url: http://www.torasql.com
Packager: Andrew Clark <andyc@altlinux.ru>
Source: http://sourceforge.net/projects/tora/files/tora/2.1.3/%name-%version.tar.bz2

Source3: %name.png
Source4: %name.desktop

BuildRequires(pre): rpm-macros-cmake

# Automatically added by buildreq on Tue Jan 03 2012
# optimized out: cmake-modules fontconfig libpq-devel libqscintilla2-6-qt4 libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-xml libstdc++-devel
BuildRequires: cmake gcc-c++ libqscintilla2-qt4-devel phonon-devel postgresql-devel

%description
TOra is a Toolkit for Oracle which aims to help the DBA or
developer of database applications. Features PL/SQL debugger,
SQL worksheet with syntax highlighting, DB browser and a full
set of DBA tools. TOra also includes support for MySQL and Postgres.

%prep
%setup -n %name-%version

%build
%cmake -DCMAKE_INSTALL_PREFIX:PATH="%_prefix" \
       -DTORA_PLUGIN_DIR=CMAKE_INSTALL_PREFIX/share/tora \
       -DTORA_DOC_DIR=CMAKE_INSTALL_PREFIX/share/doc/tora \
       -DTORA_HELP_DIR=CMAKE_INSTALL_PREFIX/share/tora/help \
       -DENABLE_TERADATA=1 \
       -DENABLE_ORACLE=0 

%make_build -C BUILD/

%install
mkdir -p %buildroot/{%_bindir,%_datadir/%name/{i18n,help/images},%_docdir/%name,%_desktopdir,%_liconsdir}

install -pD -m 755 %_builddir/%name-%version/BUILD/src/%name %buildroot%_bindir/
install -pD -m 644 %_builddir/%name-%version/BUILD/src/*.qm %buildroot%_datadir/%name/i18n/ 
install -pD -m 644 %_builddir/%name-%version/doc/help/*.html %buildroot%_datadir/%name/help 
install -pD -m 644 %_builddir/%name-%version/doc/help/images/*.png %buildroot%_datadir/%name/help/images
install -pD -m 644 %_builddir/%name-%version/rpm/%name.desktop %buildroot%_desktopdir/%name.desktop

install -pm 644 %SOURCE3 %buildroot%_liconsdir/%name.png
install -pm 644 %SOURCE4 %buildroot%_desktopdir/%name.desktop

for i in $(ls | grep '^[A-Z]' | egrep -v "(Make|BUILD)"); do
	install -pD -m 644 %_builddir/%name-%version/$i %buildroot%_docdir/%name/
done 

%files
%_bindir/*
%_datadir/%name
%_docdir/%name
%_liconsdir/*
%_desktopdir/*

%changelog
* Mon Apr 30 2012 Andrew Clark <andyc@altlinux.ru> 2.1.3-alt2.svn4289
- version update to 2.1.3-alt1.svn4289

* Sun Feb 19 2012 Andrew Clark <andyc@altlinux.ru> 2.1.3-alt2.svn4238
- version update to 2.1.3-alt1.svn4238

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

