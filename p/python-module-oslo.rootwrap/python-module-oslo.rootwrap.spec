%define pypi_name oslo.rootwrap

%def_with python3

Name: python-module-%pypi_name
Version: 2.3.0
Release: alt1.1.1
Summary: Oslo Rootwrap

Group: Development/Python
License: ASL 2.0
URL: https://launchpad.net/oslo
Source: %name-%version.tar
BuildArch:      noarch

Provides: python-module-oslo-rootwrap = %EVR
Obsoletes: python-module-oslo-rootwrap < %EVR

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-enum34 python-module-flake8 python-module-genshi python-module-hacking python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-ndg-httpsclient python-module-ntlm python-module-pbr python-module-pyasn1 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-mccabe python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-yieldfrom.http.client python3-module-yieldfrom.urllib3 python3-pyflakes python3-tools-pep8
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-oslosphinx python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-sphinx python3-module-yieldfrom.requests rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 1.6
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx
#BuildRequires: python-module-six >= 1.9.0

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 1.6
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-oslosphinx
#BuildRequires: python3-module-six >= 1.9.0
%endif

%description

The Oslo Rootwrap allows fine filtering of shell commands to run as `root`
from OpenStack services.

* License: Apache License, Version 2.0
* Documentation: http://docs.openstack.org/developer/oslo.rootwrap
* Source: http://git.openstack.org/cgit/openstack/oslo.rootwrap
* Bugs: http://bugs.launchpad.net/oslo.rootwrap


%if_with python3
%package -n python3-module-oslo.rootwrap
Summary: OpenStack oslo.rootwrap library
Group: Development/Python3
Provides: python3-module-oslo-rootwrap = %EVR

%description -n python3-module-oslo.rootwrap

The Oslo Rootwrap allows fine filtering of shell commands to run as `root`
from OpenStack services.

* License: Apache License, Version 2.0
* Documentation: http://docs.openstack.org/developer/oslo.rootwrap
* Source: http://git.openstack.org/cgit/openstack/oslo.rootwrap
* Bugs: http://bugs.launchpad.net/oslo.rootwrap
%endif

%package doc
Summary: Documentation for the Oslo rootwrap handling library
Group: Development/Documentation
Provides: python-module-oslo-rootwrap-doc = %EVR

%description doc
Documentation for the Oslo rootwrap handling library.


%prep
%setup

# Remove bundled egg-info
rm -rf %pypi_name.egg-info

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


# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/oslo-rootwrap \
   %buildroot%_bindir/python3-oslo-rootwrap
mv %buildroot%_bindir/oslo-rootwrap-daemon \
   %buildroot%_bindir/python3-oslo-rootwrap-daemon
popd
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst LICENSE
%python_sitelibdir/*
%_bindir/oslo-rootwrap
%_bindir/oslo-rootwrap-daemon

%if_with python3
%files -n python3-module-oslo.rootwrap
%python3_sitelibdir/*
%_bindir/python3-oslo-rootwrap
%_bindir/python3-oslo-rootwrap-daemon
%endif

%files doc
%doc html

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0
- rename package from python-module-oslo-rootwrap to python-module-oslo.rootwrap
- add python3 package

* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.0-alt1
- First build for ALT
