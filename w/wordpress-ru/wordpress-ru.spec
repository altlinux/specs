
Name: wordpress-ru
Version: 2.9
Release: alt1

Summary: The powerful blogging web publishing platform
License: %gpl2only
Group: Networking/WWW
Url: http://mywordpress.ru/download/
BuildArch: noarch
Requires: webserver-common php-engine
BuildRequires: rpm-macros-webserver-common rpm-macros-apache2 rpm-build-licenses

# Automatically added by buildreq on Tue Dec 29 2009
BuildRequires: unzip

Source: wordpress-%version-ru_RU.zip
Source1: %name.httpd2.conf

Patch1: wordpress-ru-2.9-alt-translation.patch

%description
WordPress is a powerful blogging web publishing platform, and it comes 
with a great set of features designed to make your experience as a 
publisher on the Internet as easy, pleasant and appealing as possible. 

%package apache2
Summary: Apache2 config file for wordpress-ru
Group: Networking/WWW
Requires: %name = %version-%release
Requires: apache2

%description apache2
Apache2 config file for wordpress-ru

%prep
%__rm -f '!README_RUS!.html'
%setup -q -n wordpress
%patch1 -p1

%build

%install
%__install -d -m755 %buildroot%webserver_webappsdir/%name
%__cp -r ./* %buildroot%webserver_webappsdir/%name/
%__install -pD -m0644 %SOURCE1 %buildroot%_sysconfdir/httpd2/conf/addon.d/A.%name.conf
%__rm -f \
  %buildroot%webserver_webappsdir/%name/license.txt \
  %buildroot%webserver_webappsdir/%name/readme.html
%__mv %buildroot/%webserver_webappsdir/%name/wp-config-sample.php %buildroot/%webserver_webappsdir/%name/wp-config.php 

%files
%doc license.txt readme.html
#FIXME:files rights:see ALT Linux WebPolicy for further information;
%attr(755,root,%webserver_group) %webserver_webappsdir/%name

%files apache2
%config(noreplace) %_sysconfdir/httpd2/conf/addon.d/A.%name.conf

%post apache2
%post_service %apache2_dname
exit 0

%postun apache2
%post_service %apache2_dname
exit 0

%changelog
* Mon Dec 28 2009 Michael Pozhidaev <msp@altlinux.ru> 2.9-alt1
- First RPM for ALT Linux Sisyphus

