
#add_findreq_skiplist %python_sitelibdir/pyudev/*

Name: python-module-pyudev
Version: 0.14
Release: alt1
%setup_python_module pyudev

Group: System/Libraries
Summary: Udev bindings for Python
Url: http://packages.python.org/pyudev/
License: LGPLv2.1+

BuildArch: noarch

Source: pyudev-%version.tar


# Automatically added by buildreq on Tue Feb 14 2012 (-bi)
# optimized out: python-base python-devel python-module-4Suite-XML python-module-BeautifulSoup python-module-Pygments python-module-SQLAlchemy python-module-babel python-module-beaker python-module-cups python-module-dateutil python-module-distribute python-module-docutils python-module-genshi python-module-html5lib python-module-imaging python-module-jinja2 python-module-lxml python-module-mako python-module-matplotlib python-module-mpmath python-module-nose python-module-numpy python-module-protobuf python-module-pyExcelerator python-module-pyglet python-module-pylib python-module-pytz python-module-simplejson python-module-sphinx python-module-sympy python-module-whoosh python-module-xlwt python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings
#BuildRequires: dblatex java-1.5.0-gcj-aot-compile libudev mercurial python-module-Reportlab python-module-cupshelpers python-module-numpydoc python-module-pyxdg python-module-scipy rpm-build-gir
BuildRequires: libudev-devel python-devel python-module-distribute

%description
A Python binding to libudev, the hardware management library and service found
in modern linux systems.

%prep
%setup -q -n pyudev-%version

%build
%python_build

%install
%python_install

%files
%doc CHANGES.rst COPYING README.rst
%python_sitelibdir/pyudev
%python_sitelibdir/pyudev-*

%changelog
* Tue Feb 14 2012 Sergey V Turchin <zerg@altlinux.org> 0.14-alt1
- initial build
