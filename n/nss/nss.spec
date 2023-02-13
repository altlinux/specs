Summary:	Netscape Network Security Services(NSS)
Name:		nss
Version:	3.88.1
Release:	alt1
License:	MPL-2.0
Group:		System/Libraries
Url:		http://www.mozilla.org/projects/security/pki/nss

Source0:	nss-%version.tar
Source1:	nss.pc.in
Source2:	nss-config.in
Source4:	nss-db-%version.tar
Source5:	setup-nsssysinit.sh
Source6:	system-pkcs11.txt

Patch1: 0001-Disable-test-dbtest-r-w-in-a-readonly-directory.patch

BuildRequires:  gcc-c++
BuildRequires:  chrpath zlib-devel libsqlite3-devel
BuildRequires:  rpm-macros-alternatives
BuildRequires:  python3
BuildRequires:  gyp
BuildRequires:  ninja-build
BuildRequires:  libnspr-devel

%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec
%global unsupported_bindir %_libexecdir/nss

%description
Network Security Services (NSS) is a set of libraries designed
to support cross-platform development of security-enabled server
applications. Applications built with NSS can support SSL v2
and v3, TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME,
X.509 v3 certificates, and other security standards.  See:
http://www.mozilla.org/projects/security/pki/nss/overview.html

%package -n lib%name
Summary:	Netscape Network Security Services(NSS)
Group:		System/Libraries

Provides:	%name = %version-%release

Provides:	%name-sysinit
Provides:	%name-system-init

Provides:	lib%name-sysinit = %version-%release
Obsoletes:	lib%name-sysinit

%description -n lib%name
Network Security Services (NSS) is a set of libraries designed
to support cross-platform development of security-enabled server
applications. Applications built with NSS can support SSL v2
and v3, TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME,
X.509 v3 certificates, and other security standards.  See:
http://www.mozilla.org/projects/security/pki/nss/overview.html

%package -n lib%name-devel
Summary:	NSS development kit
Group:		Development/C
Requires:	lib%name = %version-%release

Provides:	%name-devel        = %version-%release
Provides:	%name-pkcs11-devel = %version-%release

%description -n lib%name-devel
NSS development kit

%package -n lib%name-devel-static
Summary:	NSS static libraries
Group:		Development/C
Requires:	lib%name-devel = %version-%release

Provides:	%name-devel-static        = %version-%release
Provides:	%name-pkcs11-devel-static = %version-%release

%description -n lib%name-devel-static
NSS development kit (static libs)

%package -n lib%name-nssckbi-checkinstall
Summary: Check p11-kit-trust.so and libnssckbi.so compatibility
Group: Security/Networking
Requires: p11-kit-checkinstall

%description -n lib%name-nssckbi-checkinstall
During installation check that p11-kit-trust.so and libnssckbi.so are
compatible with each other.
This package intedent to be used in the install check step in the build
system only and should not be installed in the real systems.

%package -n %name-utils
Summary:	Netscape Network Security Services Utilities
Group:		Development/Other
Requires:	lib%name = %version-%release

Provides:	%name-tools

%description -n %name-utils
Netscape Network Security Services Utilities

%prep
%setup -q
%patch1 -p1 -d nss

%build
mkdir -p bin
export PATH="$PWD/bin:$PATH"

ln -s %_bindir/python3 bin/python

%{?_is_lp64:export USE_64=1}

cd nss
./build.sh \
	--gcc \
	--opt \
	--system-nspr \
	--system-sqlite \
	--enable-legacy-db \
	--enable-libpkix \
	#

%install
# Get some variables
DESTDIR="$PWD/dist/Release"
NSPR_VERSION="$(nspr-config --version)"
nss_h="nss/lib/nss/nss.h"
NSS_VMAJOR="$(sed -ne 's,^#define[[:space:]]\+NSS_VMAJOR[[:space:]]\+,,p' "$nss_h")"
NSS_VMINOR="$(sed -ne 's,^#define[[:space:]]\+NSS_VMINOR[[:space:]]\+,,p' "$nss_h")"
NSS_VPATCH="$(sed -ne 's,^#define[[:space:]]\+NSS_VPATCH[[:space:]]\+,,p' "$nss_h")"

# Install NSS libraries
cd dist

