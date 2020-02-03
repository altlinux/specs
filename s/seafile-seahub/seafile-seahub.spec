Name: seafile-seahub
Version: 7.1.1
Release: alt1

Summary: Seahub is the web frontend for Seafile.

Group: Networking/File transfer
License: Apache-2.0
Url: https://github.com/haiwen/seahub

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>


# Source-url: https://github.com/haiwen/seahub/archive/v%version-server.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-build-intro

# TODO:
AutoReq:no
#seafile-seahub#7.1.1-alt1    python3(django.conf.urls.defaults) < 0
#seafile-seahub#7.1.1-alt1    python3(django.views.generic.simple) < 0
#seafile-seahub#7.1.1-alt1    python3(django_liveserver.testcases) < 0
#seafile-seahub#7.1.1-alt1    python3(fabric.api) < 0
#seafile-seahub#7.1.1-alt1    python3(fabric.colors) < 0
#seafile-seahub#7.1.1-alt1    python3(fpformat) < 0
#seafile-seahub#7.1.1-alt1    python3(group.models) < 0
#seafile-seahub#7.1.1-alt1    python3(mod_python) < 0
#seafile-seahub#7.1.1-alt1    python3(post_office) < 0
#seafile-seahub#7.1.1-alt1    python3(post_office.models) < 0
#seafile-seahub#7.1.1-alt1    python3(seaserv) < 0
#seafile-seahub#7.1.1-alt1    python3(south.db) < 0
#seafile-seahub#7.1.1-alt1    python3(south.v2) < 0
#seafile-seahub#7.1.1-alt1    python3(twilio.rest) < 0


AutoProv:yes,nopython

%add_python3_path %_datadir/%name
# TODO: autofill from requirements.txt
#BuildRequires: python3(django) python3(future) python3(captcha) python3(django_statici18n) python3(django_post_office) python3(django_webpack_loader) python3(gunicorn) python3(pymysql) python3(django_picklefield) python3(openpyxl) python3(qrcode) python3(django_formtools) python3(django_simple_captcha) python3(djangorestframework) python3(dateutil) python3(requests) python3(PIL) python3(jwt) python3(pycryptodome)

%description
Seahub is the web frontend for Seafile.

%prep
%setup
find -type f -name "*.py" | xargs subst "s|#!/usr/bin/env python|#!%__python3|"
%__subst "s|python$|python3|" tools/*
%__subst "s|^\([[:space:]]*\)python |\1python3 |" tools/sqlite-to-mysql.sh Makefile *.template

%build

%install
mkdir -p %buildroot%_datadir/%name/
cp -a * %buildroot%_datadir/%name/
rm -rf %buildroot%_datadir/%name/tests/

%files
%_datadir/%name/

%changelog
* Mon Feb 03 2020 Vitaly Lipatov <lav@altlinux.ru> 7.1.1-alt1
- new version 7.1.1 (with rpmrb script)
- build from a tarball
- switch to python3

* Tue Aug 30 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.4-alt1
- initial build for ALT Linux Sisyphus
