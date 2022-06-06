%define  modulename RxPY

Name:    python3-module-rx
Version: 3.2.0
Release: alt1

Summary: ReactiveX for Python
License: MIT
Group:   Development/Python3
URL:     https://github.com/ReactiveX/RxPY

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
A library for composing asynchronous and event-based programs using observable
collections and query operator functions in Python.

%prep
%setup -n %modulename-%version

%build
#echo "import setuptools; setuptools.setup(name='reactivex',version='%version',packages=['reactivex'],)" > setup.py
%python3_build

%install
%python3_install

%files
%doc README.rst authors.txt changes.md
%python3_sitelibdir/rx
%python3_sitelibdir/*.egg-info

%changelog
* Mon Jun 06 2022 Andrey Cherepanov <cas@altlinux.org> 3.2.0-alt1
- Initial build for Sisyphus.
