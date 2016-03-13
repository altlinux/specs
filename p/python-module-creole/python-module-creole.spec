%define oname creole

%def_with python3

Name: python-module-%oname
Version: 1.2.0
Release: alt1.1

Summary: Markup converter in pure Python for: creole2html, html2creole, html2ReSt, html2textile
License: GPLv3+
Group: Development/Python
BuildArch: noarch

Url: http://code.google.com/p/python-creole
# sourcecode: http://github.com/jedie/python-creole
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%description
Python lib for:
 - creole markup -> html
 - html -> creole markup
python-creole is pure python. No external libs needed.
The creole2html part based on the creole markup parser and emitter from
the MoinMoin project by Radomir Dopieralski and Thomas Waldmann.

%package -n python3-module-%oname
Summary: Markup converter in pure Python for: creole2html, html2creole, html2ReSt, html2textile
Group: Development/Python3

%description -n python3-module-%oname
Python lib for:
 - creole markup -> html
 - html -> creole markup
python-creole is pure python. No external libs needed.
The creole2html part based on the creole markup parser and emitter from
the MoinMoin project by Radomir Dopieralski and Thomas Waldmann.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%files
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/%oname
%exclude %python_sitelibdir/%oname/tests
%python_sitelibdir/python_%oname-*.egg-info
%doc AUTHORS README.%oname LICENSE

%if_with python3
%files -n python3-module-%oname
%_bindir/*.py3
%python3_sitelibdir/%oname
%exclude %python3_sitelibdir/%oname/tests
%python3_sitelibdir/python_%oname-*.egg-info
%doc AUTHORS README.%oname LICENSE
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Version 1.2.0
- Added module for Python 3

* Fri May 24 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Mon Jul 09 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.3-alt1.2
- exclude tests from package

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.3-alt1.1
- Rebuild with Python-2.7

* Mon Mar 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Mon Dec 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- first build for Sisyphus
