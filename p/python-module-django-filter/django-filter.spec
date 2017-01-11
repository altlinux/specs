%define _unpackaged_files_terminate_build 1
%define oname django-filter

%def_with python3
%def_disable check
%def_enable light_version

Name: python-module-%oname
Version: 1.0.1
Release: alt1
Summary: A generic system for filtering Django QuerySets based on user selections
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-filter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/alex/django-filter.git
Source0: https://pypi.python.org/packages/f0/c4/b83b7a599201f84e8cbdbe325458d7d0281298e8b4e13edafebc936fa226/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
%if_disabled light_version
#BuildPreReq: python-module-django python-module-django-discover-runner
#BuildPreReq: python-module-mock python-module-coverage
#BuildPreReq: python-module-django-dbbackend-sqlite3
#BuildPreReq: python-module-sphinx-devel
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%if_disabled light_version
#BuildPreReq: python3-module-django python3-module-django-discover-runner
#BuildPreReq: python3-module-mock python3-module-coverage
#BuildPreReq: python3-module-django-dbbackend-sqlite3
%endif
%endif

%py_provides django_filters

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

%description
Django-filter is a reusable Django application for allowing users to
filter querysets dynamically.

%package -n python3-module-%oname
Summary: A generic system for filtering Django QuerySets based on user selections
Group: Development/Python3
%py3_provides django_filters

%description -n python3-module-%oname
Django-filter is a reusable Django application for allowing users to
filter querysets dynamically.

%if_disabled light_version
%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Django-filter is a reusable Django application for allowing users to
filter querysets dynamically.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Django-filter is a reusable Django application for allowing users to
filter querysets dynamically.

This package contains documentation for %oname.
%endif

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%if_disabled light_version
%prepare_sphinx .
ln -s ../objects.inv docs/
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

%if_disabled light_version
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

install -d %buildroot%python_sitelibdir/%oname

%check
python setup.py test
python runtests.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 runtests.py
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/*
%if_disabled light_version
%exclude %python_sitelibdir/*/pickle
%endif

%if_disabled light_version
%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt2.git20140929.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7-alt2.git20140929.1
- NMU: Use buildreq for BR.

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 0.7-alt2.git20140929
- Rebuild with "def_disable check"
- Light version with minimal build req

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20140929
- Initial build for Sisyphus

