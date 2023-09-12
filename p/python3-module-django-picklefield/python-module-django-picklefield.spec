%define _unpackaged_files_terminate_build 1

%define module_name django-picklefield

Name: python3-module-%module_name
Version: 3.1.0
Release: alt1

Summary: django-picklefield provides an implementation of a pickled object field

License: MIT
Group: Development/Python3
URL: http://github.com/gintas/django-picklefield.git

Source0: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django

BuildArch: noarch

%description
django-picklefield provides an implementation of a pickled object field.
Such fields can contain any picklable objects.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE README.rst
%python3_sitelibdir/django_picklefield*
%python3_sitelibdir/picklefield*

%changelog
* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Automatically updated to 3.1.0.

* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt1
- Version updated to 2.0.0
- build for python2 disabled

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt1.git20131115.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt1.git20131115.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20131115
- Version 0.3.1
- Added module for Python 3

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.1-alt1
- build for ALT
