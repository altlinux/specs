Name:		python-module-pylibmc
Version:	1.2.3
Release:	alt1
Summary:	Quick and small memcached client for Python
License:	BSD
Group:		Development/Python
URL:		https://pypi.python.org/pypi/pylibmc
Source:		pylibmc-%version.tar.gz

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
* Wed Jul 17 2013 Fr. Br. George <george@altlinux.ru> 1.2.3-alt1
- Initial build from upstream PKG-INFO

