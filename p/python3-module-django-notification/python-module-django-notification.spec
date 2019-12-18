%define module_name django-notification

Name: python3-module-%module_name
Version: 0.2.2
Release: alt2

Summary: User notification management for the Django web framework
License: MIT License
Group: Development/Python3
URL: http://github.com/Star2Billing/django-notification
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
User notification management for the Django web framework

%prep
%setup

sed -i 's|NoArgsCommand|BaseCommand|' $(find ./ -name 'emit_notices.py')

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%if "%_target_libdir_noarch" != "%_libdir"
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc AUTHORS CHANGELOG LICENSE README docs/*
%python3_sitelibdir/django_notification*
%python3_sitelibdir/notification*


%changelog
* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.2-alt2
- build for python2 disabled

* Tue Jul 16 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.2-alt1
- Build new version.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.1-alt1.git20140207.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20140207.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20140207.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20140207
- Version 0.2.1
- Added module for Python 3

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2-alt1
- build for ALT
