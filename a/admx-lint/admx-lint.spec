%define _unpackaged_files_terminate_build 1

Name: admx-lint
Version: 0.1.0
Release: alt1

Summary: ADMX/ADML verification tool.
License: GPLv2+
Group: Other
Url: https://github.com/august-alt/admx-lint

BuildRequires: cmake
BuildRequires: rpm-macros-cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++

BuildRequires: doxygen
BuildRequires: libxerces-c-devel
BuildRequires: xsd
BuildRequires: boost-devel
BuildRequires: boost-program_options-devel

Source0: %name-%version.tar

%description
Is a file verification tool, that checks ADMX/ADML contents against their XSD schema.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md
%doc INSTALL.md
%_bindir/admx-lint

%changelog
* Tue Jul 06 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt1
- Initial build
