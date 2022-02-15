%define user grmilter

Name: milter-greylist
Version: 4.6.4
Release: alt2
Group: System/Servers
License: BSD-3-Clause
Summary: GreyList milter for milter-capable MTA
Source0: ftp://ftp.espci.fr/pub/milter-greylist/%name-%version.tar
Source1: %name.init.alt
Patch0: %name.alt.patch
Url: http://hcpnet.free.fr/milter-greylist/

Packager: L.A. Kostis <lakostis@altlinux.org>

%def_enable postfix
%def_enable dnsrbl
%def_disable p0f
%def_with libspf2
%def_with libGeoIP2
%def_with libcurl

%if_enabled postfix
Requires: MTA
%else
Requires: sendmail >= 8.11
Requires: sendmail-cf >= 8.11
%endif
BuildRequires: sendmail-devel >= 8.11
BuildRequires: flex
BuildRequires: bison
BuildRequires: chrpath
# for DNSRBL support
BuildRequires: bind-devel
%{?_with_libspf2:BuildPreReq: libspf2-devel}
%{?_with_libcurl:BuildPreReq: libcurl-devel}
%{?_with_libGeoIP:BuildPreReq: libGeoIP-devel}

%description
milter-greylist is a stand-alone milter written in C that implements the
greylist filtering method, as proposed by Evan Harris.

Grey listing works by assuming that unlike legitimate MTA, spam engines will
not retry sending their junk mail on a temporary error. The filter will
always temporarily reject mail on a first attempt, and to accept it after
some time has elapsed.

If spammers ever try to resend rejected messages, we can assume they will
not stay idle between the two sends (if they do, the spam problem would just
be solved). Odds are good that the spammer will send a mail to an honey pot
address and get blacklisted in several real-time distributed black list
before the second attempt.

%prep
%setup
%patch0 -p1

%build
subst 's,_BSD_SOURCE,_DEFAULT_SOURCE,gi' configure.ac Makefile.in
%autoreconf
%configure \
	--with-user=%user \
	%{subst_enable postfix} \
	%{subst_enable dnsrbl} \
	%{subst_enable p0f} \
	--with-libbind \
	%{?_with_libspf2:--with-libspf2=%_libdir} \
	%{?_with_libcurl:--with-libcurl=%_libdir} \
	%{?_with_libGeoIP:--with-libGeoIP=%_libdir}

# SMP incompatible build?
%__make

%install
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_sysconfdir/{mail,sysconfig}
mkdir -p %buildroot%_localstatedir/milter-greylist

install -m 755 %SOURCE1 %buildroot%_initdir/milter-greylist
%if_disabled postfix
mkdir -p %buildroot%_datadir/sendmail-cf/feature
install -m 644 milter-greylist.m4 %buildroot%_datadir/sendmail-cf/feature/milter-greylist.m4
%endif
touch %buildroot%_localstatedir/milter-greylist/greylist.db
touch %buildroot%_sysconfdir/sysconfig/%name

make DESTDIR=%buildroot install
chrpath -d %buildroot%_sbindir/%name

%pre
/usr/sbin/useradd -r -d /etc/mail -s /sbin/nologin \
        -c "GreyList Milter" %user >/dev/null 2>&1 || :

%post
%post_service %name
%if_disabled postfix
/bin/grep -q -E '(FEATURE|INPUT_MAIL_FILTER).*milter-greylist' /etc/mail/sendmail.mc
if [ $? -ne 0 ]
then
	echo "You can enable milter-greylist in your sendmail, adding the line : "
	echo "FEATURE(\`milter-greylist')dnl"
	echo "to /etc/mail/sendmail.mc file"
fi
%endif

%preun
%preun_service %name
%if_disabled postfix
	/bin/grep -q -E '(FEATURE|INPUT_MAIL_FILTER).*milter-greylist' /etc/mail/sendmail.mc
	if [ $? -eq 0 ]
	then
		echo "You must remove the milter-greylist config"
		echo "from /etc/mail/sendmail.mc file"
	fi
%endif

%postun
if [ $1 -eq 0 ]; then
	rm -rf %_localstatedir/milter-greylist/
        grep -q "$%user:.*GreyList Milter:"
	if [ $? -eq 0 ]
        then
		/usr/sbin/userdel %user >/dev/null 2>&1 || :
		/usr/sbin/groupdel %user >/dev/null 2>&1 || :
	fi
else
	/sbin/service milter-greylist condrestart > /dev/null 2>&1 || :
fi

%files
%doc README ChangeLog
%config (noreplace) %_sysconfdir/mail/greylist.conf
%config (noreplace) %_sysconfdir/sysconfig/%name
%_initdir/%name
%_sbindir/%name
%_man5dir/*
%_man8dir/*
%if_disabled postfix
%_datadir/sendmail-cf/feature/milter-greylist.m4
%dir %attr(0710,%user,root) %_localstatedir/milter-greylist
%else
%dir %attr(0710,%user,postfix) %_localstatedir/milter-greylist
%endif
%attr(0600,%user,root) %ghost %_localstatedir/milter-greylist/greylist.db

%changelog
* Tue Feb 15 2022 L.A. Kostis <lakostis@altlinux.ru> 4.6.4-alt2
- init: fix socket permissions.
- alt.patch: use postfix group by default.

* Wed Mar 03 2021 L.A. Kostis <lakostis@altlinux.ru> 4.6.4-alt1
- Updated to 4.6.4.
- .spec: fix License field.

* Sun Sep 25 2016 L.A. Kostis <lakostis@altlinux.ru> 4.6.1-alt1
- Updated to 4.6.1.
- Build fixes:
  + removed obsoleted build flags.
  + added bind-devel (for DNSRBL support).
  + removed -postfix patch (fixed by upstream).

* Thu Jan 01 2015 L.A. Kostis <lakostis@altlinux.ru> 4.5.9-alt2
- .spec cleanup.

* Tue Dec 30 2014 L.A. Kostis <lakostis@altlinux.ru> 4.5.9-alt1
- Add conftest action to init.d script.

* Mon Dec 29 2014 L.A. Kostis <lakostis@altlinux.ru> 4.5.9-alt0.1
- Updated to 4.5.9.
- Build fixes:
  + update -alt patch.
  + compile fix for postfix build.

* Sun Dec 28 2014 L.A. Kostis <lakostis@altlinux.ru> 4.2.7-alt0.2
- build fixes:
  + init.d script typo fix.
  + correct socket default permission.
  + use group postfix for socket path in postfix build.
  + disable p0f.

* Sun Dec 28 2014 L.A. Kostis <lakostis@altlinux.ru> 4.2.7-alt0.1
- initial build for ALTLinux.
