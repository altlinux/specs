Name: wfc
Version: R2211
Release: alt1

Summary: Wire Format Compiler
License: GPLv3+
Group: Development/C++
Url: https://github.com/maierkomor/wfc

Packager: L.A. Kostis <lakostis@altlinux.org>

# https://github.com/maierkomor/wfc/archive/refs/tags/<version>.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ mercurial flex xxd

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
* Fri Mar 24 2023 L.A. Kostis <lakostis@altlinux.ru> R2211-alt1
- Initial build for ALTLinux.

