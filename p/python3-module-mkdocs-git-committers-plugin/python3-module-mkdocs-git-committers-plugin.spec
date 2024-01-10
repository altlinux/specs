%define pypi_name mkdocs-git-committers-plugin
%define mod_name mkdocs_git_committers_plugin

Name:    python3-module-%pypi_name
Version: 0.2.3
Release: alt1

Summary: A mkdocs plugin for displaying the last commit and a list of a file's contributors
License: MIT
Group:   Development/Python3
URL:     https://github.com/byrnereese/mkdocs-git-committers-plugin

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
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jan 09 2024 Alexander Burmatov <thatman@altlinux.org> 0.2.3-alt1
- New 0.2.3 version.

* Wed Oct 25 2023 Alexander Burmatov <thatman@altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus.
