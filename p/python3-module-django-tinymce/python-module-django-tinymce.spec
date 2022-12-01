%define _unpackaged_files_terminate_build 1
%define modname django-tinymce
%def_with check

Name: python3-module-%modname
Version: 3.5.0
Release: alt1

Summary: A Django app for render a form field as a TinyMCE editor
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/django-tinymce
BuildArch: noarch

Source: %modname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(sphinx)

%if_with check
BuildRequires: python3(django)
BuildRequires: python3(coverage)
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%py3_provides %modname

%description
django-tinymce is a Django application that contains a widget to render a form field as a TinyMCE editor.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%pyproject_build

%if_with check
%check
%tox_check_pyproject
%endif

%install
%pyproject_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html

%files
%doc LICENSE.txt README.* docs/.build/html
%python3_sitelibdir/tinymce
%python3_sitelibdir/%{pyproject_distinfo %modname}
%exclude %python3_sitelibdir/tests

%changelog
* Thu Dec 01 2022 Alexander Makeenkov <amakeenk@altlinux.org> 3.5.0-alt1
- NMU:
  + Updated to version 3.5.0
  + Use pyproject macroses for build
  + Added py3_provides
  + Enabled tests

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
