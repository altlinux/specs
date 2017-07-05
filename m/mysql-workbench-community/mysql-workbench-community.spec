Name: mysql-workbench-community
Version: 6.3.4
Release: alt3
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

Summary: A MySQL visual database modeling tool

License: %gpllgpl2only
Group: Development/Databases
Url: http://wb.mysql.com
Source0: %name-%version.tar.gz

Patch1: mysql-workbench-mariadb-build.patch
Patch2: mysql-workbench-mariadb-check.patch
Patch3: mysql-workbench-6.3.4-c++11.patch
Patch4: %name-%version-alt-gcc6.patch

Provides: mysql-workbench-oss = %version-%release
Obsoletes: mysql-workbench-oss < %version-%release
Provides: mysql-workbench-gpl = %version-%release
Obsoletes: mysql-workbench-gpl < %version-%release

Provides: mysql-administrator = %version-%release
Obsoletes: mysql-administrator < %version-%release

Provides: mysql-query-browser = %version-%release
Obsoletes: mysql-query-browser < %version-%release

# "_mforms" and "grt" are accessable from "MySQL Workbench GRT Shell" only.
%add_python_req_skip _mforms grt mforms

# internal Workbench's libraries
%add_python_req_skip wb workbench cairo_utils wb_common

# shell_snippets.py is not pure Python
%add_findreq_skiplist */mysql-workbench/shell_snippets.py

# templates only
%add_findreq_skiplist */mysql-workbench/script_templates/*

%add_findreq_skiplist */mysql-workbench/libraries/grt_python_debugger.py

Requires: python-module-paramiko python-module-pexpect
Requires: mysql-client gnome-keyring
Requires: %name-data = %version

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Mar 20 2011
# and edited manualy
# - removed mysql-workbench-gpl
# - boost-devel-headers changed to boost-devel
BuildRequires: boost-devel gcc-c++ libglade-devel libgnome-devel libgtkmm2-devel liblua5-devel libmysqlclient-devel libpcre-devel libsqlite3-devel libuuid-devel libxml2-devel libzip-devel python-devel

BuildRequires: boost-signals-devel

BuildRequires: libGL-devel
BuildRequires: libctemplate-devel
BuildRequires: libiodbc-devel

# 6.3.4
BuildRequires: rpm-macros-cmake cmake
BuildRequires: mysql-connector-c++-devel libXdmcp-devel libXdamage-devel libXxf86vm-devel
BuildRequires: swig libgdal-devel libpcrecpp-devel libpixman-devel libexpat-devel libvsqlite++-devel
BuildRequires: libgnome-keyring-devel libharfbuzz-devel libxshmfence-devel tinyxml-devel

%description
MySQL Workbench is modeling tool that allows you to design
and generate MySQL databases graphically.

%package data
Summary: Architecture independent files for %name
License: %gpllgpl2only
Group: Development/Databases
BuildArch: noarch
Conflicts: %name < %version
Conflicts: mysql-workbench-gpl-data

%description data
Architecture independent files for %name

%prep

%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2

sed -i "s|pcre.h|pcre/pcre.h|" library/base/util_functions.cpp

%set_verify_elf_method unresolved=relaxed

%build
%add_optflags -std=c++11
%cmake
cd BUILD
%make_build VERBOSE=1

%install
pushd %_builddir/%name-%version/BUILD
make install DESTDIR=%buildroot
popd

mkdir -p %buildroot%_niconsdir
cp %_builddir/%name-%version/images/icons/MySQLWorkbench-32.png %buildroot%_niconsdir/mysql-workbench.png

mkdir -p %buildroot%_iconsdir/hicolor/32x32/mimetypes
cp %_builddir/%name-%version/images/icons/MySQLPlugin-32.png %buildroot%_iconsdir/hicolor/32x32/mimetypes/application-vnd.mysql-workbench-plugin.png
cp %_builddir/%name-%version/images/icons/MySQLWorkbenchDocIcon32x32.png %buildroot%_iconsdir/hicolor/32x32/mimetypes/application-vnd.mysql-workbench-model.png

