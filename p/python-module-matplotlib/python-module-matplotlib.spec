# TODO: fix dest on x86_64
# TODO: Move mpl-data to share?

%define oname matplotlib
%define major 1.2

%def_enable docs
%def_with python3

Name: python-module-%oname
Version: %major.0
Release: alt2.git20120608

Summary: Matlab(TM) style python plotting package

License: see LICENSE
Group: Development/Python
Url: http://matplotlib.sourceforge.net

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://matplotlib.svn.sourceforge.net/svnroot/matplotlib/trunk
Source: %oname-%version.tar
Source1: setup.cfg

%setup_python_module pylab

BuildPreReq: python-module-matplotlib python-module-numpydoc ipython 
BuildRequires: dvipng gcc-c++ libgtk+2-devel python-module-PyQt4
BuildPreReq: python-module-ctypes python-module-pygtk_git-devel
BuildPreReq: python-module-qt python-module-wx2.9 graphviz
BuildPreReq: python-modules-encodings python-modules-tkinter
BuildPreReq: rpm-build-java rpm-build-mono rpm-build-seamonkey
BuildPreReq: texlive-latex-base tk-devel xorg-sdk xpdf
BuildPreReq: libnumpy-devel latex2html texlive-latex-recommended
BuildPreReq: linuxdoc-tools python-module-sphinx-devel
BuildPreReq: libgeos-devel python-module-geos zlib-devel
BuildPreReq: python-module-scipy-devel rpm-macros-make
BuildPreReq: libpng-devel libfreetype-devel
BuildPreReq: python-module-pytz python-module-dateutil
BuildPreReq: python-module-markupsafe strace libgtk+3-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel libnumpy-py3-devel python-tools-2to3
BuildPreReq: python3-module-scipy-devel python3-module-markupsafe
BuildPreReq: python3-module-pytz python3-module-dateutil
BuildPreReq: python3-module-PyQt4-devel python3-module-PySide
BuildPreReq: python3-module-pycairo python3-module-pygobject3-devel
%endif

#Requires: dvipng %name-gtk = %version-%release
Requires: dvipng %name-gtk3 = %version-%release

# hack for unknown deps
%add_python_req_skip AppKit Foundation PyObjCTools numarray paint _Py
%add_python_req_skip _winreg builtins
%py_provides backend_agg backend_cairo
#%py_package_provides backend_agg

%description
matplotlib is a pure python 2D plotting library with a Matlab(TM)
syntax which produces publication quality figures using in a
variety of hardcopy formats (PNG, JPG, TIFF, PS) and interactive
GUI environments (WX, GTK) across platforms. matplotlib can be used
in python scripts, interactively from the python shell (ala matlab
or mathematica), in web application servers generating dynamic
charts, or embedded in GTK or WX applications; see backends.

%if_with python3
%package -n python3-module-%oname
Summary: Matlab(TM) style python 3 plotting package
Group: Development/Python3
Requires: dvipng
Requires: python3-module-%oname-gtk3 = %version-%release
%add_python3_req_skip AppKit Foundation PyObjCTools numarray paint _Py
%add_python3_req_skip _winreg builtins
%py3_provides backend_agg backend_cairo

%description -n python3-module-%oname
matplotlib is a pure python 2D plotting library with a Matlab(TM)
syntax which produces publication quality figures using in a
variety of hardcopy formats (PNG, JPG, TIFF, PS) and interactive
GUI environments (WX, GTK) across platforms. matplotlib can be used
in python scripts, interactively from the python shell (ala matlab
or mathematica), in web application servers generating dynamic
charts, or embedded in GTK or WX applications; see backends.

%package -n python3-module-%oname-tests
Summary: Tests for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Tests for %oname.

%package -n python3-module-%oname-fltk
Summary: fltk backend for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-fltk
fltk backend for %oname.

%package -n python3-module-%oname-qt4
Summary: qt4 backend for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-qt4
qt4 backend for %oname.

%package -n python3-module-%oname-qt
Summary: qt backend for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-qt
qt backend for %oname.

%package -n python3-module-%oname-gtk
Summary: gtk backend for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%add_python3_req_skip gtk_git pango_git

%description -n python3-module-%oname-gtk
gtk backend for %oname.

%package -n python3-module-%oname-gtk3
Summary: gtk3 backend for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-gtk3
gtk3 backend for %oname.

%package -n python3-module-%oname-wx
Summary: wx backend for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-wx
ex backend for %oname.

%package -n python3-module-%oname-tk
Summary: tk backend for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tk
tk backend for %oname.

