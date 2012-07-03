Name: python-module-kivy
Version: 1.2.0
Release: alt1
Summary: Open source library for rapid development of applications
License: LGPLv3
Url: http://kivy.org
Source: Kivy-%version.tar.gz
Group: Development/Python

%setup_python_module kivy
%add_python_req_skip AppKit
%add_python_req_skip freenect

# Automatically added by buildreq on Mon Jan 16 2012
# optimized out: python-base python-devel python-module-BeautifulSoup python-module-Pygments python-module-SQLAlchemy python-module-distribute python-module-docutils python-module-genshi python-module-html5lib python-module-jinja2 python-module-jinja2-tests python-module-lxml python-module-protobuf python-module-simplejson python-module-whoosh python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-multiprocessing python-modules-unittest
BuildRequires: libGL-devel python-module-Cython python-module-Pyrex python-module-distutils-extra python-module-sphinx python-modules-json time

%description
Kivy - Open source library for rapid development of applications
that make use of innovative user interfaces, such as multi-touch apps.

%package examples
Group: Development/Python
Summary: Example files for Kyvy, %summary

%description examples
Example files for Kyvy, %summary

%prep
%setup -n Kivy-%version
rm -rf kivy/tools/packaging/osx
# XXX WTF
sed -i '/glGetIntegerv(GL_VIEWPORT/s/[&]self/self/' kivy/graphics/fbo.pyx

%build
%python_build
(
cd doc
export PYTHONPATH=`ls -d ../build/lib*`
python autobuild.py
export PYTHONPATH=$PYTHONPATH:../kivy/tools/highlight/pygments
make html
)

%install
%python_install

%files
%doc doc/README PKG-INFO doc/build/html
%python_sitelibdir/kivy

%files examples
%_datadir/kivy-examples

%changelog
* Thu May 03 2012 Fr. Br. George <george@altlinux.ru> 1.2.0-alt1
- Autobuild version bump to 1.2.0

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.9-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Mar 01 2012 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1
- Fix build

* Fri Jan 20 2012 Fr. Br. George <george@altlinux.ru> 1.0.9-alt1
- Autobuild version bump to 1.0.9
- Remove non-linux dependencies
