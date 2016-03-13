# vim: set ft=spec: -*- rpm-spec -*-

%define modulename sekizai

%def_disable check
%def_with python3

Name: python-module-django-%modulename
Version: 0.7
Release: alt4.git20140813.1.1

%setup_python_module %modulename

Summary: Django Template Blocks with extra functionality
License: %bsd
Group: Development/Python

Url: http://django-sekizai.readthedocs.org/
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

# git://github.com/ojii/django-sekizai.git
Source: %name-%version.tar

#Requires: Django >= 1.2.7
# see setup.py
#Requires: python-module-django-classy-tags >= 0.3.1


#BuildPreReq: rpm-build-licenses
#BuildPreReq: Django >= 1.2.7
#BuildPreReq: python-module-django-tests
#BuildPreReq: python-module-django-dbbackend-sqlite3 >= 1.2.7
#BuildPreReq: python-module-django-classy-tags >= 0.3.1
#BuildPreReq: python-module-setupdocs
#BuildPreReq: python-module-sphinx
#BuildPreReq: python-module-alabaster python-module-django python-module-docutils python-module-html5lib python-module-setupdocs
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-module-django-tests python3-devel
#BuildPreReq: python3-module-django-dbbackend-sqlite3
#BuildPreReq: python3-module-django-classy-tags
#BuildPreReq: python3-module-setupdocs
#BuildPreReq: python3-module-django python3-module-setupdocs
%endif

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-psycopg2 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-psycopg2 python3-module-setuptools python3-module-yaml
BuildRequires: python-module-alabaster python-module-django python-module-docutils python-module-html5lib python-module-setupdocs python3-module-django python3-module-setupdocs rpm-build-python3 time

%description
Sekizai means "blocks" in Japanese, and that's what this app provides.
A fresh look at blocks. With django-sekizai you can define placeholders
where your blocks get rendered and at different places in your templates
append to those blocks. This is especially useful for css and javascript.
Your subtemplates can now define css and javscript files to be included,
and the css will be nicely put at the top and the javascript to the
bottom, just like you should. Also sekizai will ignore any duplicate
content in a single block.

%package -n python3-module-django-%modulename
Summary: Django Template Blocks with extra functionality
Group: Development/Python3

%description -n python3-module-django-%modulename
Sekizai means "blocks" in Japanese, and that's what this app provides.
A fresh look at blocks. With django-sekizai you can define placeholders
where your blocks get rendered and at different places in your templates
append to those blocks. This is especially useful for css and javascript.
Your subtemplates can now define css and javscript files to be included,
and the css will be nicely put at the top and the javascript to the
bottom, just like you should. Also sekizai will ignore any duplicate
content in a single block.

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

# doc
pushd docs
make html
popd

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python runtests.py
%if_with python3
pushd ../python3
python3 runtests.py
popd
%endif

%files
%doc LICENSE README.rst docs/_build
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-django-%modulename
%doc LICENSE README.rst docs/_build
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt4.git20140813.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.7-alt4.git20140813.1
- NMU: Use buildreq for BR.

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 0.7-alt4.git20140813
- Rebuild with "def_disable check"
- Clean buildreq

* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt3.git20140813
- New snapshot
- Added module for Python 3

* Fri Oct 04 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7-alt3.1
- Fix build requires.

* Tue Apr 02 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7-alt3
- Fix build requires

* Tue Feb 26 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7-alt2
- Fix requires

* Tue Feb 26 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7-alt1
- Initial build for ALT Linux Sisyphus
