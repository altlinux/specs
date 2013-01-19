Summary: Regulatory compliance agent for 802.11 wireless networking
Name: crda
Version: 1.1.2
Release: alt1.2013.01.11
License: ISC
Group: Networking/Other
Source: %name-%version.tar
Source1: wireless-regdb.tar
Source2: setregdomain
Source3: setregdomain.1
# Add udev rule to call setregdomain on wireless device add
Patch0: regulatory-rules-setregdomain.patch
Patch1: %name-%version-alt.patch
Url: http://www.linuxwireless.org/en/developers/Regulatory/CRDA
Packager: Evgenii Terechkov <evg@altlinux.org>

BuildRequires: libgcrypt-devel python-module-m2crypto libssl-devel openssl
BuildRequires: kernel-headers >= 2.6.27
BuildRequires: libnl-devel >= 1.1

# Requires: udev, iw

%description
CRDA acts as the udev helper for communication between the kernel
and userspace for regulatory compliance. It relies on nl80211
for communication. CRDA is intended to be run only through udev
communication from the kernel.

For more information see:
http://wireless.kernel.org/en/developers/Regulatory/

%prep
%setup -c
%setup -T -D -a 1
%patch0 -p1 -b .setregdomain

%build
# Use our own signing key to generate regulatory.bin
cd wireless-regdb
make %{?_smp_mflags} CFLAGS="%optflags" maintainer-clean
make %{?_smp_mflags} CFLAGS="%optflags" REGDB_PRIVKEY=key.priv.pem REGDB_PUBKEY=key.pub.pem
# Build CRDA using the new key and regulatory.bin from above
cd ../crda-%version
cp ../wireless-regdb/key.pub.pem pubkeys
make %{?_smp_mflags} CFLAGS="%optflags" REG_BIN=../wireless-regdb/regulatory.bin

%install
cd crda-%version
cp README README.crda
cp LICENSE LICENSE.crda
make install DESTDIR=%buildroot PREFIX='' MANDIR=%_mandir
cd ../wireless-regdb
cp README README.wireless-regdb
cp LICENSE LICENSE.wireless-regdb
make install DESTDIR=%buildroot PREFIX='' MANDIR=%_mandir
install -D -pm 0755 %SOURCE2 %buildroot/sbin
install -D -pm 0644 %SOURCE3 %buildroot%_man1dir/setregdomain.1

%files
/sbin/%name
/sbin/regdbdump
/sbin/setregdomain
/lib/udev/rules.d/85-regulatory.rules
# location of database is hardcoded to /lib/%name
/lib/%name
%_man1dir/setregdomain.1*
%_man5dir/regulatory.bin.5*
%_man8dir/crda.8*
%_man8dir/regdbdump.8*
%doc %name-%version/LICENSE.crda %name-%version/README.crda
%doc wireless-regdb/README.wireless-regdb wireless-regdb/LICENSE.wireless-regdb

%changelog
* Fri Jan 18 2013 Terechkov Evgenii <evg@altlinux.org> 1.1.2-alt1.2013.01.11
- wireless-regdb tag master-2013-01-11

* Tue Sep 11 2012 Terechkov Evgenii <evg@altlinux.org> 1.1.2-alt1.2012.09.10
- Initial build for ALT Linux Sisyphus
