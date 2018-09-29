Name: openssl-gost-engine
Version: 1.1.0.3.0.21.ga2174a8
Release: alt1

License: BSD-style
Summary: A reference implementation of the Russian GOST crypto algorithms for OpenSSL

Group: System/Libraries

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake libssl-devel

%{?!_without_check:%{?!_disable_check:BuildRequires: ctest perl-devel openssl}}

%description
A reference implementation of the Russian GOST crypto algorithms for OpenSSL.

%package -n gostsum
Summary: GOST file digesting utilites
Group: File tools

%description -n gostsum
GOST file digesting utilites.

%prep
%setup

%build
%cmake \
	#

%cmake_build

%install
enginesdir="$(pkg-config --variable=enginesdir libcrypto)"
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot$enginesdir

cp bin/gost.so %buildroot$enginesdir/
cp bin/gost*sum %buildroot%_bindir/
cp gost*sum.1 %buildroot%_man1dir/

%check
OPENSSL_ENGINES="$PWD/bin" \
	LD_LIBRARY_PATH="$PWD/bin" \
	CTEST_OUTPUT_ON_FAILURE=1 \
	make test -C BUILD ARGS="--verbose"

%files
%_libdir/openssl/engines-1.1/gost.so

%files -n gostsum
%_bindir/gost*sum*
%_man1dir/gost*sum*

%changelog
* Sat Sep 29 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.0.3.0.21.ga2174a8-alt1
- Initial build (v1.1.0.3-21-ga2174a8).
