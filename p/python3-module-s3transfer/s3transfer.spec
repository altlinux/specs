%define _unpackaged_files_terminate_build 1

%define oname s3transfer

Name: python3-module-%oname
Version: 0.3.3
Release: alt2

Summary:  Amazon S3 Transfer Manager for Python

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/s3transfer/

BuildArch: noarch

# Source-git: https://github.com/boto/s3transfer.git
Source: %name-%version.tar

Patch1: %oname-alt-unvendor.patch
# https://github.com/boto/s3transfer/pull/164
Patch2: %oname-upstream-python-3.8-compat.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-unittest2 python3-module-mock
BuildRequires: python3-module-botocore python3-module-html5lib python3-module-nose python3-module-pbr
BuildRequires: python3(requests) python3(six)
BuildRequires: /usr/bin/py.test3

%py3_provides %oname
%add_python3_req_skip requests.packages.urllib3.exceptions

%description
S3transfer is a Python library for managing Amazon S3 transfers.

Note

This project is not currently GA. If you are planning to use this code in production,
make sure to lock to a minor version as interfaces may break from minor version to minor version.
For a basic, stable interface of s3transfer, try the interfaces exposed in boto3

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%python3_build_debug

%install
%python3_install

%check
# remove tests depending on network
rm -rf tests/integration

py.test3

%files
%doc *.rst
%doc LICENSE.txt
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info

%changelog
* Thu Jun 17 2021 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt2
- build python3 module separately

* Tue Sep 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.3-alt1
- Updated to upstream version 0.3.3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.10-alt1
- Initial build for ALT.
