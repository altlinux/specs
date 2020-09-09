%define _unpackaged_files_terminate_build 1
%define oname django-filter

# https://github.com/carltongibson/django-filter/issues/1050
%def_disable check
%def_enable docs

Name: python3-module-%oname
Version: 2.3.0
Release: alt1

Summary: A generic system for filtering Django QuerySets based on user selections
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-filter/
# https://github.com/alex/django-filter.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/f0/c4/b83b7a599201f84e8cbdbe325458d7d0281298e8b4e13edafebc936fa226/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%if_enabled docs
BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme
%endif

%py3_provides django_filters


%description
Django-filter is a reusable Django application for allowing users to
filter querysets dynamically.

%if_enabled docs
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

%if_enabled docs
sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile
%endif

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%if_enabled docs
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/django_filters
%endif

%check
python3 setup.py test
python3 runtests.py

%files
%doc AUTHORS *.rst
%python3_sitelibdir/django_filters
%python3_sitelibdir/*.egg-info
%if_enabled docs
%exclude %python3_sitelibdir/django_filters/pickle

%files pickles
%python3_sitelibdir/django_filters/pickle

%files docs
%doc docs/_build/html/*
%endif

%changelog
* Wed Sep 09 2020 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt1
- Build new version.
- Build with docs.
- Fix pickles.

* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt3
- shebang fixed (py2 -> py3)

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

