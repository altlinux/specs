%define pypi_name django-cors-headers

# need tox >= 4.2
%def_without check

Name:    python3-module-%pypi_name
Version: 4.3.1
Release: alt1

Summary: Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS)
License: MIT
Group:   Development/Python3
URL:     https://github.com/adamchainz/django-cors-headers

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3(django)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses.
This allows in-browser requests to your Django application from other origins.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir_noarch/corsheaders/
%python3_sitelibdir_noarch/*.dist-info/

%check
#%%tox_create_default_config
%tox_check_pyproject -- -m "not internet"

%changelog
* Tue Dec 12 2023 Alexander Burmatov <thatman@altlinux.org> 4.3.1-alt1
- Update version to 4.3.1.

* Tue Sep 26 2023 Alexander Burmatov <thatman@altlinux.org> 4.2.0-alt1
- Initial build for Sisyphus.
