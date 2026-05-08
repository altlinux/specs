%define _unpackaged_files_terminate_build 1
%define _name alterator-glib
%define soversion %(cmake -P %SOURCE1 %SOURCE2 2>&1)

Name:          lib%_name
Version:       0.1.2
Release:       alt1
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
Obsoletes: %name

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
