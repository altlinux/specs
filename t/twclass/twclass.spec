Name:		twclass
Version:	0.3.2
Release:	alt1.qa1
Packager:	Dmitri Plakhov <dplakhov at altlinux.ru>

Summary:	eLearning System

Group:		Networking/WWW
License:	GPLv2+
URL:		http://www.ksob.ru/
Source:		http://www.ksob.ru/downloads/twclass.tar.gz
BuildArch:	noarch
Requires:	php5 apache2-mod_php5 php5-mysql apache2-httpd-worker MySQL-server MySQL-client

%define sdowebdir %_var/www/html/%name
%define apache_group apache2

%description
TWClass - system of remote training the representing specialised server
software providing storage, support of teaching materials on a server and
access of users to them, and as interaction of the teacher and the pupil at
development of a training course (courses). The system comprises tools of
carrying out of testing, interrogations, questioning, and as gathering and
the statistics analysis on training process.
User support and the additional information - on a site http://ksob.ru

%prep
%setup -q -n %name

%build

%install
%__mkdir_p %buildroot%sdowebdir
%__cp -rf * %buildroot%sdowebdir/

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%clean

%files
%attr(770,%apache_group,%apache_group) %sdowebdir/*
%attr(770,%apache_group,%apache_group) %dir %sdowebdir
%sdowebdir/*
%dir %sdowebdir

%changelog
* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.3.2-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * windows-thumbnail-database-in-package for twclass
  * postclean-05-filetriggers for spec file

* Thu Oct 29 2009 Dmitri Plakhov <dplakhov@altlinux.org> 0.3.2-alt1
- Conf. files fixed
* Mon Oct 19 2009 Dmitri Plakhov <dplakhov@altlinux.org> 0.3.1-alt1
- DB charset fixed
* Mon Oct 19 2009 Dmitri Plakhov <dplakhov@altlinux.org> 0.3-alt1
- New distro
* Fri Sep  4 2009 Dmitri Plakhov <dplakhov@altlinux.org> 0.2.2-alt1
- English description added
* Fri Aug 21 2009 Dmitri Plakhov <dplakhov@altlinux.org> 0.2-alt1
- New version
* Wed Oct  1 2008 Dmitri Plakhov <dplakhov@altlinux.org> 0.1-alt1
- initial build
