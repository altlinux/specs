%define  modulename cppy

Name:    python3-module-%modulename
Version: 1.2.1
Release: alt1

Summary: A collection of C++ headers which make it easier to write Python C extension modules
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/nucleic/cppy

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3(setuptools_scm)

BuildArch: noarch

Source:  %modulename-%version.tar

%description
A small C++ header library which makes it easier to write Python
extension modules. The primary feature is a PyObject smart pointer which
automatically handles reference counting and provides convenience
methods for performing common object operations.

%prep
%setup -n %modulename-%version

# if build from git source tree
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM. These files will be packaged unless filtered by MANIFEST.in.
git init
git config user.email author@example.com
git config user.name author
git add .
git commit -m 'release'
git tag '%version'

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version-py%_python3_version.egg-info/

%changelog
* Thu Apr 07 2022 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- New version.

* Sat Mar 12 2022 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version.

* Fri Mar 27 2020 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
