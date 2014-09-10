%define appname music
%define installdir %webserver_webappsdir/owncloud/apps/%appname

Name: owncloud-apps-%appname
Version: 0.3.4 
Release: alt1

Summary: Music player for owncloud
Group: Networking/WWW
License: AGPLv3
Url: http://www.owncloud.org/

BuildArch: noarch
BuildRequires(pre): rpm-macros-webserver-common
Requires: owncloud >= 7.0.0 

Source0: %name-%version.tar

%description
ownCloud gives you easy and universal access to all of your files.
This package provides a music player application to run into owncloud.


%prep
%setup

%install
# install owncloud apps
mkdir -p %buildroot%installdir

cp -rp * %buildroot%installdir/
rm -f %buildroot%installdir/l10n/l10n.pl

%files
%installdir/*

%changelog
* Wed Sep 10 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3.4-alt1
- first build
