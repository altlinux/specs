Name: foomatic-filters
Version: 4.0.17
Release: alt1

Summary: Foomatic filters needed to run print queues with Foomatic PPDs
License: GPL
Group: Publishing

Url: http://www.linuxprinting.org
Source: %url/download/foomatic/%name-%version.tar

BuildPreReq: libgs-devel

BuildRequires: cups enscript mpage libdbus-devel

Obsoletes: beh = 0.0
Provides: beh = %version-%release

%description
This package contains the filters needed to run print queues based on
Foomatic PPD files.

%prep
%setup -n %name-%version

%build
%configure
%make

%install
make \
    DESTDIR=%buildroot \
    PREFIX=%_prefix \
    install

%files
%doc README USAGE ChangeLog
%_bindir/*
%_prefix/lib/cups/filter/*
%_prefix/lib/cups/backend/*
%_prefix/lib/ppr/interfaces/*
%_prefix/lib/ppr/lib/foomatic-rip
%_man1dir/*
%dir %_sysconfdir/foomatic
%dir %_sysconfdir/foomatic/direct
%config(noreplace) %_sysconfdir/foomatic/filter.conf

%changelog
* Tue Jul 10 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.17-alt1
- 4.0.17

* Wed Apr 04 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.15-alt1
- 4.0.15

* Thu Jan 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.9-alt1
- 4.0.9

* Fri Dec 17 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Tue Oct 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Thu Oct 01 2009 Stanislav Ievlev <inger@altlinux.org> 4.0.3-alt1
- 4.0.3

* Tue Jun 09 2009 Michael Shigorin <mike@altlinux.org> 3.0.2.20081203-alt7.2
- NMU: spec cleanup

* Tue Jun 09 2009 Michael Shigorin <mike@altlinux.org> 3.0.2.20081203-alt7.1
- NMU: added Provides:/Obsoletes: beh (closes: #12941)

* Wed Dec 03 2008 Igor Vlasenko <viy@altlinux.ru> 3.0.2.20081203-alt7
- 20081203

* Thu Jun 05 2008 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt6
- 20080605

* Thu Sep 06 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt5
- 20070820

* Fri May 26 2006 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt4
- latest snapshot, noarch again

* Thu Apr 06 2006 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt3.20060109
- arch now

* Mon Apr 03 2006 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt2.20060109
- new snapshot

* Thu May 26 2005 Dmitry V. Levin <ldv@altlinux.org> 3.0.2-alt2.20050128
- Enhanced multilib support patch (mouse, closes #6734).

* Thu Apr 14 2005 Stanislav Ievlev <inger@altlinux.org> 3.0.2-alt1.20050128
- 3.0.2

* Tue Sep 21 2004 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt1.20040828
- latest snapshot

* Fri Sep 03 2004 Dmitry V. Levin <ldv@altlinux.org> 3.0.1-alt0.20040428.1
- Applied patch from upstream, to fix CAN-2004-0801.

* Wed May 05 2004 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt0.20040428
- latest snapshot

* Wed Feb 11 2004 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt0.20040128
- new snapshot

* Thu Dec 25 2003 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt0.20031219
- 3.0.1

* Tue Apr 29 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt3.20030310
- added symlink from usr/lib/cups/filter/cupsomatic to /usr/bin/foomatic-rip
  to backward compatibility

* Mon Mar 31 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt2.20030310
- latest snapshot

* Wed Feb 26 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt1.20030213
- Initial release

