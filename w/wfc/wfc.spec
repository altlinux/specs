%define gcc_ver 14

Name: wfc
Version: R2304
Release: alt1.1

Summary: Wire Format Compiler
License: GPLv3+
Group: Development/C++
Url: https://github.com/maierkomor/wfc

Packager: L.A. Kostis <lakostis@altlinux.org>

# https://github.com/maierkomor/wfc/archive/refs/tags/<version>.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc%{gcc_ver}-c++ libstdc++%{gcc_ver}-devel mercurial flex xxd

%description
Wire Format Compiler (WFC) is a tool that generates C++ code from data
structure descriptions for handling serialization, deserialization and access
to the specified data. The generated code provide an API for accessing the data
with get, set, and clear functions and serializing it to byte stream and
restoring the data structures from a byte stream in memory.

%prep
%setup
%patch -p1

%build
%autoreconf
export GCC_VERSION=%gcc_ver
%configure
# smp incompatible build
make

%install
make install PREFIX=%buildroot%_prefix

%files
%doc LICENSE README.md examples
%_bindir/%name
%_includedir/%{name}
%_datadir/%{name}
%_man1dir/%{name}*

%changelog
* Wed May 06 2026 L.A. Kostis <lakostis@altlinux.ru> R2304-alt1.1
- downgrade gcc to 14.0 (to FTBFS with gcc15).

* Thu May 04 2023 L.A. Kostis <lakostis@altlinux.ru> R2304-alt1
- R2304.

* Fri Mar 24 2023 L.A. Kostis <lakostis@altlinux.ru> R2211-alt1
- Initial build for ALTLinux.

