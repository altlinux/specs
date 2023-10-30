%define pypi_name mkdocs-minify-plugin
%define mod_name mkdocs_minify_plugin

%def_without check

Name:    python3-module-%pypi_name
Version: 0.7.1
Release: alt1

Summary: A mkdocs plugin to minify the HTML of a page before it is written to disk
License: MIT
Group:   Development/Python3
URL:     https://github.com/byrnereese/mkdocs-minify-plugin

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-csscompressor
BuildRequires: python3-module-htmlmin
BuildRequires: python3-module-jsmin
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
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 25 2023 Alexander Burmatov <thatman@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus.
