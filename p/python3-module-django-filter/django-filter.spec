%define _unpackaged_files_terminate_build 1
%define oname django-filter

%def_with check

Name: python3-module-%oname
Version: 24.3
Release: alt1

Summary: A generic system for filtering Django QuerySets based on user selections
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/django-filter
Vcs: https://github.com/carltongibson/django-filter

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-django
BuildRequires: python3-module-pytz
BuildRequires: python3-module-djangorestframework
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
Django-filter is a reusable Django application allowing users to declaratively
add dynamic QuerySet filtering from URL parameters.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- %__python3 runtests.py -v 2

%files
%doc README.*
%python3_sitelibdir/django_filters
%python3_sitelibdir/django_filter-%version.dist-info

%changelog
* Thu Aug 08 2024 Anton Vyatkin <toni@altlinux.org> 24.3-alt1
- New version 24.3.

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

