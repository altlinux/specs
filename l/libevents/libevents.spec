%define _unpackaged_files_terminate_build 1
%define abiversion 0

Name: libevents
Version: 2026.01.13
Release: alt2

Summary: Events interface project by MAVLink
License: BSD-3-Clause
Group: Development/C++
URL: https://github.com/mavlink/libevents
Vcs: https://github.com/mavlink/libevents.git

Source: %name-%version.tar
Patch: alt-fix-lib-name.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3 python3-module-jinja2
BuildRequires: /proc

%description
This project contains the events interface, which includes the following:
- a protocol to send events based on an ID (and possibly arguments) to inform
other components (in a reliable way)
- using MAVLink as a transport layer. Each MAVLink component can send and/or
receive events to/from other components. The primary use-case is for an
autopilot to inform a user (through a GCS) about certain events (such as a
failsafe action).
- metadata for each event, for example a description, stored as JSON. Metadata
is typically distributed via the COMPONENT_INFORMATION MAVLink API.
- a set of commonly used predefined events that can be used to build simple
protocols
- a parser (MAVLink-independent) to combine event ID's with the JSON metadata
for display or analysis purposes. This also includes log processing.

%package devel
Summary: Development files for libevents
Group: Development/Other

%description devel
Headers for libevents package.

%package -n libevents%abiversion
Summary: Libraries for libevents
Group: Development/C++

%description -n libevents%abiversion
Shared libraries for libevents.

%prep
%setup -q
%autopatch -p1
%ifarch %e2k
sed -i 's/-Werror/-Wno-error/g' libs/cpp/{parse,tests}/CMakeLists.txt
%endif

%build
pushd libs/cpp
%cmake -DENABLE_TESTING=OFF \
       -DBUILD_SHARED_LIBS=ON \
       #
%cmake_build
popd

%install
pushd libs/cpp
%cmake_install
cp -r generated %buildroot%_includedir/libevents/
popd

%files devel
%_includedir/libevents
%_cmakedir/libevents
%_libdir/libevents_health_and_arming_checks.so
%_libdir/libevents_parser.so

%files -n libevents%abiversion
%doc README.md LICENSE.md
%_libdir/libevents_health_and_arming_checks.so.%abiversion
%_libdir/libevents_parser.so.%abiversion

%changelog
* Tue May 12 2026 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2026.01.13-alt2
- e2k build fix

* Tue Jan 13 2026 Ilya Muhamadeev <nicourced@altlinux.org> 2026.01.13-alt1
- Initial build.
