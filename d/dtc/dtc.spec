%define _unpackaged_files_terminate_build 1
%def_without docs
%def_with python3
%global optflags_lto %nil

Name: dtc
Version: 1.7.0
Release: alt1

Summary: Device Tree Compiler for Flat Device Trees
License: GPL-2.0-or-later
Group: Development/Tools

Url: https://git.kernel.org/cgit/utils/dtc/dtc.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: meson
BuildRequires: flex bison
%{?_with_python3:BuildRequires: swig python3-devel python3-module-setuptools_scm}
%{?_with_docs:BuildRequires: texlive-base texlive-latex-extra}

%description
Device Tree Compiler, dtc, takes as input a device-tree in a given
format and outputs a device-tree in another format for booting kernels
on embedded systems. Typically, the input format is "dts", a human
readable source format, and creates a "dtb", or binary format as output.

%package -n libfdt
Summary: Flat Device Trees manipulation library
Group: System/Libraries
License: GPL-2.0-or-later OR BSD-2-Clause

%description -n libfdt
This is a library containing functions for manipulating Flat Device
Trees.

%package -n libfdt-devel
Summary: Flat Device Trees manipulation library - development files
Group: Development/C
Requires: libfdt = %EVR

%description -n libfdt-devel
This is a library containing functions for manipulating Flat Device
Trees.
This package contains the files needed for development against libfdt.

%package -n libfdt-devel-static
Summary: Static version of device tree library
Group: Development/C
Requires: libfdt-devel = %EVR

%description -n libfdt-devel-static
This package provides the static library of libfdt

%package -n libfdt-doc
Summary: Documentation for Device Tree Compiler for Flat Device Trees 
Group: Development/Other
BuildArch: noarch

%description -n libfdt-doc
This is a library containing functions for manipulating Flat Device
Trees.
This package contains documentation for development against libfdt.

%package -n python3-module-libfdt
Summary: Python bindings for device tree library
Group: Development/Python
Requires: libfdt = %EVR

%description -n python3-module-libfdt
This package provides python bindings for libfdt

%prep
%setup
%patch -p1
%ifarch %e2k
# lcc 1.23 doesn't do -MG and there's -Werror=pointer-arith there
sed -i 's,-MG ,,;s,-Werror,,' Makefile
echo '#define DTC_VERSION "%version"' > version_gen.h
%endif

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%meson -Dstatic-build=false
%meson_build
%if_with docs
pushd Documentation
latex dtc-paper.tex
dvips dtc-paper.dvi
pdflatex dtc-paper.tex
bzip2 -9 dtc-paper.dvi dtc-paper.ps dtc-paper.pdf
popd
%endif

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%meson_install
rm -f %buildroot%_bindir/ftdump

%files
%doc README.license
%doc Documentation/manual.txt
%doc Documentation/dts-format.txt
%_bindir/*

%files -n libfdt
%doc README.license
%_libdir/libfdt.so.*

%files -n libfdt-devel
%doc README.license
%_libdir/libfdt.so
%_includedir/*
%_pkgconfigdir/libfdt.pc

%files -n libfdt-devel-static
%_libdir/libfdt.a

%if_with python3
%files -n python3-module-libfdt
%python3_sitelibdir/*
%endif

%if_with docs
%files -n libfdt-doc
%doc README.license
%doc Documentation/dtc-paper.dvi.bz2
%doc Documentation/dtc-paper.ps.bz2
%doc Documentation/dtc-paper.pdf.bz2
%endif

%changelog
* Thu Feb 16 2023 Alexey Shabalin <shaba@altlinux.org> 1.7.0-alt1
- 1.7.0
- switch to meson build

* Fri Nov 18 2022 Ivan A. Melnikov <iv@altlinux.org> 1.6.1-alt2
- build python3 libfdt module
  + switch to python3
  + fix python module build and install
  + enable building of the module by default

* Wed Jun 09 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Oct 06 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sun Apr 19 2020 Michael Shigorin <mike@altlinux.org> 1.5.1-alt2
- E2K: fix ftbfs with OSL-inspired hacks

* Sun Dec 15 2019 Alexey Shabalin <shaba@altlinux.org> 1.5.1-alt1
- 1.5.1 release

* Sat Jun 01 2019 Alexey Shabalin <shaba@altlinux.org> 1.5.0.0.20.2431-alt1
- v1.5.0-20-g243176c
- build without python

* Sat Aug 18 2018 Alexey Shabalin <shaba@altlinux.org> 1.4.7-alt1
- 1.4.7
- add python package
- add devel-static package

* Fri Apr 21 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Fri Feb 06 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.1-alt1
- 1.4.1 released

* Wed Dec 25 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0 released

* Thu Dec 27 2012 Ivan Ovcherenko <asdus@altlinux.org> 1.3.0-alt2
- Increase package version due the ugly correlation with package version
  in the FC AutoImports repository.

* Mon Dec 24 2012 Ivan Ovcherenko <asdus@altlinux.org> 1.3.0-alt1
- Initial build for ALT Linux Sisyphus, v1.3.0-e4b497f
