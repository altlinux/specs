%define _unpackaged_files_terminate_build 1

Name: libdomain
Version: 0.1.0
Release: alt1

Summary: Libdomain library provides ability to manipulate LDAP entries.
License: GPLv2+
Group: Other
Url: https://github.com/august-alt/libdomain

BuildRequires: cmake
BuildRequires: rpm-macros-cmake
BuildRequires: cmake-modules
BuildRequires: gcc

BuildRequires: doxygen

Source0: %name-%version.tar

%description
Group policy editor

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md

%_libdir/libdomain.so

%changelog
* Mon Jan 23 2023 Vladimir Rubanov <august@altlinux.org> 0.1.0-alt1
- Initial build
