%define pypi_name reno
%def_with python3
%def_without doc

Name: python-module-%pypi_name
Version: 1.2.0
Release: alt1.1.1
Summary: Release NOtes manager
Group: Development/Python

License: ASL 2.0
Url: http://www.openstack.org/
Source: %name-%version.tar
BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-flake8 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-netaddr python-module-pbr python-module-pyasn1 python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-stevedore python-module-twisted-core python-module-unittest2 python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-mccabe python3-module-mimeparse python3-module-netaddr python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-stevedore python3-module-unittest2 python3-module-yieldfrom.http.client python3-module-yieldfrom.urllib3 python3-pyflakes python3-tools-pep8
BuildRequires: python-module-chardet python-module-hacking python-module-html5lib python-module-ndg-httpsclient python-module-ntlm python-module-oslo.config python-module-tox python-module-yaml python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-oslo.config python3-module-tox python3-module-yaml python3-module-yieldfrom.requests rpm-build-python3

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 1.4
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx
#BuildRequires: python-module-babel
#BuildRequires: python-module-yaml
#BuildRequires: python-module-oslotest

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 1.4
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-oslosphinx
#BuildRequires: python3-module-babel
#BuildRequires: python3-module-yaml
#BuildRequires: python3-module-oslotest
%endif

%description
Reno is a release notes manager for storing
release notes in a gitnrepository and then building documentation from them.

Managing release notes for a complex project over a long period
of time with many releases can be time consuming and error prone. Reno
helps automate the hard parts.

%if_with python3
%package -n python3-module-%pypi_name
Summary: RElease NOtes manager
Group: Development/Python3

%description -n python3-module-%pypi_name
Reno is a release notes manager for storing
release notes in a gitnrepository and then building documentation from them.

Managing release notes for a complex project over a long period
of time with many releases can be time consuming and error prone. Reno
helps automate the hard parts.
%endif

%package doc
Summary: reno documentation
Group: Development/Documentation

%description doc
Documentation for reno

%prep
%setup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

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
mv %buildroot%_bindir/%pypi_name %buildroot%_bindir/%pypi_name.py3
popd
%endif
%python_install

%if_with doc
# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%files
%doc README.rst
%_bindir/%pypi_name
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%doc README.rst
%_bindir/%pypi_name.py3
%python3_sitelibdir/*
%endif

%if_with doc
%files doc
%doc html
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Dec 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial Package
