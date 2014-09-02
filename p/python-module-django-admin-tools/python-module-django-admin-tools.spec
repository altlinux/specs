%define module_name django-admin-tools

%def_with python3

Name: python-module-%module_name
Version: 0.5.2
Release: alt1

Summary: A collection of tools for the django administration interface

License: MIT License
Group: Development/Python
Url: http://www.bitbucket.org/izi/django-admin-tools

Source: %module_name-%version.tar.gz

BuildArch: noarch

%setup_python_module %module_name
BuildPreReq: python-module-setuptools python-module-sphinx-devel
BuildPreReq: python-module-django
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

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
%setup -n %module_name-%version

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
%doc AUTHORS CHANGELOG LICENSE README docs/_build/html
%python_sitelibdir/django_admin_tools-*
%python_sitelibdir/admin_tools

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS CHANGELOG LICENSE README docs/_build/html
%python3_sitelibdir/django_admin_tools-*
%python3_sitelibdir/admin_tools
%endif

%changelog
* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Version 0.5.2
- Added module for Python 3

* Thu Apr 19 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.1-alt1
- Initial build for ALT Linux
