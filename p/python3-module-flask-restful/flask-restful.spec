%define oname Flask-RESTful

# In 0.3.10 upstream did not moved from nose
# https://github.com/flask-restful/flask-restful/issues/926
# https://github.com/flask-restful/flask-restful/issues/930
%def_without check

Name: python3-module-flask-restful
Version: 0.3.10
Release: alt1

Summary: Simple framework for creating REST APIs

License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/Flask-RESTful
VCS: https://github.com/flask-restful/flask-restful

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-aniso8601
BuildRequires: python3-module-flask
BuildRequires: python3-module-pytz
%endif

%description
Flask-RESTful provides the building blocks for creating a great REST API.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.md
%python3_sitelibdir/flask_restful
%python3_sitelibdir/Flask_RESTful-%version.dist-info

%changelog
* Tue Sep 19 2023 Grigory Ustinov <grenka@altlinux.org> 0.3.10-alt1
- Build new version.

* Thu Mar 09 2023 Grigory Ustinov <grenka@altlinux.org> 0.3.9-alt1
- Build new version.

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.3.8-alt2
- NMU: cleanup spec, disable tests packing

* Thu Feb 13 2020 Nikita N. <rav263@altlinux.org> 0.3.8-alt1
- Update to 0.3.8.

* Thu Apr 18 2019 Andrew A. Vasilyev <andy@altlinux.org> 0.3.7-alt1
- Update to 0.3.7.

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 0.3.6-alt1
- Initial build for Sisyphus.
