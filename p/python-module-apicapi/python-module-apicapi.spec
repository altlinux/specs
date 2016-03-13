%define oname apicapi
%def_with python3

Name:       python-module-%oname
Version:    1.0.3
Release:    alt1.1.1
Summary:    Library for APIC REST api
License:    ASL 2.0
URL:       http://github.com/noironetworks/%oname
Source:    %name-%version.tar
Group:      Development/Python

BuildArch:  noarch

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-alembic python-module-babel python-module-beaker python-module-cffi python-module-cryptography python-module-cssselect python-module-docutils python-module-ecdsa python-module-ed25519 python-module-enum34 python-module-genshi python-module-jinja2 python-module-lingua python-module-mako python-module-migrate python-module-mimeparse python-module-netaddr python-module-nose python-module-nss python-module-oslo.config python-module-paste python-module-pbr python-module-polib python-module-pyasn1 python-module-pycrypto python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-stevedore python-module-twisted-core python-module-unittest2 python-module-wrapt python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-Pygments python3-module-alembic python3-module-babel python3-module-beaker python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-genshi python3-module-jinja2 python3-module-lingua python3-module-mako python3-module-migrate python3-module-mimeparse python3-module-netaddr python3-module-nose python3-module-ntlm python3-module-oslo.config python3-module-paste python3-module-pbr python3-module-pip python3-module-polib python3-module-pycparser python3-module-pycrypto python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-stevedore python3-module-unittest2 python3-module-wrapt python3-module-zope python3-module-zope.interface
BuildRequires: python-module-html5lib python-module-oslo.db python3-module-html5lib python3-module-oslo.db rpm-build-python3

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-oslo.config >= 1.4.0
#BuildRequires: python-module-oslo.db >= 1.0.0

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-oslo.config >= 1.4.0
#BuildRequires: python3-module-oslo.db >= 1.0.0
%endif

%description
There is a Python library provides an interface to the APIC REST api.

%if_with python3
%package -n python3-module-%oname
Summary: Library for APIC REST api
Group: Development/Python3

%description -n python3-module-%oname
There is a Python library provides an interface to the APIC REST api.
%endif

%prep
%setup

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install

%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/apic-cleanup %buildroot%_bindir/python3-apic-cleanup
mv %buildroot%_bindir/apic-route-reflector %buildroot%_bindir/python3-apic-route-reflector
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/test
rm -fr %buildroot%python3_sitelibdir/*/test

%files
%doc AUTHORS README.rst
%_bindir/*
%exclude %_bindir/python3-*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%_bindir/python3-*
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1.1
- NMU: Use buildreq for BR.

* Fri Mar 13 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- Initial release for Sisyphus

