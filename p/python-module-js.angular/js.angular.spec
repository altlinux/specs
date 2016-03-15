%define mname js
%define oname %mname.angular

%def_with python3

Name: python-module-%oname
Version: 1.1.4
Release: alt2.1
Summary: Fanstatic packaging of AngularJS
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/js.angular/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

Requires: python-module-%mname = %EVR

%description
This library packages AngularJS for fanstatic.

This requires integration between your web framework and fanstatic, and
making sure that the original resources (shipped in the resources
directory in js.angular) are published to some URL.

%package -n python3-module-%oname
Summary: Fanstatic packaging of AngularJS
Group: Development/Python3
Requires: python3-module-%mname = %EVR

%description -n python3-module-%oname
This library packages AngularJS for fanstatic.

This requires integration between your web framework and fanstatic, and
making sure that the original resources (shipped in the resources
directory in js.angular) are published to some URL.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python

%description -n python-module-%mname
Core files of %mname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3

%description -n python3-module-%mname
Core files of %mname.

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/
%if_with python3
pushd ../python3
install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/
popd
%endif

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

%files
%doc *.rst
%python_sitelibdir/*.egg-info
%python_sitelibdir/%mname/*
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/%mname/*
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.4-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt2
- Applied python-module-js.angular-1.1.4-alt1.diff

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt1
- Initial build for Sisyphus

