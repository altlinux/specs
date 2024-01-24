%define        _unpackaged_files_terminate_build 1
%define        oname s2n

Name:          lib%oname
Version:       1.4.1
Release:       alt1
Group:         Development/C
Summary:       An implementation of the TLS/SSL protocols
License:       Apache-2.0
Url:           https://github.com/aws/s2n-tls
Vcs:           https://github.com/aws/s2n-tls.git

Source:        %name-%version.tar
Patch:         path.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: libssl-devel

%description
s2n-tls is a C99 implementation of the TLS/SSL protocols that is designed to be
simple, small, fast, and with security as a priority. It is released and
licensed under the Apache License 2.0.

s2n-tls is short for "signal to noise" and is a nod to the almost magical act of
encryption - disguising meaningful signals, like your critical data, as
seemingly random noise.


%package       devel
Group:         Development/C
Summary:       An implementation of the TLS/SSL protocols development files
Requires:      cmake
Requires:      ctest
Requires:      libssl-devel

%description   devel
Development headers and libraries for %oname.

s2n-tls is a C99 implementation of the TLS/SSL protocols that is designed to be
simple, small, fast, and with security as a priority. It is released and
licensed under the Apache License 2.0.

s2n-tls is short for "signal to noise" and is a nod to the almost magical act of
encryption - disguising meaningful signals, like your critical data, as
seemingly random noise.


%prep
%setup
%autopatch

%build
%cmake_insource \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DBUILD_SHARED_LIBS=ON


%install
%cmakeinstall_std

%check
#make test


%files
%doc README*
%_libdir/%name.so.*

%files         devel
%doc README*
%_libdir/%name.so
%_libdir/cmake/%oname
%_includedir/%{oname}*


%changelog
* Wed Jan 03 2024 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- Initial build v1.4.1 for Sisyphus
