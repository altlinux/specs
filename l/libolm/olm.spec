%define _unpackaged_files_terminate_build 1

Name: libolm
Version: 3.2.16
Release: alt2

Summary: An implementation of the Double Ratchet cryptographic ratchet

Group: Development/Other
License: Apache v2.0
Url: https://gitlab.matrix.org/matrix-org/olm.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: cmake ctest gcc-c++
BuildRequires: python3(cffi) python3(setuptools)

%description
An implementation of the Double Ratchet cryptographic ratchet described by
https://whispersystems.org/docs/specifications/doubleratchet/, written
in C and C++11 and exposed as a C API.

The specification of the Olm ratchet can be found in `<docs/olm.rst>`.

This library also includes an implementation of the Megolm cryptographic
ratchet, as specified in `<docs/megolm.rst>`.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
The %name-devel package contains C++ header files for developing
applications that use %name.

%package -n python3-module-%name
Summary: Python3 bindings for %name
Group: Development/Python3
Requires: %name = %version-%release

%description -n python3-module-%name
This package contains Python3 bindings for %name.

%prep
%setup

%build
%cmake
%cmake_build

# symlink for consistent build path
ln -s %_host_alias build

pushd python
%pyproject_build
popd

%install
%cmakeinstall_std

pushd python
%pyproject_install
popd

%check
%make_build test

%files
%doc README.md
%doc LICENSE
%_libdir/*.so.*

%files devel
%doc docs
%_libdir/*.so
%_includedir/olm
%_libdir/cmake/Olm
%_pkgconfigdir/olm.pc

%files -n python3-module-%name
%python3_sitelibdir/olm/
%python3_sitelibdir/_libolm.abi3.so
%python3_sitelibdir/%{pyproject_distinfo python_olm}

%changelog
* Thu Dec 04 2025 Ivan Mazhukin <vanomj@altlinux.org> 3.2.16-alt2
- add python3 binding subpackage

* Wed Feb 07 2024 Paul Wolneykien <manowar@altlinux.org> 3.2.16-alt1
- New version 3.2.16.

* Wed Sep 27 2023 Paul Wolneykien <manowar@altlinux.org> 3.2.15-alt2
- Remove Fix-build-on-GCC13 patch.

* Tue Sep 26 2023 Paul Wolneykien <manowar@altlinux.org> 3.2.15-alt1
- New version 3.2.15.

* Mon Jul 17 2023 Artyom Bystrov <arbars@altlinux.org> 3.2.6-alt2
- Fix build on GCC13

* Tue Nov 16 2021 Paul Wolneykien <manowar@altlinux.org> 3.2.6-alt1
- new version 3.2.6

* Tue Sep 14 2021 Paul Wolneykien <manowar@altlinux.org> 3.2.4-alt1
- Updated to v3.2.4.

* Sun Feb 14 2021 Paul Wolneykien <manowar@altlinux.org> 3.2.1-alt1
- Fresh up to v3.2.1.

* Fri Jul 03 2020 Paul Wolneykien <manowar@altlinux.org> 3.1.5-alt1
- Fresh up to v3.1.5.

* Tue Mar 31 2020 Paul Wolneykien <manowar@altlinux.org> 3.1.4-alt1
- New upstream version 3.1.4.

* Fri Nov 30 2018 Paul Wolneykien <manowar@altlinux.org> 3.0.0-alt1
- Initial release.
