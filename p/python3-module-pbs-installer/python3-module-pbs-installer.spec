%define pypi_name pbs-installer
%define mod_name pbs_installer
%define short_version 2026.4.7

Name:    python3-module-%pypi_name
Version: 2026.04.07
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
%python3_sitelibdir/%mod_name-%short_version.dist-info

%changelog
* Wed Apr 15 2026 Alexander Burmatov <thatman@altlinux.org> 2026.04.07-alt1
- New 2026.04.07 version.

* Thu Dec 19 2024 Alexander Burmatov <thatman@altlinux.org> 2024.10.16-alt1
- Initial build for Sisyphus.
