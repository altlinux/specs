%global softhsm_module "SoftHSM PKCS #11 Module"
%global nssdb %_sysconfdir/pki/nssdb

%define beta rc1

Name: softhsm
Version: 2.0.0
Release: alt0.%beta.1

Summary: Software version of a PKCS#11 Hardware Security Module
License: BSD
Group: System/Libraries

Url: http://www.opendnssec.org/
Source0: http://dist.opendnssec.org/source/testing/%name-%version%beta.tar.gz
Source1: http://dist.opendnssec.org/source/testing/%name-%version%beta.tar.gz.sig
Source2: softhsm.module
# taken from coolkey which is not build on all arches we build on
Source3: softhsm2-pk11install.c

# Automatically added by buildreq on Fri Oct 30 2015
# optimized out: libcom_err-devel libkrb5-devel libnspr-devel libstdc++-devel pkg-config
BuildRequires: gcc-c++ libnss-devel libsqlite3-devel libssl-devel sqlite3 zlib-devel

Requires(pre):	shadow-utils
Requires(post):	nss-utils

%description
OpenDNSSEC is providing a software implementation of a generic
cryptographic device with a PKCS#11 interface, the SoftHSM.

SoftHSM is designed to meet the requirements of OpenDNSSEC, but can also
work together with other cryptographic products because of the PKCS#11
interface.

%package devel
Summary: Development package of softhsm that includes the header files
Group: Development/Other
BuildArch: noarch

%description devel
The devel package contains the libsofthsm include files.

%prep
%setup -n %name-%version%beta

%build
%autoreconf

# remove softhsm/ subdir auto-added to --libdir
sed -i "s:full_libdir/softhsm:full_libdir:g" configure
sed -i 's:^full_libdir=":#full_libdir=":g' configure.ac
sed -i "s:libdir)/@PACKAGE@:libdir):" Makefile.in

%configure \
	--libdir=%_libdir/pkcs11 \
	--with-openssl=%prefix \
	--enable-ecc \
	--disable-gost \
	--with-migrate \
	--enable-visibility
%make
# install our copy of pk11install taken from coolkey package
cp %SOURCE3 .
cc %optflags $(pkg-config --cflags nss) -c softhsm2-pk11install.c
cc %optflags softhsm2-pk11install.o -o softhsm2-pk11install \
	$(pkg-config --libs nss) -lpthread  -lsoftokn3 -ldl -lz

%install
%makeinstall_std
install -pDm644 %SOURCE2 %buildroot/%_datadir/p11-kit/modules/softhsm.module

rm %buildroot%_sysconfdir/softhsm2.conf.sample
rm -f %buildroot%_libdir/pkcs11/*a
mkdir -p %buildroot%_includedir/softhsm
cp -a src/lib/*.h %buildroot%_includedir/softhsm
mkdir -p %buildroot%_sharedstatedir/softhsm/tokens
install -pDm755 softhsm2-pk11install %buildroot%_bindir/softhsm2-pk11install

# leave a softlink where softhsm-1 installed its library. Programs like
# opendnssec have that filename in their configuration file.
mkdir -p %buildroot%_libdir/softhsm/
ln -s ../pkcs11/libsofthsm2.so %buildroot%_libdir/softhsm/libsofthsm.so

%pre
getent group ods >/dev/null || groupadd -r ods
getent passwd ods >/dev/null || \
    useradd -r -g ods -d /%_sharedstatedir/softhsm -s /sbin/nologin \
    -c "softhsm private keys owner" ods
:

%post
isThere=`modutil -rawlist -dbdir %nssdb | grep %softhsm_module || echo NO`
if [ "$isThere" == "NO" ]; then
	softhsm2-pk11install -p %nssdb \
		'name=%softhsm_module library=libsofthsm2.so'
fi

if [ $1 -eq 0 ]; then
	modutil -delete %softhsm_module -dbdir %nssdb -force ||:
fi

%files
%doc LICENSE README.md NEWS
%config(noreplace) %_sysconfdir/softhsm2.conf
%_bindir/*
%dir %_libdir/softhsm
%_libdir/pkcs11/libsofthsm2.so
%_libdir/softhsm/libsofthsm.so
%attr(644,root,root) %_datadir/p11-kit/modules/softhsm.module
%attr(770,ods,ods) %dir %_sharedstatedir/softhsm
%attr(770,ods,ods) %dir %_sharedstatedir/softhsm/tokens
%_man1dir/*
%_man5dir/*

%files devel
%dir %_includedir/softhsm
%_includedir/softhsm/*.h

%changelog
* Fri Oct 30 2015 Michael Shigorin <mike@altlinux.org> 2.0.0-alt0.rc1.1
- built for ALT Linux (based on rosa/fedora package)
- fixed broken as-needed linking of softhsm2-pk11install.c,
  see also https://bugzilla.mozilla.org/124318
