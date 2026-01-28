%define _unpackaged_files_terminate_build 1

# The "soversion" value can be found in the file "src/meson.build"
%define abiversion 0

Name: libspecbleach
Version: 0.2.0
Release: alt2

Summary: Library for audio noise reduction and other spectral effects

License: LGPL-2.1+
Group: System/Libraries
URL: https://github.com/lucianodato/libspecbleach
VCS: https://github.com/lucianodato/libspecbleach

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(sndfile)
BuildRequires: meson

%description
%summary.

%package -n %name%abiversion
Summary: Library for audio noise reduction and other spectral effects
Group: System/Libraries

%description -n %name%abiversion
%summary.

%package examples
Summary: Example utilities for libspecbleach
Requires: %name%abiversion = %EVR
Group: Sound

%description examples
%summary.

%package devel
Summary: Development files for libspecbleach
Requires: %name%abiversion = %EVR
Group: Development/Other

%description devel
%summary.

%prep
%setup -q
%patch -p1

%build
%meson \
    -Denable_examples=true \
    -Denable_tests=true

%meson_build

%install
%meson_install

%check
%meson_test

%files -n %name%abiversion
%doc LICENSE CONTRIBUTING.md CHANGELOG.md README.md
%_libdir/*.so.%abiversion
%_libdir/*.so.%abiversion.*

%files examples
%_bindir/*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/%name.pc

%changelog
* Wed Jan 28 2026 Sergey Savelev <medovi@altlinux.org> 0.2.0-alt2
- Backport upstream overflow and null pointers fixes.

* Wed Jan 28 2026 Sergey Savelev <medovi@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus.
