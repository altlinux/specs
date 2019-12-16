%define _unpackaged_files_terminate_build 1
%define modname django-tinymce

Name: python3-module-%modname
Version: 2.8.0
Release: alt1

Summary: A Django app for render a form field as a TinyMCE editor
License: MIT
Group: Development/Python3
Url: http://code.google.com/p/django-tinymce/
# https://github.com/aljosa/django-tinymce.git
BuildArch: noarch

Source: %modname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx


%description
django-tinymce is a Django application that contains a widget to render a form field as a TinyMCE editor.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html

%files
%doc LICENSE.txt README.* docs/.build/html
%python3_sitelibdir/*


%changelog
* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.8.0-alt1
- Version updated to 2.8.0
- build for python2 disabled

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
