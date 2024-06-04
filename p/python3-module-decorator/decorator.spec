%define modname decorator

Name: python3-module-%modname
Version: 5.1.1
Release: alt1

Summary: Better living through Python with decorators

License: BSD-2-Clause
Group: Development/Python3
URL: https://pypi.org/project/decorator
VCS: https://github.com/micheles/decorator

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Python decorators are an interesting example of why syntactic sugar
matters. In principle, their introduction in Python changed nothing,
since they do not provide any new functionality which was not already
present in the language. In practice, their introduction has
significantly changed the way we structure our programs in Python. I
believe the change is for the best, and that decorators are a great idea
since:

* decorators help reducing boilerplate code;

* decorators help separation of concerns;

* decorators enhance readability and maintenability;

* decorators are explicit.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc CHANGES.md LICENSE.txt README.rst
%python3_sitelibdir/%modname.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%modname-%version.dist-info

%changelog
* Tue Jun 04 2024 Grigory Ustinov <grenka@altlinux.org> 5.1.1-alt1
- Build new version.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 4.4.2-alt2
- Drop python2 support.

* Mon May 03 2021 Yuri N. Sedunov <aris@altlinux.org> 4.4.2-alt1
- 4.4.2
- made python2 build optional

* Mon Dec 24 2018 Alexey Shabalin <shaba@altlinux.org> 4.3.0-alt1
- 4.3.0

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.10-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.2-alt1.1
- NMU: Use buildreq for BR.

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.4.0-alt1.1
- Rebuild with Python-3.3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Version 3.4.0

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1
- Version 3.3.3
- Added module for Python 3

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.2-alt1
- Version 3.3.2

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.3.1-alt1.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1
- Version 3.3.1

* Tue Jul 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1
- Version 3.2.0

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt2
- Rebuilt with python 2.6

* Tue Sep 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1
- Initial build for Sisyphus

