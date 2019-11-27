%define oname Objects

Name: python3-module-%oname
Version: 0.4.2
Release: alt2

Summary: Python catalogs of objects providers
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Objects/
BuildArch: noarch

# https://github.com/rmk135/objects.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six

%py3_provides objects
%py3_requires six


%description
Python catalogs of objects providers.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.md examples
%python3_sitelibdir/*


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1.git20150225.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20150225.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1.git20150225.1
- NMU: Use buildreq for BR.

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20150225
- Version 0.4.2

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150123
- Initial build for Sisyphus

