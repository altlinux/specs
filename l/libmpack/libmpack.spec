Name: libmpack
Version: 1.0.5
Release: alt1

Summary: small binary serialization/RPC library

Group: Development/Tools
License: MIT
Url: https://github.com/libmpack/libmpack

Source: %name-%version.tar

%description
libmpack is a small binary serialization/RPC library that implements both the msgpack and msgpack-rpc specifications.

%package devel
Summary: Devel package for libmpack
Group: Development/Other
Requires: %name = %version-%release

%description devel
libmpack header and build tools.

%prep
%setup

%build
make

%install
make LIBDIR=%buildroot%_libdir PREFIX=%buildroot%_prefix install

%files
%_libdir/*.so
%_libdir/*.so.*
%exclude %_libdir/*.a

%files devel
%_includedir/*
%_pkgconfigdir/*.pc


%changelog
* Wed Sep 18 2019 Vladimir Didenko <cow@altlinux.ru> 1.0.5-alt1
- initial build for Sisyphus
