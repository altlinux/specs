%define oname objgraph

%def_with check

Name: python3-module-%oname
Version: 3.6.2
Release: alt1

Summary: Draws Python object reference graphs with graphviz

License: MIT
Group: Development/Python3
URL:    https://pypi.org/project/objgraph/
VCS:    https://github.com/mgedmin/objgraph
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: graphviz
BuildRequires: fontconfig
BuildRequires: fonts-ttf-liberation
%endif

%description
objgraph is a module that lets you visually explore Python object
graphs.

You'll need graphviz if you want to draw the pretty graphs.

I recommend xdot for interactive use. pip install xdot should suffice;
objgraph will automatically look for it in your PATH.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 tests.py

%files
%doc *.rst docs
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Thu Oct 10 2024 Grigory Ustinov <grenka@altlinux.org> 3.6.2-alt1
- Automatically updated to 3.6.2.

* Thu Apr 04 2024 Grigory Ustinov <grenka@altlinux.org> 3.6.1-alt1
- Automatically updated to 3.6.1.

* Sun Aug 13 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 3.6.0-alt1
- Version 3.6.0. This one actually works with python 3.11.
- Added missing build dependencies for the test suite.

* Thu Aug 04 2022 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1
- Build new version.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 3.4.1-alt2
- Drop python2 support.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 3.4.1-alt1
- Build new version.

* Tue Feb 05 2019 Grigory Ustinov <grenka@altlinux.org> 3.4.0-alt1
- Build new version.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1
- Version 1.8.1
- Added module for Python 3

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1
- Version 1.7.2

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt1
- Version 1.7.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.0-alt1.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus

