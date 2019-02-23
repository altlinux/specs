%define modulename seafobj

Name: python-module-seafobj
Version: 6.3.3
Release: alt1

Summary: Python library for accessing seafile data model

Group: Development/Python
License: Apache 2.0
Url: https://github.com/haiwen/seafobj

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/haiwen/seafobj/archive/v%version-server.tar.gz
Source: %name-%version.tar

# some unknown storage
%add_python_req_skip oss2

# disable ceph storage
%add_python_req_skip rados

%setup_python_module %modulename

%description
Python library for accessing seafile data model.

%prep
%setup

#build
#python_build

%install
#python_install
# TODO
mkdir -p %buildroot%python_sitelibdir/
cp -a %modulename/ %buildroot%python_sitelibdir/

%files
%python_sitelibdir/%modulename/

%changelog
* Sat Feb 23 2019 Vitaly Lipatov <lav@altlinux.ru> 6.3.3-alt1
- new version 6.3.3 (with rpmrb script)
- really disable rados

* Sat Feb 23 2019 Vitaly Lipatov <lav@altlinux.ru> 6.2.2-alt2
- disable rados, oss2 requires

* Tue Nov 07 2017 Vitaly Lipatov <lav@altlinux.ru> 6.2.2-alt1
- new version 6.2.2 (with rpmrb script)

* Wed Aug 03 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.4-alt1
- initial build for ALT Linux Sisyphus

