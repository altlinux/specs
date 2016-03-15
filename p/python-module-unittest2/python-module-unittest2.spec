%define oname unittest2

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.1.0
Release: alt2.hg20150630.1

Summary: Backport of Python 2.7 unittest module
License: Same as Python
Group: Development/Python

BuildArch: noarch

Url: http://pypi.python.org/pypi/unittest2

# hg clone https://hg.python.org/unittest2
Source: %name-%version.tar

%setup_python_module %oname
BuildRequires: python-module-pytest python-module-traceback2

#BuildPreReq: python-module-setuptools-tests
#BuildPreReq: python-module-traceback2 python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-traceback2 python3-module-six
BuildRequires: python3-module-pytest python3-module-traceback2
BuildPreReq: python-tools-2to3
%endif

#%py_requires traceback2 six

%description
unittest2 is a backport of the new features added to the unittest
testing framework in Python 2.7. It is tested to run on Python 2.4 -
2.7.

%if_with python3
%package -n python3-module-%oname
Summary: Port of Python 2.7 unittest module
Group: Development/Python3
#%py3_requires traceback2 six

%description -n python3-module-%oname
unittest2 is a port of the features added to the unittest testing
framework in Python 2.7.
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
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif
%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README.txt
%_bindir/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.txt
#_bindir/*
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt2.hg20150630.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.1.0-alt2.hg20150630
- Rebuild with "def_disable check"
- Cleanup buildreq

* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.hg20150630
- Version 1.1.0

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.a1.hg20120312
- Version 0.6.0a1

* Sun Oct 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Wed Sep 29 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.5.1-alt1
- initial build
