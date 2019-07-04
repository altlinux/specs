Name: openssl-gost-engine
Version: 1.1.0.3.0.255.ge3af41d.p1
Release: alt1

License: BSD-style
Summary: A reference implementation of the Russian GOST crypto algorithms for OpenSSL

Group: System/Libraries

Source: %name-%version.tar

Patch0: %name-1.1.0.3.0.255.ge3af41d-mac-iv.patch
Patch1: %name-1.1.0.3.0.255.ge3af41d-gost89-ecb.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
# due to gost algorithms identifiers (in headers)
BuildRequires: libssl-devel >= 1.1.0j-alt2

%{?!_without_check:%{?!_disable_check:BuildRequires: ctest perl-devel perl-Test2-Suite openssl}}

# due to gost algorithms identifiers (inside libcrypto)
Requires: libcrypto1.1 >= 1.1.0j-alt2

%description
A reference implementation of the Russian GOST crypto algorithms for OpenSSL.

%package -n gostsum
Summary: GOST file digesting utilites
Group: File tools

%description -n gostsum
GOST file digesting utilites.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%cmake \
	#

%cmake_build

%install
enginesdir="$(pkg-config --variable=enginesdir libcrypto)"
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot$enginesdir

cp BUILD/bin/gost.so %buildroot$enginesdir/
cp BUILD/bin/gost*sum %buildroot%_bindir/
cp gost*sum.1 %buildroot%_man1dir/

%check
CTEST_OUTPUT_ON_FAILURE=1 \
	make test -C BUILD ARGS="--verbose"

%files
%_libdir/openssl/engines-1.1/gost.so

%files -n gostsum
%_bindir/gost*sum*
%_man1dir/gost*sum*

%changelog
* Thu Jul 04 2019 Paul Wolneykien <manowar@altlinux.org> 1.1.0.3.0.255.ge3af41d.p1-alt1
- Allow to set an IV for MAC using EVP_MD_CTRL_SET_IV (patch).
- Added ECB mode GOST28147-89 cipher (patch).

* Mon Mar 04 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.0.3.0.255.ge3af41d-alt1
- Backported new algorithms from upstream master.

* Sat Sep 29 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.0.3.0.21.ga2174a8-alt1
- Initial build (v1.1.0.3-21-ga2174a8).
