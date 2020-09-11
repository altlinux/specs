%define _unpackaged_files_terminate_build 1

%define oname s3transfer

%def_with python3

Name: python-module-%oname
Version: 0.3.3
Release: alt1
Summary:  Amazon S3 Transfer Manager for Python 
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/s3transfer/

BuildArch: noarch

# https://github.com/boto/s3transfer.git
Source: %name-%version.tar
Patch1: %oname-alt-unvendor.patch
# https://github.com/boto/s3transfer/pull/164
Patch2: %oname-upstream-python-3.8-compat.patch

BuildRequires: python-devel python-module-setuptools python-module-unittest2 python-module-mock
BuildRequires: python-module-botocore python-module-html5lib python-module-nose python-module-pbr
BuildRequires: python-module-futures
BuildRequires: python2.7(requests) python2.7(six)
BuildRequires: /usr/bin/py.test
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-unittest2 python3-module-mock
BuildRequires: python3-module-botocore python3-module-html5lib python3-module-nose python3-module-pbr
BuildRequires: python3(requests) python3(six)
BuildRequires: /usr/bin/py.test3
%endif

%py_provides %oname
%py_requires concurrent.futures

%description
S3transfer is a Python library for managing Amazon S3 transfers.

Note

This project is not currently GA. If you are planning to use this code in production,
make sure to lock to a minor version as interfaces may break from minor version to minor version.
For a basic, stable interface of s3transfer, try the interfaces exposed in boto3

%if_with python3
%package -n python3-module-%oname
Summary:  Amazon S3 Transfer Manager for Python 
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip requests.packages.urllib3.exceptions

%description -n python3-module-%oname
S3transfer is a Python library for managing Amazon S3 transfers.

Note

This project is not currently GA. If you are planning to use this code in production,
make sure to lock to a minor version as interfaces may break from minor version to minor version.
For a basic, stable interface of s3transfer, try the interfaces exposed in boto3
%endif

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
pushd ../python3
%patch2 -p1
popd
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
# remove tests depending on network
rm -rf tests/integration

py.test
%if_with python3
pushd ../python3
# remove tests depending on network
rm -rf tests/integration

py.test3
popd
%endif

%files
%doc LICENSE.txt
%doc *.rst
%python_sitelibdir/%oname
%python_sitelibdir/%oname-%version-py*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%doc LICENSE.txt
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info
%endif

%changelog
* Tue Sep 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.3-alt1
- Updated to upstream version 0.3.3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.10-alt1
- Initial build for ALT.
