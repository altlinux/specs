%define pypi_name editor

%def_with check

Name:    python3-module-%pypi_name
Version: 1.6.6
Release: alt1

Summary: Open the default text editor
License: MIT
Group:   Development/Python3
URL:     https://github.com/rec/editor

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-tdir
BuildRequires: python3-module-runs
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Editor opens the default text editor or your favorite editor to edit an existing
file, a new file, or a tempfile, blocks while the user edits text, then returns
the contents of the file.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Aug 09 2024 Alexander Burmatov <thatman@altlinux.org> 1.6.6-alt1
- Initial build for Sisyphus.
