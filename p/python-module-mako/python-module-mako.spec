%define oname mako

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt1.1
Summary: template library written in Python

Group: Development/Python
License: MIT
Url: http://www.makotemplates.org

Source: %name-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

# Fix #23203
Requires: python-module-beaker

BuildArch: noarch
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3 time

#BuildRequires: python-module-setuptools python-module-markupsafe
%if_with python3
#BuildRequires: /usr/bin/2to3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python3-module-markupsafe
%endif

%description
Mako is a template library written in Python. It provides a familiar,
non-XML syntax which compiles into Python modules for maximum
performance. Mako's syntax and API borrows from the best ideas of many
others, including Django templates, Cheetah, Myghty, and Genshi.
Conceptually, Mako is an embedded Python (i.e. Python Server Page)
language, which refines the familiar ideas of componentized layout and
inheritance to produce one of the most straightforward and flexible
models available, while also maintaining close ties to Python calling
and scoping semantics.

%if_with python3
%package -n python3-module-%oname
Summary: template library written in Python 3
Group: Development/Python3
Requires: python3-module-beaker

%description -n python3-module-%oname
Mako is a template library written in Python. It provides a familiar,
non-XML syntax which compiles into Python modules for maximum
performance. Mako's syntax and API borrows from the best ideas of many
others, including Django templates, Cheetah, Myghty, and Genshi.
Conceptually, Mako is an embedded Python (i.e. Python Server Page)
language, which refines the familiar ideas of componentized layout and
inheritance to produce one of the most straightforward and flexible
models available, while also maintaining close ties to Python calling
and scoping semantics.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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
mv %buildroot%_bindir/mako-render %buildroot%_bindir/mako-render3
2to3 -wn %buildroot%_bindir/mako-render3
%endif
%python_install

%files
%_bindir/mako-render
%python_sitelibdir/mako
%python_sitelibdir/Mako-%version-*
%doc CHANGES LICENSE README*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES LICENSE README*
%_bindir/mako-render3
%python3_sitelibdir/mako
%python3_sitelibdir/Mako-%version-*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1.1
- NMU: Use buildreq for BR.

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Version 1.0.1

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Wed Apr 17 2013 Fr. Br. George <george@altlinux.ru> 0.7.3-alt1.1
- Fix build with 2to3

* Wed Feb 20 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7.3-alt1
- Version 0.7.3

* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Version 0.7.0
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.0-alt1.1
- Rebuild with Python-2.7

* Tue Mar 01 2011 Vladimir Lettiev <crux@altlinux.ru> 0.4.0-alt1
- New version 0.4.0

* Sat Nov 20 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.6-alt1
- New version 0.3.6

* Fri Oct 22 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.5-alt1
- New version 0.3.5

* Tue Jun 29 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.4-alt1
- New version 0.3.4

* Sat Jun 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.3-alt1
- New version 0.3.3

* Thu Apr 15 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.2-alt2
- added python-module-beaker to requires (Closes: #23203)

* Mon Mar 15 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.2-alt1
- New version 0.3.2

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.1
- Rebuilt with python 2.6

* Sun Oct 18 2009 Vladimir Lettiev <crux@altlinux.ru> 0.2.5-alt1
- initial build