%package -n python3-module-%oname-sphinxext
Summary: sphinxext extension for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-sphinxext
sphinxext extension for %oname.
%endif

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %version-%release

%description tests
Tests for %oname.

%package examples
Summary: Example files for %oname
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description examples
Example files for %oname.

%if_enabled docs

%package other-docs
Summary: Some addition documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description other-docs
Some addition documentation for %oname.

%package doc-html
Summary: Documentation for %oname in HTML
Group: Development/Documentation

%description doc-html
Documentation for %oname in HTML.

%package doc-pdf
Summary: Documentation for %oname in PDF
Group: Development/Documentation

%description doc-pdf
Documentation for %oname in PDF.

%package pickles
Summary: Pickles for %oname
Group: Development/Python
AutoReqProv: yes,nopython

%description pickles
Pickles for %oname.

%endif

%package fltk
Summary: fltk backend for %oname
Group: Development/Python
Requires: %name = %version-%release

%description fltk
fltk backend for %oname.

%package qt4
Summary: qt4 backend for %oname
Group: Development/Python
Requires: %name = %version-%release

%description qt4
qt4 backend for %oname.

%package qt
Summary: qt backend for %oname
Group: Development/Python
Requires: %name = %version-%release

%description qt
qt backend for %oname.

%package gtk
Summary: gtk backend for %oname
Group: Development/Python
Requires: %name = %version-%release

%description gtk
gtk backend for %oname.

%package gtk3
Summary: gtk3 backend for %oname
Group: Development/Python
Requires: %name = %version-%release

%description gtk3
gtk3 backend for %oname.

%package wx
Summary: wx backend for %oname
Group: Development/Python
Requires: %name = %version-%release

%description wx
ex backend for %oname.

%package tk
Summary: tk backend for %oname
Group: Development/Python
Requires: %name = %version-%release

%description tk
tk backend for %oname.

%package sphinxext
Summary: sphinxext extension for %oname
Group: Development/Python
Requires: %name = %version-%release

%description sphinxext
sphinxext extension for %oname.


%prep
%setup
subst "s,/usr/lib/,%_libdir/,g" setupext.py

sed -i "s|@TOP@|$PWD|" doc/conf.py \

%if_enabled docs
%prepare_sphinx .
%endif

install -p -m644 %SOURCE1 .

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.h') \
	 $(find ./ -name '*.c') \
	 $(find ./ -name '*.cpp')
do
	sed -i 's|\(include.*numpy\)/|\1-py3/|' $i
done
sed -i 's|^\(gtkagg\).*|\1 = False|' setup.cfg
sed -i 's|import xlwt|import xlwt3|' lib/mpl_toolkits/exceltools.py
export CC=g++
%python3_build_debug
popd
%endif

%python_build_debug

%install
%if_with python3
pushd ../python3
%python3_install

subst "s|WXAgg|GTK3Agg|g" \
	%buildroot%python3_sitelibdir/%oname/mpl-data/matplotlibrc

export PYTHONPATH=%buildroot%python3_sitelibdir

# TODO: breaks something?
# matplotlib can use system fonts, so drop these copies (thanks, PLD)
#rm -f %buildroot%python3_sitelibdir/matplotlib/mpl-data/Vera*.ttf

sed -i 's|^\(backend\).*|\1 : GTK3Agg|' \
	%buildroot%python3_sitelibdir/%oname/mpl-data/matplotlibrc

# fonts

%define reduce_fonts cmex10.ttf cmmi10.ttf cmr10.ttf cmsy10.ttf

#pushd %buildroot%python3_sitelibdir/%oname/mpl-data/fonts/ttf
#for i in %reduce_fonts
#do
#	rm -f $i
#	ln -s %_datadir/fonts/ttf/reduce/$i .
#done
#for i in Vera*.ttf
#do
#	rm -f $i
#	ln -s /usr/share/fonts/ttf/TrueType-vera/$i .
#done
#popd

popd
%endif

%python_install

# Use gtk by default
subst "s|WXAgg|GTK3Agg|g" \
	%buildroot%python_sitelibdir/%oname/mpl-data/matplotlibrc

export PYTHONPATH=%buildroot%python_sitelibdir

# doc

%if_enabled docs
pushd doc
./make.py html
./make.py latex
sphinx-build -b pickle -d build/doctrees . build/pickle
popd
%endif

install -d %buildroot%_docdir/%name/pdf
cp -fR examples LICENSE %buildroot%_docdir/%name/
install -p -m644 README.txt CHANGELOG INSTALL TODO \
	%buildroot%_docdir/%name

