Name: BASE
Version: 1.4.5
Release: alt8

Summary: BASE - Basic Analysis and Security Engine
License: GPLv2
Group: Networking/Other

Url: http://secureideas.sourceforge.net/

Source0: base-%version.tar
Source1: nginx.conf

Patch1: base-1.4.5-alt-font-path.patch
Patch2: base-1.4.5-alt-urlpath.patch

BuildArch: noarch

Requires: php5-adodb fonts-ttf-dejavu pear-Image_Graph php5-mysql
Requires: pear-Mail_Mime pear-Mail pear-Image_Canvas pear-Image_Color

Obsoletes: base <= 1.4.5

%description
BASE is the Basic Analysis and Security Engine.  It is based on the code
from the Analysis Console for Intrusion Databases (ACID) project.  This
application provides a web front-end to query and analyze the alerts
coming from a SNORT IDS system.

BASE is a web interface to perform analysis of intrusions that SNORT
has detected on your network.  It uses a user authentication and
role-based system, so that you as the security admin can decide
which and how much information each user can see.  It also has a
simple to use, web-based setup program for people who feel not
comfortable with editing files directly.

BASE is supported by a group of volunteers.  They are available to
answer any questions you may have or help you out in setting up your
system.
They are also skilled in intrusion detection systems and make use of
that knowledge in the development of BASE. You can contact them
through the website http://secureideas.sourceforge.net/ or by
emailing them at base@secureideas.net

%package nginx
Summary: BASE with configuration for nginx
Group: Networking/Other
BuildArch: noarch
Requires: %name = %version-%release
Requires: nginx nginx-webapps
Obsoletes: base-nginx <= 1.4.5

%description nginx
BASE with nginx support.

%prep
%setup -n base-%version

%patch1 -p2
%patch2 -p2

%define _worldmap_target_dir usr/share/pear/Image/Graph/Images/Maps
%define _php_files_target_dir var/www/webapps/BASE/base

%build

%install
# At first, establish all the directories
mkdir -p %buildroot/%{_php_files_target_dir}
mkdir -p %buildroot/%{_worldmap_target_dir}
mkdir -p %buildroot%{_docdir}/%name-%version
mkdir -p %buildroot%{_docdir}/%name-%version/contrib

# Install the sub directories INCLUDING the files inside
cp -dpR admin %buildroot/%{_php_files_target_dir}/
cp -dpR help %buildroot/%{_php_files_target_dir}/
cp -dpR images %buildroot/%{_php_files_target_dir}/
cp -dpR includes %buildroot/%{_php_files_target_dir}/
cp -dpR languages %buildroot/%{_php_files_target_dir}/
cp -dpR setup %buildroot/%{_php_files_target_dir}/
cp -dpR sql %buildroot/%{_php_files_target_dir}/
cp -dpR styles %buildroot/%{_php_files_target_dir}/

# Install the files in the top level directory
install -m 0644 index.php %{buildroot}/%{_php_files_target_dir}/
install -m 0644 base* %{buildroot}/%{_php_files_target_dir}/

# These two files have to go in a PEAR specific direction
install -m 0644 world_map6.txt %{buildroot}/%{_worldmap_target_dir}/
install -m 0644 world_map6.png %{buildroot}/%{_worldmap_target_dir}/

# The docs go to a doc-specific location
# And this particular document HAS TO be enclosed by quotation marks
# because of the multibyte inside.
install -m 0644 "docs/contrib/Snort, Apache, MYSQL, PHP, and BASE instalación en Slackware.pdf" %{buildroot}%{_docdir}/%name-%version/contrib/
cp -dpR docs/* %{buildroot}%{_docdir}/%name-%version/

install -Dpm 644 %SOURCE1 %buildroot/%_sysconfdir/nginx/webapps-available.d/%name.conf

%files
/var/www/webapps/BASE/
%_docdir/*
/%_worldmap_target_dir

%files nginx
%_sysconfdir/nginx/webapps-available.d/%name.conf

%changelog
* Wed Dec 17 2014 Mikhail Efremov <sem@altlinux.org> 1.4.5-alt8
- Require more pear-* packages.

* Tue Aug 19 2014 Mikhail Efremov <sem@altlinux.org> 1.4.5-alt7
- Move content to /var/www/webapps/BASE/base.
- Use nginx-webapps.
- Don't create directories for httpd.
- Cleanup description.
- Use '/base' as urlpath.
- Rename package to BASE.

* Wed May 28 2014 Timur Aitov <timonbl4@altlinux.org> 1.4.5-alt6
- add Requires: php5-mysql

* Mon Feb 18 2013 Timur Aitov <timonbl4@altlinux.org> 1.4.5-alt5
- add Requires for build graphs

* Fri Jan 25 2013 Timur Aitov <timonbl4@altlinux.org> 1.4.5-alt4
- base, base-nginx - noarch now

* Thu Jan 24 2013 Timur Aitov <timonbl4@altlinux.org> 1.4.5-alt3
- fix spec

* Wed Jan 23 2013 Timur Aitov <timonbl4@altlinux.org> 1.4.5-alt2
- add config for nginx

* Wed Jan 23 2013 Timur Aitov <timonbl4@altlinux.org> 1.4.5-alt1
- [1.4.5]

