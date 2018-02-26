%define version svn20080222
%define release alt3

%define oname decimal-c
%setup_python_module %oname

Summary: An attempt to rewrite the decimal module in C
Name: python-module-%oname
Version: %version
Release: %release.1
Source: %modulename-%version.tar.bz2
License: GPL
Group: Development/Python
Url: http://svn.python.org/projects/sandbox/branches/jim-fix-setuptools-cli/decimal-c/
Packager: Python Development Team <python at packages.altlinux.org>

# Automatically added by buildreq on Fri Feb 22 2008
BuildRequires: python-devel

%description
The decimal-c branch is an attempt to rewrite the decimal module in C

_decimal builds as a regular stand-alone python extension module
decimal.py and test_decimal.py are copies from the 2.5 trunk

At the beginning decimal was meant to inherit from _decimal, and wrap
not implemented functions. Now, when almost all functions work properly
it is not necessary.

%prep
%setup

%build
mkdir -p buildroot

# Unfortunately build and install steps should be done at once
# because otherwise .pyo files won't get into INSTALLED_FILES
# record
%python_build_install --optimize=2 \
                --root=`pwd`/buildroot \
                --record=INSTALLED_FILES
               
%install
cp -pr buildroot %buildroot
unset RPM_PYTHON

%files -f INSTALLED_FILES

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> svn20080222-alt3.1
- Rebuild with Python-2.7

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> svn20080222-alt3
- Rebuilt for debuginfo

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> svn20080222-alt2
- Rebuilt with python 2.6

* Fri Feb 22 2008 Eugine V. Kosenko <maverik@altlinux.ru> svn20080222-alt1
- Initial build

