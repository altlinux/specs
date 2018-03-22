%define origname Cheetah

%def_with python3

Summary: Template engine and code-generator
Name: python-module-%origname
Version: 3.1.0
Release: alt1.1
Source0: Cheetah-%version.tar
License: MIT
Group: Development/Python
URL: http://cheetahtemplate.org/
# https://github.com/CheetahTemplate3/cheetah3
#BuildArch: noarch

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-markdown python-module-setuptools time
BuildRequires: python-module-sphinx

#BuildPreReq: python-module-markdown python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-distribute python3-module-setuptools
BuildPreReq: python3-module-markdown python-tools-2to3
BuildPreReq: python3-module-sphinx
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
%setup -n Cheetah-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build
popd
%endif

export PYTHONPATH=$PWD
%make -C docs html
mkdir man
cp -fR docs/_build/html/* man/

%install
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
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
%doc *.rst man/
%exclude %python_sitelibdir/Cheetah/Tests

%files tests
%python_sitelibdir/Cheetah/Tests
%exclude %python_sitelibdir/Cheetah/Tests/Performance.py*

%files -n python3-module-%origname-tests
%python3_sitelibdir/Cheetah/Tests
%exclude %python3_sitelibdir/Cheetah/Tests/Performance.py*

%files -n python3-module-%origname
%doc *.rst man/
%_bindir/py3_*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/Cheetah/Tests


%changelog
* Tue Mar 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Mar 27 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.1.0-alt1
- Version 3.1.0-alt1

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.4-alt2.git20121217.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.4.4-alt2.git20121217.1
- NMU: Use buildreq for BR.

* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.4-alt2.git20121217
- Snapshot from git

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.4-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.4-alt1.1
- Rebuild with Python-3.3

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
