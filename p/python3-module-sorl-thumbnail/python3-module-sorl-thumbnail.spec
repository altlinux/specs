%define pypi_name sorl-thumbnail
%define mod_name sorl

# Disabled due to an improper configuration error when tested against django
%def_without check

Name:    python3-module-%pypi_name
Version: 12.11.0
Release: alt1

Summary: Thumbnails for Django
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/jazzband/sorl-thumbnail

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
# Deprecated
%add_python3_req_skip boto
%add_python3_req_skip boto.dynamodb2.table
%add_python3_req_skip wand

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-Pillow
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

%check
%pyproject_run_unittest

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/sorl_thumbnail-0.0.0.dist-info/

%changelog
* Wed Sep 03 2025 Alexander Burmatov <thatman@altlinux.org> 12.11.0-alt1
- Initial build for Sisyphus.
