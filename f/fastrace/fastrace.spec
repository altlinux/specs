%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: fastrace
Version: 0.3.0
Release: alt1

Summary: A fast, dependency-free traceroute implementation in pure C
License: BSD-2-Clause
Group: Networking/Other
Url: https://github.com/davidesantangelo/fastrace

Source: %name-%version.tar

%description
Fastrace is a blazingly fast traceroute utility designed for network
diagnostics and performance analysis. It maps the route that packets
take across an IP network from source to destination, providing
detailed timing information and identifying potential bottlenecks or
routing issues.

%prep
%setup

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc CHANGELOG.md docs LICENSE README.md
%_bindir/%name

%changelog
* Sun Nov 23 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

* Fri Nov 14 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus
