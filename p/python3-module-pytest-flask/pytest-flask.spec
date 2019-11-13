%define _unpackaged_files_terminate_build 1
%define oname pytest-flask

Name: python3-module-%oname
Version: 0.10.0
Release: alt2

Summary: A set of py.test fixtures to test Flask applications
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-flask/
# https://github.com/vitalk/pytest-flask.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/b4/b5/6d86a2362be78d1d817c7a1d5105100b7b51089dd56ca907d4fed9461570/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flask
BuildRequires: python3-module-pytest

%py3_provides pytest_flask


%description
A set of py.test fixtures to test Flask extensions and applications.

Plugin provides some fixtures to simplify app testing:

* client - an instance of app.test_client,
* client_class - client fixture for class-based tests,
* config - you application config,
* accept_json, accept_jsonp, accept_any - accept headers suitable to use
  as parameters in client.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc PKG-INFO README.rst docs
%python3_sitelibdir/*


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.10.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt1.git20141124.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1.git20141124.1
- NMU: Use buildreq for BR.

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20141124
- Version 0.6.0

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20141103
- Version 0.5.0

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20141028
- Initial build for Sisyphus

