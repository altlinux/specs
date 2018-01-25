# TODO: fix dest on x86_64
# TODO: Move mpl-data to share?
# TODO: gtk3 knob too?

%define oname matplotlib
%define major 2.0

%def_disable docs
%def_with python3
%def_with qt4
%def_with qt5
%def_with wx

Name: python-module-%oname
Version: %major.0
Release: alt7

Summary: Matlab(TM) style python plotting package

License: see LICENSE
Group: Development/Python
Url: http://matplotlib.sourceforge.net
# https://github.com/matplotlib/matplotlib.git
Packager: Python Development Team <python@packages.altlinux.org>

Source: %oname-%version.tar
Source1: setup.cfg

%setup_python_module pylab

BuildRequires(pre): rpm-build-gir
BuildRequires: gcc-c++ git-core libnumpy-devel time tk-devel libgtk+3-gir-devel libpng-devel libfreetype-devel
BuildRequires: python-module-pycairo python-module-pygobject3 python-modules-tkinter python-module-cycler python-module-pyparsing python-module-pytz python-module-dateutil
%{?!_without_check:BuildRequires: python-module-numpy-testing}
%{?_with_qt4:BuildRequires: python-module-PyQt4}
%{?_with_qt5:BuildRequires: python-module-PyQt5}
%{?_with_wx:BuildRequires: python-module-wx}
Requires: %name-gtk3

%if_with docs
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-html5lib 
%endif #docs

%if_with python3
BuildRequires(pre): rpm-build-python3 python3-devel 
BuildRequires: python3-module-numpy-testing python3-module-pycairo python3-module-pygobject3 python3-modules-tkinter python3-module-cycler python3-module-pyparsing python3-module-pytz python3-module-dateutil
%{?_with_qt4:BuildRequires: python3-module-PyQt4}
%{?_with_qt5:BuildRequires: python3-module-PyQt5}
%endif #python3

# hack for unknown deps
%add_python_req_skip AppKit Foundation PyObjCTools numarray paint _Py
%add_python_req_skip _winreg builtins
#py_provides backend_agg
%py_requires functools32
%py_requires numpy pytz six subprocess32

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
Requires: python3-module-%oname-gtk3
Requires: python3-module-mpl_toolkits = %EVR
%add_python3_req_skip AppKit Foundation PyObjCTools numarray paint _Py
%add_python3_req_skip _winreg builtins distutils
#add_python3_req_skip IPython.display  #needed matplotlib.backends.backend_nbagg
#py3_provides backend_agg
#py3_provides matplotlib.externals.six.moves
#py3_provides matplotlib.externals.six.moves.urllib.parse
#py3_provides matplotlib.externals.six.moves.urllib.request
%py3_requires pytz

%description -n python3-module-%oname
matplotlib is a pure python 2D plotting library with a Matlab(TM)
syntax which produces publication quality figures using in a
variety of hardcopy formats (PNG, JPG, TIFF, PS) and interactive
GUI environments (WX, GTK) across platforms. matplotlib can be used
in python scripts, interactively from the python shell (ala matlab
or mathematica), in web application servers generating dynamic
charts, or embedded in GTK or WX applications; see backends.

%package -n python3-module-%oname-cairo
Summary: Cairo backend for %oname
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
#py3_provides backend_cairo
%py3_requires cairo

%description -n python3-module-%oname-cairo
Cairo backend for %oname.

%package -n python3-module-%oname-nbagg
Summary: Interactive figures in the IPython notebook
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-nbagg
Interactive figures in the IPython notebook.

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

%package -n python3-module-%oname-qt5
Summary: qt5 backend for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires PyQt5
#fix me!!!
Requires: python3-module-%oname-qt4 = %version-%release

%description -n python3-module-%oname-qt5
qt5 backend for %oname.

%package -n python3-module-%oname-qt4
Summary: qt4 backend for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires PyQt4
#fix me!!!
#matplotlib.backends.backend_qt4* needed import matplotlib.backends.backend_qt5
Requires: python3-module-%oname-qt5 = %version-%release

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
Requires: typelib(Gtk) = 2.0
Requires: python3-module-%oname-cairo = %version-%release
%add_python3_req_skip gtk_git pango_git

