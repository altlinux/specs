%define _unpackaged_files_terminate_build 1
# TODO: fix dest on x86_64
# TODO: Move mpl-data to share?
# TODO: gtk3 knob too?
%define oname matplotlib
%define major 2.2

%def_with wx

Name: python-module-%oname
Version: %major.3
Release: alt10

Summary: Matlab(TM) style python plotting package

License: see LICENSE
Group: Development/Python
Url: http://matplotlib.sourceforge.net
# https://github.com/matplotlib/matplotlib.git
Packager: Python Development Team <python@packages.altlinux.org>

Source: %oname-%version.tar
Source1: setup.cfg

Patch1: %oname-alt-deps-detection.patch
Patch2: %oname-alt-version.patch
Patch3: %oname-2.2.3-remove-unused-matplotlib.testing-import.patch

%setup_python_module pylab

BuildRequires(pre): rpm-build-xdg
BuildRequires(pre): rpm-build-gir
BuildRequires: gcc-c++ libnumpy-devel time tk-devel libgtk+3-gir-devel libpng-devel libfreetype-devel
BuildRequires: python-module-pycairo python-module-pygobject3 python-modules-tkinter python-module-cycler python-module-pyparsing python-module-pytz python-module-dateutil
%{?_with_wx:BuildRequires: python-module-wx}
Requires: %name-gtk3

# hack for unknown deps
%add_python_req_skip AppKit Foundation PyObjCTools numarray paint _Py
%add_python_req_skip _winreg builtins
%py_requires functools32
%py_requires numpy pytz six subprocess32 backports.functools_lru_cache

%description
matplotlib is a pure python 2D plotting library with a Matlab(TM)
syntax which produces publication quality figures using in a
variety of hardcopy formats (PNG, JPG, TIFF, PS) and interactive
GUI environments (WX, GTK) across platforms. matplotlib can be used
in python scripts, interactively from the python shell (ala matlab
or mathematica), in web application servers generating dynamic
charts, or embedded in GTK or WX applications; see backends.

%package cairo
Summary: Cairo backend for %oname
Group: Development/Python
Requires: %name = %version-%release
#py_provides backend_cairo
%py_requires cairo

%description cairo
Cairo backend for %oname.

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

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
sed -i -e "s|@VERSION@|%version|g" setup.py setupext.py
subst "s,/usr/lib/,%_libdir/,g" setupext.py

sed -i "s|@TOP@|$PWD|" doc/conf.py \

install -p -m644 %SOURCE1 .

echo -e "[versioneer]\nparentdir_prefix=python-module-matplotlib-" >> setup.cfg

%build
%add_optflags -fno-strict-aliasing -fpermissive

#sed -i 's|^\(gtk3agg\).*|\1 = False|' setup.cfg
%if_without wx
sed -i 's|^\(wxagg\).*|\1 = False|' setup.cfg
%endif
%python_build_debug

%install

%python_install
cp -fR lib/mpl_toolkits %buildroot%python_sitelibdir/

# don't package tests
rm -r %buildroot%python_sitelibdir/%oname/testing
rm -r %buildroot%python_sitelibdir/mpl_toolkits/tests

# Use gtk by default
subst "s|WXAgg|GTK3Cairo|g" \
	%buildroot%python_sitelibdir/%oname/mpl-data/matplotlibrc

sed -i 's|^\(backend\).*|\1 : GTK3Cairo|' \
	%buildroot%python_sitelibdir/%oname/mpl-data/matplotlibrc

# fonts

%define reduce_fonts cmex10.ttf cmmi10.ttf cmr10.ttf cmsy10.ttf

%pre
rm -f %python_sitelibdir/%oname/mpl-data/fonts/ttf/Vera*.ttf
for i in %reduce_fonts
do
	rm -f %python_sitelibdir/%oname/mpl-data/fonts/ttf/$i
done

%files
%doc README.rst
%python_sitelibdir/*.py*
%python_sitelibdir/*.egg-info
%dir %python_sitelibdir/matplotlib/
%python_sitelibdir/matplotlib-*-nspkg.pth
%python_sitelibdir/matplotlib/*.py*
%python_sitelibdir/matplotlib/*.so
%python_sitelibdir/mpl_toolkits/
%python_sitelibdir/matplotlib/projections/
%python_sitelibdir/matplotlib/mpl-data/
%python_sitelibdir/matplotlib/cbook/
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
%exclude %python_sitelibdir/matplotlib/backends/qt_editor
%python_sitelibdir/matplotlib/tri
%python_sitelibdir/matplotlib/compat
%python_sitelibdir/matplotlib/axes
%python_sitelibdir/matplotlib/style
%exclude %python_sitelibdir/mpl_toolkits

%files cairo
%python_sitelibdir/matplotlib/backends/backend_cairo*

%files gtk3
%python_sitelibdir/matplotlib/backends/backend_gtk3*

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

%files sphinxext
%python_sitelibdir/%oname/sphinxext

%files -n python-module-mpl_toolkits
%python_sitelibdir/mpl_toolkits
#needed fix NameError: name 'gtk_git' is not defined

%changelog
* Thu Jul 22 2021 Stanislav Levin <slev@altlinux.org> 2.2.3-alt10
- Dropped unused dep on numpy.testing.

* Tue May 11 2021 Grigory Ustinov <grenka@altlinux.org> 2.2.3-alt9
- Drop python3 support.
- Build without qt4 and qt5 subpackages (Closes: #38047).

* Thu Jan 14 2021 Nikita Ermakov <arei@altlinux.org> 2.2.3-alt8
- Disable Qt4 for riscv64.
- Do not package python3-module-%%oname-qt{4,5} when building without qt{4,5}
  respectively.

* Sun Nov 01 2020 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt7
- disable python-module-matplotlib-nbagg subpackage (required ipython)

* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.3-alt6
- Fixed build with numpy.

* Wed Feb 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.3-alt5
- Updated interpackage dependencies (Closes: #38030).

* Tue Oct 01 2019 Stanislav Levin <slev@altlinux.org> 2.2.3-alt4
- Dropped runtime dependency on Pytest.

* Mon Feb 04 2019 Alexey Shabalin <shaba@altlinux.org> 2.2.3-alt3
- Drop requirement on dvipng for python3-module-matplotlib.

* Tue Dec 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.3-alt2
- Package testing module in main package (ALT #35714).
- Drop tests subpackages.
- Requires backports.functools_lru_cache module.

* Mon Nov 26 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.3-alt1
- New version.

* Thu Oct 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt8
- fixed build with new freetype.
- rebuilt with pygtk instead of pygtk_git.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt7.1
- (NMU) Rebuilt with python-3.6.4.

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
