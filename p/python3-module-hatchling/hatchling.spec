%define _unpackaged_files_terminate_build 1
%define pypi_name hatchling
%define wheel_dir %_builddir/dist

Name: python3-module-%pypi_name
Version: 0.22.0
Release: alt1

Summary: Modern, extensible Python build backend
License: MIT
Group: Development/Python3
# Source-git: https://github.com/ofek/hatch.git
Url: https://pypi.org/project/hatchling

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3

# build frontend
BuildRequires: python3(build)

# installer
BuildRequires: python3(installer)

# runtime deps which should be removed from BRs,
# required due to build from PKG-INFO
BuildRequires: python3(editables)
BuildRequires: python3(pathspec)
BuildRequires: python3(pluggy)

BuildArch: noarch

# try-except import
%py3_requires editables

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%__python3 -m build --no-isolation --outdir %wheel_dir .

%install
%__python3 -m installer --destdir %buildroot %wheel_dir/%pypi_name-%version-*.whl

%check
# Requires Internet, see tests/downstream/integrate.py

%files
%doc README.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.22.0-alt1
- Initial build for Sisyphus.
