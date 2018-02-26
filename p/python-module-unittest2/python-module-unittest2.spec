%define oname unittest2

%def_without python3

Name: python-module-%oname
Version: 0.6.0
Release: alt1.a1.hg20120312

Summary: Backport of Python 2.7 unittest module
License: Same as Python
Group: Development/Python

BuildArch: noarch

Url: http://pypi.python.org/pypi/unittest2

Source: %name-%version.tar

Packager: Andrey Rahmatullin <wrar@altlinux.org>

%setup_python_module %oname

BuildPreReq: python-module-setuptools
%{?!_without_check:%{?!_disable_check:BuildRequires: %py_dependencies setuptools.command.test}}
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute-tests
BuildPreReq: python-tools-2to3
%endif

%description
unittest2 is a backport of the new features added to the unittest
testing framework in Python 2.7. It is tested to run on Python 2.4 -
2.7.

%if_with python3
%package -n python3-module-%oname
Summary: Port of Python 2.7 unittest module
Group: Development/Python3

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
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc README.txt
#_bindir/*
%python3_sitelibdir/*
%endif

%changelog
* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.a1.hg20120312
- Version 0.6.0a1

* Sun Oct 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Wed Sep 29 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.5.1-alt1
- initial build
