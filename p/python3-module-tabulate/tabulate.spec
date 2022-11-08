%define _unpackaged_files_terminate_build 1
%define pypi_name tabulate

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt1
Summary: Pretty-print tabular data
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tabulate/
VCS: https://github.com/astanin/python-tabulate.git

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(pytest)
%endif

%description
Pretty-print tabular data in Python.

%prep
%setup

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject -- -vra

%files
%doc CHANGELOG README
%_bindir/tabulate
%python3_sitelibdir/tabulate/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Nov 08 2022 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- 0.8.9 -> 0.9.0.

* Mon Feb 14 2022 Stanislav Levin <slev@altlinux.org> 0.8.9-alt1
- 0.8.7 -> 0.8.9 (closes: #41933).

* Fri Oct 16 2020 Stanislav Levin <slev@altlinux.org> 0.8.7-alt1
- 0.7.3 -> 0.8.7.
- Stopped Python2 package build.

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.3-alt2
- Fixed build spec with pytest3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.3-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1
- Initial build for Sisyphus