%description -n python3-module-%oname-gtk
gtk backend for %oname.

%package -n python3-module-%oname-gtk3
Summary: gtk3 backend for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname-cairo = %version-%release
Requires: typelib(Gtk) = 3.0
Requires: python3-module-pygobject3

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
%py3_requires _tkinter

%description -n python3-module-%oname-tk
tk backend for %oname.

%package -n python3-module-%oname-sphinxext
Summary: sphinxext extension for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-sphinxext
sphinxext extension for %oname.

%package -n python3-module-mpl_toolkits
Summary: mpl_toolkits extension for %oname
Group: Development/Python3

%description -n python3-module-mpl_toolkits
mpl_toolkits extension for %oname.

%package -n python3-module-mpl_toolkits-tests
Summary: Tests for mpl_toolkits
Group: Development/Python3
Requires: python3-module-mpl_toolkits = %version-%release
Requires: python3-module-%oname-tests = %version-%release

%description -n python3-module-mpl_toolkits-tests
Tests for mpl_toolkits.
%endif #python3

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

%package fltk
Summary: fltk backend for %oname
Group: Development/Python
Requires: %name = %version-%release

%description fltk
fltk backend for %oname.

%package qt5
Summary: qt5 backend for %oname
Group: Development/Python
Requires: %name = %version-%release
%py_requires PyQt5
#fix me!!!
Requires: %name-qt5 = %version-%release

%description qt5
qt5 backend for %oname.

%package qt4
Summary: qt4 backend for %oname
Group: Development/Python
Requires: %name = %version-%release
%py_requires PyQt4
#fix me!!!
#matplotlib.backends.backend_qt4* needed matplotlib.backends.backend_qt5
Requires: %name-qt5 = %version-%release

%description qt4
qt4 backend for %oname.

%package qt
Summary: qt backend for %oname
Group: Development/Python
Requires: %name = %version-%release

%description qt
qt backend for %oname.

%package cairo
Summary: Cairo backend for %oname
Group: Development/Python
Requires: %name = %version-%release
#py_provides backend_cairo
%py_requires cairo

%description cairo
Cairo backend for %oname.

%package nbagg
Summary: Interactive figures in the IPython notebook
Group: Development/Python3
Requires: %name = %version-%release

%description nbagg
Interactive figures in the IPython notebook.

%package gtk
Summary: gtk backend for %oname
Group: Development/Python
Requires: %name-cairo = %version-%release
Requires: typelib(Gtk) = 2.0

%description gtk
gtk backend for %oname.

%package gtk3
Summary: gtk3 backend for %oname
Group: Development/Python
Requires: %name-cairo = %version-%release
Requires: typelib(Gtk) = 3.0
Requires: python-module-pygobject3

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
%py_requires _tkinter

%description tk
tk backend for %oname.

%package sphinxext
Summary: sphinxext extension for %oname
Group: Development/Python
Requires: %name = %version-%release

%description sphinxext
sphinxext extension for %oname.

%package -n python-module-mpl_toolkits
Summary: mpl_toolkits extension for %oname
Group: Development/Python

%description -n python-module-mpl_toolkits
mpl_toolkits extension for %oname.

%package -n python-module-mpl_toolkits-tests
Summary: Tests for mpl_toolkits
Group: Development/Python
Requires: python-module-mpl_toolkits
Requires: %name-tests = %version-%release

%description -n python-module-mpl_toolkits-tests
Tests for mpl_toolkits.

%prep
%setup
subst "s,/usr/lib/,%_libdir/,g" setupext.py

sed -i "s|@TOP@|$PWD|" doc/conf.py \

%if_enabled docs
%prepare_sphinx .
%endif

install -p -m644 %SOURCE1 .

git config --global user.email "<python@packages.altlinux.org>"
git config --global user.name "Python Development Team"
git init-db
git add . -A
git commit -a -m "REL: v%version"
git tag -m "v%version" v%version

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
%endif

