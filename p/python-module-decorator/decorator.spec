%define oname decorator

%def_with python3

Name: python-module-%oname
Version: 3.3.3
Release: alt1
Summary: Better living through Python with decorators
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/decorator
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

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

                     Michele Simionato <michele simionato at gmail com>

%if_with python3
%package -n python3-module-%oname
Summary: Better living through Python 3 with decorators
Group: Development/Python3

%description -n python3-module-%oname
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

                     Michele Simionato <michele simionato at gmail com>
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.txt documentation.*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.txt documentation.*
%python3_sitelibdir/*
%endif

%changelog
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

