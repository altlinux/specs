%define _unpackaged_files_terminate_build 1
%define oname detox

%def_disable check

Name: python3-module-%oname
Version: 0.10.0
Release: alt2

Summary: Distributing activities of the tox tool
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/detox/
BuildArch: noarch

Source0: https://pypi.python.org/packages/43/09/104095be078149e441ef926112521ec4bb5796a7828850167f7d0d95ab50/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

BuildRequires: python3-module-pytest


%description
detox is the distributed version of "tox". It makes efficient use of
multiple CPUs by running all possible activities in parallel. It has the
same options and configuration that tox has.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
export PYTHONPATH=%buildroot%python_sitelibdir
sed -i 's|"detox"|"detox.py3"|' tests/conftest.py
py.test-%_python3_version

%files
%doc CHANGELOG
%_bindir/*
%python3_sitelibdir/*


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.10.0-alt2
- python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.4-alt2.1
- NMU: Use buildreq for BR.

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 0.9.4-alt2
- Rebuild with "def_disable check"
- Turn off some build dependencies

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1
- Version 0.9.4

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt2
- Enabled testing for Python 3 module

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1
- Initial build for Sisyphus

