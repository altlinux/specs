%def_with python3

Name: python-module-glanceclient
Version: 2.5.0
Release: alt2
Summary: Python API and CLI for OpenStack Glance

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/python-glanceclient
Source: %name-%version.tar
Patch: workaround-requests.patch

BuildArch: noarch

Requires: python-module-requests >= 2.12.0

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-prettytable >= 0.7
BuildRequires: python-module-keystoneclient >= 2.0.0
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-OpenSSL >= 0.11
BuildRequires: python-module-warlock >= 1.0.1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-oslo.utils >= 3.16.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
%py_requires urllib3

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-prettytable
BuildRequires: python3-module-keystoneclient >= 2.0.0
BuildRequires: python3-module-OpenSSL >= 0.11
BuildRequires: python3-module-requests >= 2.10.0
BuildRequires: python3-module-warlock >= 1.0.1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.utils >= 3.16.0
%endif

%description
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100 percent of the OpenStack Glance API.

%if_with python3
%package -n python3-module-glanceclient
Summary: Python API and CLI for OpenStack Glance
Group: Development/Python3
%py3_requires urllib3

%description -n python3-module-glanceclient
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100 percent of the OpenStack Glance API.
%endif

%package doc
Summary: Documentation for OpenStack Glance API Client
Group: Development/Documentation

%description doc
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100 percent of the OpenStack Glance API.

This package contains auto-generated documentation.

%prep
%setup
%patch -p1

# Remove bundled egg-info
rm -rf python_glanceclient.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py
rm -rf {,test-}requirements.txt

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

python setup.py build_sphinx

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/glance %buildroot%_bindir/python3-glance
%endif

%python_install

# generate man page
sphinx-build -b man doc/source man
install -p -D -m 644 man/glance.1 %buildroot%_mandir/man1/glance.1

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst
%doc LICENSE
%_bindir/glance
%python_sitelibdir/*
%_man1dir/glance*

%if_with python3
%files -n python3-module-glanceclient
%_bindir/python3-glance
%python3_sitelibdir/*
%endif

%files doc
%doc doc/build/html

%changelog
* Tue Feb 21 2017 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt2
- add patch for workaround requests >= 2.12

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt2.1
- NMU: Use buildreq for BR.

* Tue Nov 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt2
- fix work with system urllib3

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 0.17.2-alt1
- 0.17.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.16.1-alt1
- 0.16.1
- add python3 package

* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 0.12.0-alt1
- First build for ALT (based on Fedora 0.12.0-1.fc20.src)

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.4.1-alt1
- Initial release for Sisyphus (based on Fedora)

