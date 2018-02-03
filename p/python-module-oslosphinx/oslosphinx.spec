%define oname oslosphinx

%def_with python3

Name: python-module-%oname
Version: 4.10.0
Release: alt1.1
Summary: OpenStack Sphinx Extensions and Theme
License: ASLv2.0
Group: Development/Python
Url: http://docs.openstack.org/developer/oslosphinx

# https://github.com/openstack/oslosphinx.git
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx-devel >= 1.2.1
BuildRequires: python-module-hacking >= 0.10.0
BuildRequires: python-module-reno >= 1.8.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-requests >= 2.10.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-sphinx-devel >= 1.2.1
BuildRequires: python3-module-hacking >= 0.10.0
BuildRequires: python3-module-reno >= 1.8.0
%endif

%py_provides %oname

%description
Theme and extension support for Sphinx documentation from the OpenStack
project.

%package -n python3-module-%oname
Summary: OpenStack Sphinx Extensions and Theme
Group: Development/Python3
%py3_provides %oname
%py3_requires hacking

%description -n python3-module-%oname
Theme and extension support for Sphinx documentation from the OpenStack
project.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Theme and extension support for Sphinx documentation from the OpenStack
project.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Theme and extension support for Sphinx documentation from the OpenStack
project.

This package contains documentation for %oname.

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

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

pushd doc
sphinx-build -b pickle -d build/doctrees source build/pickle
sphinx-build -b html -d build/doctrees source build/html
popd

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Apr 28 2017 Alexey Shabalin <shaba@altlinux.ru> 4.10.0-alt1
- 4.10.0

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 4.7.0-alt1
- 4.7.0

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 4.3.0-alt1
- 4.3.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.2.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.2.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 3.2.0-alt1
- 3.2.0

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1
- Version 3.0.0

* Fri May 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt2.git20141011
- Added necessary requirements
- Enabled testing

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.git20141011
- Initial build for Sisyphus

