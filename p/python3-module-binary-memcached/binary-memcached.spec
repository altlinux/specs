%define  oname binary-memcached

%def_without check

Name:    python3-module-%oname
Version: 0.31.2
Release: alt1

Summary: A pure python module (thread safe) to access memcached via it's binary protocol with SASL auth support.

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/python-binary-memcached

# https://github.com/jaysonsantos/python-binary-memcached
Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-m2r2

%if_with check
BuildRequires: python3-module-uhashring
BuildRequires: python3-module-trustme
BuildRequires: python3-module-six
%endif

BuildArch: noarch

%description
A pure python module (thread safe) to access memcached via it's binary with SASL
auth support.

The main purpose of this module it to be able to communicate with memcached using
binary protocol and support authentication, so it can work with Heroku for example.

%prep
%setup

# https://github.com/jaysonsantos/python-binary-memcached/issues/249
sed -i 's/m2r/m2r2/' setup.py

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/bmemcached
%python3_sitelibdir/python_binary_memcached-%version.dist-info

%changelog
* Mon Dec 19 2022 Grigory Ustinov <grenka@altlinux.org> 0.31.2-alt1
- Automatically updated to 0.31.2.

* Wed Oct 12 2022 Grigory Ustinov <grenka@altlinux.org> 0.31.1-alt1
- Initial build for Sisyphus.
