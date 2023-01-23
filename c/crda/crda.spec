%define crda_lib /lib/crda
%define sbindir /sbin
%define _db wireless-regdb
%define _db_date 2022.08.12

Summary: Regulatory compliance agent for 802.11 wireless networking
Name: crda
Version: 4.15
Release: alt1
License: copyleft-next-0.3.0
Group: Networking/Other

Url: http://www.linuxwireless.org/en/developers/Regulatory/CRDA

Requires: firmware-%_db >= %EVR

Source: %name-%version.tar
Source1: %_db.tar
Source2: setregdomain
Source3: setregdomain.1

# Add udev rule to call setregdomain on wireless device add
Patch: crda-3.18-regulatory-rules-setregdomain.patch
# Do not call ldconfig in crda Makefile
Patch1: crda-remove-ldconfig.patch
Patch2: crda-ldflags.patch
Patch3: %_db-fw-dependency.patch
Patch4: %_db-pubcert-conf.patch
# https://gitweb.gentoo.org/repo/gentoo.git/plain/net-wireless/crda/files/crda-4.14-python-3.patch
Patch5: crda-4.14-python-3.patch

BuildRequires: libgcrypt-devel openssl chrpath
BuildRequires: rpm-build-python3
BuildRequires: python3-module-future python3-module-attrs python3-module-m2crypto

BuildRequires: kernel-headers >= 2.6.27
BuildRequires: libnl-devel >= 1.1

%description
CRDA is no longer needed as of kernel v4.15 since commit 007f6c5e6eb45
("cfg80211: support loading regulatory database as firmware file") added
support to use the kernel's firmware request API which looks for the
firmware on /lib/firmware. Because of this CRDA is legacy software for
older kernels. It will continue to be maintained.

CRDA acts as the udev helper for communication between the kernel
and userspace for regulatory compliance. It relies on nl80211
for communication. CRDA is intended to be run only through udev
communication from the kernel.

%package devel
Summary: Header files for use with libreg
Group: Development/Tools
BuildArch: noarch

%description devel
Header files to make use of libreg for accessing regulatory info.

%package -n firmware-%_db
Summary: Central Regulatory Database
Group: System/Kernel and hardware
BuildArch: noarch

%description -n firmware-%_db
This repository contains the regulatory database file for use with Central
Regulatory Database Agent daemon (CRDA).

%prep
%setup -c
%setup -T -D -a 1

# Set correct python3 executable in shebang
subst 's|#!.*python$|#!%__python3|' $(grep -Rl '#!.*python$' *)

cd %name-%version
%patch -p1 -b .setregdomain
%patch1 -p2 -b .ldconfig-remove
%patch2 -p2 -b .ldflags
%patch5 -p1
cd ../%_db
%patch3 -p2 -b .fwsign
%patch4 -p2 -b .pubcert

%build
%add_optflags %optflags_shared
export CFLAGS="%optflags -Wno-error=unused-const-variable"
cd %name-%version
%make SBINDIR=%sbindir/ LIBDIR=%crda_lib \
	REG_BIN=../%_db/regulatory.bin V=1

%install
cd crda-%version
%makeinstall_std MANDIR=%_mandir SBINDIR=%sbindir/ LIBDIR=/%_lib

cd ../%_db
%makeinstall_std PREFIX='' MANDIR=%_mandir
install -D -pm 0755 %SOURCE2 %buildroot/sbin
install -D -pm 0644 %SOURCE3 %buildroot%_man1dir/setregdomain.1
install -d %buildroot%_sysconfdir/%_db/pubkeys

rm %buildroot%_man5dir/regulatory.db.5* ||:
rm -f %buildroot/lib/%name/pubkeys/linville.key.pub.pem
ln -s regulatory.bin.5 %buildroot%_man5dir/regulatory.db.5

%files
%doc %name-%version/LICENSE %name-%version/README

/%_lib/libreg.so
# location of database is hardcoded to /lib/%%name
%crda_lib
# distribution custom keys
%_sysconfdir/%_db
%sbindir/%name
%sbindir/regdbdump
%sbindir/setregdomain
%_udevrulesdir/85-regulatory.rules

%_man1dir/setregdomain.1*
%_man5dir/regulatory.*.5*
%_man8dir/crda.8*
%_man8dir/regdbdump.8*

%files -n firmware-%_db
%doc %_db/README %_db/LICENSE
/lib/firmware/*.db*

%files devel
%_includedir/reglib

%changelog
* Mon Jan 23 2023 L.A. Kostis <lakostis@altlinux.ru> 4.15-alt1
- regdb: updated to 20220812.
- crda: updated to 4.15.
- added crda deprecation notice.

* Thu Aug 05 2021 Grigory Ustinov <grenka@altlinux.org> 4.14-alt6
- Transfer on python3.

* Tue Jul 06 2021 Andrey Cherepanov <cas@altlinux.org> 4.14-alt5.1
- FTBFS: use %%_python in Python shebangs.

* Sun Jun 06 2021 L.A. Kostis <lakostis@altlinux.ru> 4.14-alt5
- regdb updated to 20210421

* Mon Jul 27 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.14-alt4
- regdb updated to 20200429

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 4.14-alt3.2018.05.31.qa1
- NMU: applied repocop patch

* Sat Jun 30 2018 L.A. Kostis <lakostis@altlinux.ru> 4.14-alt3.2018.05.31
- fix sbin dir.

* Wed Jun 27 2018 L.A. Kostis <lakostis@altlinux.ru> 4.14-alt2.2018.05.31
- wireless-regdb:
  + split to separate package;
  + make noarch.
- crda:
  + relocate libreg.so to /%%_lib and get rid of RPATH;
  + fix libreg.so unresolved symbols.
- more .spec cleanup.

* Wed Jun 27 2018 L.A. Kostis <lakostis@altlinux.ru> 4.14-alt1.2018.05.31
- crda: update to 4.14.
- crda: fix cert verify (use rpath after build).
- wireless-regdb tag master-2018-05-31.
- .spec cleanup.

* Sat Mar 25 2017 Hihin Ruslan <ruslandh@altlinux.ru> 3.18-alt1.2017.03.07
- 3.18

* Sat Mar 25 2017 Hihin Ruslan <ruslandh@altlinux.ru> 1.1.3-alt1.2017.03.07
- wireless-regdb tag master-2017.03.07

* Sat Jul 20 2013 Terechkov Evgenii <evg@altlinux.org> 1.1.3-alt1.2013.02.13
- 1.1.3
- Build with openssl (enable dynamic loading of trusted public keys from
  /etc/wireless-regdb/pubkeys)

* Sun Feb 17 2013 Terechkov Evgenii <evg@altlinux.org> 1.1.2-alt1.2013.02.13
- wireless-regdb tag master-2013-02-13
- Fix build with libnl3

* Fri Jan 18 2013 Terechkov Evgenii <evg@altlinux.org> 1.1.2-alt1.2013.01.11
- wireless-regdb tag master-2013-01-11

* Tue Sep 11 2012 Terechkov Evgenii <evg@altlinux.org> 1.1.2-alt1.2012.09.10
- Initial build for ALT Linux Sisyphus

