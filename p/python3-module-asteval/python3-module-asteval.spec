%define pypi_name asteval

%def_with check

Name:    python3-module-%pypi_name
Version: 1.0.6
Release: alt1

Summary: Minimalistic evaluator of python expression using ast module
License: MIT
Group:   Development/Python3
URL:     https://lmfit.github.io/asteval
VCS:     https://github.com/lmfit/asteval

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildREquires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest-cov
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
ASTEVAL is a safe(ish) evaluator of Python expressions and statements, using
Python's ast module. The idea is to provide a simple, safe, and robust miniature
mathematical language that can handle user input. The emphasis here is on
mathematical expressions so that many functions from numpy are imported and used
if available.

Many Python language constructs are supported by default, These include slicing,
subscripting, list comprehension, conditionals (if-elif-else blocks and if
expressions), flow control (for loops, while loops, and try-except-finally
blocks). All data are Python objects and built-in data structures (dictionaries,
tuples, lists, Numpy arrays, strings) are fully supported by default.

Many of the standard built-in Python functions are available, as are all
mathematical functions from the math module. If the Numpy module is installed,
many of its functions will also be available. Users can define and run their own
functions within the confines of the limitations of Asteval.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc LICENSE README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Oct 03 2026 Evgeniy Serov <scala@altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus.
