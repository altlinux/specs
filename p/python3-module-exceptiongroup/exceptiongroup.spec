%define _unpackaged_files_terminate_build 1
%define pypi_name exceptiongroup

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.1
Release: alt1

Summary: Backport of PEP 654 (exception groups)
License: MIT
Group: Development/Python3
VCS: https://github.com/agronholm/exceptiongroup
Url: https://pypi.org/project/exceptiongroup

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(flit_scm)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%py3_provides %pypi_name

%description
Backport of PEP 654 (exception groups)

%prep
%setup
%autopatch -p1

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM. These files will be packaged unless filtered by MANIFEST.in.
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

%check
%tox_check_pyproject -- -vra

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Nov 10 2022 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
