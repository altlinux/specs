Name: euca2ools
Version: 1.1
Release: alt1.1
Summary: Elastic Utility Computing Architecture Command-Line Tools

Group: Networking/Other
License: BSD
Url: http://open.eucalyptus.com/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: http://eucalyptussoftware.com/downloads/releases/%name-%version.tar.gz

# Automatically added by buildreq on Wed Feb 03 2010
BuildRequires: python-module-m2crypto python-module-setuptools

BuildArch: noarch

%description
EUCALYPTUS is an open source service overlay that implements elastic
computing using existing resources. The goal of EUCALYPTUS is to allow
sites with existing clusters and server infrastructure to co-host an
elastic computing service that is interface-compatible with Amazon's EC2.

This package contains the command line tools to interact with Eucalyptus.
This tools are compatible with Amazon EC2.

%prep
%setup -q

%build
cd euca2ools
%python_build

%install

pushd euca2ools
%__python setup.py install --skip-build --root %buildroot
%__python setup.py install -O1 --skip-build --root %buildroot
popd

mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_man1dir
cp -p bin/* %buildroot/%_bindir
cp -p man/* %buildroot/%_man1dir

%files
%_bindir/euca-*
%_man1dir/euca*
%python_sitelibdir/%name-*.egg-info
%python_sitelibdir/%name/*.py
%python_sitelibdir/%name/*.pyc
%python_sitelibdir/%name/*.pyo
%doc CHANGELOG
%doc COPYING
%doc INSTALL
%doc README

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.1
- Rebuild with Python-2.7

* Wed Feb 03 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1
- Initial

