%define appname contacts
%define installdir %webserver_webappsdir/owncloud/apps/%appname

Name: owncloud-apps-%appname
Version: 7.0.9
Release: alt1

Summary: Contacts storage for owncloud
Group: Networking/WWW
License: AGPLv3
Url: http://www.owncloud.org/

BuildArch: noarch
BuildRequires(pre): rpm-macros-webserver-common
Requires: owncloud = %version

Source0: %name-%version.tar

%description
ownCloud gives you easy and universal access to all of your files.
This package provides a contacts storage application to run into owncloud.


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
* Wed Jun 29 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 7.0.9-alt1
- 7.0.9

* Wed Feb 04 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.4-alt1
- 7.0.4

* Wed Sep 03 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.2-alt1
- 7.0.2

* Wed May 21 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.3-alt1
- 6.0.3

* Wed Jan 29 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.1-alt1
- 6.0.1

* Wed Jan 15 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.14a-alt1
- 5.0.14a

* Wed Nov 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.13-alt1
- 5.0.13

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
