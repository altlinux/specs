%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-datadir

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.1
Release: alt1

Summary: pytest plugin for manipulating test data directories and files
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-datadir/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(setuptools-scm)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%py3_provides %pypi_name

%description
pytest plugin for manipulating test data directories and files.

%prep
%setup
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

# remove wrong-installed file
rm %buildroot%_usr/LICENSE

%check
%tox_check_pyproject

%files
%doc LICENSE README.md AUTHORS
%python3_sitelibdir/pytest_datadir/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 1.3.1-alt1
- initial build for Sisyphus

