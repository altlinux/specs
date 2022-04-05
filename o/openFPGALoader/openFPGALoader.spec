# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_with doc

Name:     openFPGALoader
Version:  0.8.0
Release:  alt2

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
%cmake
%cmake_build
%if_with doc
%make_build -C doc/ html
%endif

%install
%cmake_install

%files
%_bindir/%name
%_datadir/%name/
%doc README.md

%if_with doc
%files doc
%doc doc/_build/html/*
%endif

%changelog
* Tue Apr 05 2022 Anton Midyukov <antohami@altlinux.org> 0.8.0-alt2
- build documentation

* Tue Apr 05 2022 Anton Midyukov <antohami@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus
