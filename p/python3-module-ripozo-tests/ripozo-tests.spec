%define oname ripozo-tests

Name: python3-module-%oname
Version: 0.1.16
Release: alt2

Summary: A helper package for creating tests for ripozo and its extensions
License: UNKNOWN
Group: Development/Python
Url: https://pypi.python.org/pypi/ripozo-tests/
BuildArch: noarch

# https://github.com/vertical-knowledge/ripozo-tests.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-ripozo

%py3_provides ripozo_tests
%py3_requires six logging
%py3_requires ripozo


%description
These are the common tests that can be used for various common
extensions such as managers and adapters.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.16-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.16-alt1.dev0.git20150414.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.16-alt1.dev0.git20150414.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.16-alt1.dev0.git20150414.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.16-alt1.dev0.git20150414.1
- NMU: Use buildreq for BR.

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.16-alt1.dev0.git20150414
- Version 0.1.16.dev0

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.13-alt2.dev0.git20150323
- Added necessary requirements

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.13-alt1.dev0.git20150323
- Initial build for Sisyphus

