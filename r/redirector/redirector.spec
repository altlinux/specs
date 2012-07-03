%define redirector_cfgdir %_sysconfdir/squid/redirector

Name: redirector
Version: 3.2.8
Release: alt1

Summary: rejik3 is a redirector for squid
License: GPL
Group: Networking/Other
Url: http://rejik.ru

Source0: %name-%version.tar
Source1: redirector.banlists-2.x.x.tgz
Source2: www.tar
Source3: dbl.tar
Source4: redirector.squid-like-www-ru.tgz
Source5: redirector.squid-like-www-en.tgz
Source6: redirector.README.ALT.UTF8
Source7: redirector.dbl.conf

Provides: redirector, rejik, rejik3

BuildPreReq: perl-XML-Parser perl-Text-Iconv
BuildRequires: libpcre-devel

%package dbl
Summary: %name Distributed Banner Lists scripts
Group: Networking/Other
Requires: wget

%description
blocking of advertising, porno-sites, mp3 and so on

%description dbl
%name Distributed Banner Lists scripts

%prep
%setup -q
tar xf %SOURCE2 && mv www ban
tar xf %SOURCE3
pushd dbl
popd
tar zxf %SOURCE4 && mv squid-like-www-ru squid-like-ban-ru
tar zxf %SOURCE5 && mv squid-like-www-en squid-like-ban-en
subst 's|\(chown\)|#\1|g; s|^\(INSTALL_PATH=\).*|\1%_sbindir|' Makefile
subst 's|\(DEFAULT_CONFIG\).*|\1 "%redirector_cfgdir/redirector.conf"|' vars.h

%build
%make_build

%install
mkdir -p %buildroot%redirector_cfgdir
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_logdir/%name
%makeinstall INSTALL_PATH=%buildroot%_sbindir
mv %buildroot%_sbindir/redirector.conf.dist %buildroot%redirector_cfgdir/redirector.conf
pushd %buildroot%_localstatedir/%name
	tar xzvf %SOURCE1
popd
subst 's|/usr/local/rejik3/\(banlists/\)|%_localstatedir/%name/\1|g' %buildroot%redirector_cfgdir/redirector.conf
subst 's|\(error_log\).*|\1 %_logdir/%name/%name.err|g' %buildroot%redirector_cfgdir/redirector.conf
subst 's|\(change_log\).*|\1 %_logdir/%name/%name.log|g' %buildroot%redirector_cfgdir/redirector.conf
subst 's|\(make-cache\).*|\1 %_sbindir/make-cache|g' %buildroot%redirector_cfgdir/redirector.conf

rm -rf %buildroot%_sbindir/tools

# dbl-config
install -pD -m0644 %SOURCE7 %buildroot%redirector_cfgdir/dbl/dbl.conf

# dbl-bin
install -pD -m0755 dbl/Update %buildroot%_sbindir/dbl_update
install -pD -m0755 dbl/Update.Fast %buildroot%_sbindir/dbl_update_fast
install -pD -m0755 dbl/dbl_expand %buildroot%_sbindir/dbl_expand
install -pD -m0755 dbl/dbl_stat %buildroot%_sbindir/dbl_stat

cat >> %buildroot%_sbindir/dbl_full << EOF
#!/bin/sh

dbl_update
dbl_expand %_localstatedir/%name/dbl/list.dbl
service squid reload
EOF

cat >> %buildroot%_sbindir/dbl_fast << EOF
#!/bin/sh

dbl_update_fast
dbl_expand %_localstatedir/%name/dbl/fast.dbl
service squid reload
EOF

chmod 0755 %buildroot%_sbindir/dbl_{full,fast}
mkdir -p %buildroot%_localstatedir/%name/dbl/{NEW,lists}

install -m0644 %SOURCE6 README.ALT.KOI8-R

# set url_rewrite_program in squid.conf when installing
%post
if [ $1 -eq 1 ]; then
	subst 's,^# url_rewrite_program /path/to/redirector,url_rewrite_program %_sbindir/%name %redirector_cfgdir/%name.conf,' %_sysconfdir/squid/squid.conf
	%_initdir/squid reload >/dev/null 2>&1 ||:
fi

# comment out url_rewrite_program in squid.conf when deleting package
%preun
if [ $1 -eq 0 ]; then
	subst 's,^url_rewrite_program %_sbindir/%name %redirector_cfgdir/%name.conf,# url_rewrite_program /path/to/redirector,' %_sysconfdir/squid/squid.conf
	rm -rf %_localstatedir/%name/banlists
	%_initdir/squid reload >/dev/null 2>&1 ||:
fi

%files
%doc AUTHORS INSTALL README* ban squid-like-ban-*
%dir %redirector_cfgdir
%dir %_localstatedir/%name
%dir %_localstatedir/%name/banlists
%dir %attr(1775,root,squid) %_localstatedir/%name/banlists/banners
%dir %attr(1775,root,squid) %_localstatedir/%name/banlists/js
%dir %attr(1775,root,squid) %_localstatedir/%name/banlists/mp3
%dir %attr(1775,root,squid) %_localstatedir/%name/banlists/porno
%dir %attr(1770,root,squid) %_logdir/%name
%config(noreplace) %redirector_cfgdir/%name.conf
%attr(0644,root,squid) %_localstatedir/%name/banlists/banners/*
%attr(0644,root,squid) %_localstatedir/%name/banlists/js/*
%attr(0644,root,squid) %_localstatedir/%name/banlists/mp3/*
%attr(0644,root,squid) %_localstatedir/%name/banlists/porno/*
%_sbindir/%name
%_sbindir/make-cache

%files dbl
%_sbindir/dbl*
%attr(0640,root,squid) %config(noreplace) %redirector_cfgdir/dbl/dbl.conf
%_localstatedir/%name/dbl/NEW
%_localstatedir/%name/dbl/lists
%dir %_localstatedir/%name/dbl

%changelog
* Wed Jan 26 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 3.2.8-alt1
- 3.2.8

* Tue May 26 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 3.2.2-alt1
- 3.2.2 (Closes: #20176)
- Remove dependency on main package from -dbl subpackage (Closes: #20156)

* Mon Aug 25 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.1-alt7
- Fix permissions of /var/log/redirector
- Add dependency on wget in dbl subpackage
- Update README.ALT.UTF8

* Fri Jul 18 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.1-alt6
- Apply patch from sbolshakov@ for prevent negative IP addresses in log
- Remove dependency on squid

* Fri Aug 17 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.1-alt5
- Move banlists and dbl to /var/lib/redirector (Closes: #12566)
- Use separate dir for store logfiles

* Wed Apr 18 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.1-alt4
- Supress output of service squid reload in %%post (Closes: #11542)
- Also supress same output in %%preun
- Switch to use .gear-tags

* Wed Jan 10 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.1-alt3
- Rewrite auto-activating and auto-disabling procedure of redirector at
  install/remove time

* Mon Dec 25 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.1-alt2
- Fix absend slash in config (Closes: #10487)
- Intergate patches into source-tree
- Update www-files to 20.10.2006 version

* Mon Jun 05 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.1-alt1
- 3.2.1
- Added redirector-3.2.1-alt-makefile.patch for fix linking
- Corrected build with gcc4
- Added DBL-scripts (separate package)
- Added squid-like "error-pages"
- Added README.ALT.KOI8-R
- Changed Summary

* Fri Aug  6 2004 Grigory Milev <week@altlinux.ru> 3.1.0-alt1b
- new version released:
  * fix found bugs
  * add option for making changes in url: raw_change

* Thu Apr 15 2004 Grigory Milev <week@altlinux.ru> 3.0.0-alt1
- Initial build.

