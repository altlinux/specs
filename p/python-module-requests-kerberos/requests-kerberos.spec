%define _unpackaged_files_terminate_build 1

%define mname requests-kerberos
%def_with check

Name: python-module-%mname
Version: 0.12.0
Release: alt1%ubt
Summary: A Kerberos authentication handler for python-requests
License: %mit
Group: Development/Python
Url: https://pypi.python.org/pypi/requests-kerberos

# https://github.com/requests/requests-kerberos.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools
BuildRequires: python-module-kerberos
BuildRequires: python3-module-kerberos

%if_with check
BuildRequires: python-module-mock
BuildRequires: python-module-requests
BuildRequires: python-module-pytest
BuildRequires: python3-module-mock
BuildRequires: python3-module-requests
BuildRequires: python3-module-pytest
%endif

Requires: python-module-requests >= 1.1
Requires: python-module-kerberos

%py_provides %mname

%description
Requests is an HTTP library, written in Python, for human beings. This
library adds optional Kerberos/GSSAPI authentication support and
supports mutual authentication.

%package -n python3-module-%mname
Summary: A Kerberos authentication handler for python-requests
Group: Development/Python3
Requires: python3-module-requests >= 1.1
Requires: python3-module-kerberos
%py3_provides %mname
%add_python3_req_skip requests.packages.urllib3

%description -n python3-module-%mname
Requests is an HTTP library, written in Python, for human beings. This
library adds optional Kerberos/GSSAPI authentication support and
supports mutual authentication.

%prep
%setup
%patch -p1
rm -rf ../python3
cp -a . ../python3

%build
%python_build_debug
pushd ../python3
%python3_build_debug
popd

%install
%python_install
pushd ../python3
%python3_install
popd

%check
python -m pytest --verbose
pushd ../python3
python3 -m pytest --verbose
popd

%files
%doc AUTHORS README.rst HISTORY.rst LICENSE
%python_sitelibdir/requests_kerberos
%python_sitelibdir/requests_kerberos-%version-*.egg-info

%files -n python3-module-%mname
%doc AUTHORS README.rst HISTORY.rst LICENSE
%python3_sitelibdir/requests_kerberos
%python3_sitelibdir/requests_kerberos-%version-*.egg-info

%changelog
* Tue Feb 13 2018 Stanislav Levin <slev@altlinux.org> 0.12.0-alt1%ubt
- v0.11.0 -> v0.12.0

* Tue Feb 13 2018 Stanislav Levin <slev@altlinux.org> 0.11.0-alt2%ubt
- Fix BuildRequires for tests

* Tue Nov 14 2017 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1%ubt
- 0.6.1 -> 0.11.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt1.git20141114.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20141114
- Initial build for Sisyphus

