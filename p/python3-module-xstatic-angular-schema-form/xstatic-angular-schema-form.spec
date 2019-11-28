%define mname xstatic
%define oname %mname-angular-schema-form
%define pypi_name XStatic-Angular-Schema-Form

Name: python3-module-%oname
Version: 0.8.13.0
Release: alt3

Summary: Angular-Schema-Form (XStatic packaging standard)
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/%pypi_name/
BuildArch: noarch

Source: %pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-%mname

%py3_provides %mname.pkg.angular_schema_form
%py3_requires %mname.pkg


%description
Schema Form is a set of AngularJS directives (and a couple of services)
to generate Bootstrap 3 ready forms from a JSON Schema.

%prep
%setup -n %pypi_name-%version

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/%mname/pkg/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*.pth


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.8.13.0-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.13.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 0.8.13.0-alt2
- build as noarch

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 0.8.13.0-alt1
- Initial build for Sisyphus

