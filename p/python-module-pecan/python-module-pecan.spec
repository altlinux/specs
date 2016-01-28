%define pypi_name pecan
%def_with python3

Name: python-module-%pypi_name
Version: 1.0.3
Release: alt2.1
Summary: A lean WSGI object-dispatching web framework
Group: Development/Python

License: BSD
Url: http://github.com/dreamhost/%pypi_name
Source0: %name-%version.tar
BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-beaker python-module-cssselect python-module-ecdsa python-module-ed25519 python-module-genshi python-module-html5lib python-module-jinja2 python-module-lingua python-module-nss python-module-polib python-module-pycrypto python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-waitress python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-Pygments python3-module-babel python3-module-beaker python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-html5lib python3-module-jinja2 python3-module-lingua python3-module-polib python3-module-pycrypto python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-waitress python3-module-zope python3-module-zope.interface
BuildRequires: python-module-docutils python-module-logutils python-module-mako python-module-ordereddict python-module-webtest python3-module-logutils python3-module-mako python3-module-sphinx python3-module-webtest rpm-build-python3

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-webob >= 1.2
#BuildRequires: python-module-simplegeneric >= 0.8
#BuildRequires: python-module-mako >= 0.4.0
#BuildRequires: python-module-singledispatch
#BuildRequires: python-module-webtest >= 1.3.1
#BuildRequires: python-module-argparse
#BuildRequires: python-module-logutils

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-webob >= 1.2
#BuildRequires: python3-module-simplegeneric >= 0.8
#BuildRequires: python3-module-mako >= 0.4.0
#BuildRequires: python3-module-singledispatch
#BuildRequires: python3-module-webtest >= 1.3.1
#BuildRequires: python3-module-argparse
#BuildRequires: python3-module-logutils
%endif

Requires: python-module-singledispatch
Requires: python-module-argparse
Requires: python-module-logutils

%description
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies

%if_with python3
%package -n python3-module-%pypi_name
Summary: A lean WSGI object-dispatching web framework
Group: Development/Python3

%description -n python3-module-%pypi_name
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies
%endif

%prep
%setup

# Remove bundled egg-info
rm -rf %pypi_name.egg-info

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%python_build

%install
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/pecan \
   %buildroot%_bindir/pecan3
mv %buildroot%_bindir/gunicorn_pecan \
   %buildroot%_bindir/gunicorn_pecan3
popd
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/testing.py
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/testing.py
rm -fr %buildroot%python3_sitelibdir/*/tests


%files
%doc LICENSE README.rst
%_bindir/pecan
%_bindir/gunicorn_pecan
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%_bindir/pecan3
%_bindir/gunicorn_pecan3
%python3_sitelibdir/*
%endif


%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt2.1
- NMU: Use buildreq for BR.

* Mon Nov 09 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt2
- update R:

* Fri Oct 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- 1.0.3
- add python3 package
- delete tests

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.4.5-alt1
- First build for ALT (based on Fedora 0.4.5-4.fc21)

