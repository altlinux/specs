%define module_name django-dilla

%def_with python3

Name: python-module-%module_name
Version: 0.2
Release: alt1.beta.git20130109.1

Summary: Dilla is a multi-purpose general testing tool

License: BSD
Group: Development/Python
Url: https://github.com/aerosol/django-dilla.git

Source: %name-%version.tar

BuildArch: noarch

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%setup_python_module %module_name

%py_requires identicon

%description
Dilla is a multi-purpose general testing tool for automated
database spamming, intented to use with projects built on top of Django,
populating data within any number of internal applications.

%package -n python3-module-%module_name
Summary: Dilla is a multi-purpose general testing tool
Group: Development/Python3
%add_python3_req_skip dilla
%py3_requires identicon

%description -n python3-module-%module_name
Dilla is a multi-purpose general testing tool for automated
database spamming, intented to use with projects built on top of Django,
populating data within any number of internal applications.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README LICENSE
%python_sitelibdir/dilla*
%python_sitelibdir/django_dilla*

%if_with python3
%files -n python3-module-%module_name
%doc README LICENSE
%python3_sitelibdir/dilla*
%python3_sitelibdir/django_dilla*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.beta.git20130109.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.beta.git20130109
- New snapshot
- Added module for Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.beta.1
- Fixed build

* Thu Apr 19 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2-alt1.beta
- Initial build for ALT Linux
