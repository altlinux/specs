Summary:        Netscape Network Security Services(NSS)
Name:           nss
Version:        3.13.4
Release:       	alt2
License:        MPL/GPL/LGPL
Group:          System/Libraries
Url:		http://www.mozilla.org/projects/security/pki/nss
Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	nss-%version.tar
Source1:	nss.pc.in
Source2:	nss-config.in
Source3: 	nss-alt-ssl-addon-certs.txt
Source4:	nss-db-%version.tar
Source5:	setup-nsssysinit.sh
Source6:	system-pkcs11.txt
Source7:	nss-pem-%version.tar

Patch0:		nss_with_system_nspr.patch
Patch2:		nss-no-rpath.patch
Patch3:		nss-use-sqlite.patch
Patch4:		nss-use-mozsqlite.patch
Patch5:		nss-fix-objdir.patch

# Fedora patches
Patch10:	nss-enable-pem.patch

# https://bugzilla.mozilla.org/show_bug.cgi?id=562116
Patch11:	Bug-562116-drbg.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=695011
Patch12:	Bug-695011-PEM-logging.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=772628
# https://bugzilla.mozilla.org/show_bug.cgi?id=745224
Patch13:	Bug-772628-nss_Init-leaks-memory.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=784672
# https://bugzilla.mozilla.org/show_bug.cgi?id=734492
Patch14:	Bug-784672-protect-against-calls-before-nss_init.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=800674
# https://bugzilla.mozilla.org/show_bug.cgi?id=734484
Patch15:	Bug-800674-Unable-to-contact-LDAP-Server-during-winsync.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=801975
# https://bugzilla.mozilla.org/show_bug.cgi?id=679814
# https://bugzilla.mozilla.org/show_bug.cgi?id=698049
# https://bugzilla.mozilla.org/show_bug.cgi?id=475578
Patch16:	Bug-801975-Restore-use-of-NSS_NoDB_Init-or-alternate.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=642433
Patch17:	Bug-642433-pem.patch

BuildRequires:	chrpath zlib-devel libsqlite3-devel
BuildRequires:	libnspr-devel >= 4.9.0-alt1
Requires:	libnspr       >= 4.9.0-alt1

%description
Network Security Services (NSS) is a set of libraries designed
to support cross-platform development of security-enabled server
applications. Applications built with NSS can support SSL v2
and v3, TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME,
X.509 v3 certificates, and other security standards.  See:
http://www.mozilla.org/projects/security/pki/nss/overview.html

%package -n lib%name
Summary:        Netscape Network Security Services(NSS)
Group:          System/Libraries

Provides: 	%name = %version-%release

%description -n lib%name
Network Security Services (NSS) is a set of libraries designed
to support cross-platform development of security-enabled server
applications. Applications built with NSS can support SSL v2
and v3, TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME,
X.509 v3 certificates, and other security standards.  See:
http://www.mozilla.org/projects/security/pki/nss/overview.html

%package -n lib%name-sysinit
Summary:	System NSS Initilization
Group:		System/Libraries
Requires:	lib%name = %version-%release

Provides:	%name-sysinit
Provides:	%name-system-init

%description -n lib%name-sysinit
Default Operating System module that manages applications loading
NSS globally on the system. This module loads the system defined
PKCS #11 modules for NSS and chains with other NSS modules to load
any system or user configured modules.


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

Provides:	%name-devel-static = %version-%release

%description -n lib%name-devel-static
NSS development kit (static libs)

%package -n %name-utils
Summary:	Netscape Network Security Services Utilities
Group:		Development/Other
Requires:	lib%name = %version-%release

Provides:	%name-tools

%description -n %name-utils
Netscape Network Security Services Utilities


%prep
%setup -q
%setup -q -T -D -a7
#patch0 -p0
%patch2 -p0
#patch3 -p0
#patch4 -p0
%patch5 -p0

%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1


%build
export BUILD_OPT=1 
export NS_USE_GCC=1
export NSS_ENABLE_ECC=1
export NSS_USE_SYSTEM_SQLITE=1
export USE_SYSTEM_ZLIB=1
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1
export NSPR_INCLUDE_DIR=/usr/include/nspr
export NSPR_LIB_DIR=%_libdir

# Generate symbolic info for debuggers
export XCFLAGS=$RPM_OPT_FLAGS

%ifarch x86_64
export USE_64=1
%endif

# additional CA certificates
cat %SOURCE3 >> mozilla/security/nss/lib/ckfw/builtins/certdata.txt

make -C mozilla/security/coreconf
make -C mozilla/security/coreconf platform 2>/dev/null |grep '^Linux' >destdir
make -C mozilla/security/dbm
make -C mozilla/security/nss/lib/ckfw/builtins generate
make -C mozilla/security/nss

%install
%__mkdir_p %buildroot{%_bindir,%_libdir/pkgconfig,%_includedir}

# Get some variables
DESTDIR="$(head -1 destdir)"
NSPR_VERSION="$(nspr-config --version)"
nss_h="mozilla/security/nss/lib/nss/nss.h"
NSS_VMAJOR="$(sed -ne 's,^#define[[:space:]]\+NSS_VMAJOR[[:space:]]\+,,p' "$nss_h")"
NSS_VMINOR="$(sed -ne 's,^#define[[:space:]]\+NSS_VMINOR[[:space:]]\+,,p' "$nss_h")"
NSS_VPATCH="$(sed -ne 's,^#define[[:space:]]\+NSS_VPATCH[[:space:]]\+,,p' "$nss_h")"

# Install NSS libraries 
cd mozilla/dist
cp -aL "$DESTDIR"/bin/* %buildroot%_bindir
cp -aL "$DESTDIR"/lib/* %buildroot%_libdir

# Install NSS headers
cd public
cp -aL nss %buildroot%_includedir

# Install NSS utils
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
  %__file "$f" | grep -qs ELF || continue
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

%files -n %name-utils
%_bindir/*
%exclude %_bindir/setup-nsssysinit.sh
# Remove tests and samples
%exclude %_bindir/%name-config
%exclude %_bindir/bltest
%exclude %_bindir/dbtest
%exclude %_bindir/mangle
%exclude %_bindir/ocspclnt
%exclude %_bindir/oidcalc
%exclude %_bindir/sdrtest
%exclude %_bindir/shlibsign
%exclude %_bindir/tstclnt
%exclude %_bindir/vfyserv

%files -n lib%name
%_libdir/*.so*
%_libdir/*.chk
%dir %_sysconfdir/pki
%dir %_sysconfdir/pki/nssdb
%config(noreplace) %_sysconfdir/pki/nssdb/cert8.db
%config(noreplace) %_sysconfdir/pki/nssdb/key3.db
%config(noreplace) %_sysconfdir/pki/nssdb/secmod.db
%exclude %_libdir/libnsssysinit.so

%files -n lib%name-sysinit
%_libdir/libnsssysinit.so
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

%changelog
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

