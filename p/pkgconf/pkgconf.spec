%define sover 5

%def_disable snapshot
# have no kyua for armh
%ifarch armh
%def_disable check
%else
%def_enable check
%endif

Name: pkgconf
Version: 2.3.0
Release: alt1

Summary: Package compiler and linker metadata toolkit
Group: Development/Other
License: MIT
Url: https://pkgconf.org/

%if_disabled snapshot
Source: https://distfiles.dereferenced.org/%name/%name-%version.tar.xz
%else
Vcs: https://github.com/pkgconf/pkgconf.git
Source: %name-%version.tar
%endif

Requires: lib%name = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): meson
%{?_enable_check:BuildRequires: kyua atf-tests}

%description
pkgconf is a program which helps to configure compiler and linker flags
for development libraries. It is similar to pkg-config from
freedesktop.org.

%package -n lib%name
Summary: Shared library for %name
Group: System/Libraries

%description -n lib%name
lib%name is a library which provides access to most of pkgconf's functionality,
to allow other tooling such as compilers and IDEs to discover and use libraries.
configured by %name.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package provides development files for lib%name.

%prep
%setup

%build
%meson %{?_disable_check:-Dtests=disabled}
%nil
%meson_build

%check
%__meson_test

%install
%meson_install
mkdir -p %buildroot%_pkgconfigdir/personality.d
mkdir -p %buildroot%_datadir/pkgconfig/personality.d

%files
%dir %_pkgconfigdir/personality.d
%dir %_datadir/pkgconfig/personality.d
%_bindir/%name
%_man1dir/%name.1*
%_man5dir/pc.5*
%_man5dir/%name-personality.5*
%doc README.md AUTHORS NEWS

%files -n lib%name
%_libdir/lib%name.so.%{sover}*

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib%name.so
%_pkgconfigdir/lib%name.pc

%exclude %_datadir/aclocal
%exclude %_man7dir/pkg.m4.7*


%changelog
* Wed Aug 07 2024 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Thu Mar 28 2024 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Sun Feb 04 2024 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Thu Nov 23 2023 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Sun Sep 03 2023 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Fri Aug 18 2023 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Sat Aug 12 2023 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Fri Aug 04 2023 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Wed May 03 2023 Yuri N. Sedunov <aris@altlinux.org> 1.9.5-alt1
- 1.9.5

* Sun Jan 22 2023 Yuri N. Sedunov <aris@altlinux.org> 1.9.4-alt1
- 1.9.4

* Fri Oct 07 2022 Yuri N. Sedunov <aris@altlinux.org> 1.9.3-alt1.1
- enabled %%check

* Wed Aug 17 2022 Yuri N. Sedunov <aris@altlinux.org> 1.9.3-alt1
- 1.9.3

* Tue Aug 09 2022 Yuri N. Sedunov <aris@altlinux.org> 1.9.2-alt1
- 1.9.2

* Mon Aug 08 2022 Yuri N. Sedunov <aris@altlinux.org> 1.9.1-alt1
- 1.9.1

* Sun Aug 07 2022 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- 1.9.0

* Tue Jun 07 2022 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- first build for Sisyphus (1.8.0-32-gcf48b61)

