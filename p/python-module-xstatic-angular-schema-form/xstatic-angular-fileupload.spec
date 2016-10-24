%define mname xstatic
%define oname %mname-angular-schema-form

%def_with python3

Name: python-module-%oname
Version: 0.8.13.0
Release: alt1
Summary: Angular-Schema-Form (XStatic packaging standard)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/XStatic-Angular-Schema-Form
Source: %name-%version.tar

%py_provides %mname.pkg.angular_schema_form
%py_requires %mname.pkg

BuildRequires: python-module-setuptools-tests python-module-xstatic python3-module-setuptools-tests python3-module-xstatic
BuildRequires(pre): rpm-build-python3

%description
Schema Form is a set of AngularJS directives (and a couple of services)
to generate Bootstrap 3 ready forms from a JSON Schema.

%package -n python3-module-%oname
Summary: Angular-Schema-Form (XStatic packaging standard)
Group: Development/Python3
%py3_provides %mname.pkg.angular_schema_form
%py3_requires %mname.pkg

%description -n python3-module-%oname
Schema Form is a set of AngularJS directives (and a couple of services)
to generate Bootstrap 3 ready forms from a JSON Schema.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 0.8.13.0-alt1
- Initial build for Sisyphus