%build
#export XDG_RUNTIME_DIR=%_xdgdatadir
%add_optflags -fno-strict-aliasing -fpermissive
%if_with python3
pushd ../python3
#sed -i 's|^\(gtkagg\).*|\1 = False|' setup.cfg
#sed -i 's|^\(gtk3agg\).*|\1 = False|' setup.cfg
#sed -i 's|^\(tkagg\).*|\1 = False|' setup.cfg
sed -i 's|^\(wxagg\).*|\1 = False|' setup.cfg
export CC=g++
%python3_build_debug
popd
%endif #python3

#sed -i 's|^\(gtk3agg\).*|\1 = False|' setup.cfg
%if_without wx
sed -i 's|^\(wxagg\).*|\1 = False|' setup.cfg
%endif
%python_build_debug

%install
#export XDG_RUNTIME_DIR=%_xdgdatadir
%if_with python3
pushd ../python3
%python3_install

cp -fR lib/mpl_toolkits %buildroot%python3_sitelibdir/

subst "s|WXAgg|GTK3Cairo|g" \
	%buildroot%python3_sitelibdir/%oname/mpl-data/matplotlibrc

export PYTHONPATH=%buildroot%python3_sitelibdir

# TODO: breaks something?
# matplotlib can use system fonts, so drop these copies (thanks, PLD)
#rm -f %buildroot%python3_sitelibdir/matplotlib/mpl-data/Vera*.ttf

sed -i 's|^\(backend\).*|\1 : GTK3Cairo|' \
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
%endif #python3

%python_install

cp -fR lib/mpl_toolkits %buildroot%python_sitelibdir/

# Use gtk by default
subst "s|WXAgg|GTK3Cairo|g" \
	%buildroot%python_sitelibdir/%oname/mpl-data/matplotlibrc

export PYTHONPATH=%buildroot%python_sitelibdir

# doc

%if_enabled docs
pushd doc
./make.py html
./make.py latex
sphinx-build -b pickle -d build/doctrees . build/pickle
popd
%endif #docs

install -d %buildroot%_docdir/%name/pdf
cp -fR examples LICENSE %buildroot%_docdir/%name/
install -p -m644 README.rst CHANGELOG INSTALL \
	%buildroot%_docdir/%name

%if_enabled docs
cp -fR doc/build/html %buildroot%_docdir/%name/
cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/
cp -fR doc/build/latex/*.pdf %buildroot%_docdir/%name/pdf/
%endif #docs

# TODO: breaks something?
# matplotlib can use system fonts, so drop these copies (thanks, PLD)
#rm -f %buildroot%python_sitelibdir/matplotlib/mpl-data/Vera*.ttf

sed -i 's|^\(backend\).*|\1 : GTK3Cairo|' \
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

#find %buildroot%python3_sitelibdir/ -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
#find %buildroot%python3_sitelibdir/ -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +

%pre
rm -f %python_sitelibdir/%oname/mpl-data/fonts/ttf/Vera*.ttf
for i in %reduce_fonts
do
	rm -f %python_sitelibdir/%oname/mpl-data/fonts/ttf/$i
done

%files
%doc %dir %_docdir/%name
%doc %_docdir/%name/LICENSE
%doc %_docdir/%name/README.rst
%doc %_docdir/%name/CHANGELOG
%doc %_docdir/%name/INSTALL
%python_sitelibdir/*.py*
%python_sitelibdir/*.egg-info
%dir %python_sitelibdir/matplotlib/
%python_sitelibdir/matplotlib-*-nspkg.pth
%python_sitelibdir/matplotlib/*.py*
%python_sitelibdir/matplotlib/*.so
#python_sitelibdir/matplotlib/numerix/
%python_sitelibdir/mpl_toolkits/
%python_sitelibdir/matplotlib/projections/
%python_sitelibdir/matplotlib/delaunay/
%python_sitelibdir/matplotlib/mpl-data/
#%python_sitelibdir/matplotlib/config/
#python_sitelibdir/enthought/
#python_sitelibdir/matplotlib/backends/Matplotlib.nib/
%python_sitelibdir/matplotlib/backends/
%exclude %python_sitelibdir/matplotlib/backends/backend_gtk*
%exclude %python_sitelibdir/matplotlib/backends/backend_gdk*
%exclude %python_sitelibdir/matplotlib/backends/backend_cairo*
%exclude %python_sitelibdir/matplotlib/backends/backend_wx*
%exclude %python_sitelibdir/matplotlib/backends/wx*
%exclude %python_sitelibdir/matplotlib/backends/backend_tk*
%exclude %python_sitelibdir/matplotlib/backends/tk*
%exclude %python_sitelibdir/matplotlib/backends/_tkagg*
%exclude %python_sitelibdir/matplotlib/backends/backend_qt?*
%exclude %python_sitelibdir/matplotlib/backends/qt*_compat.*
%exclude %python_sitelibdir/matplotlib/backends/backend_macosx.*
%exclude %python_sitelibdir/matplotlib/backends/backend_nbagg*
#exclude %python_sitelibdir/matplotlib/backends/windowing.*
%exclude %python_sitelibdir/matplotlib/backends/qt_editor
%python_sitelibdir/matplotlib/tri
%python_sitelibdir/matplotlib/compat
%python_sitelibdir/matplotlib/axes
%python_sitelibdir/matplotlib/style
#python_sitelibdir/matplotlib/externals
%exclude %python_sitelibdir/mpl_toolkits
%exclude %python_sitelibdir/*/*/test*

