%define _unpackaged_files_terminate_build 1

Name: c_library_v2
Version: 2026.01.13
Release: alt1.f7ceb0e

Summary: Official reference C / C++ library for the v2 protocol
License: LGPL-3.0-or-later
Group: Development/Tools
URL: https://mavlink.io/
VCS: https://github.com/mavlink/c_library_v2
BuildArch: noarch

Source0: %name-%version.tar

%description
Official reference C / C++ library for the v2 protocol, header-only library.

%prep
%setup

%install
mkdir -pv %buildroot%_includedir/c_library_v2
cp -r %_builddir/c_library_v2-%version/* %buildroot%_includedir/c_library_v2/

%files
%_includedir/c_library_v2

%changelog
* Tue Jan 13 2026 Ilya Muhamadeev <nicourced@altlinux.org> 2026.01.13-alt1.f7ceb0e
- Initial build.
