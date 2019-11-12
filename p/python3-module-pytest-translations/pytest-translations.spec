%define oname pytest-translations

%def_disable check
%def_with bootstrap

Name: python3-module-%oname
Version: 0.2.0
Release: alt3
Summary: Test your translation files

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-translations/
# https://github.com/Thermondo/pytest-translations.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides pytest_translations
%py3_requires polib

%if_with bootstrap
%add_python3_req_skip py.test.collect
%endif

BuildRequires: python3-module-polib python3-module-pytest


%description
py.test plugin to test your translation files.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt3
- disable python2

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20150101.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20150101.1
- NMU: Use buildreq for BR.

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150101
- Initial build for Sisyphus

