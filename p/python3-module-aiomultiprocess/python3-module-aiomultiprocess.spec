%define pypi_name aiomultiprocess

%def_with check

Name:    python3-module-%pypi_name
Version: 0.9.1
Release: alt1

Summary: Take a modern Python codebase to the next level of performance
License: MIT
Group:   Development/Python3
URL:     https://aiomultiprocess.omnilib.dev/
VCS:     https://github.com/omnilib/aiomultiprocess

Patch0: aiomultiprocess-tests-asyncio-run.patch
Patch1: aiomultiprocess-tests-pickling-error.patch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-flit

BuildArch: noarch

Source: %name-%version.tar

%description
Take a modern Python codebase to the next level of performance.

On their own, AsyncIO and multiprocessing are useful, but limited: AsyncIO still
can't exceed the speed of GIL, and multiprocessing only works on one task at a
time. But together, they can fully realize their true potential.

aiomultiprocess presents a simple interface, while running a full AsyncIO event
loop on each child process, enabling levels of concurrency never before seen in
a Python application. Each child process can execute multiple coroutines at
once, limited only by the workload and number of cores available.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

# don't package upstream tests
rm -r %buildroot%python3_sitelibdir/%pypi_name/tests

%check
%pyproject_run_pytest -v aiomultiprocess/tests/__init__.py

%files
%doc LICENSE *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Oct 03 2026 Evgeniy Serov <scala@altlinux.org> 0.9.1-alt1
- Initial build for Sisyphus.
