Name: bcunit
Version: 5.2.62
Release: alt1
Summary: CUnit is a Unit testing framework for C.
Group: System/Libraries
License: GPLv2
Url: https://gitlab.linphone.org/BC/public/bcunit
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): cmake

%description
The basic framework is platform/version independent and
should be portable to all platforms. CUnit provides various
interfaces to the framework, some of which are platform
dependent (e.g. curses on *nix). Building other interfaces
should be straightforward with the facilities provided in the framework.

%package devel
Summary: Development libraries for bctoolbox
Group: Development/Other
Requires: %name = %version-%release

%description devel
Libraries and headers CUnit is a Unit testing framework for C.

%prep
%setup
%patch0 -p1

%build
%cmake -DENABLE_STATIC=FALSE
%cmake_build

%install
%cmakeinstall_std

%files
%doc AUTHORS ChangeLog COPYING NEWS README.md
%_libdir/*.so.*

%files devel
%_includedir/BCUnit
%_libdir/libbcunit.so
%_libdir/pkgconfig/bcunit.pc
%_datadir/BCUnit
%_datadir/BCunit

%changelog
* Thu Oct 26 2023 Alexei Takaseev <taf@altlinux.org> 5.2.62-alt1
- 5.2.62

* Mon Feb 17 2020 Alexei Takaseev <taf@altlinux.org> 3.0.2-alt2
- Update to git:3c720fbf67dd3c02b0c7011ed4036982b2c93532
- Fix License
- Use Cmake for build

* Sat Jul 22 2017 Alexei Takaseev <taf@altlinux.org> 3.0.2-alt1
- 3.0.2

* Thu Mar 02 2017 Alexei Takaseev <taf@altlinux.org> 3.0-alt1
- Initial build for ALT Sisyphus
