%define oname django-taggit
%define mod_name taggit

%def_with check

Name: python3-module-%oname
Version: 5.0.1
Release: alt1

Summary: Simple tagging for django
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-taggit
BuildArch: noarch

# https://github.com/alex/django-taggit.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-djangorestframework
%endif

%description
django-taggit is a reusable Django application for simple tagging.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%find_lang %name

%check
python3 -m django test -v 2 --settings=tests.settings

%files -f %name.lang
%doc AUTHORS LICENSE *.rst docs/*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %oname}/

%changelog
* Wed Jan 03 2024 Alexander Burmatov <thatman@altlinux.org> 5.0.1-alt1
- Version updated to 5.0.1.

* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt1
- Version updated to 1.2.0
- build for python2 disabled

* Wed Dec 26 2018 Grigory Ustinov <grenka@altlinux.org> 0.23.0-alt1
- Build new version.

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.12.2-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.12.2-alt1.git20140921.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.12.2-alt1.git20140921.1
- NMU: Use buildreq for BR.

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2-alt1.git20140921
- Initial build for Sisyphus
