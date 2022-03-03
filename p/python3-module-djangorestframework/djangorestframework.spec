%define _unpackaged_files_terminate_build 1
%define oname djangorestframework

%def_with docs
%def_with check

Name: python3-module-%oname
Version: 3.13.1
Release: alt1
Summary: Web APIs for Django, made easy
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/djangorestframework

# Source-git: https://github.com/encode/django-rest-framework.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with docs
BuildRequires: python3-module-mkdocs >= 1.0.4-alt2
BuildRequires: python3(tornado)
BuildRequires: python3(livereload)
%endif

%if_with check
# install_requires=
BuildRequires: python3(pytz)
BuildRequires: python3-module-django

BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(pytest_django)
BuildRequires: python3-module-django-tests
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

# we have several versions of Django
# so, we cannot rely on auto-requires
%filter_from_requires /^python3(django\(\..*\)\?)/d
%description
Django REST framework is a powerful and flexible toolkit for building
Web APIs.

%if_with docs
%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
Django REST framework is a powerful and flexible toolkit for building
Web APIs.

This package contains documentation for %oname.
%endif

%prep
%setup
%autopatch -p1

%build
%python3_build

%if_with docs
mkdocs build
%endif

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --no-deps -vvr

%files
%doc *.md
%python3_sitelibdir/rest_framework/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%if_with docs
%files docs
%doc site/*
%endif


%changelog
* Mon Feb 28 2022 Stanislav Levin <slev@altlinux.org> 3.13.1-alt1
- 3.12.4 -> 3.13.1.

* Thu Sep 09 2021 Alexey Shabalin <shaba@altlinux.org> 3.12.4-alt3
- Fix BR.
- Backport upstream patches for fix tests with Django-3.2.

* Fri Apr 16 2021 Stanislav Levin <slev@altlinux.org> 3.12.4-alt2
- Applied upstream fix for new Pygments.

* Wed Apr 14 2021 Stanislav Levin <slev@altlinux.org> 3.12.4-alt1
- 3.12.1 -> 3.12.4.

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 3.12.1-alt1
- 3.11.0 -> 3.12.1.

* Thu Jun 04 2020 Stanislav Levin <slev@altlinux.org> 3.11.0-alt1
- 3.10.2 -> 3.11.0.

* Wed Feb 05 2020 Stanislav Levin <slev@altlinux.org> 3.10.2-alt3
- Fixed FTBS.

* Mon Aug 19 2019 Stanislav Levin <slev@altlinux.org> 3.10.2-alt2
- Allowed testing against Pytest5.1+.

* Fri Aug 16 2019 Stanislav Levin <slev@altlinux.org> 3.10.2-alt1
- 3.5.3 -> 3.10.2.
- Enabled testing.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.5.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 3.5.3-alt1
- Version 3.6.3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.4-alt2.git20150128.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 3.0.4-alt2.git20150128
- Rebuild with "def_disable check"
- Cleanup buildreqs

* Wed Jan 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt1.git20150128
- Version 3.0.4

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.git20141108
- Initial build for Sisyphus

