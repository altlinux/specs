%define mname kids
%define oname %mname.xml

%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20150205.1.1
Summary: Kids XML library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kids.xml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/0k/kids.xml.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests git xmllint
#BuildPreReq: python-module-d2to1 python-module-coverage
#BuildPreReq: python-module-nose python-module-kids.file
#BuildPreReq: python-module-kids.sh python-module-lxml
#BuildPreReq: python-module-kids.cache python-module-kids.test
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests git
#BuildPreReq: python3-module-d2to1 python3-module-coverage
#BuildPreReq: python3-module-nose python3-module-kids.file
#BuildPreReq: python3-module-kids.sh python3-module-lxml
#BuildPreReq: python3-module-kids.cache python3-module-kids.test
%endif

%py_provides %oname
Requires: xmllint
%py_requires %mname kids.file kids.sh lxml kids.cache

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: libgpg-error python-base python-devel python-module-cssselect python-module-genshi python-module-kids python-module-kids.cache python-module-kids.test python-module-kids.txt python-module-lxml python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-cssselect python3-module-genshi python3-module-kids python3-module-kids.txt python3-module-lxml python3-module-pytest python3-module-setuptools xz
BuildRequires: git-core python-module-coverage python-module-d2to1 python-module-html5lib python-module-kids.file python-module-kids.sh python-module-nose python-module-setuptools-tests python3-module-coverage python3-module-d2to1 python3-module-html5lib python3-module-kids.cache python3-module-kids.file python3-module-kids.sh python3-module-kids.test python3-module-nose python3-module-setuptools-tests rpm-build-python3 time xml-utils

%description
kids.xml is a Python library providing helpers when writing xml thingy
in python.

It's part of 'Kids' (for Keep It Dead Simple) library.

%package -n python3-module-%oname
Summary: Kids XML library
Group: Development/Python3
%py3_provides %oname
Requires: xmllint
%py3_requires %mname kids.file kids.sh lxml kids.cache

%description -n python3-module-%oname
kids.xml is a Python library providing helpers when writing xml thingy
in python.

It's part of 'Kids' (for Keep It Dead Simple) library.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version -m "%version"

%if_with python3
cp -fR . ../python3
%endif

%build
./autogen.sh
%python_build_debug

%if_with python3
pushd ../python3
./autogen.sh
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

%check
python setup.py test
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.rst TODO
%python_sitelibdir/%mname/xml
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst TODO
%python3_sitelibdir/%mname/xml
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.git20150205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.git20150205.1
- NMU: Use buildreq for BR.

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20150205
- Initial build for Sisyphus

