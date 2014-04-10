Name: python-module-pylibmc
Version: 1.3.0
Release: alt1
Summary: Quick and small memcached client for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pylibmc
Source: pylibmc-%version.tar.gz

%setup_python_module pylibmc

# Automatically added by buildreq on Wed Jul 17 2013
# optimized out: python-base python-modules python-modules-compiler python-modules-email
BuildRequires: libmemcached-devel python-devel zlib-devel

%description
Pylibmc is a Python client for memcached (<http://memcached.org/>)
written in C.

%prep
%setup -n pylibmc-%version

%build
%python_build

%install
%python_install

%files
%doc README.rst docs
%python_sitelibdir/*pylibmc*

%changelog
* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 1.3.0-alt1
- Autobuild version bump to 1.3.0

* Wed Jul 17 2013 Fr. Br. George <george@altlinux.ru> 1.2.3-alt1
- Initial build from upstream PKG-INFO

