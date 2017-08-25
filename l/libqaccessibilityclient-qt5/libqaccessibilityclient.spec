%define bname qaccessibilityclient
Name: lib%bname-qt5
Version: 0.2.0
Release: alt1%ubt

Summary: This library is used when writing accessibility clients
License: %lgpl21only
Group: System/Libraries
Url: https://cgit.kde.org/libqaccessibilityclient.git
Source0: %name-%version.tar
BuildRequires(pre): rpm-build-ubt rpm-build-licenses
BuildRequires: cmake qt5-base-devel

%description
%summary.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Conflicts: libqaccessibilityclient-devel
%description devel
%summary.

%prep
%setup
#exclude tests and examples from build
sed -i '/add_subdirectory(tests)\|add_subdirectory(examples)/d' ./CMakeLists.txt

%build
%cmake \
	-DKDE4_BUILD_TESTS=OFF \
	#
%cmake_build

%install
%cmakeinstall_std

%files
%doc COPYING* AUTHORS ChangeLog README
%_libdir/%{name}.so.*

%files devel
%_includedir/%{bname}/
%_libdir/cmake/QAccessibilityClient/
%_libdir/%{name}.so

%changelog
* Fri Aug 25 2017 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1%ubt
- Initial build
