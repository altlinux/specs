%def_disable backportM4x_mode

Packager: Stanislav Ievlev <inger@altlinux.org>

Name: foomatic-db-engine
Version: 4.0.8
Release: alt1

Provides: foomatic-addon = %version
Obsoletes: foomatic-addon

PreReq: alternatives >= 0.3

Summary: Foomatic database access, printer admin, and printing utils
License: GPL
Group: Publishing

Url: http://www.linuxprinting.org

Source: http://www.linuxprinting.org/download/foomatic/%name-%version.tar
Source1: foomatic-db-engine.alternatives

Patch1: foomatic-db-engine-3.0.2-suse-A4.patch

%define _compress_method gzip

BuildPreReq: cups >= 1.2.1


# Automatically added by buildreq on Fri May 26 2006
BuildRequires: cups curl foomatic-filters ghostscript-classic libxml2-devel netcat perl-devel samba-client wget zlib-devel perl-Encode

%description
This package contains the tools for accessing the Foomatic database,
for printer administration, and for printing.

%prep
%setup -q -n %name-%version
%patch1 -p1

%build
%configure
%make

%install
make \
    DESTDIR=%buildroot \
    PREFIX=%_prefix \
    INSTALLSITELIB=%perl_vendor_privlib \
    INSTALLSITEARCH=%perl_vendor_archlib \
    install

#cd lib
#_perl_vendor_install

install -d $RPM_BUILD_ROOT/var/cache/foomatic/pcache
install -d $RPM_BUILD_ROOT/var/cache/foomatic/compiled

( cd $RPM_BUILD_ROOT%_bindir
  ln -s foomatic-printjob lpr-foomatic
  ln -s foomatic-printjob lpq-foomatic
  ln -s foomatic-printjob lprm-foomatic
)
( cd $RPM_BUILD_ROOT%_sbindir
  ln -s %_bindir/foomatic-printjob lpc-foomatic
)

(cd $RPM_BUILD_ROOT%_man1dir
 ln -s foomatic-printjob.1.gz  lpr-foomatic.1.gz
 ln -s foomatic-printjob.1.gz  lpq-foomatic.1.gz
 ln -s foomatic-printjob.1.gz  lprm-foomatic.1.gz
)

( cd $RPM_BUILD_ROOT%_man8dir
  ln -s ../man1/foomatic-printjob.1.gz lpc-foomatic.8.gz
)

%__install -Dpm644 %SOURCE1 %buildroot%_altdir/%name

%if_enabled backportM4x_mode
%post
%register_alternatives %name -- lpr lpr.1.gz lpq lpq.1.gz lprm lprm.1.gz lpc lpc.1.gz

%preun
%unregister_alternatives %name
%endif

%files
%doc README USAGE ChangeLog
%_altdir/%name
%_cachedir/*
%_datadir/foomatic/templates
%_man1dir/*
%_man8dir/*
%_bindir/*
%_sbindir/*
%_prefix/lib/cups/driver/foomatic
%perl_vendor_privlib/Foomatic*

%changelog
* Thu Jan 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.8-alt1
- 4.0.8

* Mon Dec 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Tue Oct 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Wed Sep 30 2009 Stanislav Ievlev <inger@altlinux.org> 4.0.3-alt1
- 4.0.3

* Thu Dec 04 2008 Igor Vlasenko <viy@altlinux.ru> 3.0.2.20081204-alt5
- 20081204
- added date to version
- alternatives 0.4 support

* Thu Nov 08 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt4
- add suse patch: force A4 format

* Thu Sep 06 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt3
- 20070820

* Fri May 26 2006 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt2
- new snapshot

* Mon Apr 03 2006 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt1.20060228
- new snapshot, fixed linking

* Thu Apr 14 2005 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt1.20050224
- 3.0.2

* Tue Sep 21 2004 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt3.20040828
- latest snapshot

* Wed May 05 2004 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt2.20040428
- latest snapshot

* Mon Mar 15 2004 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt2.20040128
- really ignore -t option (was problems with printer setup in kde)

* Wed Feb 11 2004 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt1.20040128
- new foomatic snapshot

* Fri Dec 26 2003 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt1.20031219
- remove use strict and '-w' foomatic not ready for it yet.

* Thu Dec 25 2003 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt0.20031219
- 3.0.1

* Mon Sep 29 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt6.20030310
- fix building in hasher (Thanks to Alexey Tourbin)

* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt5.20030310
- new alternatives config format

* Mon Mar 31 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt4.20030310
- latest snapshot

* Fri Mar 14 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt3.20030213
- PreReq fixes

* Thu Mar 13 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt2.20030213
- move to new alternatives scheme

* Wed Feb 26 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt1.20030213
- Initial release