%if_enabled docs
cp -fR doc/build/html %buildroot%_docdir/%name/
cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/
cp -fR doc/build/latex/*.pdf %buildroot%_docdir/%name/pdf/
%endif

# TODO: breaks something?
# matplotlib can use system fonts, so drop these copies (thanks, PLD)
#rm -f %buildroot%python_sitelibdir/matplotlib/mpl-data/Vera*.ttf

sed -i 's|^\(backend\).*|\1 : GTK3Agg|' \
	%buildroot%python_sitelibdir/%oname/mpl-data/matplotlibrc

# fonts

%define reduce_fonts cmex10.ttf cmmi10.ttf cmr10.ttf cmsy10.ttf

#pushd %buildroot%python_sitelibdir/%oname/mpl-data/fonts/ttf
#for i in %reduce_fonts
#do
#	rm -f $i
#	ln -s %_datadir/fonts/ttf/reduce/$i .
#done
#for i in Vera*.ttf
#do
#	rm -f $i
#	ln -s /usr/share/fonts/ttf/TrueType-vera/$i .
#done
#popd

%pre
rm -f %python_sitelibdir/%oname/mpl-data/fonts/ttf/Vera*.ttf
for i in %reduce_fonts
do
	rm -f %python_sitelibdir/%oname/mpl-data/fonts/ttf/$i
done

%files
%doc %dir %_docdir/%name
%doc %_docdir/%name/LICENSE
%doc %_docdir/%name/README.txt
%doc %_docdir/%name/CHANGELOG
%doc %_docdir/%name/INSTALL
%doc %_docdir/%name/TODO
%python_sitelibdir/*.py*
%python_sitelibdir/*.egg-info
%dir %python_sitelibdir/matplotlib/
%python_sitelibdir/matplotlib/*.py*
%python_sitelibdir/matplotlib/*.so
%dir %python_sitelibdir/matplotlib/backends/__init__.*
#python_sitelibdir/matplotlib/numerix/
%python_sitelibdir/mpl_toolkits/
%python_sitelibdir/matplotlib/projections/
%python_sitelibdir/matplotlib/delaunay/
%python_sitelibdir/matplotlib/mpl-data/
#%python_sitelibdir/matplotlib/config/
#%python_sitelibdir/enthought/
%python_sitelibdir/matplotlib/backends/Matplotlib.nib/
%dir %python_sitelibdir/matplotlib/backends/
%python_sitelibdir/matplotlib/backends/backend_agg*
%python_sitelibdir/matplotlib/backends/*_agg.so
%python_sitelibdir/matplotlib/backends/backend_template*
%python_sitelibdir/matplotlib/backends/backend_mixed*
%python_sitelibdir/matplotlib/backends/backend_svg*
#%python_sitelibdir/matplotlib/backends/backend_gd.py*
%python_sitelibdir/matplotlib/backends/backend_pdf*
%python_sitelibdir/matplotlib/backends/backend_ps*
%python_sitelibdir/matplotlib/backends/backend_cairo*
%python_sitelibdir/matplotlib/backends/backend_emf*
%python_sitelibdir/matplotlib/backends/backend_cocoa*
%python_sitelibdir/matplotlib/tri

%files fltk
%python_sitelibdir/matplotlib/backends/backend_fltk*

#files gtk
#python_sitelibdir/matplotlib/backends/backend_gtk*
#python_sitelibdir/matplotlib/backends/backend_gdk*
#python_sitelibdir/matplotlib/backends/*gdk*.so
#python_sitelibdir/matplotlib/backends/_gtk*.so
#python_sitelibdir/matplotlib/backends/backend_gdk.py*

%files gtk3
%python_sitelibdir/matplotlib/backends/backend_gtk3*

%files qt
%python_sitelibdir/matplotlib/backends/backend_qt.*
%python_sitelibdir/matplotlib/backends/backend_qtagg*

%files wx
%python_sitelibdir/matplotlib/backends/backend_wx*
#%python_sitelibdir/matplotlib/backends/_wx*

# problem with checking?
%files tk
%python_sitelibdir/matplotlib/backends/backend_tk*
%python_sitelibdir/matplotlib/backends/tk*
%python_sitelibdir/matplotlib/backends/_tkagg*

%files qt4
%python_sitelibdir/matplotlib/backends/backend_qt4*
%python_sitelibdir/matplotlib/backends/qt4_compat.*
%python_sitelibdir/matplotlib/backends/qt4_editor

%files examples
%doc %dir %_docdir/%name
%doc %_docdir/%name/examples

%if_enabled docs
#files other-docs
#doc %dir %_docdir/%name
#doc %_docdir/%name/py4science
#doc %_docdir/%name/sample_data

%files doc-html
%doc %dir %_docdir/%name
%doc %_docdir/%name/html

%pre doc-pdf
rm -fR %_docdir/%name/pdf

%files doc-pdf
%doc %dir %_docdir/%name
%doc %_docdir/%name/pdf

%files pickles
%python_sitelibdir/%oname/pickle
%endif

%files tests
%python_sitelibdir/%oname/testing
%python_sitelibdir/%oname/tests

%files sphinxext
%python_sitelibdir/%oname/sphinxext

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.txt CHANGELOG INSTALL TODO
%python3_sitelibdir/*.py*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/*.egg-info
%dir %python3_sitelibdir/matplotlib/
%python3_sitelibdir/matplotlib/*.py*
%python3_sitelibdir/matplotlib/*.so
%python3_sitelibdir/matplotlib/__pycache__
%dir %python3_sitelibdir/matplotlib/backends/__init__.*
#python_sitelibdir/matplotlib/numerix/
%python3_sitelibdir/mpl_toolkits/
%python3_sitelibdir/matplotlib/projections/
%python3_sitelibdir/matplotlib/delaunay/
%python3_sitelibdir/matplotlib/mpl-data/
#%python3_sitelibdir/matplotlib/config/
#%python3_sitelibdir/enthought/
%python3_sitelibdir/matplotlib/backends/Matplotlib.nib/
%dir %python3_sitelibdir/matplotlib/backends/
%python3_sitelibdir/matplotlib/backends/backend_agg*
%python3_sitelibdir/matplotlib/backends/*_agg.*.so
%python3_sitelibdir/matplotlib/backends/backend_template*
%python3_sitelibdir/matplotlib/backends/backend_mixed*
%python3_sitelibdir/matplotlib/backends/backend_svg*
#%python_sitelibdir/matplotlib/backends/backend_gd.py*
%python3_sitelibdir/matplotlib/backends/backend_pdf*
%python3_sitelibdir/matplotlib/backends/backend_ps*
%python3_sitelibdir/matplotlib/backends/backend_cairo*
%python3_sitelibdir/matplotlib/backends/backend_emf*
%python3_sitelibdir/matplotlib/backends/backend_cocoa*
%dir %python3_sitelibdir/matplotlib/backends/__pycache__
%python3_sitelibdir/matplotlib/backends/__pycache__/*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_fltk*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_gtk*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_gdk*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_qt.*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_qtagg*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_wx*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_tk*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/tk*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_qt4*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/qt4_compat.*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_macosx.*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/windowing.*
%python3_sitelibdir/matplotlib/tri

%files -n python3-module-%oname-fltk
%python3_sitelibdir/matplotlib/backends/backend_fltk*
%python3_sitelibdir/matplotlib/backends/__pycache__/backend_fltk*

%files -n python3-module-%oname-gtk3
%python3_sitelibdir/matplotlib/backends/backend_gtk3*
%python3_sitelibdir/matplotlib/backends/__pycache__/backend_gtk3*

%files -n python3-module-%oname-qt
%python3_sitelibdir/matplotlib/backends/backend_qt.*
%python3_sitelibdir/matplotlib/backends/__pycache__/backend_qt.*
%python3_sitelibdir/matplotlib/backends/backend_qtagg*
%python3_sitelibdir/matplotlib/backends/__pycache__/backend_qtagg*

#files -n python3-module-%oname-wx
#python3_sitelibdir/matplotlib/backends/backend_wx*
#python3_sitelibdir/matplotlib/backends/__pycache__/backend_wx*

%files -n python3-module-%oname-tk
%python3_sitelibdir/matplotlib/backends/backend_tk*
%python3_sitelibdir/matplotlib/backends/__pycache__/backend_tk*
%python3_sitelibdir/matplotlib/backends/tk*
%python3_sitelibdir/matplotlib/backends/__pycache__/tk*
%python3_sitelibdir/matplotlib/backends/_tkagg*

%files -n python3-module-%oname-qt4
%python3_sitelibdir/matplotlib/backends/backend_qt4*
%python3_sitelibdir/matplotlib/backends/__pycache__/backend_qt4*
%python3_sitelibdir/matplotlib/backends/qt4_compat.*
%python3_sitelibdir/matplotlib/backends/__pycache__/qt4_compat.*
%python3_sitelibdir/matplotlib/backends/qt4_editor

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/testing
%python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-sphinxext
%python3_sitelibdir/%oname/sphinxext
%endif

%changelog
* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2.git20120608
- New snapshot
- Fixed Cairo and FltkAgg backends
- Set GTK3Agg as default backend

* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2.git20120505
- Added module for Python 3

* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20120505
- Version 1.2.x

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt3.svn20110218.1
- Rebuild to remove redundant libpython2.7 dependency

* Tue Nov 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt3.svn20110218
- Fixed upgrade

* Sun Nov 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2.svn20110218
- Enabled docs (except pdf generating)

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1.svn20110218.2.1
- Rebuild with Python-2.7

* Wed Oct 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.svn20110218.2
- Rebuilt with updated NumPy

* Mon Jul 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.svn20110218.1
- Rebuilt with updated NumPy

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.svn20110218
- Version 1.1.0

* Sat Apr 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100609.9
- Replaced font by links to fonts from fonts-ttf-vera and
  fonts-ttf-reduce (ALT #25327)

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100609.8
- No strict-aliasing rules

* Wed Mar 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100609.7
- Rebuilt with linuxdoc-tools instead of sgml-tools

* Tue Mar 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100609.6
- Added -g into compiler flags
- Added sphinxext extension

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100609.5
- Rebuilt for debuginfo

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100609.4
- Rebuilt for soname set-versions

* Tue Sep 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100609.3
- Added requirement on dvipng
- Set default backend to GTKAgg (ALT #24108)

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100609.2
- Rebuilt with python-module-wx2.9

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100609.1
- Added matplotlib.tri

* Wed Jun 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100609
- Version 1.0

* Fri Apr 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.1.2-alt1.svn20100401.1
- Rebuilt with NumPy
- Rebuilt with new NumPy

* Tue Mar 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.1.2-alt1.svn20100209.2
- Rebuilt with pygtk_git instead of pygtk

* Thu Feb 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.1.2-alt1.svn20100209.1
- Set examples as noarch

* Wed Feb 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.1.2-alt1.svn20100209
- New snapshot
- Refored using of git-svn (trunk instead full repository)

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.1.2-alt1.svn20100204
- New snapshot
- Extracted tests into separate package
- Added:
  + documentation (HTML, PDF and other too)
  + pickles package

* Sat Jan 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.1.2-alt1.svn20100102
- Version 0.99.1.2
- Rebuilt with texlive instead of tetex

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.0-alt2.1
- Rebuilt with python 2.6

* Fri Sep 04 2009 Vitaly Lipatov <lav@altlinux.ru> 0.99.0-alt2
- rebuild with new numpy (bug #21410)

* Wed Aug 26 2009 Vitaly Lipatov <lav@altlinux.ru> 0.99.0-alt1
- new version (0.99.0) 

* Sun Jul 12 2009 Vitaly Lipatov <lav@altlinux.ru> 0.98.5.3-alt1
- new version 0.98.5.3 (with rpmrb script)

* Wed Feb 18 2009 Vitaly Lipatov <lav@altlinux.ru> 0.98.3-alt3
- fix build on x86_64 (thanks to Dmitry Levin)

* Sun Nov 30 2008 Vitaly Lipatov <lav@altlinux.ru> 0.98.3-alt2
- fix enthought requires

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.98.3-alt1
- new version 0.98.3 (with rpmrb script)

* Mon Mar 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.91.2-alt1
- new version 0.91.2
- update buildreqs, fix packing

* Fri Feb 01 2008 Grigory Batalov <bga@altlinux.ru> 0.90.1-alt1.1
- Rebuilt with python-2.5.

* Sat Oct 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.90.1-alt1
- new version 0.90.1 (with rpmrb script)

* Sun Feb 25 2007 Vitaly Lipatov <lav@altlinux.ru> 0.90.0-alt1
- new version 0.90.0, update buildreq
- enable qt4 backend build
- disable wx backend build (no longer supported by mainstream)

* Mon Dec 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.87.7-alt1
- add missed backends dir
- move backend_gdk to gtk package
- set gtk backend by default (see mpl-data/matplotlibrc)

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.87.7-alt0.1
- new version 0.87.7
- build with numpy 1.0
- split backends by subpackages
- disable qt4, tk backends

* Wed Jun 07 2006 Vitaly Lipatov <lav@altlinux.ru> 0.87.2-alt0.2
- fix requires

* Wed Jun 07 2006 Vitaly Lipatov <lav@altlinux.ru> 0.87.2-alt0.1
- initial build for ALT Linux Sisyphus
