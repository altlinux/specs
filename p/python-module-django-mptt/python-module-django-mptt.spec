%define modulename mptt
%def_without check

Name: python-module-django-%modulename
Version: 0.9.0
Release: alt1

Summary: Modified Preorder Tree Traversal Django application
License: BSD
Group: Development/Python
Url: http://github.com/django-mptt/django-mptt/
BuildArch: noarch

Source: %name-%version.tar
#Patch10: %%name-%%version-alt-fix-test_run_doctest.patch

Requires: Django >= 1.2
Conflicts: python-module-django-cms < 2.2

BuildRequires: rpm-build-licenses
BuildRequires: python-module-django-tests >= 1.2
BuildRequires: python-module-django-dbbackend-sqlite3 >= 1.2
BuildRequires: python-module-sphinx

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools


%description
Django MPTT is a reusable/standalone Django application which aims to
make it easy for you to use Modified Preorder Tree Traversal with your
own Django models in your own applications.

It takes care of the details of managing a database table as a tree
structure and provides tools for working with trees of model instances.

%package -n python3-module-%modulename
Summary: Modified Preorder Tree Traversal Django application
Group: Development/Python3
%add_python3_req_skip mptt.exceptions

%description -n python3-module-%modulename
Django MPTT is a reusable/standalone Django application which aims to
make it easy for you to use Modified Preorder Tree Traversal with your
own Django models in your own applications.

It takes care of the details of managing a database table as a tree
structure and provides tools for working with trees of model instances.

%prep
%setup
#%%patch10 -p1

cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

# doc
pushd docs
make text
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%if_with check
%check
pushd tests
./runtests.sh
popd
%endif

%files
%doc INSTALL README.rst build/docs
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%files -n python3-module-%modulename
%doc INSTALL README.rst build/docs
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info


%changelog
* Fri May 25 2018 Sergey Alembekov <mrdrew@altlinux.ru> 0.9.0-alt1
- Updated version to 0.9.0

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 0.5.5-alt4.git20130402
- Rebuild with "def_disable check"

* Wed Apr 03 2013 Aleksey Avdeev <solo@altlinux.ru> 0.5.5-alt3.git20130402
- Version 0.5.5 (9068e148af4fb091275ea945542fc1fed896231a)

* Wed Feb 27 2013 Aleksey Avdeev <solo@altlinux.ru> 0.5.5-alt2
- Fix requires

* Mon Feb 25 2013 Aleksey Avdeev <solo@altlinux.ru> 0.5.5-alt1
- Initial build for ALT Linux Sisyphus
