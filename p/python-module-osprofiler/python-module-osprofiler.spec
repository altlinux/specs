%define sname osprofiler

%def_with python3

Name: python-module-%sname
Version: 0.3.0
Release: alt1.1.1
Summary: OpenStack cross-project profiling library
Group: Development/Python
License: ASL 2.0
Url: https://github.com/openstack/%sname
Source: %name-%version.tar

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-enum34 python-module-flake8 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-pbr python-module-pyasn1 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-mccabe python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-yieldfrom.http.client python3-module-yieldfrom.urllib3 python3-pyflakes python3-tools-pep8
BuildRequires: python-module-alabaster python-module-chardet python-module-d2to1 python-module-docutils python-module-hacking python-module-html5lib python-module-ndg-httpsclient python-module-ntlm python-modules-wsgiref python3-module-d2to1 python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-sphinx python3-module-yieldfrom.requests rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 0.6
#BuildRequires: python-module-d2to1
#BuildRequires: python-module-six >= 1.7.0
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx
#BuildRequires: python-module-argparse
#BuildRequires: python-module-webob >= 1.2.3

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 0.6
#BuildRequires: python3-module-d2to1
#BuildRequires: python3-module-six >= 1.7.0
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-oslosphinx
#BuildRequires: python3-module-argparse
#BuildRequires: python3-module-webob >= 1.2.3

%endif

BuildArch: noarch

%description
OSProfiler is an OpenStack cross-project profiling library.

%if_with python3
%package -n python3-module-%sname
Summary: OpenStack cross-project profiling library
Group: Development/Python3

%description -n python3-module-%sname
OSProfiler is an OpenStack cross-project profiling library.
%endif


%package doc
Summary: Documentation for OpenStack cross-project profiling library
Group: Development/Documentation

%description doc
Documentation for OSProfiler is an OpenStack cross-project profiling library.

%prep
%setup

# Remove bundled egg-info
rm -rf %sname.egg-info

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
mv %buildroot%_bindir/%sname %buildroot%_bindir/python3-%sname
popd
%endif
%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees   source build/html
popd

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%files
%doc AUTHORS ChangeLog LICENSE PKG-INFO README.rst
%python_sitelibdir/*
%_bindir/%sname

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%_bindir/python3-%sname
%endif

%files doc
%doc doc/build/html

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Mar 12 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- Initial release
