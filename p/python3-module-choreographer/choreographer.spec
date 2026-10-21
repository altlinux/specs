%define _unpackaged_files_terminate_build 1
%define pypi_name choreographer
%def_with check

Name: python3-module-%pypi_name
Version: 1.4.0
Release: alt1

Summary: Browser remote control library for Python
License: MIT
Group: Development/Python3
Url: https://github.com/plotly/choreographer
Vcs: https://github.com/plotly/choreographer.git

BuildArch: noarch

Source:  %pypi_name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %{pypi_name}-%{version}-alt-set-starting-version.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
# poethepoet is a task runner, pytest-xdist is unused,
# typing-extensions is needed only for Python < 3.11
%add_pyproject_deps_check_filter 'poethepoet$' 'pytest-xdist$' 'typing-extensions$'
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Choreographer allows remote control of browsers from Python. It was
created to support image generation from browser-based charting tools,
but can be used for other purposes as well. Supports Chromium-based
browsers.

%package -n %pypi_name-tools
Summary: Diagnostic tool for %pypi_name
Group: Development/Tools
Requires: %name = %EVR

%description -n %pypi_name-tools
%summary.

%prep
%setup -q -n %pypi_name-%version
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install
# drop chrome downloader
rm %buildroot%_bindir/choreo_get_chrome
rm %buildroot%python3_sitelibdir/choreographer/resources/last_known_good_chrome.json

%check
# require running chromium
%pyproject_run_pytest tests \
    --deselect tests/test_browser_search.py::test_canary \
    --ignore=tests/test_process.py \
    --ignore=tests/test_browser.py \
    --ignore=tests/test_chunking.py \
    --ignore=tests/test_devtools_async_helpers.py \
    --ignore=tests/test_placeholder.py \
    --ignore=tests/test_session.py \
    --ignore=tests/test_tab.py

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%pypi_name-%version.dist-info/
%doc README.md LICENSE.md

%files -n %pypi_name-tools
%_bindir/choreo_diagnose

%changelog
* Tue Oct 20 2026 Mikhail Nogin <joycap@altlinux.org> 1.4.0-alt1
- Initial build for ALT Sisyphus.
