%define installdir %webserver_webappsdir/owncloud/3rdparty

Name: owncloud-3rdparty
Version: 5.0.0
Release: alt1

Summary: 3rdparty libs for owncloud
Group: Networking/WWW
License: Varioud free licenses
Url: http://www.owncloud.org/

BuildArch: noarch
BuildRequires(pre): rpm-macros-webserver-common
Requires: owncloud = %version

Source0: %name-%version.tar

%description
ownCloud gives you easy and universal access to all of your files.
This package provides a set of 3rdparty libs for owncloud.


%prep
%setup

%install
# install 
mkdir -p %buildroot%installdir

cp -rp * %buildroot%installdir/

%files
%installdir/*

%changelog
* Wed Mar 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt1
- 5.0.0

