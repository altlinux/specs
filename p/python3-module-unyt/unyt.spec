%define _unpackaged_files_terminate_build 1

%define oname unyt

%def_with check

Name: python3-module-%oname
Version: 2.9.4
Release: alt1
Summary: Handle, manipulate, and convert data with units in Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/unyt/
VCS: https://github.com/yt-project/unyt

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
# dependencies
BuildRequires: python3(numpy)
BuildRequires: python3(sympy)

# tests
BuildRequires: python3(h5py)
BuildRequires: python3(packaging)
BuildRequires: python3(pytest)
BuildRequires: python3(numpy.testing)
BuildRequires: python3(matplotlib)
%endif

%description
A package for handling numpy arrays with units.

Often writing code that deals with data that has units can be confusing.
A function might return an array but at least with plain NumPy arrays,
there is no way to easily tell what the units of the data are
without somehow knowing a priori.

%package tests
Summary: Handle, manipulate, and convert data with units in Python
Group: Development/Python3
Requires: %name = %EVR

%description tests
A package for handling numpy arrays with units.

Often writing code that deals with data that has units can be confusing.
A function might return an array but at least with plain NumPy arrays,
there is no way to easily tell what the units of the data are
without somehow knowing a priori.

This package contains tests.

%prep
%setup

sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: v%version\)\"/" \
	./%oname/_version.py

# if build from git source tree
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM. These files will be packaged unless filtered by MANIFEST.in.
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
%pyproject_run_pytest -ra unyt/tests/

%files
%doc HISTORY.rst README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}/
%python3_sitelibdir/%oname/testing.py
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Thu Feb 09 2023 Stanislav Levin <slev@altlinux.org> 2.9.4-alt1
- 2.8.0 -> 2.9.4.

* Tue Apr 20 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.0-alt1
- Initial build for ALT.
