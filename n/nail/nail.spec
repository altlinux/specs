Name: nail
Version: 10.7
Release: alt2

Summary: The /bin/nail program for send and receive MIME conformant mail
License: BSD
Group: Networking/Mail
URL: http://nail.sourceforge.net

Source: http://aleron.dl.sourceforge.net/sourceforge/nail/nail-10.7.tar.bz2

%description
Nail is an intelligent mail processing system, which has a command syntax
reminiscent of ed(1) with lines replaced by messages.  It is based on Berkeley Mail 8.1,
is intended to provide the functionality  of the POSIX.2 mailx command,
and offers extensions for MIME messages, POP3 and SMTP.

%prep
%setup

%build
%add_optflags -fcommon
%configure --with-csh=/bin/csh \
	    --with-vi="/bin/vi -c 'set ft=mail tw=74' '+/^$'" \
	    --with-sendmail=/usr/sbin/sendmail
%make_build

%install
%make_install install DESTDIR=$RPM_BUILD_ROOT

%files
%_bindir/*
%config(noreplace) %_sysconfdir/nail.rc
%_man1dir/*
%doc COPYING README AUTHORS INSTALL ChangeLog

%changelog
* Tue Mar 30 2021 Grigory Ustinov <grenka@altlinux.org> 10.7-alt2
- Fixed FTBFS with -fcommon.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 10.7-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Apr 20 2004 Anton Farygin <rider@altlinux.ru> 10.7-alt1
- new version

* Wed Aug 20 2003 Rider <rider@altlinux.ru> 10.5-alt1
- first build for ALT Linux
