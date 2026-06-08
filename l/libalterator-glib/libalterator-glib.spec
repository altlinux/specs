%define _unpackaged_files_terminate_build 1
%define _name alterator-glib
%define soversion %(cmake -P %SOURCE1 %SOURCE2 2>&1)

Name:          lib%_name
Version:       0.1.7
Release:       alt3
Group:         System/Libraries
Summary:       Library for alterator objects
License:       LGPLv3+
Url:           https://altlinux.space/alterator/libalterator-glib
Vcs:           https://altlinux.space/alterator/libalterator-glib.git

Source:        %name-%version.tar
Source1:       get_soversion.cmake
Source2:       CMakeLists.txt
BuildRequires(pre): cmake
BuildRequires: libtomlc99-devel
BuildRequires: libcheck-devel
BuildRequires: glib2-devel
BuildRequires: libdbus-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libcjson-devel
BuildRequires: libgio-devel
BuildRequires: gobject-introspection-devel
BuildRequires: vala-tools
BuildRequires: libpolkit-devel

%description
Library for alterator objects.

%package -n %name%soversion
Group: System/Libraries
Summary: Library for alterator objects
Requires: alterator-backend-packages >= 0.2.14-alt1
Requires: alterator-backend-component >= 0.3.1
Requires: alterator-backend-systeminfo >= 0.4.2
Requires: alterator-backend-edition >= 0.4.1
Requires: alt-components-base >= 0.7.12-alt1
Requires: alterator-interface-diag >= 0.1.4
Provides: %name = %EVR

%description -n %name%soversion
Library for alterator objects.

%package       devel
Group:         Development/C
Summary:       Library for alterator objects development files
Requires:      %name%soversion = %EVR

%description   devel
Library for alterator objects development files.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files -n %name%soversion
%doc README*
%_libdir/%name.so.*
%_typelibdir/Alterator-1.0.typelib

%files         devel
%_includedir/%_name
%_libdir/%name.so
%_pkgconfigdir/*.pc
%_girdir/Alterator-1.0.gir
%_vapidir/%_name.vapi

%check
cd src/tests
../../%_cmake__builddir/src/tests/libalterator-glib-tests

%changelog
* Mon Jun 08 2026 Vasiliy Doylov <neko@altlinux.org> 0.1.7-alt3
- Fix package dependencies.

* Mon Jun 08 2026 Vasiliy Doylov <neko@altlinux.org> 0.1.7-alt2
- Fix package provides.

* Fri Jun 05 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.7-alt1
- Update version to 0.1.7.

* Fri Jun 05 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.6-alt1
- Update version to 0.1.6.

* Thu Jun 04 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.5-alt1
- Update version to 0.1.5.

* Wed Jun 03 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.4-alt1
- Update version to 0.1.4.

* Thu May 21 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.3-alt1
- Update version to 0.1.3.

* Fri May 08 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.2-alt1
- Update version to 0.1.2.

* Fri May 08 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.1-alt1
- Update version to 0.1.1.
- Add test execution.

* Sat Mar 14 2026 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt2
- Initial build for Sisyphus in accordance with shared libraries policy.
- The project has been moved to the alterator organization on altlinux.space.

* Tue Mar 10 2026 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- Initial build
