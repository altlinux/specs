%define oname repoze.django

Name: python3-module-%oname
Version: 0.2
Release: alt4

Summary: A wrapper that allows us to run Django under PasteDeploy
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/repoze.django/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_requires repoze paste.script
Requires: python3-module-django


%description
A way to run Django under PasteDeploy.

%prep
%setup

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt4
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.2-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

