%define _unpackaged_files_terminate_build 1
%define module_name django-tastypie

Name: python3-module-%module_name
Version: 0.14.2
Release: alt2

Summary: Creating delicious APIs for Django apps since 2010
License: BSD License
Group: Development/Python3
URL: https://github.com/toastdriven/django-tastypie.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx


%description
Creating delicious APIs for Django apps since 2010
There are other, better known API frameworks out there for Django. You need to
assess the options available and decide for yourself. That said, here are some
common reasons for tastypie.

%package docs
Summary: Documentation for %module_name
Group: Development/Documentation
BuildArch: noarch

%description docs
Creating delicious APIs for Django apps since 2010
There are other, better known API frameworks out there for Django. You need to
assess the options available and decide for yourself. That said, here are some
common reasons for tastypie.

This package contains documentation for %module_name.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%if "%_target_libdir_noarch" != "%_libdir"
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html

%files
%doc AUTHORS LICENSE README.rst TODO
%doc BACKWARDS-INCOMPATIBLE.txt CONTRIBUTING
%python3_sitelibdir/tastypie*
%python3_sitelibdir/django_tastypie*

%files docs
%doc docs/_build/html/*


%changelog
* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.14.2-alt2
- build for python2 disabled

* Tue Jul 16 2019 Grigory Ustinov <grenka@altlinux.org> 0.14.2-alt1
- Build new version.

* Wed Dec 26 2018 Grigory Ustinov <grenka@altlinux.org> 0.14.1-alt1
- Build new version.

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.12.2-alt1.dev.git20141022.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.12.2-alt1.dev.git20141022.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.12.2-alt1.dev.git20141022.1
- NMU: Use buildreq for BR.

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2-alt1.dev.git20141022
- Version 0.12.2-dev

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.1-alt1.dev.git20140925
- Version 0.12.1-dev

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.2-alt1.dev.git20140823
- Version 0.11.2-dev
- Added module for Python 3

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.11-alt1
- build for ALT
