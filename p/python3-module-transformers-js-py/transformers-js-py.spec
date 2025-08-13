%define _unpackaged_files_terminate_build 1
%define modulename transformers-js-py
%define pypi_name transformers_js_py
%define mod_name transformers_js

%def_with check

Name: python3-module-%modulename
Version: 0.19.1
Release: alt1
Summary: Use Transformers.js on Pyodide and Pyodide-based frameworks.
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/whitphx/transformers.js.py
Vcs: https://pypi.org/project/transformers-js-py/

BuildArch: noarch 

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(hatchling)
BuildRequires: python3-module-hatch-vcs
BuildRequires: python3-module-discord

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name
%add_python3_req_skip js
%add_python3_req_skip pyodide
%add_python3_req_skip pyodide.code
%add_python3_req_skip pyodide.ffi
%add_python3_req_skip pyodide.webloop

%description
%summary 

%package -n python3-module-%mod_name
Summary: python3-module-%mod_name for frameworks
Group: Development/Python3

%description -n python3-module-%mod_name
Files for js with python3-module-%mod_name.

%prep
%setup
%autopatch -p1
sed -ri 's/^[[:space:]]*dynamic[[:space:]]*=[[:space:]]*\[.*"version".*\]/version = "%{version}"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
#pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n python3-module-%mod_name
%python3_sitelibdir/%mod_name/


%changelog
* Sat Aug 09 2025 Pavel Shilov <zerospirit@altlinux.org> 0.19.1-alt1
- Initial build for Sisyphus.