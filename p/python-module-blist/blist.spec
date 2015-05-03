%def_with python3

Name: python-module-blist
Version: 1.3.6
Release: alt1
Summary: A list-like type with better asymptotic performance and similar performance on small lists
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/blist/
%setup_python_module blist
Source: blist-%version.tar.gz

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

# Automatically added by buildreq on Sun May 03 2015
# optimized out: libcloog-isl4 python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-dev python3-module-pytest

BuildRequires: python-module-setuptools-tests
%if_with python3
BuildRequires: python3-module-setuptools-tests
%endif

%description
The blist is a drop-in replacement for the Python list that provides
better performance when modifying large lists. The blist package also
provides sortedlist, sortedset, weaksortedlist, weaksortedset,
sorteddict, and btuple types.

%package -n python3-module-%modulename
Summary: %summary
Group: Development/Python3

%description -n python3-module-%modulename
The blist is a drop-in replacement for the Python list that provides
better performance when modifying large lists. The blist package also
provides sortedlist, sortedset, weaksortedlist, weaksortedset,
sorteddict, and btuple types.

%prep
%setup -n %modulename-%version
sed -i '/ez_setup/d' setup.py

%build
%python_build
%python3_build

%install
%python_install
%python3_install

%files
%doc README.rst
%python_sitelibdir/*%{modulename}*

%if_with python3
%files -n python3-module-%modulename
%doc README.rst
%python3_sitelibdir/*%{modulename}*
%endif

%check
python setup.py test
python3 setup.py test

%changelog
* Sun May 03 2015 Fr. Br. George <george@altlinux.ru> 1.3.6-alt1
- Autobuild version bump to 1.3.6

* Sun May 03 2015 Fr. Br. George <george@altlinux.ru> 1.3.5-alt1
- Initial build for ALT

