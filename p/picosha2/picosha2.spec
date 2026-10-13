%define _unpackaged_files_terminate_build 1

Name: picosha2
Version: 1.0.1
Release: alt1

Summary: Header-only C++ library for SHA-256 hashing
License: MIT
Group: Development/C++
Url: https://github.com/okdshin/PicoSHA2
Vcs: https://github.com/okdshin/PicoSHA2.git
BuildArch: noarch

Source0: %name-%version.tar

%description
PicoSHA2 is a small, header-only C++ library for computing SHA-256
hashes. It uses only the C++ standard library and supports hashing
strings, STL containers, iterator ranges and input streams.

%prep
%setup -q

%install
install -D -m 0644 picosha2.h %buildroot%_includedir/picosha2.h

%files
%doc README.md LICENSE
%_includedir/picosha2.h

%changelog
* Tue Oct 13 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.0.1-alt1
- Initial build for ALT Sisyphus.
