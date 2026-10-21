%define pypi_name sanic-cors
%define mod_name sanic_cors

%def_with check

Name:    python3-module-%pypi_name
Version: 2.2.0
Release: alt1

Summary: CORS support extension for Sanic applications
License: MIT
Group:   Development/Python3
URL:     https://github.com/ashleysommer/sanic-cors
VCS:     https://github.com/ashleysommer/sanic-cors

# Fix duplicate route names in tests for Sanic >= 23.3
Patch0: sanic-cors-2.2.0-fix-test-route-names.patch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-sanic
BuildRequires: python3-module-aiofiles
BuildRequires: python3-module-sanic-testing
%endif

BuildArch: noarch

%description
This package has a simple philosophy, when you want to enable CORS, you wish to
enable it for all use cases on a domain. This means no mucking around with
different allowed headers, methods, etc. By default, submission of cookies
across domains is disabled due to the security implications, please see the
documentation for how to enable credential'ed requests, and please make sure
you add some sort of CSRF protection before doing so!

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc LICENSE README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 07 2026 Evgeniy Serov <scala@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus.
