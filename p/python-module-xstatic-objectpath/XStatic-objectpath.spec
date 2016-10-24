%define mname xstatic
%define oname %mname-objectpath

%def_with python3

Name: python-module-%oname
Version: 1.2.1.0
Release: alt1
Summary: Objectpath (XStatic packaging standard)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/XStatic-objectpath

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py_provides %mname.pkg.objectpath
%py_requires %mname.pkg

BuildRequires: python-module-setuptools-tests python-module-xstatic python3-module-setuptools-tests python3-module-xstatic

%description
Parse js object paths using both dot and bracket notation. Stringify an array of properties into a valid path.

- parse JS object reference fragments
- build JS object reference fragments
- supports presence of unicode characters
- supports presence of control characters in key names

%package -n python3-module-%oname
Summary: Objectpath (XStatic packaging standard)
Group: Development/Python3
%py3_provides %mname.pkg.objectpath
%py3_requires %mname.pkg

%description -n python3-module-%oname
Parse js object paths using both dot and bracket notation. Stringify an array of properties into a valid path.

- parse JS object reference fragments
- build JS object reference fragments
- supports presence of unicode characters
- supports presence of control characters in key names

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.1.0-alt1
- Initial build for Sisyphus
