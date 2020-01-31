%define modulename seafobj

Name:       python3-module-seafobj
Version:    6.3.3
Release:    alt2

Summary:    Python library for accessing seafile data model
License:    Apache 2.0
Group:      Development/Python3
Url:        https://github.com/haiwen/seafobj

Packager:   Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/haiwen/seafobj/archive/v%version-server.tar.gz
Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

# some unknown storage
%add_python3_req_skip oss2

# disable ceph storage
%add_python3_req_skip rados


%description
Python library for accessing seafile data model.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build

%install
mkdir -p %buildroot%python3_sitelibdir/
cp -a %modulename/ %buildroot%python3_sitelibdir/

%files
%doc LICENSE.txt README.md
%python3_sitelibdir/%modulename/


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 6.3.3-alt2
- Porting on Python3.

* Sat Feb 23 2019 Vitaly Lipatov <lav@altlinux.ru> 6.3.3-alt1
- new version 6.3.3 (with rpmrb script)
- really disable rados

* Sat Feb 23 2019 Vitaly Lipatov <lav@altlinux.ru> 6.2.2-alt2
- disable rados, oss2 requires

* Tue Nov 07 2017 Vitaly Lipatov <lav@altlinux.ru> 6.2.2-alt1
- new version 6.2.2 (with rpmrb script)

* Wed Aug 03 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.4-alt1
- initial build for ALT Linux Sisyphus

