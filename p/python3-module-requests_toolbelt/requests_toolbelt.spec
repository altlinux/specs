%define oname requests_toolbelt

%def_disable check

Name: python3-module-%oname
Version: 0.9.1
Release: alt2
Summary: A toolbelt of useful classes and functions to be used with python-module-requests
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/requests-toolbelt

# https://github.com/requests/toolbelt.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-requests

%py3_provides %oname

%description
This is just a collection of utilities for python-requests,
but don't really belong in requests proper.
The minimum tested requests version is 2.1.0.
In reality, the toolbelt should work with 2.0.1 as well,
but some idiosyncracies prevent effective or sane testing on that version.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=$PWD
python3 setup.py test
py.test3

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/*

%changelog
* Tue Jul 13 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.1-alt2
- Drop python2 support.

* Sun Sep 22 2019 Anton Farygin <rider@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.0-alt1
- Initial build for ALT.
