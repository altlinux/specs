%define  modulename async_generator

Name:    python3-module-%modulename
Version: 1.10
Release: alt1

Summary: Making it easy to write async iterators in Python 3.5
License: MIT or Apache 2.0
Group:   Development/Python3
URL:     https://github.com/python-trio/async_generator

Packager: Evgeny Sinelnikov <sin@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Python 3.6 added async generators. (What's an async generator?
Check out my 5-minute lightning talk demo from PyCon 2016.)

Python 3.7 adds some more tools to make them usable,
like contextlib.asynccontextmanager.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md *.rst

%changelog
* Tue Jan 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.10-alt1
- Initial build for Sisyphus
