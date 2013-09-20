%define installdir %webserver_webappsdir/owncloud/apps/

Name: owncloud-apps
Version: 5.0.11
Release: alt1

Summary: Applications for owncloud
Group: Networking/WWW
License: AGPLv3
Url: http://www.owncloud.org/

BuildArch: noarch
BuildRequires(pre): rpm-macros-webserver-common
Requires: owncloud = %version

Source0: %name-%version.tar

%description
ownCloud gives you easy and universal access to all of your files.
This package provides a set of applications to run into owncloud.


%prep
%setup

%install
# install owncloud apps
mkdir -p %buildroot%installdir

cp -rp * %buildroot%installdir/
rm -f %buildroot%installdir/l10n/l10n.pl
rm -f %buildroot%installdir/l10n/init.sh

%files
%installdir/*

%changelog
* Thu Sep 19 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.11-alt1
- 5.0.11

* Mon May 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.6-alt1
- 5.0.6

* Thu Apr 11 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.4-alt1
- 5.0.4

* Fri Mar 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt1
- 5.0.0

* Thu Mar 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.5.8-alt1
- 4.5.8
