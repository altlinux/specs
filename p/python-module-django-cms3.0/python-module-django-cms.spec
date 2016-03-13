%define module_name django-cms3.0

%def_with python3

Name: python-module-%module_name
Version: 3.0.5
Release: alt1.git20140820.1

Summary: An Advanced Django CMS

License: BSD
Group: Development/Python
Url: http://www.django-cms.org

# https://github.com/divio/django-cms.git
Source: %module_name-%version.tar

BuildArch: noarch

# see docs/getting_started/installation.rst
Requires: Django >= 1.2.3
Requires: python-module-django-classy-tags >= 0.2.2

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%setup_python_module %module_name

#add_python_req_skip south tinymce dbgettext testapp

%description
An Advanced Django CMS.

%package -n python3-module-%module_name
Summary: An Advanced Django CMS
Group: Development/Python3
Requires: python3-module-django-classy-tags

%description -n python3-module-%module_name
An Advanced Django CMS.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%files
%doc CHANGELOG.txt AUTHORS LICENSE RELEASE_INFO *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%module_name
%doc CHANGELOG.txt AUTHORS LICENSE RELEASE_INFO *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.5-alt1.git20140820.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.5-alt1.git20140820
- Version 3.0.5
- Added module for Python 3

* Tue Feb 26 2013 Aleksey Avdeev <solo@altlinux.ru> 2.1.5-alt3
- Fix requires

* Tue Feb 26 2013 Aleksey Avdeev <solo@altlinux.ru> 2.1.5-alt2
- Fix conflicts

* Fri Feb 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2.1.5-alt1
- Version 2.1.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.3-alt1.git.6db7026.1
- Rebuild with Python-2.7

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.3-alt1.git.6db7026
- Version 2.1.3

* Sun Nov 28 2010 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt3.git.1b5ea0a
- cleanup spec
- build for ALT Linux Sisyphus

* Thu Nov 18 2010 Devaev Maxim <mdevaev@etersoft.ru> 2.1.0-alt2.git.1b5ea0a
- fixed python-testapp requires

* Wed Nov 17 2010 Devaev Maxim <mdevaev@etersoft.ru> 2.1.0-alt1.git.1b5ea0a
- New version

* Sat Mar 27 2010 Denis Klimov <zver@altlinux.org> 2.0.2-alt1.git.b035f83
- Initial build for ALT Linux

