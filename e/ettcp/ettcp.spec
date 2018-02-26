Name: ettcp
Version: 1.0
Release: alt5

Summary: A tool for testing TCP throughut between two nodes
License: Public Domain
Group: Networking/Other

URL: http://sourceforge.net/projects/ettcp/
Source0: %name-%version.tar.bz2
Patch1: ettcp-1.0-alt-path.patch
Packager: Michael Shigorin <mike@altlinux.org>

Conflicts: suck

Summary(ru_RU.KOI8-R): Средство тестирования производительности TCP между двумя хостами

%description
ettcp is an updated version of ttcp. It supports the suck and
blow xinetd severs.  suck and blow and the associated xinetd.d
files are included in the package.  ttcp is a tool for testing
the throughput of TCP connections.  Unlike other tools which
might be used for this purpose (such as FTP clients), ttcp does
not read or write data from or to a disk while operating, which
helps ensure more accurate results.

%description -l ru_RU.KOI8-R
ettcp - обновленная версия ttcp. Поддерживает службы suck и blow
через xinetd.  Является средтвом измерения пропускной способности
TCP-соединений. В отличие от других средств, которые могут
использоваться для подобных целей, например, FTP-клиентов, ttcp
не читает и не записывает данные на диск в процессе своей работы,
что позволяет получить более достоверные результаты.

%prep
%setup
%patch1 -p1

%build
%make_build

%install
mkdir -p %buildroot{%_man1dir,%_bindir,%_sysconfdir/xinetd.d}
%makeinstall \
	RPM_INSTALL_DIR=%buildroot%_bindir \
	RPM_MAN_DIR=%buildroot%_mandir \
	RPM_ETC_DIR=%buildroot%_sysconfdir

%files
%doc README TODO
%_bindir/*
%_mandir/man?/*
%_sysconfdir/xinetd.d/*

%changelog
* Sat Aug 01 2009 Michael Shigorin <mike@altlinux.org> 1.0-alt5
- added explicit Conflicts: suck (repocop)
- minor spec cleanup

* Sun Dec 17 2006 Michael Shigorin <mike@altlinux.org> 1.0-alt3
- fixing trivial bugs (accepted #4759, fixed #5103) since package
  is still in Sisyphus but if anyone's interested, please take over
- minor spec cleanup

* Tue Oct 11 2005 Denis Ovsienko <pilot@altlinux.ru> 1.0-alt2
- NMU: fixing #4759

* Mon Aug 25 2003 Egor S. Orlov <oes@altlinux.ru> 1.0-alt1.2
- Added russian translation for description and summary 

* Mon Jul 14 2003 Egor S. Orlov <oes@altlinux.ru> 1.0-alt1.1
- Added URL 

* Tue Jul 08 2003 Egor S. Orlov <oes@altlinux.ru> 1.0-alt1
- Build for sisyphus
- Cleanup spec acording the policy

* Sun Jun 29 2003 Egor S. Orlov <oes@altlinux.ru> 1.0-alt0.1
- Initial build for ALT

