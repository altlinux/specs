%define _unpackaged_files_terminate_build 1
%define pypi_name memray
%def_with check

Name: python3-module-%pypi_name
Version: 1.19.3
Release: alt1

Summary: A memory profiler for Python
License: Apache-2.0
Group: Development/Python3
Url: https://bloomberg.github.io/memray
Vcs: https://github.com/bloomberg/memray.git

Source0: %name-%version.tar
# https://github.com/bloomberg/memray/pull/785
Patch0: 0001-Fix-imports-in-exercise-tests.patch
# https://github.com/bloomberg/memray/pull/787
Patch1: 0002-Fix-assertion-error-in-test.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pkgconfig
BuildRequires: python3-module-cython
BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: liblz4-devel
BuildRequires: libunwind-devel
BuildRequires: libdebuginfod-devel

%if_with check
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-rich
BuildRequires: python3-module-textual
BuildRequires: /dev/pts
BuildRequires: python3-module-greenlet-devel
BuildRequires: python3-module-ipython
BuildRequires: python3-module-pytest-textual-snapshot
%endif

%description
Memray is a memory profiler for Python. It can track memory allocations in
Python code, in native extension modules, and in the Python interpreter itself.
It can generate several different types of reports to help you analyze the
captured memory usage data. While commonly used as a CLI tool, it can also be
used as a library to perform more fine-grained profiling tasks.

%prep
%setup
%autopatch -p1
# Create these files for right imports in test examples.
touch docs/__init__.py
touch docs/tutorials/__init__.py

# Required for update snapshots.
TEXTUAL_VER=$(%__python3 -c "import textual; print(textual.__version__)")
sed -i "s/\"textual\" *: *\"[0-9.]*\"/\"textual\": \"$TEXTUAL_VER\"/" \
  tests/conftest.py


%build
%pyproject_build
# Copy .so files into src/memray that`s required for tests.
%__python3 setup.py build_ext --inplace

%install
%pyproject_install

%check
%pyproject_run_pytest --snapshot-update

%files
%exclude %_bindir/memray3.*
%_bindir/memray
%python3_sitelibdir/memray/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed May 13 2026 Ivan Khanas <xeno@altlinux.org> 1.19.3-alt1
- New version.

* Thu Feb 05 2026 Grigory Ustinov <grenka@altlinux.org> 1.19.1-alt1
- Build new version.

* Sun Jun 29 2025 Ivan Khanas <xeno@altlinux.org> 1.17.2-alt1
- First build for ALT.
