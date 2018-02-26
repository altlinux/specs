%define oname nss
Name:           mingw32-libnss
Version:        3.12.9.0
Release:       	alt1

Summary:        Netscape Network Security Services(NSS)

License:        MPL/GPL/LGPL
Group:          System/Libraries
Url:		http://www.mozilla.org/projects/security/pki/nss

Source0:	https://ftp.mozilla.org/pub/mozilla.org/%oname/releases/v%version/src/nss-%version.tar
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
Patch6:		nss-enable-pem.patch
Patch11:	nss-sysinit-fix-trustorder.patch
Patch12:	nss-sysinit-userdb-first.patch
Patch13:	allow-content-types-beyond-smime.patch
Patch14:	dont-use-cpp-reserved-words.patch
Patch15:	nsspem-642433.patch
Patch16:	nss-recurse.patch

# mingw
Patch20:         nss-3.12.7-build.patch

BuildArch: noarch

# Automatically added by buildreq on Wed Feb 13 2008 (-bi)
#BuildRequires: chrpath zlib-devel libsqlite3-devel
BuildRequires:	mingw32-libnspr-devel >= 4.8.7-alt1
Requires:	mingw32-libnspr       >= 4.8.7-alt1

BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-runtime >= 3.15.1
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-pkg-config

BuildRequires: mingw32-zlib-static mingw32-sqlite


%description
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


%package devel
Summary:	NSS development kit
Group:		Development/C
#Requires:	%name = %version-%release

#Provides:	%name-devel        = %version-%release
#Provides:	%name-pkcs11-devel = %version-%release

%description devel
NSS development kit

%package utils
Summary:	Netscape Network Security Services Utilities
Group:		Development/Other
Requires:	%name = %version-%release

%description utils
Netscape Network Security Services Utilities

%prep
%setup -n %oname-%version
%setup -n %oname-%version -T -D -a7
#patch0 -p0 -b .fix0
%patch2 -p0 -b .fix2
#patch3 -p0 -b .fix3
#patch4 -p0 -b .fix4
%patch5 -p0 -b .fix5

#patch6 -p1 -b .libpem
%patch11 -p1 -b .643134
%patch12 -p0 -b .603313
%patch13 -p1 -b .contenttypes
%patch14 -p1 -b .676036
%patch15 -p1 -b .642433
%patch16 -p1 -b .recurse
%patch20 -p1 -b .mingw

%build
export BUILD_OPT=1 
export NS_USE_GCC=1
export NSS_ENABLE_ECC=1
export NSS_USE_SYSTEM_SQLITE=1
export USE_SYSTEM_ZLIB=1
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1
#export NSPR_INCLUDE_DIR=/usr/include/nspr
#export NSPR_LIB_DIR=%_libdir

export NSPR_INCLUDE_DIR=`%{_mingw32_target}-pkg-config --cflags-only-I nspr | sed 's/-I//'`
export NSPR_LIB_DIR=`%{_mingw32_target}-pkg-config --libs-only-L nspr | sed 's/-L//'`

(cd mozilla/security/coreconf/nsinstall && mkdir Linux && \
gcc -o Linux/nsinstall nsinstall.c pathsub.c)

# broken linking on x86_64
#make -C mozilla/security/coreconf

#make -C mozilla/security/coreconf platform 2>/dev/null |grep '^Linux' >destdir
echo "WINNT" >destdir

pushd mozilla/security

#mozilla/security/coreconf/nsinstall
%__subst "s|= nsinstall|= \$(NSINSTALL_DIR)/nsinstall|g" coreconf/WIN32.mk.mingw

# Generate symbolic info for debuggers
export XCFLAGS=$RPM_OPT_FLAGS

%ifarch x86_64
export USE_64=1
%endif

# additional CA certificates
#cat %SOURCE3 >> mozilla/security/nss/lib/ckfw/builtins/certdata.txt


#

#make -C mozilla/security/dbm
%{_mingw32_make} -C dbm OS_TARGET=WINNT OS_RELEASE=5.0 XP_WIN=1 \
	NSINSTALL=$(pwd)/coreconf/nsinstall/Linux/nsinstall NS_USE_GCC=1 \
	NSS_USE_SYSTEM_SQLITE=1 USE_SYSTEM_ZLIB=1 ZLIB_LIBS=%{_mingw32_libdir}/libz.dll.a \
	CC=%{_mingw32_cc} RC=%{_mingw32_windres} RANLIB=%{_mingw32_ranlib}

#make -C mozilla/security/nss/lib/ckfw/builtins generate

#make -C mozilla/security/nss
%{_mingw32_make} -C nss OS_TARGET=WINNT OS_RELEASE=5.0 XP_WIN=1 \
	NSINSTALL=$(pwd)/coreconf/nsinstall/Linux/nsinstall NS_USE_GCC=1 \
	NSS_USE_SYSTEM_SQLITE=1 USE_SYSTEM_ZLIB=1 ZLIB_LIBS=%{_mingw32_libdir}/libz.dll.a \
	CC=%{_mingw32_cc} RC=%{_mingw32_windres} RANLIB=%{_mingw32_ranlib}

