%define _unpackaged_files_terminate_build 1

%define ns_root svg

# The purpose of this package is the ownership of xxx/site-packages/%ns_root/
# namespace root directories. Other %ns_root packages will be installed on those
# paths, but the packages can't own the root paths.

Name: python3-module-%ns_root-alt-namespace
Version: 0.0.1
Release: alt1
Summary: ALT Namespace package for %ns_root
License: MIT
Group: Development/Python3
Url: https://git.altlinux.org/gears/p/python3-module-%ns_root-alt-namespace.git
BuildRequires(pre): rpm-macros-python3
%py3_provides %ns_root
Provides: python3-module-svg = %EVR
Obsoletes: python3-module-svg <= 6.1-alt4

%description
%summary.

%prep

%build

%install
# Note: implicit namespace package can't contain __init__.py in namespace root
mkdir -p -m0755 %buildroot%python3_sitelibdir/%ns_root/
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
mkdir -p -m0755 %buildroot%python3_sitelibdir_noarch/%ns_root/
%endif

%files
%python3_sitelibdir/%ns_root/
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
%python3_sitelibdir_noarch/%ns_root/
%endif

%changelog
* Thu Oct 17 2024 Stanislav Levin <slev@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus.
