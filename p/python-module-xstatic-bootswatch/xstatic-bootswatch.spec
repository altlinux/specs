%define mname xstatic
%define oname %mname-bootswatch

%def_with python3

Name: python-module-%oname
Version: 3.3.5.3
Release: alt1.1.1
Summary: bootswatch (XStatic packaging standard)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/XStatic-bootswatch

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-%mname
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-%mname
%endif

%py_provides %mname.pkg.bootswatch
%py_requires %mname.pkg

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools-tests python-module-xstatic python3-module-setuptools-tests python3-module-xstatic rpm-build-python3

%description
bootswatch javascript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

%package -n python3-module-%oname
Summary: bootswatch (XStatic packaging standard)
Group: Development/Python3
%py3_provides %mname.pkg.bootswatch
%py3_requires %mname.pkg

%description -n python3-module-%oname
bootswatch javascript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

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

%ifarch x86_64
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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.5.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.3.5.3-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 05 2015 Alexey Shabalin <shaba@altlinux.ru> 3.3.5.3-alt1
- Initial build for Sisyphus
