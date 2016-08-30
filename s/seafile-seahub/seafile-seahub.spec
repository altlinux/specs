# See requirements.txt and thirdpart
#	python2.7(constance)
#	python2.7(django_liveserver)
#	python2.7(exam)
#	python2.7(factory)
#	python2.7(mod_python)
#	python2.7(openpyxl)
#	python2.7(post_office)
#	python2.7(seaserv)
#	python2.7(selenium)
#	python2.7(south)
#	python2.7(splinter)

Name: seafile-seahub
Version: 5.1.4
Release: alt1

Summary: Seahub is the web frontend for Seafile.

Group: Networking/File transfer
License: Apache 2.0
Url: https://github.com/haiwen/seahub

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>

AutoReq:yes,nopython

# Source-url: https://github.com/haiwen/seahub/archive/v%version.tar.gz
Source: %name-%version.tar

%description
Seahub is the web frontend for Seafile.

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/%name/
cp -a * %buildroot%_datadir/%name/

%files
%_datadir/%name/

%changelog
* Tue Aug 30 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.4-alt1
- initial build for ALT Linux Sisyphus
