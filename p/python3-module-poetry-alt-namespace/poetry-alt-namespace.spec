%define _unpackaged_files_terminate_build 1

# The purpose of this package is the ownership of xxx/site-packages/poetry/
# namespace root directories. Other poetry packages will be installed on those
# paths, but the packages can't own the root paths.

Name: python3-module-poetry-alt-namespace
Version: 0.0.1
Release: alt1

Summary: Namespace package for poetry
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/poetry

BuildRequires(pre): rpm-macros-python3

# file conflicts on root poetry directory, poetry-core was a previous owner
Conflicts: python3-module-poetry-core <= 1.0.8-alt1

%py3_provides poetry

%description
%summary.

%prep

%build

%install
# Note: implicit namespace package can't contain __init__.py in namespace root
mkdir -p -m0755 %buildroot%python3_sitelibdir/poetry/
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
mkdir -p -m0755 %buildroot%python3_sitelibdir_noarch/poetry/
%endif

%files
%python3_sitelibdir/poetry/
# for fixing: warning: File listed twice
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
%python3_sitelibdir_noarch/poetry/
%endif

%changelog
* Tue Sep 13 2022 Stanislav Levin <slev@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus.
