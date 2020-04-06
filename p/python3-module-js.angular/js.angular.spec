%define mname js
%define oname %mname.angular

Name: python3-module-%oname
Version: 1.1.4
Release: alt3

Summary: Fanstatic packaging of AngularJS
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.angular/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

Requires: python3-module-%mname = %EVR

%description
This library packages AngularJS for fanstatic.

This requires integration between your web framework and fanstatic, and
making sure that the original resources (shipped in the resources
directory in js.angular) are published to some URL.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

%files
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

%changelog
* Mon Apr 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.4-alt3
- Build for python2 disabled.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.4-alt2.2
- Rebuild with python3.7.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.4-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.4-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt2
- Applied python-module-js.angular-1.1.4-alt1.diff

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt1
- Initial build for Sisyphus

