%define pypi_name mkdocs-d2-plugin

Name:    python3-module-%pypi_name
Version: 1.5.0
Release: alt1

Summary: A plugin for embedding D2 diagrams in MkDocs
License: MIT
Group:   Development/Python3
URL:     https://github.com/landmaj/mkdocs-d2-plugin

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

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

%files
%doc *.md
%python3_sitelibdir/d2/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 11 2024 Alexander Burmatov <thatman@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus.