%files
%exclude %_libdir/mysql-workbench/modules/*.py?

%exclude %_datadir/applications/*.desktop
%exclude %_datadir/mysql-workbench/*

%doc COPYING COPYING.LGPL README AUTHORS
%exclude %_datadir/doc/mysql-workbench/COPYING
%exclude %_datadir/doc/mysql-workbench/README

%_bindir/mysql-workbench
%_bindir/mysql-workbench-bin
%_bindir/wbcopytables
%_bindir/wbcopytables-bin
%dir %_libdir/mysql-workbench
%_libdir/mysql-workbench/*

%files data
%_datadir/applications/*.desktop
%dir %_datadir/mysql-workbench
%_datadir/mysql-workbench/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_iconsdir/hicolor/128x128/apps/*
%_iconsdir/hicolor/16x16/mimetypes/*
%_iconsdir/hicolor/32x32/mimetypes/*
%_iconsdir/hicolor/48x48/mimetypes/*
%_iconsdir/hicolor/128x128/mimetypes/*
%_xdgmimedir/packages/*.xml
%_xdgdatadir/mime-info/*.mime

%changelog
* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.3.4-alt3
- Updated build with gcc-6

* Fri Oct 23 2015 Sergey Y. Afonin <asy@altlinux.ru> 6.3.4-alt2
- updated mysql-workbench-6.3.4-c++11.patch from http://bugs.mysql.com/78668

* Mon Oct 12 2015 Sergey Y. Afonin <asy@altlinux.ru> 6.3.4-alt1
- Updated to last release (renamed to mysql-workbench-community)
- Removed patches for mysql-workbench 5.x
- Fixed build with new libsigc++ (requires "-std=c++11" for c++)
- Added draft patch for support administration of MariaDB 10

* Fri Oct 09 2015 Sergey Y. Afonin <asy@altlinux.ru> 5.2.47-alt2
- Changed "MySQL-client" to "mysql-client" in "Requires" (ALT #31271)
- Used %%gpllgpl2only macro instead of %%gpl2only
- Warning: libmysqlclient-devel of MariaDB is used since 5.2.47-alt1.1

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.2.47-alt1.1.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2.47-alt1.1
- Rebuilt with new ctemplate

* Sat Mar 02 2013 Sergey Y. Afonin <asy@altlinux.ru> 5.2.47-alt1
- Update to last release

* Sun Jul 29 2012 Evgeny Sinelnikov <sin@altlinux.ru> 5.2.41-alt1
- Update to last release

* Thu Apr 26 2012 Evgeny Sinelnikov <sin@altlinux.ru> 5.2.39-alt1
- Update to last release
- Fix and delete unneeded old patches
- Add icon and mime files

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2.33-alt2.2
- Rebuilt with new glib2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.33-alt2.1
- Rebuild with Python-2.7

* Mon Mar 21 2011 Sergey Y. Afonin <asy@altlinux.ru> 5.2.33-alt2
- fixed building with libgtkmm2-2.24.0 (thanks to <iv@altlinux.org>)
- moved library.forms.Makefile.am.patch to alt-build.patch
- updated alt-build.patch for building with new libglade-devel
  (without requires libxml2-devel; thanks to <at@altlinux.ru>)
- fixed relative requires between mysql-workbench-gpl and
  mysql-workbench-gpl-data subpackages

* Sun Mar 13 2011 Sergey Y. Afonin <asy@altlinux.ru> 5.2.33-alt1
- New version

* Wed Dec 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.31a-alt1
- 5.2.31a

* Wed Oct 13 2010 Sergey Y. Afonin <asy@altlinux.ru> 5.2.29-alt1
- New version
- Architecture independent files moved to mysql-workbench-gpl-data subpackage
- Removed "Vendor" tag: not need in ALT Linux

* Mon Sep 27 2010 Sergey Y. Afonin <asy@altlinux.ru> 5.2.28-alt1
- New version

* Sun Aug 15 2010 Sergey Y. Afonin <asy@altlinux.ru> 5.2.26-alt1
- New version
- added libGL-devel to BuildRequires (14/08/2010 test rebuild failed for
  5.2.25-alt1 with "configure: error: OpenGL headers not found")

* Thu Jul 08 2010 Sergey Y. Afonin <asy@altlinux.ru> 5.2.25-alt1
- New version, renamed from mysql-workbench-oss to mysql-workbench-gpl
- Removed patch for linking problem with my_stat() (fixed in mainstream)
- Removed python-devel-static and rpm-build-compat from BuildRequires

* Sun May 02 2010 Evgeny Sinelnikov <sin@altlinux.ru> 5.2.20-alt1
- Update to new release (5.2.20 Beta 10)
- Fix linking problem with my_stat()

* Wed Apr 21 2010 Evgeny Sinelnikov <sin@altlinux.ru> 5.2.19-alt1
- Build new version for Sisyphus

* Fri Apr 02 2010 Sergey Y. Afonin <asy@altlinux.ru> 5.2.16-alt1
- Initial build for AltLinux (5.2.16 Beta 6)
