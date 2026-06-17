%define _unpackaged_files_terminate_build 1
%define srcname Fast-CDR

Name:    fast-cdr
Version: 2.3.6
Release: alt1

Summary: Fast Common Data Representation (CDR) Serialization Library
License: Apache-2.0
Group:   Other
URL:     https://github.com/eProsima/Fast-CDR
VCS:     https://github.com/eProsima/Fast-CDR.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libgtest-devel

%description
eProsima FastCDR is a C++ library that provides two serialization mechanisms.
One is the standard CDR serialization mechanism, while the other is a faster
implementation that modifies the standard.

%package devel
Summary:    Development files and libraries for %name
Group: Development/C++
Requires:   %name = %EVR

%description devel
Development files and libraries for %name

%prep
%setup

%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo

%cmake_build

%install
%cmake_install

rm -f %buildroot%_datadir/fastcdr/LICENSE

%files
%doc LICENSE README.md
%_libdir/libfastcdr.so.*

%files devel
%_includedir/fastcdr/
%_libdir/libfastcdr.so
%_libdir/cmake/fastcdr/

%changelog
* Wed Jun 17 2026 Sergey Palcheh <minergenon@altlinux.org> 2.3.6-alt1
- new version 2.3.6

* Mon Jun 01 2026 Sergey Palcheh <minergenon@altlinux.org> 2.3.5-alt1
- Initial build for Sisyphus
