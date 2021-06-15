
Name: jerasure
Version: 2.0
Release: alt1.gitde1739
Summary: Forward error correction erasure channel library
License: BSD-3-Clause
Group: System/Libraries
Url: http://jerasure.org/jerasure/jerasure
Source: %name-%version.tar

BuildRequires: libgf-complete-devel

%description
In information theory, an erasure code is a forward error correction (FEC)
code for the binary erasure channel, which transforms a message of symbols
into a longer message (code word) with symbols such that the original
message can be recovered from a subset of the symbols.
Jerasure is a shared library that been designed to be modular, fast and
flexible. It is used in storage systems such as Swift and Ceph to add fault
tolerance.

%package -n lib%name
Summary: Forward error correction erasure channel library
Group: System/Libraries

%description -n lib%name
In information theory, an erasure code is a forward error correction (FEC)
code for the binary erasure channel, which transforms a message of symbols
into a longer message (code word) with symbols such that the original
message can be recovered from a subset of the symbols.
Jerasure is a shared library that been designed to be modular, fast and
flexible. It is used in storage systems such as Swift and Ceph to add fault
tolerance.

%package -n lib%name-devel
Summary: Forward error correction erasure development files
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
In information theory, an erasure code is a forward error correction (FEC)
code for the binary erasure channel, which transforms a message of symbols
into a longer message (code word) with symbols such that the original
message can be recovered from a subset of the symbols.
Jerasure is a shared library that been designed to be modular, fast and
flexible. It is used in storage systems such as Swift and Ceph to add fault
tolerance.

%package examples
Summary: Examples for %name
Group: Development/Tools
Requires: lib%name = %EVR

%description examples
Examples for %name

%prep
%setup

%build
%autoreconf
%configure \
           --disable-static \
           --disable-silent-rules \
           --disable-rpath
%make_build

%install
%makeinstall_std
mv %buildroot%_bindir/decoder %buildroot%_bindir/%name-decoder
mv %buildroot%_bindir/encoder %buildroot%_bindir/%name-encoder

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files examples
%_bindir/*

%changelog
* Fri Mar 19 2021 Alexey Shabalin <shaba@altlinux.org> 2.0-alt1.gitde1739
- Initial build.