%files cairo
%python_sitelibdir/matplotlib/backends/backend_cairo*

%files nbagg
%python_sitelibdir/matplotlib/backends/backend_nbagg*

#files fltk
#python_sitelibdir/matplotlib/backends/backend_fltk*

#files gtk
#python_sitelibdir//matplotlib/backends/backend_gtk.py*
#python_sitelibdir//matplotlib/backends/backend_gdk.py*
#python_sitelibdir//matplotlib/backends/backend_gtkagg.py*
#python_sitelibdir//matplotlib/backends/backend_gtkcairo.py*

%files gtk3
%python_sitelibdir/matplotlib/backends/backend_gtk3*

#files qt
#python_sitelibdir/matplotlib/backends/backend_qt.*
#python_sitelibdir/matplotlib/backends/backend_qtagg*

%if_with wx
%files wx
%python_sitelibdir/matplotlib/backends/backend_wx*
%python_sitelibdir/matplotlib/backends/wx*
%endif

# problem with checking?
%files tk
%python_sitelibdir/matplotlib/backends/backend_tk*
%python_sitelibdir/matplotlib/backends/tk*
%python_sitelibdir/matplotlib/backends/_tkagg*

%if_with qt5
%files qt5
%python_sitelibdir/matplotlib/backends/backend_qt5*
%endif

