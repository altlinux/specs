# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt3.git20121222.1.1
%define mname cairo
%define oname py%mname
Name: python3-module-%oname
Version: 1.10.1
#Release: alt3.git20121222.1

Summary: Pycairo is a set of Python bindings for the vector graphics library cairo

License: GPL
Group: Development/Python3
Url: http://www.cairographics.org/pycairo

# git://git.cairographics.org/git/pycairo
Source: pycairo-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libcairo-devel python3-devel
BuildPreReq: python3-module-sphinx-devel python3-module-Pygments
BuildPreReq: texlive-latex-base python-tools-2to3
BuildPreReq: python3-module-distribute

%py3_provides %mname

%description
James Henstridge has created cairo bindings for Python.
Cairo is a library for drawing vector graphics.
Vector graphics are interesting because when they appear on screen,
they don't lose clarity when resized or transformed.

%package devel
Summary: Development files for pycairo
Group: Development/Python3
Requires: %name = %version-%release

%description devel
Development files for pycairo.

%package docs
Summary: Documentation for pycairo
Group: Development/Documentation
BuildArch: noarch

%description docs
Documentation for pycairo.

%package tests
Summary: Tests for pycairo
Group: Development/Python3
Requires: %name = %version-%release
%add_python3_req_skip pygame
%py3_requires pytest numpy

%description tests
Documentation for pycairo.

%package pickles
Summary: Pickles for pycairo
Group: Development/Python3

%description pickles
Pickles for pycairo.

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv doc/

%build
%python3_build_debug

pushd doc
%make_build pickle
%make_build html
popd

%install
%python3_install

%if "%python3_sitelibdir_noarch/%mname" != "%python3_sitelibdir/%mname"
install -d %buildroot%_pkgconfigdir
mv %buildroot%_libexecdir/pkgconfig/* %buildroot%_pkgconfigdir/
mv %buildroot%python3_sitelibdir_noarch/%mname/* \
	%buildroot%python3_sitelibdir/%mname/
%endif

# docs

install -d %buildroot%_docdir/%name-%version
install -p -m644 AUTHORS COPYING* NEWS README RELEASING \
	%buildroot%_docdir/%name-%version

cp -fR doc/_build/html %buildroot%_docdir/%name-%version/

# pickles

cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%mname/

# tests

find test -type f -name '*.py' -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find test -type f -name '*.py' -exec 2to3 -w -n '{}' +
cp -fR test %buildroot%python3_sitelibdir/%mname/
for i in $(find %buildroot%python3_sitelibdir/%mname/test -type d)
do
	touch $i/__init__.py
done

#export LC_ALL=en_US.iso885915
export LC_ALL=en_US.UTF-8

%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/AUTHORS
%doc %_docdir/%name-%version/COPYING*
%doc %_docdir/%name-%version/NEWS
%doc %_docdir/%name-%version/README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%mname/test
%exclude %python3_sitelibdir/%mname/pickle

%files devel
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/RELEASING
%_includedir/*
%_pkgconfigdir/*

%files docs
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version
%exclude %_docdir/%name-%version/AUTHORS
%exclude %_docdir/%name-%version/COPYING*
%exclude %_docdir/%name-%version/NEWS
%exclude %_docdir/%name-%version/README
%exclude %_docdir/%name-%version/RELEASING

%files tests
%python3_sitelibdir/%mname/test

%files pickles
%dir %python3_sitelibdir/%mname
%python3_sitelibdir/%mname/pickle

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.1-alt3.git20121222.1.1
- (AUTO) subst_x86_64.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.1-alt3.git20121222.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt3.git20121222
- New snapshot

* Tue Feb 19 2013 Aleksey Avdeev <solo@altlinux.ru> 1.10.1-alt3.git20120819.1
- Fix build with Python 3.3

* Thu Oct 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt3.git20120819
- New snapshot

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt3.git20120505
- Fixed build

* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt2.git20120505
- Rebuilt

* Sat May 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1.git20120505
- Initial build for Sisyphus (bootstrap)

