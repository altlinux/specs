%define _unpackaged_files_terminate_build 1
%define pypi_name httptools
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.6.4
Release: alt1
Summary: A collection of framework independent HTTP protocol utils
License: MIT
Group: Development/Python
Url: https://pypi.org/project/httptools/
Vcs: https://github.com/MagicStack/httptools
Source0: %name-%version.tar
Source1: modules.tar
Source2: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: libhttp-parser-devel
%if_with check
%pyproject_builddeps_metadata
%endif

%description
%summary

%prep
%setup -a1
# use system http-parser and vendored llhttp (not packaged yet)
rm -r vendor/http-parser
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build --backend-config-settings='{"--build-option": ["build_ext", "--cython-always", "--use-system-http-parser"]}'

%install
%pyproject_install
# remove Cython dev files
rm -v %buildroot%python3_sitelibdir/%mod_name/parser/*.{pyx,pxd}

%check
# .github/workflows/tests.yml
%pyproject_run -- bash -s <<-'ENDTESTS'
set -eux
mkdir empty
cd empty
python -m unittest discover -v ../tests
ENDTESTS

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 22 2024 Stanislav Levin <slev@altlinux.org> 0.6.4-alt1
- 0.1.1 -> 0.6.4.

* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.1-alt1
- initial
