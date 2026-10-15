%def_disable   check
%def_enable    devel
%{?!_disable_check:%define _unpackaged_files_terminate_build 1}
%define        nomen s2n

Name:          lib%nomen
Version:       1.7.11
Release:       alt1
Group:         Development/C
Summary:       An implementation of the TLS/SSL protocols
License:       Apache-2.0
Url:           https://github.com/aws/s2n-tls
Vcs:           https://github.com/aws/s2n-tls.git

Source:        %name-%version.tar
Patch:         path.patch
BuildRequires(pre): rpm-build-cmake
%{?!_disable_check:BuildRequires: ctest}
BuildRequires: cmake
BuildRequires: clang-tools
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libseccomp)

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%description
s2n-tls is a C99 implementation of the TLS/SSL protocols that is designed to be
simple, small, fast, and with security as a priority. It is released and
licensed under the Apache License 2.0.

s2n-tls is short for "signal to noise" and is a nod to the almost magical act of
encryption - disguising meaningful signals, like your critical data, as
seemingly random noise.


%if_enabled    devel
%package       devel
Group:         Development/C
Summary:       An implementation of the TLS/SSL protocols development files
Requires:      ctest
Requires:      cmake
Requires:      clang-tools
Requires:      pkgconfig(libssl)
Requires:      pkgconfig(libseccomp)

%description   devel
Development headers and libraries for %nomen.

s2n-tls is a C99 implementation of the TLS/SSL protocols that is designed to be
simple, small, fast, and with security as a priority. It is released and
licensed under the Apache License 2.0.

s2n-tls is short for "signal to noise" and is a nod to the almost magical act of
encryption - disguising meaningful signals, like your critical data, as
seemingly random noise.
%endif


%package       -n %nomen
Group:         Development/C
Summary:       An implementation of the TLS/SSL protocols %nomen executables

%description   -n %nomen
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
%cmake \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DCMAKE_PREFIX_PATH=%_usr \
   -DCMAKE_C_COMPILER=clang \
   -DBUILD_SHARED_LIBS=ON \
   -DUNSAFE_TREAT_WARNINGS_AS_ERRORS=OFF \
   -DS2N_ENFORCE_PROPER_LIBCRYPTO_FEATURE_PROBE=ON \
   -DS2N_LTO=ON \
%if_enabled check
   -DCOVERAGE=ON \
%endif
   -DS2N_INTEG_TESTS=ON \
   -DS2N_INSTALL_S2NC_S2ND=ON \
   -DTSAN=ON \
   -DSECCOMP=ON \
   -DS2N_USE_CRYPTO_SHARED_LIBS=ON \
   %nil
%cmake_build

%install
%cmakeinstall_std

%check
%ctest


%files
%doc README*
%_libdir/%name.so.*

%if_enabled    devel
%files         devel
%doc README*
%_libdir/%name.so
%_libdir/cmake/%nomen
%_includedir/%{nomen}*
%endif

%files         -n %nomen
%doc README*
%_bindir/%{nomen}*

%changelog
* Wed Oct 07 2026 Pavel Skrylev <majioa@altlinux.org> 1.7.11-alt1
- ^ 1.4.1 -> 1.7.11

* Wed Jan 03 2024 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- Initial build v1.4.1 for Sisyphus
