%define _unpackaged_files_terminate_build 1
%define pypi_name aiothreads
%define module_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.1
Release: alt2

Summary: Glue between async and thread worlds
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/aiothreads/
Vcs: https://github.com/mosquito/aiothreads/
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
aiothreads is a Python library that provides seamless integration
between asyncio and thread-based execution. It offers decorators and
utilities to run synchronous functions and generators in threads while
maintaining clean async/await syntax in your asyncio applications.

While Python 3.9+ provides asyncio.to_thread() for running sync
functions in threads, aiothreads goes far beyond this basic
functionality.

Key Features:
* Zero Dependencies: Pure Python implementation with no external
  dependencies.
* Simple Decorators: Transform sync functions into async-compatible
  versions with @threaded.
* Generator Support: Convert sync generators to async iterators with
  @threaded_iterable.
* Thread Isolation: Run code in separate threads with
  @threaded_separate.
* Async-to-Sync Bridge: Call async code from synchronous threads.
* Context Variable Support: Proper context propagation across thread
  boundaries.
* Method Support: Works with instance methods, class methods, and
  static methods.
* Full Type Safety: Complete typing support with ParamSpec and TypeVar
  for static type checkers.
* Consistent Interface: All decorated functions become objects with
  sync_call, async_call, and __call__ (alias for async_call) methods.

%prep
%setup
%autopatch -p1

# Fix the version in pyproject.toml
sed -i '/^version/s/= .*$/= "%version"/' pyproject.toml
# Remove pytest addopts containing cov options
sed -i '/^addopts = .*/d' pyproject.toml
# Fix mypy type output format: newer mypy omits "builtins." prefix
sed -i \
    -e 's/builtins\\\.int/int/g' \
    -e 's/builtins\\\.str/str/g' \
    -e 's/builtins\\\.bool/bool/g' \
    -e 's/builtins\\\.float/float/g' \
    tests/test_type_checking.yml

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Apr 15 2026 Maxim Tulskiy <tulskijms@altlinux.org> 1.1.1-alt2
- Fixed type checking tests for newer mypy output (strip builtins. prefix).

* Tue Mar 10 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.1.1-alt1
- Updated to 1.1.1.

* Tue Mar 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.1.0-alt1
- Initial build for ALT Sisyphus.
