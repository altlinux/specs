%define _unpackaged_files_terminate_build 1

# The purpose of this package is the ownership of xxx/site-packages/pdm/
# namespace root directories. Other pdm packages will be installed on those
# paths, but the packages can't own the root paths.

Name: python3-module-pdm-alt-namespace
Version: 0.0.1
Release: alt1

Summary: Namespace package for pdm
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pdm

BuildRequires(pre): rpm-macros-python3

%py3_provides pdm

%description
%summary.

%prep

%build

%install
# Note: implicit namespace package can't contain __init__.py in namespace root
mkdir -p -m0755 %buildroot%python3_sitelibdir/pdm/
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
mkdir -p -m0755 %buildroot%python3_sitelibdir_noarch/pdm/
%endif

%files
%python3_sitelibdir/pdm/
# for fixing: warning: File listed twice
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
%python3_sitelibdir_noarch/pdm/
%endif

%changelog
* Tue Sep 13 2022 Stanislav Levin <slev@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus.
