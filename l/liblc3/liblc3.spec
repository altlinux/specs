%define _unpackaged_files_terminate_build 1

%define _name lc3

%def_enable tools
%def_enable check

Name: lib%_name
Version: 1.1.1
Release: alt1

Summary: Low Complexity Communication Codec (LC3)
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/google/liblc3

Vcs: https://github.com/google/liblc3.git
Source: https://github.com/google/liblc3/archive/v%version/%name-%version.tar.gz
Patch10: liblc3-1.1.1-up-rpath.diff

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libgomp-devel
%{?_enable_check:BuildRequires: python3(scipy) python3(numpy) libnumpy-py3-devel}

%description
Low Complexity Communication Codec (LC3) Library

%package devel
Summary: Development files for LC3 library
Group: Development/C
Requires: %name = %EVR

%description devel
This package provides LC3 development files.

%package tools
Summary: The LC3 library command line tools
Group: Sound
Requires: %name = %EVR

%description tools
This package provides LC3 tools.


%prep
%setup
%patch10 -p1 -R

%build
%meson \
    %{?_enable_tools:-Dtools=true}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/%name.so.*
%doc README*

%files devel
%_libdir/%name.so
%_includedir/%{_name}*.h
%_pkgconfigdir/%_name.pc

%if_enabled tools
%files tools
%_bindir/e%_name
%_bindir/d%_name
%endif

%changelog
* Sat Apr 20 2024 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Thu Mar 28 2024 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Fri Aug 04 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Mon May 08 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Sat Feb 18 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Mon Oct 17 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- first build for Sisyphus


