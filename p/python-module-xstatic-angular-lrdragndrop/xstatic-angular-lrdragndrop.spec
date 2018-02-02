%define mname xstatic
%define oname %mname-angular-lrdragndrop
%define pypi_name XStatic-Angular-lrdragndrop

%def_with python3

Name: python-module-%oname
Version: 1.0.2.2
Release: alt2.1
Summary: Angular-lrdragndrop (XStatic packaging standard)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/%pypi_name/
Source: %pypi_name-%version.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-%mname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-%mname
%endif

%py_provides %mname.pkg.angular_lrdragndrop
%py_requires %mname.pkg

%description
lrDragNDrop javascript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

%package -n python3-module-%oname
Summary: Angular-lrdragndrop (XStatic packaging standard)
Group: Development/Python3
%py3_provides %mname.pkg.angular_lrdragndrop
%py3_requires %mname.pkg

%description -n python3-module-%oname
lrDragNDrop javascript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

%prep
%setup -n %pypi_name-%version

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/%mname/pkg/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/%mname/pkg/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*.pth
%endif


%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0.2.2-alt2
- rebuild

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Sep 09 2015 Lenar Shakirov <snejok@altlinux.ru> 1.0.2.2-alt1
- First build for ALT (based on Fedora 1.0.2.2-2.fc23.src)
