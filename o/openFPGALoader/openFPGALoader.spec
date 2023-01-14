# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_with doc

Name:     openFPGALoader
Version:  0.10.0
Release:  alt1

Summary:  Universal utility for programming FPGA
License:  Apache-2.0
Group:    Engineering
Url:      https://github.com/trabucayre/openFPGALoader

Source:   %name-%version.tar
# ALT patches
Patch:    0001-doc-Makefile-fix-build-with-python3-module-sphinx.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libftdi1-devel
BuildRequires: libhidapi-devel
BuildRequires: zlib-ng-devel
BuildRequires: libudev-devel
BuildRequires: libgpiod-devel
%if_with doc
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-yaml
BuildRequires: python3-module-tabulate
%endif

%description
%summary.

%package doc
Summary: Documentation for %name
Group:   Documentation

%description doc
%summary.

%prep
%setup
%autopatch -p1

%build
# fix build with gcc12
%add_optflags -Wno-narrowing

%cmake
%cmake_build
%if_with doc
%make_build -C doc/ man html
%endif

%install
%cmake_install

# install udev rules
mkdir -p %buildroot/lib/udev/rules.d/
install -pm644 99-openfpgaloader.rules %buildroot/lib/udev/rules.d/

# install man
mkdir -p %buildroot%_man1dir
install -pm644 doc/_build/man/openFPGALoader.1 %buildroot%_man1dir

%files
%_bindir/%name
/lib/udev/rules.d/99-openfpgaloader.rules
%_datadir/%name/
%doc README.md
%if_with doc
%_man1dir/openFPGALoader.1*
%endif

%if_with doc
%files doc
%doc doc/_build/html/*
%endif

%changelog
* Sat Jan 14 2023 Anton Midyukov <antohami@altlinux.org> 0.10.0-alt1
- new version 0.10.0

* Fri Oct 07 2022 Anton Midyukov <antohami@altlinux.org> 0.9.1-alt1
- new version 0.9.1

* Sun Aug 14 2022 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt1
- new version 0.9.0

* Sun Jun 19 2022 Anton Midyukov <antohami@altlinux.org> 0.8.0-alt4
- add compiler flag -Wno-narrowing for fix build with gcc12

* Tue Apr 05 2022 Anton Midyukov <antohami@altlinux.org> 0.8.0-alt3
- add udev rules
- build man

* Tue Apr 05 2022 Anton Midyukov <antohami@altlinux.org> 0.8.0-alt2
- build documentation

* Tue Apr 05 2022 Anton Midyukov <antohami@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus
