Name: sleezeball
Version: 0.6
Release: alt8

Summary: A redirector for Squid2 that zapps banners
License: GPL
Group: System/Servers
URL: http://fredrik.rambris.com/%name/

Source0: %url/%name-%version.tar.bz2
Source1: %name.logrotate
Source2: %name.conf
Patch: %name-0.6-make.patch

Requires: squid-server

%description
SlezeBall is a redirector to be used with the Squid proxy. It tries to guess
what is a banner and then tells Squid to load a local image instead. This
has the nice effect of saving you from downloading and seeing alot of ugly
banners (linux.com has such goodlooking banners that I can't bring me to
filter them out).

%prep
%setup
%patch -p1

%build
%make_build

%install
%make_install install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_sysconfdir/squid
mkdir -p $RPM_BUILD_ROOT%_datadir/squid/icons/
mv $RPM_BUILD_ROOT%_libdir/squid/icons/banner.gif $RPM_BUILD_ROOT%_datadir/squid/icons/banner.gif
install -p -m644 %name.{conf,definitions} $RPM_BUILD_ROOT%_sysconfdir/squid
install -d -m755 $RPM_BUILD_ROOT%_sysconfdir/logrotate.d
install -m644 %SOURCE1 \
        $RPM_BUILD_ROOT%_sysconfdir/logrotate.d/sleezeball
install -m644 %SOURCE2 \
        $RPM_BUILD_ROOT%_sysconfdir/squid


%post
if ! grep -qs '^internal-banner' %_sysconfdir/squid/mime.conf; then
	echo 'internal-banner	-	banner.gif	-	image' >>%_sysconfdir/squid/mime.conf
fi

%files
%config(noreplace) %_sysconfdir/squid/%name.*
%config(noreplace) %_sysconfdir/logrotate.d/sleezeball
%_libdir/squid/%name
%_datadir/squid/icons/banner.gif
%_sbindir/reloadszb
%doc README ChangeLog

%changelog
* Fri Jul 01 2005 Nazar Yurpeak <phoenix@altlinux.ru> 0.6-alt8
- updated Requires

* Thu Jun 21 2005 Nazar Yurpeak <phoenix@altlinux.ru> 0.6-alt7
- Fixed bug #6267

* Thu May 27 2004 Nazar Yurpeak <phoenix@altlinux.ru> 0.6-alt6
- bug #4088 fix

* Fri Apr 25 2003 Nazar Yurpeak <phoenix@altlinux.ru> 0.6-alt5
- bug #0002541 fix

* Mon Mar 03 2003 Nazar Yurpeak <phoenix@altlinux.ru> 0.6-alt4
- fixed logrotate script

* Thu Feb 13 2003 Nazar Yurpeak <phoenix@altlinux.ru> 0.6-alt3
- added logrotate script

* Sat Nov 16 2002 Nazar Yurpeak <phoenix@altlinux.ru> 0.6-alt2
- Rebuilt in new environment
- change URL

* Tue Jun 19 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.6-alt1
- First build for Sisyphus
