%define pypi_name pbs-installer
%define mod_name pbs_installer

Name:    python3-module-%pypi_name
Version: 2024.10.16
Release: alt1

Summary: An installer for python-build-standalone
License: MIT
Group:   Development/Python3
URL:     https://github.com/frostming/pbs-installer

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm python3-module-wheel
BuildRequires: python3-module-pdm
BuildRequires: python3-module-pdm-backend

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%_bindir/pbs-install
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Dec 19 2024 Alexander Burmatov <thatman@altlinux.org> 2024.10.16-alt1
- Initial build for Sisyphus.
