Name: openssl-gost-engine
Version: 3.0.2
Release: alt4

License: Apache-2.0
Summary: A reference implementation of the Russian GOST crypto algorithms for OpenSSL

Group: System/Libraries

URL: https://github.com/gost-engine/engine.git

Source: %name-%version.tar
Source1: openssl-gost.control
Source2: openssl-gost-control-check.sh
Source3: libprov.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
# due to gost algorithms identifiers (in headers)
BuildRequires: libssl-devel >= 3.0.0
# to test the control script
BuildRequires: control libcrypto >= 3.0.0

%{?!_without_check:%{?!_disable_check:BuildRequires: ctest perl-devel perl-Test2-Suite openssl}}

# due to gost algorithms identifiers (inside libcrypto)
Requires: libcrypto >= 1.1.0j-alt2

%description
A reference implementation of the Russian GOST crypto algorithms for OpenSSL.

%package -n gostsum
Summary: GOST file digesting utilites
Group: File tools

%description -n gostsum
GOST file digesting utilites.

%prep
%setup -a3
%patch -p1

%build
%ifarch %e2k
# lcc 1.23.12: test_curves.c: if ((test = (e)))
%add_optflags -Wno-error=assign-where-compare-meant
%endif
%cmake \
	#

%cmake_build

%install
enginesdir="$(pkg-config --variable=enginesdir libcrypto)"
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot$enginesdir

cp %_cmake__builddir/bin/gost.so %buildroot$enginesdir/
cp %_cmake__builddir/bin/gost*sum %buildroot%_bindir/
cp gost*sum.1 %buildroot%_man1dir/

# Install the control scripts
install -D -p -m0755 %_sourcedir/openssl-gost.control \
        %buildroot%_controldir/openssl-gost

%check
CTEST_OUTPUT_ON_FAILURE=1 \
	%cmake_build -t test

%_sourcedir/openssl-gost-control-check.sh %_sourcedir/openssl-gost.control

%files
%_libdir/openssl/engines-3/gost.so
%_controldir/openssl-gost

%files -n gostsum
%_bindir/gost*sum*
%_man1dir/gost*sum*

%changelog
* Thu Apr 11 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.0.2-alt4
- Fixed License: tag (BSD-style -> Apache-2.0).
- Added a ctrl command to set whole IV for magma and grasshopper ciphers
  (needed for openssh-gostcrypto for ctr cipher modes).

* Tue Mar 12 2024 Paul Wolneykien <manowar@altlinux.org> 3.0.2-alt3
- Fix: Require OpenSSL >= 3.0.0 to build.

* Wed Oct 04 2023 Paul Wolneykien <manowar@altlinux.org> 3.0.2-alt2
- Remove libcrypto1.1 dependencies.

* Mon Aug 14 2023 Paul Wolneykien <manowar@altlinux.org> 3.0.2-alt1
- Upstream version 3.0.2.

* Mon Aug 14 2023 Paul Wolneykien <manowar@altlinux.org> 3.0.1-alt2
- Disable GOST 28147-89 ECB cipher (patch).
- Disable setting IV for MAC (patch).

* Tue May 02 2023 Paul Wolneykien <manowar@altlinux.org> 3.0.1-alt1
- Fix: Implement GOST 28147-89 ECB cipher test case.
- Upstream version 3.0.1.

* Fri Apr 07 2023 Paul Wolneykien <manowar@altlinux.org> 1.1.0.3.0.255.ge3af41d-alt6
- Fix the version: don't use the .pN suffix.

* Thu Dec 23 2021 Paul Wolneykien <manowar@altlinux.org> 1.1.0.3.0.255.ge3af41d.p1-alt5
- Run tests on the control script after build.
- openssl-gost.control: Fixed appending a "name = value" pair to
  the end of the configuration file.
- openssl-gost.control: Insert new "name = value" pair before the
  first empty line (closes: 39310).

* Thu Jul 15 2021 Paul Wolneykien <manowar@altlinux.org> 1.1.0.3.0.255.ge3af41d.p1-alt4
- Fix: Remove synonyms for 'enabled' and 'disabled' states (closes: 40500).

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 1.1.0.3.0.255.ge3af41d.p1-alt3.1
- NMU: spec: adapted to new cmake macros.

* Mon Jun 01 2020 Paul Wolneykien <manowar@altlinux.org> 1.1.0.3.0.255.ge3af41d.p1-alt3
- Fix for the "openssl-gost' control: Don't override the main section
  (closes: 37922).

* Fri Oct 25 2019 Paul Wolneykien <manowar@altlinux.org> 1.1.0.3.0.255.ge3af41d.p1-alt2
- Added openssl-gost control script to turn the GOST ciphers on
  and off.

* Fri Aug 16 2019 Michael Shigorin <mike@altlinux.org> 1.1.0.3.0.255.ge3af41d.p1-alt1.1
- E2K: workaround tests ftbfs

* Thu Jul 04 2019 Paul Wolneykien <manowar@altlinux.org> 1.1.0.3.0.255.ge3af41d.p1-alt1
- Allow to set an IV for MAC using EVP_MD_CTRL_SET_IV (patch).
- Added ECB mode GOST28147-89 cipher (patch).

* Mon Mar 04 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.0.3.0.255.ge3af41d-alt1
- Backported new algorithms from upstream master.

* Sat Sep 29 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.0.3.0.21.ga2174a8-alt1
- Initial build (v1.1.0.3-21-ga2174a8).
