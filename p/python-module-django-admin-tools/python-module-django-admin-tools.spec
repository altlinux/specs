%define _unpackaged_files_terminate_build 1
%define module_name django-admin-tools

%def_with python3

Name: python-module-%module_name
Version: 0.8.0
Release: alt1

Summary: A collection of tools for the django administration interface

License: MIT License
Group: Development/Python
Url: http://www.bitbucket.org/izi/django-admin-tools

Source0: https://pypi.python.org/packages/af/1c/2f81a943c7a32c813b0bfc2a0029ca36a0fdc2c3ed60f8fd7288aa859d8e/%{module_name}-%{version}.tar.gz

BuildArch: noarch

%setup_python_module %module_name
#BuildPreReq: python-module-setuptools python-module-sphinx-devel
#BuildPreReq: python-module-django
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-psycopg2 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python3 python3-base tzdata
BuildRequires: python-module-alabaster python-module-django python-module-docutils python-module-html5lib python-module-objects.inv python3-module-setuptools rpm-build-python3 time

%description
django-admin-tools is a collection of extensions/tools for the default
django administration interface, it includes:

 * a full featured and customizable dashboard,
 * a customizable menu bar,
 * tools to make admin theming easier.

%package -n python3-module-%module_name
Summary: A collection of tools for the django administration interface
Group: Development/Python3

%description -n python3-module-%module_name
django-admin-tools is a collection of extensions/tools for the default
django administration interface, it includes:

 * a full featured and customizable dashboard,
 * a customizable menu bar,
 * tools to make admin theming easier.

%prep
%setup -q -n %{module_name}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%files
%doc AUTHORS CHANGELOG LICENSE docs/_build/html PKG-INFO README.rst docs
%python_sitelibdir/django_admin_tools-*
%python_sitelibdir/admin_tools

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS CHANGELOG LICENSE docs/_build/html PKG-INFO README.rst docs
%python3_sitelibdir/django_admin_tools-*
%python3_sitelibdir/admin_tools
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1.1
- NMU: Use buildreq for BR.

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Version 0.5.2
- Added module for Python 3

* Thu Apr 19 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.1-alt1
- Initial build for ALT Linux
