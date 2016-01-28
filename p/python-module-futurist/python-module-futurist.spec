%def_with python3

%define pypi_name futurist

Name: python-module-%pypi_name
Version: 0.5.0
Release: alt1.1
Summary: Useful additions to futures, from the future
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/futurist
Source: %name-%version.tar
BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-enum34 python-module-flake8 python-module-genshi python-module-hacking python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-ndg-httpsclient python-module-ntlm python-module-pbr python-module-pyasn1 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-mccabe python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-yieldfrom.http.client python3-module-yieldfrom.urllib3 python3-pyflakes python3-tools-pep8
BuildRequires: python-module-alabaster python-module-contextlib2 python-module-docutils python-module-futures python-module-html5lib python-module-monotonic python-module-oslosphinx python3-module-contextlib2 python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-sphinx python3-module-yieldfrom.requests rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 1.6
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx
#BuildRequires: python-module-futures >= 3.0
#BuildRequires: python-module-monotonic >= 0.3
#BuildRequires: python-module-contextlib2 >= 0.4.0
#BuildRequires: python-module-six >= 1.9.0

#Requires: python-module-six >= 1.9.0
Requires: python-module-monotonic
Requires: python-module-futures >= 3.0
Requires: python-module-contextlib2 >= 0.4.0

%description
Code from the future, delivered to you in the now.

%package doc
Summary: Documentation for futurist library
Group: Development/Documentation

%description doc
Documentation for futurist library.

%if_with python3
%package -n python3-module-%pypi_name
Summary: Useful additions to futures, from the future
Group: Development/Python3

BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 1.6
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-oslosphinx
#BuildRequires: python3-module-monotonic
#BuildRequires: python3-module-contextlib2
#BuildRequires: python3-module-six

#Requires: python3-module-six >= 1.9.0
Requires: python3-module-monotonic
Requires: python3-module-contextlib2 >= 0.4.0

%description -n python3-module-%pypi_name
Code from the future, delivered to you in the now.
%endif

%prep
%setup

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

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo


%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst
%python_sitelibdir/%pypi_name
%python_sitelibdir/*.egg-info

%files doc
%doc doc/build/html

%if_with python3
%files -n python3-module-%pypi_name
%doc README.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- Initial package.
