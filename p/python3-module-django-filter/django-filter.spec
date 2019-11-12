%define _unpackaged_files_terminate_build 1
%define oname django-filter

%def_disable check
%def_enable light_version

Name: python3-module-%oname
Version: 1.0.1
Release: alt2

Summary: A generic system for filtering Django QuerySets based on user selections
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-filter/
# https://github.com/alex/django-filter.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/f0/c4/b83b7a599201f84e8cbdbe325458d7d0281298e8b4e13edafebc936fa226/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%if_disabled light_version
BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme
%endif

%py3_provides django_filters


%description
Django-filter is a reusable Django application for allowing users to
filter querysets dynamically.

%if_disabled light_version
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

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

%if_disabled light_version
sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile
%endif

%build
%python3_build_debug

%install
%python3_install

%if_disabled light_version
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

install -d %buildroot%python3_sitelibdir/%oname

%check
python3 setup.py test
python3 runtests.py

%files
%doc AUTHORS *.rst
%python3_sitelibdir/*
%if_disabled light_version
%exclude %python3_sitelibdir/%oname
%endif

%if_disabled light_version
%files pickles
%python3_sitelibdir/%oname

%files docs
%doc docs/_build/html/*
%endif


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt2
- disable python2

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

