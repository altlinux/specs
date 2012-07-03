Name: prometeus
Version: 0.85
Release: alt1

Summary: Site and site-utils for Sisyphus and ALT Linux Team
License: GPL
Group: Networking/WWW
Packager: Avramenko Andrew <liks@altlinux.ru>

URL: http://www.sisyphus.ru

Source: %name-%version.tar.bz2
BuildArch: noarch

Provides: perl(altbase.pm)
Requires: perl-DBD-mysql
BuildRequires: perl-DBI perl-libwww perl-upstreamwatch perl-XML-Simple perl-RPM perl-CGI
# due to global vars in altbase.pm
%set_perl_req_method relaxed

%description
prometeus is a project of informational site for Sisyphus and ALT Linux Team.
It contain full information about all rpm packages, maintainers, buglist of
Sisyphus. Simple and clear interface and navigation allow one easy to get any
interesting information and statistics reposrts.
Also site can be used for any consistent repositories of rpm packages.

%prep
%setup -q -n %name
subst "s|--path--|%_datadir/%name|" A.prometeus.conf prometeus.conf web/cgi-bin/adm/altbase.pm
%build

%install
mkdir -p %buildroot%_datadir/%name
cp -R web scripts sql A.prometeus.conf prometeus.conf %buildroot%_datadir/%name

%files
%doc AUTHORS CHANGELOG COPYING INSTALL README TODO
%dir %_datadir/%name
%_datadir/%name/prometeus.conf
%_datadir/%name/A.prometeus.conf
%dir %_datadir/%name/sql
%_datadir/%name/sql/prometeus.sql
%_datadir/%name/sql/repocop.sql
%dir %_datadir/%name/scripts
%_datadir/%name/scripts/*2mysql
%attr(0640,root,root) %config %_datadir/%name/scripts/config
%dir %_datadir/%name/web
%_datadir/%name/web/html
%dir %_datadir/%name/web/cgi-bin
%_datadir/%name/web/cgi-bin/*.pl
#defattr(640,root,apache)
#attr(0750,root,apache)%dir %_datadir/%name/web/cgi-bin/adm
# dirty hack for support of both apache1 & apache2 to be removed later
# after common webservers group will appear.
%defattr(440,apache2,apache)
%attr(0550,apache2,apache)%dir %_datadir/%name/web/cgi-bin/adm
%_datadir/%name/web/cgi-bin/adm/altbase.pm

%changelog
* Wed Jul 15 2009 Grigory Batalov <bga@altlinux.ru> 0.85-alt1
- English and Portuguese (Brasilian) translations.

* Mon Feb 25 2008 Avramenko Andrew <liks@altlinux.ru> 0.82-alt1
- New version

* Fri Aug 10 2007 Avramenko Andrew <liks@altlinux.ru> 0.72-alt1
- 0.72 Merge changes from current alt.linux.kiev.ua

* Sat Apr 16 2005 Vladimir Lettiev <crux@altlinux.ru> 0.71-alt1
- 0.71
- just simple and clear install

* Mon Jul 12 2004 Vladimir Lettiev <crux@altlinux.ru> 0.3-alt1
- initial release for ALT Linux Team