# fedora utilities
mkdir -p -- %buildroot%_bindir
for n in \
	certutil cmsutil crlutil modutil nss-policy-check pk12util signver \
	ssltap \
	;
do
	cp -L -- "$DESTDIR/bin/$n" %buildroot%_bindir/
done

# fedora unsupported utilites
mkdir -p -- %buildroot%unsupported_bindir
for n in \
	bltest ecperf fbectest shlibsign atob btoa derdump listsuites \
	ocspclnt pp selfserv signtool strsclnt symkeyutil tstclnt vfyserv \
	vfychain \
	;
do
	cp -L -- "$DESTDIR/bin/$n" %buildroot%unsupported_bindir/
done

mkdir -p -- %buildroot%_libdir
cp -aL "$DESTDIR"/lib/* %buildroot%_libdir
rm -f -- %buildroot%_libdir/*.TOC

# Install NSS headers
mkdir -p %buildroot%_includedir
cp -aL public/nss %buildroot%_includedir

# Copy some freebl include files we also want
mkdir -p -- %buildroot/%_includedir/%name/private

for n in blapi.h alghmac.h cmac.h; do
    cp -aL private/nss/$n %buildroot/%_includedir/%name/private/$n
done

# Install NSS utils
mkdir -p -- %buildroot%_libdir/pkgconfig

sed -e "s,@libdir@,%_libdir,g" \
    -e "s,@prefix@,%_prefix,g" \
    -e "s,@exec_prefix@,%_prefix,g" \
    -e "s,@includedir@,%_includedir/nss,g" \
    -e "s,@NSPR_VERSION@,$NSPR_VERSION,g" \
    -e "s,@NSS_VERSION@,%version,g" \
    %SOURCE1 > %buildroot/%_libdir/pkgconfig/nss.pc

sed -e "s,@libdir@,%_libdir,g" \
    -e "s,@prefix@,%_prefix,g" \
    -e "s,@exec_prefix@,%_prefix,g" \
    -e "s,@includedir@,%_includedir/nss,g" \
    -e "s,@MOD_MAJOR_VERSION@,$NSS_VMAJOR,g" \
    -e "s,@MOD_MINOR_VERSION@,$NSS_VMINOR,g" \
    -e "s,@MOD_PATCH_VERSION@,$NSS_VPATCH,g" \
    %SOURCE2 > %buildroot/%_bindir/nss-config

chmod 755 %buildroot/%_bindir/nss-config

# Add real RPATH
find "%buildroot%_bindir" "%buildroot%_libdir" -type f |
while read f; do
  file "$f" | grep -qs ELF || continue
  if chrpath -l "$f" | fgrep -qs "RPATH="; then
    chrpath -d "$f"
  fi
done

# https://wiki.mozilla.org/NSS_Shared_DB
# https://wiki.mozilla.org/NSS_Shared_DB_Samples
# https://wiki.mozilla.org/NSS_Shared_DB_Howto
# https://wiki.mozilla.org/NSS_Shared_DB_And_LINUX
mkdir -p -- %buildroot/%_sysconfdir/pki/nssdb
tar -x -C %buildroot/%_sysconfdir/pki/nssdb -f %SOURCE4
find %buildroot/%_sysconfdir/pki/nssdb -name 'blank-*.db' -printf '%%h %%f\n' |
while read p n; do
	mv -f -- "$p/$n" "$p/${n##blank-}"
done

install -p -m755 %SOURCE5 %buildroot/%_bindir/setup-nsssysinit.sh
install -p -m644 %SOURCE6 %buildroot/%_sysconfdir/pki/nssdb/pkcs11.txt

# alternatives
mkdir -p -- %buildroot/%_libdir/nss
mv -- %buildroot/%_libdir/libnssckbi.so %buildroot/%_libdir/nss/libnssckbi.so

mkdir -p -- %buildroot/%_altdir
cat >%buildroot/%_altdir/libnssckbi-%name <<EOF
%_libdir/libnssckbi.so	%_libdir/nss/libnssckbi.so	10
EOF

%check
pushd nss/tests
./all.sh
popd

%files -n %name-utils
%_bindir/*
%unsupported_bindir
%exclude %_bindir/setup-nsssysinit.sh
%exclude %_bindir/%name-config

%files -n lib%name
%_altdir/libnssckbi-%name
%_libdir/*.so*
%_libdir/*.chk
%_libdir/nss
%dir %_sysconfdir/pki/nssdb
%config(noreplace) %_sysconfdir/pki/nssdb/cert8.db
%config(noreplace) %_sysconfdir/pki/nssdb/key3.db
%config(noreplace) %_sysconfdir/pki/nssdb/secmod.db
%config(noreplace) %_sysconfdir/pki/nssdb/cert9.db
%config(noreplace) %_sysconfdir/pki/nssdb/key4.db
%config(noreplace) %_sysconfdir/pki/nssdb/pkcs11.txt
%_bindir/setup-nsssysinit.sh

%files -n lib%name-devel
%_bindir/%name-config
%dir %_includedir/%name
%_includedir/%name
%_libdir/pkgconfig/*

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name-nssckbi-checkinstall

%changelog
* Mon Feb 13 2023 Alexey Gladkov <legion@altlinux.ru> 3.88.1-alt1
- New version (3.88.1).

* Wed Dec 14 2022 Alexey Gladkov <legion@altlinux.ru> 3.86-alt1
- New version (3.86).
- Set nssckbi version number to 2.60.
- Certificate Authority Changes:
  + Remove CN=EC-ACC
  + Remove CN=Network Solutions Certificate Authority
  + Remove CN=Staat der Nederlanden EV Root CA
  + Remove CN=SwissSign Platinum CA - G2

* Thu Nov 24 2022 Alexey Gladkov <legion@altlinux.ru> 3.85-alt1
- New version (3.85).

* Thu Oct 13 2022 Alexey Gladkov <legion@altlinux.ru> 3.84-alt1
- New version (3.84).

* Thu Sep 15 2022 Alexey Gladkov <legion@altlinux.ru> 3.83-alt1
- New version (3.83).
- Certificate Authority Changes:
  + Add CN=DIGITALSIGN GLOBAL ROOT ECDSA CA
  + Add CN=DIGITALSIGN GLOBAL ROOT RSA CA
  + Add CN=Security Communication ECC RootCA1
  + Add CN=Security Communication RootCA3
  + Remove CN=Global Chambersign Root

* Tue Sep 06 2022 Alexey Gladkov <legion@altlinux.ru> 3.82-alt1
- New version (3.82).

* Fri Jul 22 2022 Alexey Gladkov <legion@altlinux.ru> 3.81-alt1
- New version (3.81).
- Certificate Authority Changes:
  + Add CN=Certainly Root E1
  + Add CN=Certainly Root R1
  + Add CN=DigiCert SMIME ECC P384 Root G5
  + Add CN=DigiCert SMIME RSA4096 Root G5
  + Add CN=DigiCert TLS ECC P384 Root G5
  + Add CN=DigiCert TLS RSA4096 Root G5
  + Add CN=E-Tugra Global Root CA ECC v3
  + Add CN=E-Tugra Global Root CA RSA v3
  + Remove CN=Hellenic Academic and Research Institutions RootCA 2011

* Wed Jun 08 2022 Alexey Gladkov <legion@altlinux.ru> 3.79-alt1
- New version (3.79).

* Thu Apr 28 2022 Alexey Gladkov <legion@altlinux.ru> 3.78-alt1
- New version (3.78).

* Fri Apr 01 2022 Alexey Gladkov <legion@altlinux.ru> 3.77-alt1
- New version (3.77).
- Certificate Authority Changes:
  + Add CN=Telia Root CA v2
  + Add CN=D-TRUST BR Root CA 1 2020
  + Add CN=D-TRUST EV Root CA 1 2020
  + Remove CN=DigiNotar PKIoverheid CA Organisatie - G2
  + Remove CN=Trustwave Organization Issuing CA, Level 2
  + Remove TURKTRUST Mis-issued Intermediate CA 1
  + Remove TURKTRUST Mis-issued Intermediate CA 2

* Tue Mar 08 2022 Alexey Gladkov <legion@altlinux.ru> 3.76-alt1
- New version (3.76).

* Wed Feb 09 2022 Alexey Gladkov <legion@altlinux.ru> 3.75-alt1
- New version (3.75).

* Fri Jan 07 2022 Alexey Gladkov <legion@altlinux.ru> 3.74-alt1
- New version (3.74).
- Certificate Authority Changes:
  + Add HiPKI Root CA - G1
  + Add ISRG Root X2
  + Add vTrus Root CA
  + Add vTrus ECC Root CA
  + Add Autoridad de Certificacion Firmaprofesional CIF A62634068
  + Remove DST Root CA X3
  + Remove GlobalSign Root CA - R2
  + Remove Cybertrust Global Root
  + Replace GlobalSign ECC Root CA - R4
  + Replace GTS Root R1
  + Replace GTS Root R2
  + Replace GTS Root R3
  + Replace GTS Root R4

* Wed Dec 01 2021 Alexey Gladkov <legion@altlinux.ru> 3.73-alt1
- New version (3.73).
- Security fixes:
  + CVE-2021-43527: Heap overflow in NSS when verifying DSA/RSA-PSS DER-encoded signatures

* Thu Nov 11 2021 Alexey Gladkov <legion@altlinux.ru> 3.72-alt2
- nss-utils: Install utilities used by fedora and opensuse (ALT#41317).

* Tue Nov 02 2021 Alexey Gladkov <legion@altlinux.ru> 3.72-alt1
- New version (3.72).

* Wed Oct 06 2021 Alexey Gladkov <legion@altlinux.ru> 3.71-alt1
- New version (3.71).
- Certificate Authority Changes:
  + Add CN=HARICA TLS RSA Root CA 2021
  + Add CN=HARICA TLS ECC Root CA 2021
  + Add CN=HARICA Client RSA Root CA 2021
  + Add CN=HARICA Client ECC Root CA 2021
  + Add CN=TunTrust Root CA

* Tue Sep 07 2021 Alexey Gladkov <legion@altlinux.ru> 3.69.1-alt1
- New version (3.69.1).

* Tue Aug 10 2021 Alexey Gladkov <legion@altlinux.ru> 3.69.0-alt1
- New version (3.69).

* Sat Jul 17 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.66.0-alt2
- Backported upstream fixes for POWER AES-GCM Vector Acceleration (ALT#40510)
  (MBZ#1566124).
- Enabled testsuite.

* Thu Jun 03 2021 Alexey Gladkov <legion@altlinux.ru> 3.66.0-alt1
- New version (3.66).
- Certificate Authority Changes:
  + Add CN=GLOBALTRUST 2020
  + Add CN=ANF Secure Server Root CA
  + Add CN=Certum EC-384 CA
  + Add CN=Certum Trusted Root CA
  + Remove OU=Trustis FPS Root CA
  + Remove CN=QuoVadis Root Certification Authority
  + Remove CN=Sonera Class2 CA

* Wed Mar 24 2021 Alexey Gladkov <legion@altlinux.ru> 3.63.0-alt1
- New version (3.63).
- Certificate Authority Changes:
  + Add CN=GlobalSign Secure Mail Root R45
  + Add CN=GlobalSign Secure Mail Root E45
  + Add CN=GlobalSign Root R46
  + Add CN=GlobalSign Root E46
  + Add CN=AC RAIZ FNMT-RCM SERVIDORES SEGUROS
  + Remove CN=GeoTrust Primary Certification Authority - G2
  + Remove CN=VeriSign Universal Root Certification Authority
  + Turn off Websites trust bit for "Staat der Nederlanden Root CA - G3"
  + Turn off Websites trust bit for "Chambers of Commerce Root - 2008"
  + Turn off Websites trust bit for "Global Chambersign Root - 2008"

* Wed Jan 27 2021 Alexey Gladkov <legion@altlinux.ru> 3.61.0-alt1
- New version (3.61).
- Certificate Authority Changes:
  + Add CN=NAVER Global Root Certification Authority
  + Remove CN=GeoTrust Global CA
  + Remove CN=GeoTrust Primary Certification Authority
  + Remove CN=GeoTrust Primary Certification Authority - G3
  + Remove CN=GeoTrust Universal CA
  + Remove CN=GeoTrust Universal CA 2
  + Remove CN=VeriSign Class 3 Public Primary Certification Authority - G4
  + Remove CN=VeriSign Class 3 Public Primary Certification Authority - G5
  + Remove CN=thawte Primary Root CA
  + Remove CN=thawte Primary Root CA - G2
  + Remove CN=thawte Primary Root CA - G3

* Sat Dec 26 2020 Alexey Gladkov <legion@altlinux.ru> 3.59.1-alt1
- New version (3.59.1).

* Tue Nov 17 2020 Alexey Gladkov <legion@altlinux.ru> 3.59.0-alt1
- New version (3.59).

* Thu Oct 29 2020 Stanislav Levin <slev@altlinux.org> 3.58.0-alt2
- Backported fix for MBZ#1672703.

* Thu Oct 22 2020 Alexey Gladkov <legion@altlinux.ru> 3.58.0-alt1
- New version (3.58).
- Security fixes:
  + CVE-2020-25648: Tighten CCS handling for middlebox compatibility mode
- Certificate Authority Changes:
  + Add CN=Trustwave Global Certification Authority
  + Add CN=Trustwave Global ECC P256 Certification Authority
  + Add CN=Trustwave Global ECC P384 Certification Authority
  + Remove CN=EE Certification Centre Root CA
  + Remove O=Government Root Certification Authority; C=TW
  + Modify CN=OISTE WISeKey Global Root GA CA

* Tue Sep 08 2020 Alexey Gladkov <legion@altlinux.ru> 3.56.0-alt1
- New version (3.56).

* Thu Jul 30 2020 Alexey Gladkov <legion@altlinux.ru> 3.55.0-alt1
- New version (3.55).
- Security fixes:
  + CVE-2020-6829, CVE-2020-12400: Replace P384 and P521 with new, verifiable implementations from Fiat-Crypto and ECCKiila.
  + CVE-2020-12401: Remove unnecessary scalar padding.
  + CVE-2020-12403: Explicitly disable multi-part ChaCha20 (which was not functioning correctly) and more strictly enforce tag length.

* Mon Jun 29 2020 Alexey Gladkov <legion@altlinux.ru> 3.54.0-alt1
- New version (3.54).
- Merge libnss and libnss-sysinit.
- Certificate Authority Changes:
  + Add CN = certSIGN Root CA G2
  + Add CN = e-Szigno Root CA 2017
  + Add CN = Microsoft ECC Root Certificate Authority 2017
  + Add CN = Microsoft RSA Root Certificate Authority 2017
  + Remove CN = AddTrust Class 1 CA Root
  + Remove CN = AddTrust External CA Root
  + Remove CN = LuxTrust Global Root 2
  + Remove CN = Staat der Nederlanden Root CA - G2
  + Remove CN = Symantec Class 2 Public Primary Certification Authority - G4
  + Remove CN = Symantec Class 1 Public Primary Certification Authority - G4
  + Remove CN = VeriSign Class 3 Public Primary Certification Authority - G3

* Wed Jun 24 2020 Alexey Gladkov <legion@altlinux.ru> 3.53.0-alt4
- Enable an RFC3280 compliant certificate path validation library (ALT#38636).

* Wed Jun 10 2020 Alexey Gladkov <legion@altlinux.ru> 3.53.0-alt3
- Fix build with nss headers and -Werror=strict-prototypes (ALT#38597).

* Mon Jun 08 2020 Alexey Gladkov <legion@altlinux.ru> 3.53.0-alt2
- Enable NSS legacy DBM type (ALT#38590).

* Thu Jun 04 2020 Alexey Gladkov <legion@altlinux.ru> 3.53.0-alt1
- New version (3.53).
- Security fixes:
  + CVE-2020-12399 - Force a fixed length for DSA exponentiation

* Wed May 06 2020 Alexey Gladkov <legion@altlinux.ru> 3.52.0-alt1
- New version (3.52).
- Stop pulling in nss-pem automatically, packages that need it should depend on it.

* Sat Mar 14 2020 Alexey Gladkov <legion@altlinux.ru> 3.51.0-alt1
- New version (3.51).

* Fri Feb 14 2020 Alexey Gladkov <legion@altlinux.ru> 3.49.2-alt1
- New version (3.49.2).

* Thu Jan 23 2020 Alexey Gladkov <legion@altlinux.ru> 3.49.1-alt1
- New version (3.49.1).
- Security fixes:
  + CVE-2019-17023: Additional HRR Tests
- Certificate Authority Changes:
  + Add Entrust Root Certification Authority - G4 Cert

* Mon Dec 02 2019 Alexey Gladkov <legion@altlinux.ru> 3.47.1-alt1
- New version (3.47.1).
- Security fixes:
  + CVE-2019-11745: EncryptUpdate should use maxout, not block size.

* Mon Oct 28 2019 Alexey Gladkov <legion@altlinux.ru> 3.47.0-alt1
- New version (3.47).
- Update license tag.

* Tue Sep 10 2019 Alexey Gladkov <legion@altlinux.ru> 3.46.0-alt1
- New version (3.46).
- Certificate Authority Changes:
  + Remove CN = Swisscom Root CA 2
  + Remove CN = Class 2 Primary CA
  + Remove CN = Class 2 Primary CA
  + Remove CN = Deutsche Telekom Root CA 2

* Thu Jul 11 2019 Alexey Gladkov <legion@altlinux.ru> 3.45.0-alt1
- New version (3.45).

* Wed May 22 2019 Alexey Gladkov <legion@altlinux.ru> 3.44.0-alt1
- New version (3.44).

* Tue May 14 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.43.0-alt2
- Use %%_is_lp64 macro to determine if arch is 64-bit.

* Sun Mar 31 2019 Alexey Gladkov <legion@altlinux.ru> 3.43.0-alt1
- New version (3.43).

* Fri Feb 01 2019 Alexey Gladkov <legion@altlinux.ru> 3.42.1-alt1
- New version (3.42.1).

* Thu Dec 20 2018 Alexey Gladkov <legion@altlinux.ru> 3.40.1-alt1
- New version (3.40.1).

* Mon Nov 12 2018 Alexey Gladkov <legion@altlinux.ru> 3.40.0-alt1
- New version (3.40).

* Sun Sep 09 2018 Alexey Gladkov <legion@altlinux.ru> 3.39.0-alt1
- New version (3.39).

* Tue Jul 03 2018 Alexey Gladkov <legion@altlinux.ru> 3.38.0-alt1
- New version (3.38).

* Thu Jun 07 2018 Alexey Gladkov <legion@altlinux.ru> 3.36.4-alt1
- New version (3.36.4).

* Thu May 17 2018 Alexey Gladkov <legion@altlinux.ru> 3.36.1-alt1
- New version (3.36.1).

* Wed Mar 21 2018 Alexey Gladkov <legion@altlinux.ru> 3.36.0-alt1
- New version (3.36).

* Fri Jan 12 2018 Alexey Gladkov <legion@altlinux.ru> 3.34.1-alt3
- Fix the alteranatives file.

* Fri Dec 29 2017 Alexey Gladkov <legion@altlinux.ru> 3.34.1-alt2
- Add the alteranatives file for libnssckbi.so.
- Add libnss-nssckbi-checkinstall subpackage.

* Sat Dec 23 2017 Alexey Gladkov <legion@altlinux.ru> 3.34.1-alt1
- New version (3.34.1).
- Remove obsolete nss-alt-ssl-addon-certs.txt.

* Sun Oct 08 2017 Alexey Gladkov <legion@altlinux.ru> 3.33.0-alt1
- New version (3.33).

* Fri Aug 25 2017 Alexey Gladkov <legion@altlinux.ru> 3.32.0-alt1
- New version (3.32).

* Wed Jul 12 2017 Alexey Gladkov <legion@altlinux.ru> 3.31.0-alt1
- New version (3.31).

* Wed Mar 15 2017 Alexey Gladkov <legion@altlinux.ru> 3.30.0-alt1
- New version (3.30).

* Mon Jan 30 2017 Alexey Gladkov <legion@altlinux.ru> 3.28.1-alt1
- New version (3.28.1).

* Fri Oct 21 2016 Alexey Gladkov <legion@altlinux.ru> 3.27.1-alt1
- New version (3.27.1).

* Mon Aug 15 2016 Alexey Gladkov <legion@altlinux.ru> 3.26.0-alt1
- New version (3.26).

* Fri Jun 10 2016 Alexey Gladkov <legion@altlinux.ru> 3.24.0-alt1
- New version (3.24).

* Mon Mar 21 2016 Alexey Gladkov <legion@altlinux.ru> 3.23.0-alt1
- New version (3.23).
- Add tstclnt and vfyserv (ALT#31803)
- Disable SSL2.

* Wed Feb 10 2016 Alexey Gladkov <legion@altlinux.ru> 3.22.0-alt1
- New version (3.22.0).

* Fri Jan 08 2016 Alexey Gladkov <legion@altlinux.ru> 3.20.2-alt1
- New version (3.20.2).

* Thu Nov 05 2015 Alexey Gladkov <legion@altlinux.ru> 3.20.1-alt1
- New version (3.20.1).

* Sat Jul 25 2015 Alexey Gladkov <legion@altlinux.ru> 3.19.2-alt1
- New version (3.19.2).

* Mon May 18 2015 Alexey Gladkov <legion@altlinux.ru> 3.19.0-alt1
- New version (3.19.0).

* Mon Apr 06 2015 Alexey Gladkov <legion@altlinux.ru> 3.18.0-alt1
- New version (3.18.0).

* Sun Mar 08 2015 Alexey Gladkov <legion@altlinux.ru> 3.17.4-alt1
- New version (3.17.4).

* Mon Nov 17 2014 Alexey Gladkov <legion@altlinux.ru> 3.17.2-alt1
- New version (3.17.2).

* Wed Sep 24 2014 Alexey Gladkov <legion@altlinux.ru> 3.17.1-alt1
- New version (3.17.1).

* Mon Jun 30 2014 Alexey Gladkov <legion@altlinux.ru> 3.16.2-alt1
- New version (3.16.2).

* Sat May 10 2014 Alexey Gladkov <legion@altlinux.ru> 3.16.1-alt1
- New version (3.16.1).

* Thu Feb 06 2014 Alexey Gladkov <legion@altlinux.ru> 3.15.4-alt1
- New version (3.15.4).

* Wed Nov 20 2013 Alexey Gladkov <legion@altlinux.ru> 3.15.3-alt1
- New version (3.15.3).

* Thu Sep 26 2013 Alexey Gladkov <legion@altlinux.ru> 3.15.2-alt1
- New version (3.15.2).

* Fri Aug 09 2013 Alexey Gladkov <legion@altlinux.ru> 3.15.1-alt1
- New version (3.15.1).

* Wed Apr 10 2013 Alexey Gladkov <legion@altlinux.ru> 3.14.3-alt1
- New version (3.14.3).

* Thu Feb 14 2013 Alexey Gladkov <legion@altlinux.ru> 3.14.2-alt1
- New version (3.14.2).

* Fri Jan 11 2013 Alexey Gladkov <legion@altlinux.ru> 3.14.1-alt1
- New version (3.14.1).

* Tue Aug 28 2012 Alexey Gladkov <legion@altlinux.ru> 3.13.6-alt1
- New version (3.13.6).

* Mon May 07 2012 Alexey Gladkov <legion@altlinux.ru> 3.13.4-alt2
- Update external patches.
- Protect against calls before nss_init (ALT#27300).

* Wed Apr 18 2012 Alexey Gladkov <legion@altlinux.ru> 3.13.4-alt1
- New version (3.13.4).

* Thu Jan 12 2012 Alexey Gladkov <legion@altlinux.ru> 3.13.1-alt2
- Fix "__GNUC_MINOR" is not defined (ALT#26809).

* Mon Jan 02 2012 Alexey Gladkov <legion@altlinux.ru> 3.13.1-alt1
- New version (3.13.1).

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 3.12.11-alt3
- Better coverage for DigiNotarGate in NSS.

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 3.12.11-alt2
- Dis-trust DigiNotar root certificate.

* Wed Aug 17 2011 Alexey Gladkov <legion@altlinux.ru> 3.12.11-alt1
- New version (3.12.11).

* Thu Mar 10 2011 Alexey Gladkov <legion@altlinux.ru> 3.12.9.0-alt2
- Apply fedora patches.
- Rebuilt to enable proper debuginfo.

* Fri Feb 25 2011 Alexey Gladkov <legion@altlinux.ru> 3.12.9.0-alt1
- New version (3.12.9).

* Mon Oct 25 2010 Alexey Gladkov <legion@altlinux.ru> 3.12.8.0-alt1
- New version (3.12.8).
- Add libnss-sysinit subpackage.

* Tue Jun 01 2010 Alexey Gladkov <legion@altlinux.ru> 3.12.7.0-alt1.20100601
- New cvs snapshot 3.12.7.0 20100601.

* Sun Mar 28 2010 Alexey Gladkov <legion@altlinux.ru> 3.12.7.0-alt1.20100328
- New cvs snapshot 3.12.7.0 20100328.

* Thu Feb 18 2010 Alexey Gladkov <legion@altlinux.ru> 3.12.6.0-alt1.20100218
- New cvs snapshot 3.12.6.0 20100218.

* Sat Jan 16 2010 Alexey Gladkov <legion@altlinux.ru> 3.12.6.0-alt1.20100116
- New cvs snapshot 3.12.6.0 20100116.

* Wed Nov 11 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.5.0-alt3.20091106
- Change requires.

* Mon Nov 09 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.5.0-alt2.20091106
- Use system sqlite3 (again).

* Fri Nov 06 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.5.0-alt1.20091106
- New cvs snapshot 3.12.5.0 20091106.

* Sun Nov 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.5.0-alt1.20091101
- New cvs snapshot 3.12.5.0 20091101.

* Fri Sep 18 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.5.0-alt1.20090918
- New cvs snapshot 3.12.5.0 20090918.

* Mon Aug 31 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.5.0-alt1.20090831
- New cvs snapshot 3.12.5.0 20090831.

* Tue Jun 30 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.4.1-alt1.20090630
- New cvs snapshot 3.12.4.1 20090630.

* Mon Jun 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.4.1-alt1.20090601
- New cvs snapshot 3.12.4.1 20090601.

* Mon Apr 20 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.4-alt1.20090421
- New cvs snapshot 3.12.4 20090421.

* Thu Mar 05 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.3-alt1.20090305
- New cvs snapshot 3.12.3 20090305.
- Use mozsqlite3.

* Tue Nov 18 2008 Alexey Gladkov <legion@altlinux.ru> 3.12.3-alt1.20081117
- New cvs snapshot 3.12.3 20081117.

* Sat Jun 28 2008 Alexey Gladkov <legion@altlinux.ru> 3.12.1-alt1.20080628
- New cvs snapshot 3.12.1 20080628.

* Tue May 13 2008 Alexey Gladkov <legion@altlinux.ru> 3.12.1-alt1.20080513
- New version (3.12.1 beta).

* Fri Mar 28 2008 Alexey Gladkov <legion@altlinux.ru> 3.12-alt1.20080328
- New cvs snapshot 3.12 20080328.

* Sun Mar 02 2008 Alexey Gladkov <legion@altlinux.ru> 3.12-alt1.20080229
- New cvs snapshot (3.12).

* Sun Feb 03 2008 Alexey Gladkov <legion@altlinux.ru> 3.12-alt1.20080202
- New cvs snapshot (3.12).

* Wed Nov 28 2007 Alexey Gladkov <legion@altlinux.ru> 3.12-alt1.20071128
- New version (3.12 beta).
- Build with system sqlite and zlib.

* Tue Oct 30 2007 Alexey Gladkov <legion@altlinux.ru> 3.11.7-alt1
- New version (3.11.7).

* Fri Feb 23 2007 Alexey Gladkov <legion@altlinux.ru> 3.11.4-alt1
- New version (3.11.4).
- Build without NSS_ECC_MORE_THAN_SUITE_B.
- Update ALT root CA.

* Thu Nov 16 2006 Alexey Gladkov <legion@altlinux.ru> 3.11.3-alt1
- new version (3.11.3).
- large spec cleanup.
- build with new nspr-4.6.3.

* Sun Jul 16 2006 Alexey Gladkov <legion@altlinux.ru> 3.11.2-alt1
- new version.

* Sun Dec 25 2005 Alexey Gladkov <legion@altlinux.ru> 3.11-alt1
- new version.
- nss.pc was added.
- nss-config fixed.
- x86_64 flags fix.

* Fri Dec 02 2005 Alexey Gladkov <legion@altlinux.ru> 3.10-alt1.1
- NMU.
- nss-config bugfix.
- crmf builtin inside libnss (patch #1).
- New package: nss-utils, libnss-devel-static .

* Wed Nov 23 2005 Eugene Ostapets <eostapets@altlinux.ru> 3.10-alt1
- initial build for ALT Linux.

