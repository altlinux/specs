%define _unpackaged_files_terminate_build 1
%define project_name llhttp

Name: lib%project_name
Version: 9.4.2
Release: alt1
Summary: Port of http_parser to llparse
License: MIT
Group: System/Libraries
Url: https://github.com/nodejs/llhttp
Vcs: https://github.com/nodejs/llhttp
Source0: %name-%version.tar
# updated with alt/regenerate-c-sources.sh
Source1: llhttp_c_sources.tar
Patch0: %name-%version-alt.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: /proc

%description
This project is a port of http_parser to TypeScript. llparse is used to generate
the output C source file, which could be compiled and linked with the embedder's
program (like Node.js).

%package -n %name-devel
Summary: %summary
Group: Development/C

%description -n %name-devel
Development headers and libraries for %project_name.

%prep
%setup -a1
%autopatch -p1

%build
cd release
%cmake
%cmake_build

%install
cd release
%cmakeinstall_std

%check
# requires docker (see .github/workflows/ci.yaml)
# run python's aiohttp tests

%files
%_libdir/%name.so.9.*

%files -n %name-devel
%_includedir/%project_name.h
%_pkgconfigdir/%name.pc
%_libdir/%name.so
%_cmakedir/%project_name/*.cmake

%changelog
* Fri Jun 19 2026 Stanislav Levin <slev@altlinux.org> 9.4.2-alt1
- 9.4.1 -> 9.4.2.

* Tue May 12 2026 Stanislav Levin <slev@altlinux.org> 9.4.1-alt1
- 9.3.1 -> 9.4.1.

* Mon Feb 16 2026 Stanislav Levin <slev@altlinux.org> 9.3.1-alt1
- 9.3.0 -> 9.3.1.

* Mon May 26 2025 Stanislav Levin <slev@altlinux.org> 9.3.0-alt1
- Initial build for sisyphus.
