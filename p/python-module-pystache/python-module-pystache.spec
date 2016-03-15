%define sname pystache

%def_with python3

Summary: Mustache in Python 
Name: python-module-%sname
Version: 0.5.4
Release: alt1.git20121103.1.1
Source0: %name-%version.tar
License: BSD
Group: Development/Python
URL: https://github.com/defunkt/pystache
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python-devel >= 2.6
#BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Inspired by ctemplate and et, Mustache is a framework-agnostic way to
render logic-free views.
Pystache is a Python implementation of Mustache.

%package tests
Summary: Tests for %sname
Group: Development/Python
Requires: %name = %EVR

%description tests
Inspired by ctemplate and et, Mustache is a framework-agnostic way to
render logic-free views.
Pystache is a Python implementation of Mustache.

This package contains tests for %sname.

%package -n python3-module-%sname
Summary: Mustache in Python
Group: Development/Python3

%description -n python3-module-%sname
Inspired by ctemplate and et, Mustache is a framework-agnostic way to
render logic-free views.
Pystache is a Python implementation of Mustache.

%package -n python3-module-%sname-tests
Summary: Tests for %sname
Group: Development/Python3
Requires: python3-module-%sname = %EVR

%description -n python3-module-%sname-tests
Inspired by ctemplate and et, Mustache is a framework-agnostic way to
render logic-free views.
Pystache is a Python implementation of Mustache.

This package contains tests for %sname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

rm -rf tests

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
%doc LICENSE *.md
%_bindir/%sname
%python_sitelibdir/%sname
%python_sitelibdir/%sname-%version-py*.egg-info
%exclude %python_sitelibdir/%sname/*/test.py*
%exclude %python_sitelibdir/%sname/tests

%files tests
%_bindir/%sname-test
%python_sitelibdir/%sname/*/test.py*
%python_sitelibdir/%sname/tests

%if_with python3
%files -n python3-module-%sname
%doc LICENSE *.md
%_bindir/%sname.py3
%python3_sitelibdir/%sname
%python3_sitelibdir/%sname-%version-py*.egg-info
%exclude %python3_sitelibdir/%sname/*/test.py
%exclude %python3_sitelibdir/%sname/*/*/test.*
%exclude %python3_sitelibdir/%sname/tests

%files -n python3-module-%sname-tests
%_bindir/%sname-test.py3
%python3_sitelibdir/%sname/*/test.py
%python3_sitelibdir/%sname/*/*/test.*
%python3_sitelibdir/%sname/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.4-alt1.git20121103.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.4-alt1.git20121103.1
- NMU: Use buildreq for BR.

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt1.git20121103
- Version 0.5.4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt1.1
- Rebuild with Python-2.7

* Fri Jul 16 2010 Mikhail Pokidko <pma@altlinux.org> 0.3.1-alt1
- initial build



