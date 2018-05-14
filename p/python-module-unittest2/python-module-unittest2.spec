%define oname unittest2

%def_disable check

Name: python-module-%oname
Version: 1.1.0
Release: alt3

Summary: Backport of Python 2.7 unittest module
License: Same as Python
Group: Development/Python
Url: http://pypi.python.org/pypi/unittest2
# hg clone https://hg.python.org/unittest2
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-module-pytest python-module-traceback2

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-pytest python3-module-traceback2
BuildPreReq: python-tools-2to3

#%%py_requires traceback2 six


%description
unittest2 is a backport of the new features added to the unittest
testing framework in Python 2.7. It is tested to run on Python 2.4 -
2.7.

%package -n python3-module-%oname
Summary: Port of Python 2.7 unittest module
Group: Development/Python3
#%%py3_requires traceback2 six

%description -n python3-module-%oname
unittest2 is a port of the features added to the unittest testing
framework in Python 2.7.

%prep
%setup

rm -rf ../python3
cp -a . ../python3


%build
%python_build

pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build
popd

%install
pushd ../python3
%python3_install
popd

%python_install

%check
python setup.py test

pushd ../python3
python3 setup.py test
popd

%files
%doc README.txt
%_bindir/*
%python_sitelibdir/*

%files -n python3-module-%oname
%doc README.txt
#_bindir/*
%python3_sitelibdir/*


%changelog
* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt3
- rebuild with python3.6

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
