%define softhsm_module "SoftHSM PKCS #11 Module"
%define nssdb %_sysconfdir/pki/nssdb

Name: softhsm
Version: 2.1.0

Release: alt2
Summary: Software version of a PKCS#11 Hardware Security Module
License: BSD
Group: System/Configuration/Other

Url: http://www.opendnssec.org/

# repacked https://dist.opendnssec.org/source/%name-%version.tar.gz
Source0: %name-%version.tar

Source2: softhsm.module
# taken from coolkey which is not build on all arches we build on
Source3: softhsm2-pk11install.c
Patch1: softhsm2-1378800-openssl.patch

# Automatically added by buildreq on Wed Nov 02 2016
# optimized out: libcom_err-devel libkrb5-devel libnspr-devel libstdc++-devel perl pkg-config python-base python-modules
BuildRequires: gcc-c++ libnss-devel libsqlite3-devel libssl-devel sqlite3 zlib-devel

%{?!_without_check:%{?!_disable_check:BuildRequires: cppunit-devel}}

Requires: lib%name = %EVR

%description
OpenDNSSEC is providing a software implementation of a generic
cryptographic device with a PKCS#11 interface, the SoftHSM. SoftHSM is
designed to meet the requirements of OpenDNSSEC, but can also work
together with other cryptographic products because of the PKCS#11
interface.

%package -n lib%name
Summary: Library for Software Hardware Security Module
Group: System/Libraries

%description -n lib%name
This package contains development files for SoftHSM library.

%package devel
Summary: Development package of softhsm that includes the header files
Group: Development/C
Requires: lib%name = %EVR

%description devel
The devel package contains the libsofthsm include files.

%prep
%setup -n %name-%version
%patch1 -p1

%build
%autoreconf

# remove softhsm/ subdir auto-added to --libdir
sed -i "s:full_libdir/softhsm:full_libdir:g" configure
sed -i 's:^full_libdir=":#full_libdir=":g' configure.ac
sed -i "s:libdir)/@PACKAGE@:libdir):" Makefile.in

%configure \
	--localstatedir=/var \
	--libdir=%_libdir/pkcs11 \
	--with-openssl=%prefix \
	--enable-ecc \
	--disable-gost \
	--with-migrate \
	--enable-visibility \
	#

%make_build
# install our copy of pk11install taken from coolkey package
cp %SOURCE3 .
cc $(pkg-config --cflags nss) %optflags -c softhsm2-pk11install.c
cc softhsm2-pk11install.o $(pkg-config --libs nss) \
	-lpthread  -lsoftokn3 -ldl -lz %optflags \
	-o softhsm2-pk11install

%check
make check

%install
%makeinstall_std
install -D %SOURCE2 %buildroot/%_datadir/p11-kit/modules/softhsm.module

rm %buildroot/%_sysconfdir/softhsm2.conf.sample
rm -f %buildroot/%_libdir/pkcs11/*a
mkdir -p %buildroot%_includedir/softhsm
cp src/lib/*.h %buildroot%_includedir/softhsm
mkdir -p %buildroot/%_sharedstatedir/softhsm/tokens
install -m0755 -D softhsm2-pk11install %buildroot/%_bindir/softhsm2-pk11install

# leave a softlink where softhsm-1 installed its library. Programs like
# opendnssec have that filename in their configuration file.
mkdir -p %buildroot/%_libdir/softhsm/
ln -s ../pkcs11/libsofthsm2.so %buildroot/%_libdir/softhsm/libsofthsm.so
# rhbz#1272423 NSS needs it to be in the search path too
ln -s pkcs11/libsofthsm2.so %buildroot/%_libdir

%pre
getent group ods >/dev/null || groupadd -r ods
getent passwd ods >/dev/null || \
    useradd -r -g ods -d %_sharedstatedir/softhsm -s /sbin/nologin \
    -c "softhsm private keys owner" ods
exit 0

%post
isThere=`modutil -rawlist -dbdir %nssdb | grep %softhsm_module || echo NO`
if [ "$isThere" = "NO" ]; then
      softhsm2-pk11install -p %nssdb 'name=%softhsm_module library=libsofthsm2.so'
fi
if [ $1 -eq 0 ]; then
   modutil -delete %softhsm_module -dbdir %nssdb -force || :
fi

%files
%_bindir/*
%dir %_libdir/softhsm
%_libdir/softhsm/libsofthsm.so
%_libdir/pkcs11/libsofthsm2.so
%_datadir/p11-kit/modules/softhsm.module
%attr(0770,ods,ods) %dir %_sharedstatedir/softhsm
%attr(0770,ods,ods) %dir %_sharedstatedir/softhsm/tokens
%doc LICENSE README.md NEWS
%_man1dir/*

%files -n lib%name
%_libdir/libsofthsm2.so
%config(noreplace) %_sysconfdir/softhsm2.conf
%_man5dir/softhsm2.conf.5*

%files devel
%_includedir/softhsm

%changelog
* Thu Nov 03 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.1.0-alt2
- Fixed tokendir in softhsm2.conf.
- Moved softhsm2.conf.5 manpage to lib%name subpackage.

* Wed Nov 02 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.1.0-alt1
- Updated to 2.1.0.

* Fri Oct 30 2015 Michael Shigorin <mike@altlinux.org> 2.0.0-alt0.rc1.1
- built for ALT Linux (based on rosa/fedora package)
- fixed broken as-needed linking of softhsm2-pk11install.c,
  see also https://bugzilla.mozilla.org/124318
