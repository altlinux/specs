%define pypi_name django-stubs
%define ext_name django_stubs_ext

# The tests take too long
%def_without check

Name:    python3-module-%pypi_name
Version: 5.1.1
Release: alt1

Summary: PEP-484 stubs for Django
License: MIT
Group:   Development/Python3
URL:     https://github.com/typeddjango/django-stubs

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-django
BuildRequires: python3-module-mypy
BuildRequires: python3-module-pytest-mypy-plugins
BuildRequires: python3-module-tomli
BuildRequires: python3-module-pytest-shard
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
This package contains type stubs and a custom mypy plugin to provide more
precise static types and type inference for Django framework. Django uses some
Python "magic" that makes having precise types for some code patterns
problematic. This is why we need this project. The final goal is to be able to
get precise types for most common patterns.

%package -n python3-module-%pypi_name-ext
Summary: This package contains extensions and monkey-patching functions for the django-stubs package
Group: Development/Python3

%description -n python3-module-%pypi_name-ext
This package contains extensions and monkey-patching functions for the
django-stubs package. Certain features of django-stubs (i.e. generic django
classes that don't define the __class_getitem__ method) require runtime
monkey-patching, which can't be done with type stubs. These extensions were
split into a separate package so library consumers don't need mypy as a runtime
dependency.

%prep
%setup -n %pypi_name-%version

%build
pushd ext
%pyproject_build
popd
%pyproject_build

%install
pushd ext
%pyproject_install
popd
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd ext
%pyproject_run_pytest
popd
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/mypy_django_plugin/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files -n python3-module-%pypi_name-ext
%doc *.md
%python3_sitelibdir/%ext_name/
%python3_sitelibdir/%{pyproject_distinfo %ext_name}

%changelog
* Fri Nov 08 2024 Alexander Burmatov <thatman@altlinux.org> 5.1.1-alt1
- Initial build for Sisyphus.
