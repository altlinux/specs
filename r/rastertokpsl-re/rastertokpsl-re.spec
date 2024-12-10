%define _unpackaged_files_terminate_build 1

Name: rastertokpsl-re
Version: 1.0.1422
Release: alt3

Summary: Reverse engineered Kyocera rastertokpsl filter

Group: System/Configuration/Printing
License: Apache-2.0
Url: https://github.com/sv99/rastertokpsl-re

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake ctest gcc-c++
BuildRequires: libcups-devel libjbig-devel

Requires: cups

%description
Reverse engineered Kyocera rastertokpsl filter

%prep
%setup

%build
%cmake -DLIBEXEC_INSTALL_DIR=%_libexecdir
%cmake_build

%install
%cmakeinstall_std
ln -s %name %buildroot%_libexecdir/cups/filter/rastertokpsl
install -D -m0644 Kyocera_FS-1060DN.ppd %buildroot%_datadir/cups/model/Kyocera/Kyocera_FS-1060DN.ppd

%check
%make_build -C %_cmake__builddir test

%files
%_libexecdir/cups/filter/%name
%_libexecdir/cups/filter/rastertokpsl
%_datadir/cups/model/Kyocera/*.ppd

%changelog
* Tue Dec 10 2024 Paul Wolneykien <manowar@altlinux.org> 1.0.1422-alt3
- Fixed build.

* Thu Dec 19 2019 Paul Wolneykien <manowar@altlinux.org> 1.0.1422-alt2
- Initial release for Sisyphus.

* Tue Nov 05 2019 Paul Wolneykien <manowar@altlinux.org> 1.0.1422-alt1
- Test release.
