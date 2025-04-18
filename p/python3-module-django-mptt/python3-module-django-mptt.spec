%define pypi_name django-mptt

%def_with check

Name:    python3-module-%pypi_name
Version: 0.17
Release: alt1

Summary: Utilities for implementing a modified pre-order traversal tree in django
License: MIT
Group:   Development/Python3
URL:     https://github.com/django-mptt/django-mptt

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3(hatchling)

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-django-js-asset
BuildRequires: python3-module-model-bakery
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install
%find_lang %name

%check
export DJANGO_SETTINGS_MODULE=settings
export PYTHONPATH=%buildroot%python3_sitelibdir
cd tests
sed -i 's|src="/static/mptt/draggable-admin.js"|/static/mptt/draggable-admin.js"|g' myapp/tests.py
sed -i 's|}" id="draggable-admin-context"></script>|}" id="draggable-admin-context|g' myapp/tests.py
python3 -m django test

%files -f %name.lang
%doc *.rst
%python3_sitelibdir/mptt/
%python3_sitelibdir/django_mptt-%version.0.dist-info/

%changelog
* Wed Apr 16 2025 Alexander Burmatov <thatman@altlinux.org> 0.17-alt1
- New 0.17 version.

* Mon Oct 02 2023 Alexander Burmatov <thatman@altlinux.org> 0.15-alt1
- Initial build for Sisyphus.
