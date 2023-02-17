%define _unpackaged_files_terminate_build 1
%define pypi_name python-debian
%define mod_name debian

Name: python3-module-%mod_name
Version: 0.1.49
Release: alt1

Summary: Modules for Debian-related data formats
License: GPLv2+ and GPLv3+
Group: Development/Python3
Url: https://pypi.org/project/python-debian/
VCS: https://salsa.debian.org/python-debian-team/python-debian.git
Source: %name-%version.tar

BuildArch: noarch

# well-known PyPI name
%py3_provides %pypi_name
Provides: python3-module-%pypi_name = %EVR

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
The `debian` Python modules work with Debian-related data formats,
providing a means to read data from files involved in Debian packaging,
and the distribution of Debian packages. The ability to create or edit
the files is also available for some formats.

%prep
%setup

# ship release version
VERSION_FILE='lib/debian/_version.py'
grep -q '__CHANGELOG_VERSION__' "$VERSION_FILE.in" || exit 1
sed -e 's/__CHANGELOG_VERSION__/%version/g' "$VERSION_FILE.in" > "$VERSION_FILE"

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/debian_bundle/
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/deb*.py*
%doc README.rst

%changelog
* Wed Feb 08 2023 Stanislav Levin <slev@altlinux.org> 0.1.49-alt1
- 0.1.36 -> 0.1.49.

* Thu Mar 12 2020 Slava Aseev <ptrnine@altlinux.org> 0.1.36-alt1
- Update to upstream version 0.1.36
- Disable build for python2

* Tue Jan 29 2019 Slava Aseev <ptrnine@altlinux.org> 0.1.34-alt1
- Initial build for ALT
