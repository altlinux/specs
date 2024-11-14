%define pypi_name mkdocs-macros-plugin
%define mod_name mkdocs_macros

%def_without check

Name:    python3-module-%pypi_name
Version: 1.3.7
Release: alt1

Summary: Create richer and more beautiful pages in MkDocs, by using variables and calls to macros in the markdown code
License: MIT
Group:   Development/Python3
URL:     https://github.com/fralau/mkdocs-macros-plugin

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-hjson
BuildRequires: python3-module-pyaml
BuildRequires: python3-module-super-collections
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-mkdocs-test
BuildRequires: python3-module-mkdocs-material
BuildRequires: python3-module-mkdocs-d2-plugin
BuildRequires: python3-module-termcolor
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-pathspec
BuildRequires: python3-module-mkdocs-include-markdown-plugin
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version
sed -i 's/subprocess.CalledProcessError/FileNotFoundError/' test/plugin_d2/test_t2.py

%build
%pyproject_build

%install
%pyproject_install
rm -fr %buildroot%python3_sitelibdir/test

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 11 2024 Alexander Burmatov <thatman@altlinux.org> 1.3.7-alt1
- Initial build for Sisyphus.
