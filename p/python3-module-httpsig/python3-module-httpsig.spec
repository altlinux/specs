%define _unpackaged_files_terminate_build 1
%define pypi_name httpsig
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt2

Summary: HTTP request signing using the HTTP Signature draft specification
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/httpsig/
VCS: https://github.com/ahknight/httpsig

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3-module-pycryptodome
BuildRequires: python3(six)
%endif

BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

%description
Sign HTTP requests with secure signatures according to the IETF HTTP Signatures
specification (Draft 8). This is a fork of the original module to fully support
both RSA and HMAC schemes as well as unit test both schemes to prove they work.

%summary
Components for Joyent's HTTP Signature Scheme.

%prep
%setup
# if build from git source tree
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
%pyproject_run_unittest httpsig.tests

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Feb 08 2023 Stanislav Levin <slev@altlinux.org> 1.3.0-alt2
- Fixed FTBFS (setuptools 66).

* Mon May 16 2022 Andrey Bergman <vkni@altlinux.org> 1.3.0-alt1
- Initial release for Sisyphus.

