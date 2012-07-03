Name: squidGuard
Version: 1.4
Release: alt1

%define _dbhomedir %_localstatedir/%name

Summary: Filter, redirector and access controller plugin for squid
License: GPLv2
Group: System/Servers
Url: http://www.squidguard.org/

Packager: Vladimir Scherbaev <vladimir at altlinux.org>

Source0: %name-%version.tar.gz
Source1: %name.conf
Source2: blacklists.tgz
Source3: squidGuard.logrotate
Source4: sg-utils-0.2.tar.gz
Source5: %name-ru.cgi

Patch0: %name-alt-fix-perm.patch
#Patch1: %name-alt-fix-req.patch
Patch2: %name-%version-alt-make.patch

Requires: squid-server logrotate
BuildRequires: flex libdb4.7-devel perl-DBM

%description
squidGuard can be used to
    - limit the web access for some users to a list of accepted/well known
    web servers and/or URLs only.
    - block access to some listed or blacklisted web servers and/or URLs
    for some users. **)
    - block access to URLs matching a list of regular expressions or words
    for some users. **)
    - enforce the use of domainnames/prohibit the use of IP address in
    URLs. **)
    - redirect blocked URLs to an "intelligent" CGI based info page. **)
    - redirect unregistered user to a registration form.
    - redirect popular downloads like Netscape, MSIE etc. to local copies.
    - redirect banners to an empty GIF. **)
    - have different access rules based on time of day, day of the week,
     date etc.
     - have different rules for different user groups.
     - and much more..

Neither squidGuard nor Squid can be used to
     - filter/censor/edit text inside documents
     - filter/censor/edit embeded scripting languages like JavaScript or
      VBscript inside HTML

%prep
%setup -q
%patch0
#%patch1 -p1
%patch2

%build
%configure \
#--with-sg-logdir=/var/log/squid \
#--with-sg-dbhome=%_dbhomedir \


%__make

%install
%makeinstall DESTDIR=%buildroot
%__mkdir_p %buildroot%_sysconfdir/%name
%__mkdir_p %buildroot%_dbhomedir
%__install -p -m 0644 %SOURCE1 %buildroot%_sysconfdir/%name/%name.conf
#%__tar xCf %buildroot%_dbhomedir %SOURCE2

%files
%doc ANNOUNCE CHANGELOG CONFIGURATION COPYING FAQ GPL INSTALL ISSUES.txt README README.LDAP
%doc doc/*.txt doc/*.html
%doc samples/*.conf samples/*.cgi
%_bindir/*
%config(noreplace) %_sysconfdir/%name/squidGuard.conf
#%_dbhomedir

%changelog
* Mon Dec 29 2008 Vladimir Scherbaev <vladimir@altlinux.org> 1.4-alt1
- New version 1.4

* Wed Dec 10 2008 Vladimir Scherbaev <vladimir@altlinux.org> 1.3.0-alt10
- Build with libdb4.7

* Mon Jul 21 2008 Vladimir Scherbaev <vladimir@altlinux.org> 1.3.0-alt9
- Add sg-utils

* Sun May 25 2008 Vladimir Scherbaev <vladimir@altlinux.org> 1.3.0-alt8
- New version

* Thu Jun 30 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2.0-alt7
- fixed #7238

* Wed May 25 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2.0-alt6
- fixed typo in blacklists
- added test target to build

* Mon May 16 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2.0-alt5
- Initial release for Sisyphus
- Build with libdb4.3
- Fixed logrotate script
- Updated blacklists bases

* Sat Jul 24 2004 Vladimir Lettiev <crux@altlinux.ru> 1.2.0-alt4
- Updated BuildRequires (removed lynx, tcsh)
- Updated sg-utils:
+ Fixed bug in sg-mod: squidGuard ignore new entries in .db files
	added by sg-mod if .db was created by squidGuard.
	(reported by Alexander Markelov)
+ Fixed bug in sg-search: print internal error if dest section in
	squidGuard.conf contain no domains/urls.
- Updated blacklists bases

* Wed Jun 30 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.2.0-alt3.1
- Updated BuildRequires

* Mon Jun 28 2004 Vladimir Lettiev <crux@altlinux.ru> 1.2.0-alt3
- Added new blacklists bases
	merged: squidGuard, MESD, rejik.ru, some domain/urls from Mike Lykov
- Added utilities:
	sg-search - search in squidGuard .db bases
	sg-mod    - modification of squidGuard .db bases
- Added squidGuard-ru.cgi - simple cgi-script in russian
- A lot of changes in spec, added post section to create .db files

* Sun Jun 20 2004 Vladimir Lettiev <crux@altlinux.ru> 1.2.0-alt2
- Add debian patch to fix build with libdb4.2
- Some spec cleanup

* Sat Jul 27 2002 Serge A. Volkov <vserge@altlinux.ru> 1.2.0-alt1
- First release for ALT Linux TEAM
- Spec cleanup

* Mon Apr 08 2002 Oliver Pitzeier <o.pitzeier@uptime.at>
- Updated the blacklists and put it into the right place
	I also descompress them
- Added a new "forbidden" script - the other ones are too
	old and don't work.

* Fri Apr 05 2002 Oliver Pitzeier <o.pitzeier@uptime.at>
- Update to version 1.2.0

* Fri Jun  1 2001 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
- cleaned up for rhcontrib

* Fri Oct 13 2000 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
- initial build

