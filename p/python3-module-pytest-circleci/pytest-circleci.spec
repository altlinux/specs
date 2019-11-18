%define oname pytest-circleci

Name: python3-module-%oname
Version: 0.0.2
Release: alt2

Summary: py.test plugin for CircleCI
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-circleci/
# https://github.com/micktwomey/pytest-circleci.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides pytest_circleci


%description
Use CircleCI env vars to determine which tests to run

* CIRCLE_NODE_TOTAL indicates total number of nodes tests are running on
* CIRCLE_NODE_INDEX indicates which node this is

Will run a subset of tests based on the node index.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Mon Nov 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.2-alt1.git20141116.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt1.git20141116.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20141116
- Initial build for Sisyphus