%if_with qt4
%files qt4
%python_sitelibdir/matplotlib/backends/backend_qt4*
%python_sitelibdir/matplotlib/backends/qt*_compat.*
%python_sitelibdir/matplotlib/backends/qt_editor
%endif

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
#python_sitelibdir/%oname/tests
%python_sitelibdir/%oname/*/test*

%files sphinxext
%python_sitelibdir/%oname/sphinxext
#exclude %python_sitelibdir/%oname/sphinxext/test*

%files -n python-module-mpl_toolkits
%python_sitelibdir/mpl_toolkits
%exclude %python_sitelibdir/mpl_toolkits/tests
#needed fix NameError: name 'gtk_git' is not defined
%exclude %python_sitelibdir/mpl_toolkits/gtktools*

%files -n python-module-mpl_toolkits-tests
%python_sitelibdir/mpl_toolkits/tests

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.rst CHANGELOG INSTALL
%python3_sitelibdir/*.py*
#exclude %python3_sitelibdir/six.py*
%python3_sitelibdir/__pycache__/*
#exclude %python3_sitelibdir/__pycache__/six.*
%python3_sitelibdir/*.egg-info
%dir %python3_sitelibdir/matplotlib/
%python3_sitelibdir/matplotlib-*-nspkg.pth
%python3_sitelibdir/matplotlib/*.py*
%python3_sitelibdir/matplotlib/*.so
%python3_sitelibdir/matplotlib/__pycache__
#python_sitelibdir/matplotlib/numerix/
%python3_sitelibdir/mpl_toolkits/
%python3_sitelibdir/matplotlib/projections/
%python3_sitelibdir/matplotlib/delaunay/
%python3_sitelibdir/matplotlib/mpl-data/
#%python3_sitelibdir/matplotlib/config/
#%python3_sitelibdir/enthought/
#python3_sitelibdir/matplotlib/backends/Matplotlib.nib/
%python3_sitelibdir/matplotlib/backends/
%exclude %python3_sitelibdir/matplotlib/backends/backend_gtk*
%exclude %python3_sitelibdir/matplotlib/backends/backend_gdk*
%exclude %python3_sitelibdir/matplotlib/backends/backend_cairo*
%exclude %python3_sitelibdir/matplotlib/backends/backend_wx*
%exclude %python3_sitelibdir/matplotlib/backends/wx*
%exclude %python3_sitelibdir/matplotlib/backends/backend_tk*
%exclude %python3_sitelibdir/matplotlib/backends/tk*
%exclude %python3_sitelibdir/matplotlib/backends/_tkagg*
%exclude %python3_sitelibdir/matplotlib/backends/backend_qt?*
%exclude %python3_sitelibdir/matplotlib/backends/qt*_compat.*
%exclude %python3_sitelibdir/matplotlib/backends/backend_macosx.*
%exclude %python3_sitelibdir/matplotlib/backends/backend_nbagg*
#exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_fltk*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_gtk*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_gdk*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_cairo*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_wx*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/wx*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_tk*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/tk*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_qt*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/qt*_compat.*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_macosx.*
%exclude %python3_sitelibdir/matplotlib/backends/__pycache__/backend_nbagg*
%exclude %python3_sitelibdir/matplotlib/backends/qt_editor
%python3_sitelibdir/matplotlib/tri
%python3_sitelibdir/matplotlib/compat
%python3_sitelibdir/matplotlib/axes
%python3_sitelibdir/matplotlib/style
#python3_sitelibdir/matplotlib/externals
%exclude %python3_sitelibdir/mpl_toolkits
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-cairo
%python3_sitelibdir/matplotlib/backends/backend_cairo*
%python3_sitelibdir/matplotlib/backends/__pycache__/backend_cairo*

%files -n python3-module-%oname-nbagg
%python3_sitelibdir/matplotlib/backends/backend_nbagg*
%python3_sitelibdir/matplotlib/backends/__pycache__/backend_nbagg*

#files -n python3-module-%oname-fltk
#python3_sitelibdir/matplotlib/backends/backend_fltk*
#python3_sitelibdir/matplotlib/backends/__pycache__/backend_fltk*

#files -n python3-module-%oname-gtk
#python3_sitelibdir//matplotlib/backends/backend_gtk.*
#python3_sitelibdir//matplotlib/backends/backend_gdk.*
#python3_sitelibdir//matplotlib/backends/backend_gtkagg.*
#python3_sitelibdir//matplotlib/backends/backend_gtkcairo.*
#python3_sitelibdir/matplotlib/backends/__pycache__/backend_gtk.*
#python3_sitelibdir/matplotlib/backends/__pycache__/backend_gdk.*
#python3_sitelibdir/matplotlib/backends/__pycache__/backend_gtkagg.*
#python3_sitelibdir/matplotlib/backends/__pycache__/backend_gtkcairo.*

%files -n python3-module-%oname-gtk3
%python3_sitelibdir/matplotlib/backends/backend_gtk3*
%python3_sitelibdir/matplotlib/backends/__pycache__/backend_gtk3*

#files -n python3-module-%oname-qt
#python3_sitelibdir/matplotlib/backends/backend_qt.*
#python3_sitelibdir/matplotlib/backends/__pycache__/backend_qt.*
#python3_sitelibdir/matplotlib/backends/backend_qtagg*
#python3_sitelibdir/matplotlib/backends/__pycache__/backend_qtagg*

#files -n python3-module-%oname-wx
#python3_sitelibdir/matplotlib/backends/backend_wx*
#python3_sitelibdir/matplotlib/backends/__pycache__/backend_wx*
#python3_sitelibdir/matplotlib/backends/wx*
#python3_sitelibdir/matplotlib/backends/__pycache__/wx*

%files -n python3-module-%oname-tk
%python3_sitelibdir/matplotlib/backends/backend_tk*
%python3_sitelibdir/matplotlib/backends/__pycache__/backend_tk*
%python3_sitelibdir/matplotlib/backends/tk*
%python3_sitelibdir/matplotlib/backends/__pycache__/tk*
%python3_sitelibdir/matplotlib/backends/_tkagg*

%files -n python3-module-%oname-qt5
%python3_sitelibdir/matplotlib/backends/backend_qt5*
%python3_sitelibdir/matplotlib/backends/__pycache__/backend_qt5*

%files -n python3-module-%oname-qt4
%python3_sitelibdir/matplotlib/backends/backend_qt4*
%python3_sitelibdir/matplotlib/backends/__pycache__/backend_qt4*
%python3_sitelibdir/matplotlib/backends/qt*_compat.*
%python3_sitelibdir/matplotlib/backends/__pycache__/qt*_compat.*
%python3_sitelibdir/matplotlib/backends/qt_editor

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/testing
#python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/*/test*
%python3_sitelibdir/%oname/*/*/test*