%install
%__mkdir_p %buildroot{%_mingw32_bindir,%_mingw32_libdir/pkgconfig,%_mingw32_includedir}

# Get some variables
DESTDIR="$(head -1 destdir)"
NSPR_VERSION="$(%_mingw32_bindir/nspr-config --version)"
nss_h="mozilla/security/nss/lib/nss/nss.h"
NSS_VMAJOR="$(sed -ne 's,^#define[[:space:]]\+NSS_VMAJOR[[:space:]]\+,,p' "$nss_h")"
NSS_VMINOR="$(sed -ne 's,^#define[[:space:]]\+NSS_VMINOR[[:space:]]\+,,p' "$nss_h")"
NSS_VPATCH="$(sed -ne 's,^#define[[:space:]]\+NSS_VPATCH[[:space:]]\+,,p' "$nss_h")"

# Install NSS libraries 
cd mozilla/dist
cp -aL "$DESTDIR"/bin/* %buildroot%{_mingw32_bindir}/
cp -aL "$DESTDIR"/lib/*.dll %buildroot%{_mingw32_bindir}/
cp -aL "$DESTDIR"/lib/*.a %buildroot%{_mingw32_libdir}/

# Install NSS headers
cd public
cp -aL nss %buildroot%_mingw32_includedir/

# Install NSS utils
sed -e "s,@libdir@,%_mingw32_libdir,g" \
    -e "s,@prefix@,%_mingw32_prefix,g" \
    -e "s,@exec_prefix@,%_mingw32_prefix,g" \
    -e "s,@includedir@,%_mingw32_includedir/nss,g" \
    -e "s,@NSPR_VERSION@,$NSPR_VERSION,g" \
    -e "s,@NSS_VERSION@,%version,g" \
	%SOURCE1 > %buildroot/%_mingw32_libdir/pkgconfig/nss.pc

sed -e "s,@libdir@,%_mingw32_libdir,g" \
    -e "s,@prefix@,%_mingw32_prefix,g" \
    -e "s,@exec_prefix@,%_mingw32_prefix,g" \
    -e "s,@includedir@,%_mingw32_includedir/nss,g" \
    -e "s,@MOD_MAJOR_VERSION@,$NSS_VMAJOR,g" \
    -e "s,@MOD_MINOR_VERSION@,$NSS_VMINOR,g" \
    -e "s,@MOD_PATCH_VERSION@,$NSS_VPATCH,g" \
    %SOURCE2 > %buildroot/%_mingw32_bindir/nss-config

chmod 755 %buildroot/%_mingw32_bindir/nss-config

# https://wiki.mozilla.org/NSS_Shared_DB
# https://wiki.mozilla.org/NSS_Shared_DB_Samples
# https://wiki.mozilla.org/NSS_Shared_DB_Howto
# https://wiki.mozilla.org/NSS_Shared_DB_And_LINUX
#mkdir -p -- %buildroot/%_sysconfdir/pki/nssdb
#tar -x -C %buildroot/%_sysconfdir/pki/nssdb -f %SOURCE4
#find %buildroot/%_sysconfdir/pki/nssdb -name 'blank-*.db' -printf '%%h %%f\n' |
#while read p n; do
#	mv -f -- "$p/$n" "$p/${n##blank-}"
#done

#install -p -m755 %SOURCE5 %buildroot/%_bindir/setup-nsssysinit.sh
#install -p -m644 %SOURCE6 %buildroot/%_sysconfdir/pki/nssdb/pkcs11.txt

#mv %buildroot%{_mingw32_libdir}/*.dll %buildroot%{_mingw32_bindir}/
for file in softokn nss nssutil ssl smime nssdbm
do
  mv %buildroot%{_mingw32_libdir}/lib${file}3.a %buildroot%{_mingw32_libdir}/lib${file}3.dll.a
done

# conflicts with openssl
mv %buildroot%{_mingw32_libdir}/libssl.a %buildroot%{_mingw32_libdir}/libssl3.a

%files
%{_mingw32_bindir}/*.dll

%files devel
%{_mingw32_libdir}/*.a
%{_mingw32_libdir}/pkgconfig/nss.pc
%{_mingw32_bindir}/nss-config
%{_mingw32_includedir}/nss/
#%{_mingw32_sysconfdir}/pki/nssdb/*.db

%files utils
%{_mingw32_bindir}/*.exe
#%{_mingw32_libdir}/nss/*.exe

%changelog
* Fri Mar 25 2011 Vitaly Lipatov <lav@altlinux.ru> 3.12.9.0-alt1
- initial build for ALT Linux Sisyphus

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

