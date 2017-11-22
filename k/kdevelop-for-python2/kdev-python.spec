%define _unpackaged_files_terminate_build 1
%define unstable 0
%define post_version 1

%define build_req_kde_ver 4.6.0
%define build_req_kdevplatform_ver 1.7.0
%define build_req_kdevelop_ver 4.7.0
%define build_req_kdev_pg_qt_ver 1.0.0

%if %unstable
%define pkg_sfx -pre4.7
%define pkg_sfx_other %nil
%define if_unstable() %{expand:%*}
%define if_stable() %nil
%else
%define pkg_sfx %nil
%define pkg_sfx_other -pre4.7
%define if_unstable()  %nil
%define if_stable() %{expand:%*}
%endif

%define kdevplatform kdevplatform%pkg_sfx
%define kdevplatform_other kdevplatform%pkg_sfx_other
%define kdevelop kdevelop%pkg_sfx
%define kdevelop_other kdevelop%pkg_sfx_other

%define kdevelop_pg_qt kdevelop-pg-qt

# Skip python requires in documentation and correction files
%add_findreq_skiplist %_K4apps/kdevpythonsupport/documentation_files/* %_K4apps/kdevpythonsupport/correction_files/*

Name: %kdevelop-for-python2
Version: 1.7.3
Serial: 3
Release: alt1.git

Summary: Python-2.x Language Plugin for KDevelop.
License: GPLv2
Group: Development/Other
Url: https://projects.kde.org/projects/playground/devtools/plugins/kdev-python

Requires: %kdevelop-mini >= %build_req_kdevelop_ver
Requires: /usr/bin/python2
Provides: kdev-python = %version-%release
Provides: %kdevelop-for-python = %version-%release
Obsoletes: %kdevelop-for-python < %version-%release

Conflicts: %kdevelop_other-for-python2 %kdevelop_other-for-python
# Only stable package replaces unstable counterpart
%if !%unstable
Obsoletes: %{kdevelop_other}-for-python2 < %version-%release
Obsoletes: %{kdevelop_other}-for-python < %version-%release
%endif

Source: kdev-python2-%version.tar.bz2
Source1: kdev-python2-translations-%version.tar.bz2
%if %post_version
Patch0: kdev-python2-post-%version.patch
%endif
Patch1: kdev-python2-%version-altlinux-fix-build.patch
Patch2: kdev-python2-translations-%version-alt.patch

BuildRequires(pre): kde4libs-devel
BuildRequires: kde4libs-devel >= %build_req_kde_ver
BuildRequires: %kdevplatform-devel >= %build_req_kdevplatform_ver gcc-c++
BuildRequires: %kdevelop_pg_qt-devel >= %build_req_kdev_pg_qt_ver

%description
Python-2.x Language Plugin for KDevelop.

%prep
%setup -q  -a 1 -n kdev-python2-%version
%if %post_version
%patch0 -p1
%endif
%patch1 -p1
cd po
%patch2 -p1
cd ..

cat >>CMakeLists.txt <<EOF

include(MacroOptionalAddSubdirectory)
macro_optional_add_subdirectory( po )
EOF

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
%_K4lib/kcm_docfiles.so
%_K4conf/kdev_python_docfiles.knsrc
%_K4srv/kcm_kdevpythondocfiles.desktop
%_libdir/libkdev4pythoncompletion.so
%_libdir/libkdev4pythonduchain.so
%_libdir/libkdev4pythonparser.so
%_libdir/libpython2.7-kdevelop.so*
%_K4apps/kdevappwizard/templates/*

%changelog
* Wed Nov 22 2017 Oleg Solovyov <mcpain@altlinux.org> 3:1.7.3-alt1.git
- v1.7.3

* Fri Nov 13 2015 Alexey Morozov <morozov@altlinux.org> 3:1.7.2-alt1.git
- v1.7.2 + cfc34cd3914f6b8b882d900cec3a1e2b2bf5336b build fix

* Tue Jan 13 2015 Alexey Morozov <morozov@altlinux.org> 3:1.7.0-alt1.git
- Package renamed to kdevelop-for-python2 (a module for Python-3.x is
  packaged separately)
- v1.7.0 + 1 post-release fix (a723b77167b8d5aad7c9f6a5728a0633967a1f1a)
- Added translations

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

