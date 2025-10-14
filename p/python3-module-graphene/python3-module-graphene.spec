%define pypi_name graphene

%def_with check

Name:    python3-module-%pypi_name
Version: 3.4.3
Release: alt1

Summary: GraphQL framework for Python
License: MIT
Group:   Development/Python3
URL:     https://github.com/graphql-python/graphene

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-graphql-core
BuildRequires: python3-module-graphql-relay
BuildRequires: python3-module-pytest-snapshot
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-benchmark
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-typing_extensions
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version
# Fixing warnings in tests
sed -i "s/setup(/setup_method(/" graphene/relay/tests/*.py

%build
%pyproject_build

%install
%pyproject_install
rm -fr %python3_sitelibdir_noarch/%pypi_name/test
rm -fr %python3_sitelibdir_noarch/%pypi_name/tests
rm -fr %python3_sitelibdir_noarch/%pypi_name/relay/tests
rm -fr %python3_sitelibdir_noarch/%pypi_name/types/tests
rm -fr %python3_sitelibdir_noarch/%pypi_name/utils/tests
rm -fr %python3_sitelibdir_noarch/%pypi_name/validation/tests

%check
%pyproject_run_pytest graphene

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Oct 13 2025 Alexander Burmatov <thatman@altlinux.org> 3.4.3-alt1
- New 3.4.3 version.

* Thu Oct 05 2023 Alexander Burmatov <thatman@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus.
