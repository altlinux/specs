%define _unpackaged_files_terminate_build 1

%define oname stone

%def_with check

Name:    python3-module-%oname
Version: 3.3.1
Release: alt1

Summary: The Official API Spec Language for Dropbox API V2
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/stone/

VCS:     https://github.com/dropbox/stone
Source:  python3-module-%oname-%version.tar
Patch0:  stone-3.3.1-alt-fix-pytest-runner.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-mock
BuildRequires: python3-module-ply
BuildRequires: python3-module-pytest
BuildRequires: python3-module-six
%endif

BuildArch: noarch

%description
%summary

%prep
%setup
%patch0

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=$PWD
py.test-3

%files
%doc *.md LICENSE README.rst
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info

%changelog
* Mon Feb 13 2023 Anton Vyatkin <toni@altlinux.org> 3.3.1-alt1
- Initial build for Sisyphus
