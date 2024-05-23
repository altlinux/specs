%define oname pylru

Name:       python3-module-%oname
Version:    1.2.1
Release:    alt1

Summary:    A least recently used (LRU) cache implementation

License:    GPLv2
Group:      Development/Python3
URL:        https://pypi.org/project/pylru
VCS:        https://github.com/jlhutch/pylru

BuildArch:  noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%py3_provides %oname

%description
Pylru implements a true LRU cache along with several support classes.
The cache is efficient and written in pure Python. It works with Python
2.6+ including the new 3.x series. Basic operations (lookup, insert,
delete) all run in a constant amount of time.


%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.txt *.rst
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Thu May 23 2024 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1
- Build new version.

* Mon Feb 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.9-alt2
- Build for python2 disabled.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.6-alt1.git20141014.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.6-alt1.git20141014.1
- NMU: Use buildreq for BR.

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.git20141014
- Initial build for Sisyphus