%files -n python3-module-%oname-sphinxext
%python3_sitelibdir/%oname/sphinxext
#exclude %python3_sitelibdir/%oname/sphinxext/test*
#exclude %python3_sitelibdir/%oname/sphinxext/*/test*

%files -n python3-module-mpl_toolkits
%python3_sitelibdir/mpl_toolkits
%exclude %python3_sitelibdir/mpl_toolkits/tests
%exclude %python3_sitelibdir/mpl_toolkits/gtktools*
%exclude %python3_sitelibdir/mpl_toolkits/__pycache__/gtktools*

%files -n python3-module-mpl_toolkits-tests
%python3_sitelibdir/mpl_toolkits/tests
%endif

%changelog
* Mon Jan 29 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt7
- Fix Requires of python3-module-matplotlib
  (mpl_toolkits is needed for namespace package import)

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt6
- Rebuilt with updated setuptools.

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt5
- Updated runtime dependencies.

* Tue Jun 27 2017 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt4
- Fix version egg-info (Closes: 33574)

* Sat Jun 24 2017 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt3
- Added missing requires.

* Wed May 31 2017 Michael Shigorin <mike@altlinux.org> 2.0.0-alt2.1
- BOOTSTRAP: introduce qt4, qt5, wx knobs (on by default)

* Fri May 26 2017 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt2
- Remove subpackages python-module-matplotlib-pylab and python3-module-matplotlib-pylab

* Thu Apr 27 2017 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- New version 2.0.0
- Disable convert python 2 to python3 script
- New subpackages:
    - python-module-matplotlib-cairo
    - python3-module-matplotlib-cairo
    - python-module-matplotlib-pylab
    - python3-module-matplotlib-pylab
    - python-module-matplotlib-nbagg
    - python3-module-matplotlib-nbagg

* Mon Mar 27 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.5.0-alt6.git20150829
- Rebuilt against Tcl/Tk 8.6
- Added missing provides
- Fixed build

* Sat May 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt5.git20150829
- NMU: rebuild with python-module-xlwt

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.0-alt4.git20150829.1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.0-alt4.git20150829.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt4.git20150829.1
- NMU: Use buildreq for BR.

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt4.git20150829
- Added qt5 backend

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt3.git20150829
- New snapshot

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt3.git20150425
- New snapshot

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt3.git20141101
- Added necessary files into qt4 subpackage

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2.git20141101
- Tuned requirements

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20141101
- Version 1.5.x

* Tue May 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt5.git20140504
- Fixed build

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt4.git20140504
- New snapshot

* Thu Oct 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt4.git20131022
- Removed mpl_toolkits from main package

* Wed Oct 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt3.git20131022
- New snapshot

* Wed Sep 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt3.git20130611
- Fixed build

* Sun Jun 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.git20130611
- Added compat for main package
- Set default backend: GTK3Cairo

* Sat Jun 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.git20121010
- Version 1.4.x

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt4.git20121010
- Excluded six.py

* Wed Mar 27 2013 Aleksey Avdeev <solo@altlinux.ru> 1.3.0-alt3.git20121010.1
- Rebuild with Python-3.3

* Tue Jan 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt3.git20121010
- Fixed build

* Tue Jan 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2.git20121010
- Rebuilt with python3-module-PyQt4-devel

* Sat Oct 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20121010
- Version 1.3.0

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt3.git20120608
- Rebuilt with libpng15

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
