%define _unpackaged_files_terminate_build 1

Name: codefetch
Version: 0.12.3
Release: alt1

Summary: Fast & comprehensive tool for source code analysis
License: MIT
Group: System/Libraries
Url: https://github.com/yellow-footed-honeyguide/codefetch
VCS: https://github.com/yellow-footed-honeyguide/codefetch.git

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++

%description
codefetch is a modern, multi-threaded command-line tool designed
to provide detailed insights and analytics for software codebases.
It offers a complete analysis suite that helps developers understand
their projects better through various metrics and statistics.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/codefetch

%changelog
* Wed Aug 13 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 0.12.3-alt1
- Initial build for ALT.
