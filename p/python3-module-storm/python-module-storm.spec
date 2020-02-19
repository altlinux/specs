%define oname storm

Name: python3-module-%oname
Version: 0.21
Release: alt3

Summary: An object-relational mapper (ORM) for Python
License: LGPLv2+
Group: Development/Python3
Url: https://storm.canonical.com/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar.gz
BuildRequires(pre): rpm-build-python3


%description
Storm is an object-relational mapper (ORM) for Python. It offers a clean and
lightweight API offers a short learning curve and long-term maintainability and
it is easy to written backends for it.

%package -n python3-module-storm-mysql
Summary: MySQL backend for %name
Group: Development/Python3
Requires: python3-module-storm = %version

%description -n python3-module-storm-mysql
The %name-mysql package contains the MySQL database backend for
%name.

%package -n python3-module-storm-postgresql
Summary: PostgreSQL backend for %name
Group: Development/Python3
Requires: python3-module-storm = %version

%description -n python3-module-storm-postgresql
The %name-postgresql package contains the PostgreSQL database
backend for %name.

%package -n python3-module-storm-django
Summary: Support for using %name as Django ORM
Group: Development/Python3
Requires: python3-module-storm-zope = %version

%description -n python3-module-storm-django
The %name-django package contains an alternative ORM implementation
for Django.

%package -n python3-module-storm-zope
Summary: Zope integration for %name
Group: Development/Python3
Requires: python3-module-storm = %version

%description -n python3-module-storm-zope
The %name-zope package provides Zope integration for %name.

%package -n python3-module-storm-twisted
Summary: Twisted integration for %name
Group: Development/Python3
Requires: python3-module-storm = %version

%description -n python3-module-storm-twisted
The %name-twisted package provides Twisted integration for %name.

%prep
%setup

rm -rf storm.egg-info

%build
%python3_build_debug

%install
%python3_install

%files
%doc LICENSE NEWS README TODO
%doc storm/tests/tutorial.txt
%exclude %python3_sitelibdir/storm/django
%exclude %python3_sitelibdir/storm/zope
%exclude %python3_sitelibdir/storm/cextensions.c
%exclude %python3_sitelibdir/storm/databases
%exclude %python3_sitelibdir/storm/twisted
%python3_sitelibdir/storm*

%files -n python3-module-storm-django
%python3_sitelibdir/storm/django

%files -n python3-module-storm-zope
%python3_sitelibdir/storm/zope

%files -n python3-module-storm-mysql
%python3_sitelibdir/storm/databases/

%files -n python3-module-storm-postgresql
%python3_sitelibdir/storm/databases/postgres.*

%files -n python3-module-storm-twisted
%python3_sitelibdir/storm/twisted


%changelog
* Wed Feb 19 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.21-alt3
- Porting on python3.

* Mon Sep 23 2019 Artyom Bystrov <arbars@altlinux.org> 0.21-alt2
- initial build for ALT Sisyphus

