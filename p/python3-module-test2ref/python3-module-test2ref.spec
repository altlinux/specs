%define modname test2ref

%def_enable check

Name: python3-module-%modname
Version: 1.1.1
Release: alt1

Summary: Testing Against Learned Reference Data

License: MIT
Group: Development/Python3
Url: https://test2ref.readthedocs.io
VCS: https://github.com/nbiotcloud/test2ref

# Source-url: https://github.com/nbiotcloud/test2ref/archive/%version/%modname-%version.tar.gz
Source: %modname-%version.tar
Patch: %modname-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-wheel python3-module-pdm python3-module-pdm-backend
%if_enabled check
BuildRequires: python3-module-pytest-cov python3-module-binaryornot
%endif

%description
%summary.

%prep
%setup -n %modname-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%if_enabled check
%check
%pyproject_run_pytest
%endif

%files
%doc docs README.md LICENSE CONTRIBUTING.md
%python3_sitelibdir_noarch/%{modname}*

%changelog
* Thu Nov 06 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.1-alt1
- Initial build for ALT Sisyphus (for anytree tests).
