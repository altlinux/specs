%define _unpackaged_files_terminate_build 1
%define unstable 0
%define post_version 1

%define build_req_kde_ver 4.6.0
%define build_req_kdevplatform_ver 1.5.0
%define build_req_kdevelop_ver 4.5.0
%define build_req_kdev_pg_qt_ver 1.0.0

%if %unstable
%define pkg_sfx -pre4.5
%define pkg_sfx_other %nil
%define if_unstable() %{expand:%*}
%define if_stable() %nil
%else
%define pkg_sfx %nil
%define pkg_sfx_other -pre4.5
%define if_unstable()  %nil
%define if_stable() %{expand:%*}
%endif

%define kdevplatform kdevplatform%pkg_sfx
%define kdevplatform_other kdevplatform%pkg_sfx_other
%define kdevelop kdevelop%pkg_sfx
%define kdevelop_other kdevelop%pkg_sfx_other

%define kdevelop_pg_qt kdevelop-pg-qt

# temporary disable certain python paths as they contain a non-valid
# python code (and this is intended :/)
%add_findreq_skiplist %_K4apps/kdevpythonsupport/documentation_files/__builtin_types__.py
%add_findreq_skiplist %_K4apps/kdevpythonsupport/documentation_files/subprocess.py

Name: %kdevelop-for-python
Version: 1.5.2
Serial: 3
Release: alt1.git

Summary: Python Language Plugin for KDevelop.
License: GPLv2
Group: Development/Other
Url: https://projects.kde.org/projects/playground/devtools/plugins/kdev-python

Requires: %kdevelop-mini >= %build_req_kdevelop_ver
Requires: /usr/bin/python
Provides: kdev-python = %version-%release

Conflicts: %kdevelop_other-for-python
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevelop_other}-for-python < %version-%release

Source: kdev-python-%version.tar.bz2
%if %post_version
Patch0: kdev-python-post-%version.patch
%endif
Patch1: kdev-python-%version-altlinux-fix-build.patch

BuildRequires(pre): kde4libs-devel
BuildRequires: kde4libs-devel >= %build_req_kde_ver
BuildRequires: %kdevplatform-devel >= %build_req_kdevplatform_ver gcc-c++
BuildRequires: %kdevelop_pg_qt-devel >= %build_req_kdev_pg_qt_ver

%description
Python Language Plugin for KDevelop.

%prep
%setup -q -n kdev-python-%version
%if %post_version
%patch0 -p1
%endif
%patch1 -p1

%build
%K4cmake
%K4make

%install
%K4install

%K4find_lang --output=%name.lang --with-kde          kdevpython

%files -f %name.lang
%doc TODO
%_K4apps/kdevpythonsupport
%_K4lib/kcm_pep8.so
%_K4srv/kcm_kdevpythonpep8.desktop
%_K4lib/kdevpdb.so
%_K4srv/kdevpdb.desktop
%_K4lib/kdevpythonlanguagesupport.so
%_K4srv/kdevpythonsupport.desktop
%_libdir/libkdev4pythoncompletion.so
%_libdir/libkdev4pythonduchain.so
%_libdir/libkdev4pythonparser.so
%_libdir/libpython2.7-kdevelop.so*
%_K4apps/kdevappwizard/templates/*

%changelog
* Mon Nov 18 2013 Alexey Morozov <morozov@altlinux.org> 3:1.5.2-alt1.git
- Release v1.5.2 + a small bugfix (99cd20cdbcf85bc62902b7b8146f677ded6a7c95)

* Fri Jun  7 2013 Alexey Morozov <morozov@altlinux.org> 3:1.5.1-alt1
- Release 1.5.1

* Fri May  3 2013 Alexey Morozov <morozov@altlinux.org> 3:1.5.0-alt1
- Release 1.5.0 (actually, the same codebase as for previous RPM
  build)

* Tue Apr 30 2013 Alexey Morozov <morozov@altlinux.org> 3:1.4.90-alt1.git
- Initial build for ALTLinux: a preliminary version of python module for
  KDevelop-1.5.0

