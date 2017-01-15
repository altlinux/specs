%define _unpackaged_files_terminate_build 1
%define oname decorator

%def_with python3

Name: python-module-%oname
Version: 4.0.11
Release: alt1
Summary: Better living through Python with decorators
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/decorator
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/cc/ac/5a16f1fc0506ff72fcc8fd4e858e3a1c231f224ab79bb7c4c9b2094cc570/%{oname}-%{version}.tar.gz
#Source1: https://raw.githubusercontent.com/micheles/decorator/24d5f1539f0d876e4871ecca4f671d0710ab35bf/docs/README.rst
BuildArch: noarch

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python3-devel python3-module-distribute
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
%setup -q -n %{oname}-%{version}

#install -Dm644 %SOURCE1 docs/README.rst

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
%doc *.txt documentation.*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt documentation.*
%python3_sitelibdir/*
%endif

%changelog
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

