Name: mysql-workbench-gpl
Version: 5.2.33
Release: alt2.2
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

Summary: A MySQL visual database modeling tool

License: %gpl2only
Group: Development/Databases
Url: http://wb.mysql.com
Source0: %name-%version.tar.gz

Patch1: mysql-workbench-gpl-5.2.33-alt-build.patch
Patch2: mysql-workbench-gpl-5.2.33-MySQLWorkbench.desktop.in.patch
Patch3: mysql-workbench-gpl-5.2.31a-alt-libgtkmm2-2.24-fix-build.patch
Patch4: mysql-workbench-gpl-5.2.33-alt-glib2-2.32.0.patch

Provides: mysql-workbench-oss = %version-%release
Obsoletes: mysql-workbench-oss < %version-%release

Provides: mysql-administrator = %version-%release
Obsoletes: mysql-administrator < %version-%release

Provides: mysql-query-browser = %version-%release
Obsoletes: mysql-query-browser < %version-%release

# "_mforms" and "grt" are accessable from "MySQL Workbench GRT Shell" only.
%add_python_req_skip _mforms grt

# internal Workbench's libraries
%add_python_req_skip db_utils wb

# shell_snippets.py is not pure Python
%add_findreq_skiplist */mysql-workbench/shell_snippets.py

# templates only
%add_findreq_skiplist */mysql-workbench/script_templates/*

%add_findreq_skiplist */mysql-workbench/libraries/grt_python_debugger.py

Requires: python-module-paramiko python-module-pexpect
Requires: MySQL-client gnome-keyring
Requires: %name-data = %version

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Mar 20 2011
# and edited manualy
# - removed mysql-workbench-gpl
# - boost-devel-headers changed to boost-devel
BuildRequires: boost-devel gcc-c++ libglade-devel libgnome-devel libgtkmm2-devel liblua5-devel libmysqlclient-devel libpcre-devel libsqlite3-devel libuuid-devel libxml2-devel libzip-devel python-devel


BuildRequires: libGL-devel

%description
MySQL Workbench is modeling tool that allows you to design
and generate MySQL databases graphically.

%package data
Summary: Architecture independent files for %name
License: %gpl2only
Group: Development/Databases
BuildArch: noarch
Conflicts: %name < %version

%description data
Architecture independent files for %name

%prep

%setup -q

%patch1 -p1
%patch2 -p0
%patch3 -p2
%patch4 -p2

%set_verify_elf_method unresolved=relaxed

%build

NOCONFIGURE=yes ./autogen.sh

export LIBS="-lgthread-2.0"

%configure --disable-debug

%make_build

%install

%makeinstall_std

%files
%exclude %_libdir/mysql-workbench/*.*a
%exclude %_libdir/mysql-workbench/plugins/*.*a
%exclude %_libdir/mysql-workbench/modules/*.*a
%exclude %_libdir/mysql-workbench/modules/*.py?

%exclude %_datadir/applications/*.desktop
%exclude %_datadir/mysql-workbench/*

%doc COPYING README
%exclude %_datadir/doc/mysql-workbench/COPYING
%exclude %_datadir/doc/mysql-workbench/README

%_bindir/mysql-workbench
%_bindir/mysql-workbench-bin
%dir %_libdir/mysql-workbench
%_libdir/mysql-workbench/*

%files data
%_datadir/applications/*.desktop
%dir %_datadir/mysql-workbench
%_datadir/mysql-workbench/*

%changelog
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
