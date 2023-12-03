# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: CImg
Version: 3.3.2
Release: alt1
Summary: The CImg Library is a small and open-source C++ toolkit for image processing
License: CECILL or CECILL-C
Group: Development/C++
Url: https://cimg.eu/
Vcs: https://github.com/GreycLab/CImg

Source: %name-%version.tar
%{?!_without_check:%{?!_disable_check:
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
}}

%description
%summary,

%package devel
Summary: %summary.
Group: Development/C++
BuildArch: noarch

%description devel
The CImg Library is an open-source C++ toolkit for image processing.
It consists in a single header file 'CImg.h' providing a minimal set
of C++ classes and methods that can be used in your own sources, to
load/save, process and display images. Very portable, efficient and
easy to use, it's a pleasant library for developing image processing
algorithms in C++.

%prep
%setup

%install
install -Dpm644 CImg.h -t %buildroot%_includedir
install -Dpm644 plugins/*.h -t %buildroot%_includedir/%name/plugins
install -Dpm644 resources/CImg.pc -t %buildroot%_datadir/pkgconfig

%check
%make_build -Cexamples mlinux
examples/CImg_demo || :

%files devel
%define _customdocdir %_docdir/%name
%doc *.txt
%_includedir/CImg*
%_datadir/pkgconfig/CImg.pc

%changelog
* Mon Dec 04 2023 Vitaly Chikunov <vt@altlinux.org> 3.3.2-alt1
- Update to v.3.3.2 (2023-11-09).

* Fri Nov 03 2023 Vitaly Chikunov <vt@altlinux.org> 3.3.1-alt1
- First import v.3.3.1 (2023-09-27).
