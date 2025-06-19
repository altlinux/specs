%define _unpackaged_files_terminate_build 1
%define pypi_name multiprocess

%def_with check
%def_with docs

Name: python3-module-%pypi_name
Version: 0.70.18
Release: alt1

Summary: better multiprocessing and multithreading in Python
License: BSD-3-Clause
Group: Development/Tools
Url: https://pypi.org/project/multiprocess
Vcs: https://github.com/uqfoundation/multiprocess
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%if_with docs
BuildRequires: python3-module-sphinx
%endif
%if_with check
BuildRequires: python3-module-dill
BuildRequires: python3-test
BuildRequires: python3-module-pytest
%endif

%filter_from_requires /python3(msvcrt)/d
%filter_from_requires /python3(_winapi)/d

%description
multiprocess is a fork of multiprocessing.
multiprocess extends multiprocessing to provide
enhanced serialization, using dill.
multiprocess leverages multiprocessing to support
the spawning of processes using the API
of the Python standard library's threading module.

%prep
%setup

%build
%pyproject_build
%if_with docs
export PYTHONPATH="%_builddir/%name-%version/build/lib:$PYTHONPATH"
%make -C docs html
%endif

%install
%pyproject_install

%check
pyver=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
%pyproject_run_pytest --import-mode=importlib py$pyver

%files
%doc LICENSE README.md
%if_with docs
%doc docs/build/*
%endif
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/_%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jun 19 2025 Dmitry Mikhalchenko <tascad@altlinux.org> 0.70.18-alt1
- Initial build for ALT Sisyphus.
