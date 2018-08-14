%define _unpackaged_files_terminate_build 1

%define mname kdcproxy
%def_with check

Name: python-module-%mname
Version: 0.4
Release: alt1

Summary: A kerberos KDC HTTP proxy WSGI module
License: %mit
Group: Development/Python
Url: https://pypi.org/project/kdcproxy
# Source-git: https://github.com/latchset/kdcproxy

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-tox
BuildRequires: python-module-mock
BuildRequires: python-module-dns
BuildRequires: python-module-coverage
BuildRequires: python-module-webtest
BuildRequires: python-module-asn1crypto
BuildRequires: python3-module-tox
BuildRequires: python3-module-dns
BuildRequires: python3-module-coverage
BuildRequires: python3-module-webtest
BuildRequires: python3-module-asn1crypto
%endif

BuildArch: noarch

%description
This package contains a Python 2.x WSGI module for proxying KDC requests
over HTTP by following the MS-KKDCP protocol. It aims to be simple
to deploy, with minimal configuration.

%package -n python3-module-%mname
Summary: A kerberos KDC HTTP proxy WSGI module
Group: Development/Python3

%description -n python3-module-%mname
This package contains a Python 3.x WSGI module for proxying KDC requests
over HTTP by following the MS-KKDCP protocol. It aims to be simple
to deploy, with minimal configuration.

%prep
%setup
%patch -p1
# there is no package with provided name dnspython3
# both python and python3 version have dnspython
sed -i 's/"dnspython3"/"dnspython"/g' setup.py

cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
pushd ../python3
%python3_install
popd

%check
export PIP_INDEX_URL=http://host.invalid./
export KDCPROXY_ASN1MOD=asn1crypto
TOX_TESTENV_PASSENV=KDCPROXY_ASN1MOD tox --sitepackages -e py%{python_version_nodots python} -v -- -v

pushd ../python3
TOX_TESTENV_PASSENV=KDCPROXY_ASN1MOD tox.py3 --sitepackages -e py%{python_version_nodots python3} -v -- -v
popd

%files
%doc COPYING README
%python_sitelibdir/%mname/
%python_sitelibdir/%mname-*.egg-info

%files -n python3-module-%mname
%doc COPYING README
%python3_sitelibdir/%mname/
%python3_sitelibdir/%mname-*.egg-info

%changelog
* Tue Aug 14 2018 Stanislav Levin <slev@altlinux.org> 0.4-alt1
- 0.3.3 -> 0.4.

* Thu Jul 26 2018 Stanislav Levin <slev@altlinux.org> 0.3.3-alt1
- 0.3.2 -> 0.3.3
- Build package for Python3

* Wed Sep 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Initial build.

