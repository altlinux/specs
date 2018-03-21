%define modname django-tinymce

Name: python-module-%modname
Version: 2.7.0
Release: alt1

Summary: A Django app for render a form field as a TinyMCE editor
License: MIT
Group: Development/Python
Url: http://code.google.com/p/django-tinymce/
# https://github.com/aljosa/django-tinymce.git
BuildArch: noarch

Source: %modname-%version.tar

BuildRequires: python-module-setuptools
BuildRequires: python-module-alabaster
BuildRequires: python-module-docutils
BuildRequires: python-module-html5lib
BuildRequires: python-module-objects.inv
BuildRequires: time

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
BuildPreReq: python3-module-setuptools

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base


%description
django-tinymce is a Django application that contains a widget to render a form field as a TinyMCE editor.

%package -n python3-module-%modname
Summary: A Django app for render a form field as a TinyMCE editor
Group: Development/Python3

%description -n python3-module-%modname
django-tinymce is a Django application that contains a widget to render a form field as a TinyMCE editor.

%prep
%setup

cp -fR . ../python3

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%files
%doc LICENSE.txt README.* docs/.build/html
%python_sitelibdir/tinymce
%python_sitelibdir/django_tinymce*

%files -n python3-module-%modname
%doc LICENSE.txt README.* docs/.build/html
%python3_sitelibdir/tinymce
%python3_sitelibdir/django_tinymce*


%changelog
* Wed Mar 21 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.7.0-alt1
- Version 2.7.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.2-alt1.git20140513.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.2-alt1.git20140513.1
- NMU: Use buildreq for BR.

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.git20140513
- Version 1.5.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt1.1
- Rebuild with Python-2.7

* Wed Mar 31 2010 Denis Klimov <zver@altlinux.org> 1.5-alt1
- Initial build for ALT Linux
