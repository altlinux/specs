Summary: Regulatory compliance agent for 802.11 wireless networking
Name: crda
Version: 3.18
Release: alt1.2017.03.07
License: ISC
Group: Networking/Other
Source: %name-%version.tar
Source1: wireless-regdb.tar
Source2: setregdomain
Source3: setregdomain.1

%define crda_lib /lib/crda
%define sbindir /sbin


# Add udev rule to call setregdomain on wireless device add
Patch: crda-3.18-regulatory-rules-setregdomain.patch
# Do not call ldconfig in crda Makefile
Patch1: crda-remove-ldconfig.patch

Url: http://www.linuxwireless.org/en/developers/Regulatory/CRDA

BuildRequires: libgcrypt-devel libnl-devel openssl python-module-m2crypto python3-module-yieldfrom python3-module-zope

BuildRequires: python-module-m2crypto libssl-devel openssl
BuildRequires: kernel-headers >= 2.6.27
BuildRequires: libnl-devel >= 1.1
BuildRequires: libgcrypt-devel

# Requires: udev, iw

%description
CRDA acts as the udev helper for communication between the kernel
and userspace for regulatory compliance. It relies on nl80211
for communication. CRDA is intended to be run only through udev
communication from the kernel.

For more information see:
http://wireless.kernel.org/en/developers/Regulatory/

%package devel
Summary: Header files for use with libreg
Group: Development/Tools


%description devel
Header files to make use of libreg for accessing regulatory info.

%prep
%setup -c
%setup -T -D -a 1

cd crda-%version
%patch -p1 -b .setregdomain

%patch1 -p1 -b .ldconfig-remove

%build
%add_optflags %optflags_shared
# export CFLAGS="%optflags"
export CFLAGS="%optflags -Wno-error=unused-const-variable"

# rpath="/$(printf %%s '%crda_lib' |tr '[:print:]' '_')"
rpath='%crda_lib'
export LDFLAGS="$LDFLAGS -Wl,-rpath,$rpath"


# Use our own signing key to generate regulatory.bin
cd wireless-regdb
%make_build maintainer-clean
%make_build REGDB_PRIVKEY=key.priv.pem REGDB_PUBKEY=key.pub.pem

# Build CRDA using the new key and regulatory.bin from above
cd ../crda-%version
cp ../wireless-regdb/key.pub.pem pubkeys

# make_build REG_BIN=../wireless-regdb/regulatory.bin V=1 USE_OPENSSL=1

%make_build SBINDIR=%sbindir/ LIBDIR=%crda_lib/ \
	REG_BIN=../wireless-regdb/regulatory.bin

%install
cd crda-%version

cp README README.crda
cp LICENSE LICENSE.crda

#makeinstall_std PREFIX='' MANDIR=%_mandir

%makeinstall_std MANDIR=%_mandir/ \
	SBINDIR=%sbindir/ LIBDIR=%crda_lib

cd ../wireless-regdb
cp README README.wireless-regdb
cp LICENSE LICENSE.wireless-regdb
%makeinstall_std PREFIX='' MANDIR=%_mandir
install -D -pm 0755 %SOURCE2 %buildroot/sbin
install -D -pm 0644 %SOURCE3 %buildroot%_man1dir/setregdomain.1

mkdir -p %buildroot%_sysconfdir/wireless-regdb/pubkeys

rm -f %buildroot/lib/%name/pubkeys/linville.key.pub.pem

%files
%doc %name-%version/LICENSE.crda %name-%version/README.crda
%doc wireless-regdb/README.wireless-regdb wireless-regdb/LICENSE.wireless-regdb

%crda_lib/libreg.so
%_sysconfdir/wireless-regdb/pubkeys
%sbindir/%name
%sbindir/regdbdump
%sbindir/setregdomain
/lib/udev/rules.d/85-regulatory.rules

# location of database is hardcoded to /lib/%name
/lib/%name
%_man1dir/setregdomain.1*
%_man5dir/regulatory.bin.5*
%_man8dir/crda.8*
%_man8dir/regdbdump.8*

%files devel
%_includedir/reglib/nl80211.h
%_includedir/reglib/regdb.h
%_includedir/reglib/reglib.h


%changelog
* Sat Mar 25 2017 Hihin Ruslan <ruslandh@altlinux.ru> 3.18-alt1.2017.03.07
- 3.18

* Sat Mar 25 2017 Hihin Ruslan <ruslandh@altlinux.ru> 1.1.3-alt1.2017.03.07
- wireless-regdb tag master-2017.03.07

* Sat Jul 20 2013 Terechkov Evgenii <evg@altlinux.org> 1.1.3-alt1.2013.02.13
- 1.1.3
- Build with openssl (enable dynamic loading of trusted public keys from /etc/wireless-regdb/pubkeys)

* Sun Feb 17 2013 Terechkov Evgenii <evg@altlinux.org> 1.1.2-alt1.2013.02.13
- wireless-regdb tag master-2013-02-13
- Fix build with libnl3

* Fri Jan 18 2013 Terechkov Evgenii <evg@altlinux.org> 1.1.2-alt1.2013.01.11
- wireless-regdb tag master-2013-01-11

* Tue Sep 11 2012 Terechkov Evgenii <evg@altlinux.org> 1.1.2-alt1.2012.09.10
- Initial build for ALT Linux Sisyphus

