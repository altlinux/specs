# vim: set ft=spec: -*- rpm-spec -*-

%define modulename mptt
%def_disable check

Name: python-module-django-%modulename
Version: 0.5.5
Release: alt4.git20130402

%setup_python_module %modulename

Summary: Modified Preorder Tree Traversal Django application
# see setup.py
License: %bsd
Group: Development/Python

Url: http://github.com/django-mptt/django-mptt/
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar
Patch10: %name-%version-alt-fix-test_run_doctest.patch

# see requirements.txt
Requires: Django >= 1.2
Conflicts: python-module-django-cms < 2.2

BuildPreReq: rpm-build-licenses
BuildPreReq: python-module-django-tests >= 1.2
BuildPreReq: python-module-django-dbbackend-sqlite3 >= 1.2
BuildPreReq: python-module-sphinx

%description
Django MPTT is a reusable/standalone Django application which aims to
make it easy for you to use Modified Preorder Tree Traversal with your
own Django models in your own applications.

It takes care of the details of managing a database table as a tree
structure and provides tools for working with trees of model instances.

%prep
%setup
%patch10 -p1

%build
%python_build

# doc
pushd docs
make text
popd

%install
%python_install

%check
pushd tests
./runtests.sh
popd

%files
%doc INSTALL LICENSE NOTES README.rst build/docs
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 0.5.5-alt4.git20130402
- Rebuild with "def_disable check"

* Wed Apr 03 2013 Aleksey Avdeev <solo@altlinux.ru> 0.5.5-alt3.git20130402
- Version 0.5.5 (9068e148af4fb091275ea945542fc1fed896231a)

* Wed Feb 27 2013 Aleksey Avdeev <solo@altlinux.ru> 0.5.5-alt2
- Fix requires

* Mon Feb 25 2013 Aleksey Avdeev <solo@altlinux.ru> 0.5.5-alt1
- Initial build for ALT Linux Sisyphus
