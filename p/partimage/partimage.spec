%define partimaged_user _partimaged
%define partimaged_group _partimaged

Summary: Partition Image
Name: partimage
Version: 0.6.9
Release: alt1.1
License: GPL
Group: System/Configuration/Hardware
URL:     http://www.partimage.org/

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: %name-%version.tar.bz2
Patch1: partimage-0.6.7-autoconf.patch
Patch2:  partimage-0.6.7-gcc43.patch
Patch3:  partimage-0.6.7-gcc44.patch

Source1: partimaged.pam
Source2: partimaged.init

Obsoletes: partimage = 0.6.5_beta3

Requires: libnewt, dmraid

# Automatically added by buildreq on Tue Feb 19 2008
BuildRequires: bzlib-devel cvs gcc-c++ libnewt-devel libpam-devel libssl-devel openssl zlib-devel

%description
Partition Image is a Linux/UNIX partition imaging utility: it saves all used
blocks in a partition to an image file. 

This allows you to back up a full Linux/Windows system with a single
operation. When problems such as viruses, crashes, or other errors occur, you
just have to restore, and after several minutes your system can be restored
(boot record and all your files) and fully working.

%package server
Summary: partimage server
Group: System/Servers

Obsoletes: partimaged, partimage-partimaged

%description server
Server to store images from partimage accross the network

%prep
%setup -q
#patch0 -p1
#patch1
#patch2 -p1 -b .gcc43
#patch3 -p1 -b .gcc44


sed -i '/^#define PARTIMAGED_USER/ s,"partimag","%{partimaged_user}",' -i src/shared/pathnames.h.in

perl -pi.orig -e 's|^[[:space:]]*chown partimag[\.:]root.*$|\\|' Makefile.am
### FIXME: Fix mkinstalldirs during 'make install' in po/
perl -pi.orig -e 's|^(mkinstalldirs) = .+$|$1 = %__mkdir_p|' po/Makefile.in.in

autoreconf -fisv

%build
%configure --with-log-dir=/var/log --enable-ssl --enable-pam --disable-static 
%make_build

%install
%makeinstall
install -d %buildroot%_spooldir/partimaged 
install -D -m 644 %SOURCE1  %buildroot/%_sysconfdir/pam.d/partimaged
install -D -m 755 %SOURCE2  %buildroot/%_initdir/partimaged
%find_lang %name

%pre server
%_sbindir/groupadd -r -f %partimaged_group 2>/dev/null ||:
%_sbindir/useradd -g %partimaged_group -c 'Partimage server' -d %_spooldir/partimaged -s '' \
        -r %partimaged_user 2>/dev/null || :

%post server
%post_service partimaged

%preun server
%preun_service partimaged

%files -f %name.lang
%doc AUTHORS BUGS  ChangeLog COPYING README README.partimaged
%_sbindir/partimage

%files server
%doc AUTHORS BUGS  ChangeLog COPYING README README.partimaged
%_sbindir/partimaged
%_initdir/partimaged
%dir %_sysconfdir/partimaged
%config(noreplace) %_sysconfdir/partimaged/*
%config(noreplace) %_sysconfdir/pam.d/partimaged
%attr(700,%partimaged_user,%partimaged_group)%_spooldir/partimaged

%changelog
* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.6.9-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Mon Aug 23 2010 Ilya Mashkin <oddity@altlinux.ru> 0.6.9-alt1
- 0.6.9

* Sun Dec 20 2009 Ilya Mashkin <oddity@altlinux.ru> 0.6.8-alt1
- 0.6.8

* Tue Mar 10 2009 Ilya Mashkin <oddity@altlinux.ru> 0.6.7-alt7
- fix build with gcc4.3
- add url

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.7-alt6.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Fri Feb 22 2008 Nick S. Grechukh <gns@altlinux.org> 0.6.7-alt6
- initscript. partimaged package renamed to partimage-server

* Fri Feb 22 2008 Nick S. Grechukh <gns@altlinux.org> 0.6.7-alt4
- pam.d config created

* Tue Feb 19 2008 Nick S. Grechukh <gns@altlinux.org> 0.6.7-alt2
- reorganization. separate package partimaged.

* Tue Feb 19 2008 Nick S. Grechukh <gns@altlinux.org> 0.6.7-alt1
- ver 0.6.7

* Fri Aug 24 2007 Mikhail Pokidko <pma@altlinux.org> 0.6.6-alt1
- Ver 0.6.6

* Thu Feb 01 2007 Mikhail Pokidko <pma@altlinux.ru> 0.6.5_rel-alt1
- Final partimage release. Fixed #10683.
