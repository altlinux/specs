%define packagename python-module-cheetah
%define origname Cheetah

%def_with python3

Summary: Template engine and code-generator
Name: %packagename
Version: 2.4.4
Release: alt1
Source0: %origname-%version.tar.gz
License: MIT
Group: Development/Python
URL: http://cheetahtemplate.org/
#BuildArch: noarch

# Automatically added by buildreq on Sat Apr 05 2008
BuildRequires: python-devel

BuildPreReq: python-module-markdown python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python3-module-markdown python-tools-2to3
%endif

%description
Cheetah is an open source template engine and code generation tool, written
in Python. It can be used standalone or combined with other tools and
frameworks. Web development is its principle use, but Cheetah is very
flexible and is also being used to generate C++ game code, Java, sql,
form emails and even Python code.

%if_with python3
%package -n python3-module-%origname
Summary: Template engine and code-generator (Python 3)
Group: Development/Python3

%description -n python3-module-%origname
Cheetah is an open source template engine and code generation tool, written
in Python 3. It can be used standalone or combined with other tools and
frameworks. Web development is its principle use, but Cheetah is very
flexible and is also being used to generate C++ game code, Java, sql,
form emails and even Python 3 code.

%package -n python3-module-%origname-tests
Summary: Tests for Cheetah, template engine and code-generator (Python 3)
Group: Development/Python3
Requires: python3-module-%origname = %version-%release

%description -n python3-module-%origname-tests
Cheetah is an open source template engine and code generation tool, written
in Python. It can be used standalone or combined with other tools and
frameworks. Web development is its principle use, but Cheetah is very
flexible and is also being used to generate C++ game code, Java, sql,
form emails and even Python code.

This package contains tests for Cheetah.
%endif

%package tests
Summary: Tests for Cheetah, template engine and code-generator
Group: Development/Python
Requires: %name = %version-%release

%description tests
Cheetah is an open source template engine and code generation tool, written
in Python. It can be used standalone or combined with other tools and
frameworks. Web development is its principle use, but Cheetah is very
flexible and is also being used to generate C++ game code, Java, sql,
form emails and even Python code.

This package contains tests for Cheetah.

%prep
%setup -n %origname-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build_debug
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w $i
done
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w $i
done
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i py3_$i
done
popd
%endif

%python_install --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%exclude %python_sitelibdir/%origname/Tests

%files tests
%python_sitelibdir/%origname/Tests
%exclude %python_sitelibdir/%origname/Tests/Performance.py*

%if_with python3
%files -n python3-module-%origname
%_bindir/py3_*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%origname/Tests

%files -n python3-module-%origname-tests
%python3_sitelibdir/%origname/Tests
%exclude %python3_sitelibdir/%origname/Tests/Performance.py*
%endif

%changelog
* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.4-alt1
- Version 2.4.4
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.3-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.3-alt2.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt2
- Rebuilt for debuginfo

* Fri Nov 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1
- Version 2.4.3
- Extracted tests into separate package

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.1
- Rebuilt with python 2.6

* Wed Jul 29 2009 Mikhail Pokidko <pma@altlinux.org> 2.2.1-alt1
- Version up

* Sat Apr 05 2008 Mikhail Pokidko <pma@altlinux.org> 2.0.1-alt1
- Initial ALT build

