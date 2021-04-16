%define _unpackaged_files_terminate_build 1

%define oname unyt

Name: python3-module-%oname
Version: 2.8.0
Release: alt1
Summary: Handle, manipulate, and convert data with units in Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/yt-project/unyt

BuildArch: noarch

# https://github.com/yt-project/unyt.git
Source: %name-%version.tar

Patch1: %oname-alt-test-import.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(numpy) python3(sympy)

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
%patch1 -p1

sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: v%version\)\"/" \
	./%oname/_version.py

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE
%doc AUTHORS.rst CONTRIBUTING.rst HISTORY.rst README.rst
%python3_sitelibdir/%oname
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/testing.py
%exclude %python3_sitelibdir/%oname/__pycache__/testing.*
%python3_sitelibdir/%oname-%version-py*.egg-info

%files tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/testing.py
%python3_sitelibdir/%oname/__pycache__/testing.*

%changelog
* Tue Apr 20 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.0-alt1
- Initial build for ALT.
