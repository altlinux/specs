%define _unpackaged_files_terminate_build 1
%define pypi_name flit-scm

%define tomli %(%__python3 -c 'import sys;print(int(sys.version_info < (3, 11)))')

Name: python3-module-%pypi_name
Version: 1.7.0
Release: alt1

Summary: Flit build backend for SCM
License: MIT
Group: Development/Python3
VCS: https://gitlab.com/WillDaSilva/flit_scm.git
Url: https://pypi.org/project/flit-scm

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(flit-core)
BuildRequires: python3(setuptools_scm)
%if %tomli
BuildRequires: python3(tomli)
%endif

BuildArch: noarch

%py3_provides %pypi_name
%if %tomli
%py3_requires tomli
%endif

%description
A PEP 518 build backend that uses setuptools_scm to generate a version file from
your version control system, then flit to build the package.

%prep
%setup
%autopatch -p1

# flit-scm relies on setuptools-scm that implements a file_finders entry point
# which returns all files tracked by SCM. These files will be packaged unless
# filtered by MANIFEST.in.
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
# no tests suite

%files
%doc README.md
%python3_sitelibdir/flit_scm/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Oct 25 2022 Stanislav Levin <slev@altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus.
