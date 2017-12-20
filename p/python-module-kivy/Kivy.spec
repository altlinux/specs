Name: python-module-kivy
Version: 1.10.0
Release: alt2
Summary: Open source library for rapid development of applications
License: LGPLv3
Group: Development/Python
Url: http://kivy.org
Source: %version.tar.gz
Patch1: kivy-1.10.0-upstream-cython-fix-1.patch
Patch2: kivy-1.10.0-upstream-cython-fix-2.patch
Patch3: kivy-1.10.0-upstream-cython-fix-3.patch
Patch4: kivy-1.10.0-upstream-cython-fix-4.patch
Patch5: kivy-1.10.0-upstream-cython-fix-5.patch
Patch6: kivy-1.10.0-upstream-sdl-mixer-2.0.2-support.patch
Patch10: kivy-1.10.0-alt-version.patch

%setup_python_module kivy
%add_python_req_skip AppKit
%add_python_req_skip freenect
%add_python_req_skip jnius
%add_python_req_skip android
# recommended
%add_python_req_skip ffpyplayer
%add_python_req_skip pyobjus
# Kivy's internal submodule (relative import is needed?)
%add_python_req_skip doc

# Automatically added by buildreq on Wed Jan 29 2014
# optimized out: libEGL-devel python-base python-devel python-module-BeautifulSoup python-module-Pygments python-module-docutils python-module-html5lib python-module-jinja2 python-module-markupsafe python-module-numpy python-module-numpy-testing python-module-protobuf python-module-setuptools python-module-simplejson python-module-six python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-multiprocessing python-modules-unittest
BuildRequires: ctags libGL-devel libGLES-devel python-module-Cython python-module-Pyrex python-module-jinja2-tests python-module-nss python-module-pygame python-module-pytz python-module-sphinx python-modules-json time
BuildRequires: xvfb-run
BuildRequires(pre): gstreamer1.0-devel
BuildRequires(pre): libSDL2_mixer-devel libSDL2_ttf-devel libSDL2-devel libSDL2_image-devel

%description
Kivy - Open source library for rapid development of applications
that make use of innovative user interfaces, such as multi-touch apps.

%package devel
Group: Development/Python
Summary: Development environment for Kivy, %summary
BuildArch: noarch

# TODO garden modules/installer

%description devel
Example files, documentation and packaging tool for Kivy, %summary

%package tests
Summary: Tests for Kiby
Group: Development/Python
Requires: %name = %EVR

%description tests
Kivy - Open source library for rapid development of applications
that make use of innovative user interfaces, such as multi-touch apps.

This package contains tests for Kivy.

%prep
%setup -n Kivy-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch10 -p2

rm -rf kivy/tools/packaging/osx

for f in `grep -rl '#!/usr/bin/kivy' examples`; do
	sed -i 's|#!/usr/bin/kivy|#!/usr/bin/env python|' $f
done

# XXX Python3
sed -i 's/from xmlrpc.client/from xmlrpclib/' kivy/tools/report.py
sed -i 's/from configparser/from ConfigParser/' kivy/config.py
sed -i 's/from configparser/from ConfigParser/' kivy/tools/pep8checker/pep8.py
sed -i 's/from configparser/from ConfigParser/' kivy/tools/report.py

# XXX
sleep 2
find . -name \*.pyx | xargs touch

%build
%add_optflags -fno-strict-aliasing
%python_build

# XXX
ln doc/sources/.static/logo-kivy.png doc/sources/logo-kivy.png

cd doc &&
  export PYTHONPATH=`ls -d ../build/lib*` &&
  python autobuild.py &&
  export PYTHONPATH=$PYTHONPATH:../kivy/tools/highlight/pygments &&
  xvfb-run make html

%install
%python_install
mkdir -p %buildroot/%_docdir
mv %buildroot/%_datadir/kivy-examples %buildroot/%_docdir

%files
%doc doc/README.md
%python_sitelibdir/kivy
%python_sitelibdir/Kivy*
%exclude %python_sitelibdir/kivy/tests

%files devel
%doc doc/build/html
%_docdir/kivy-examples
## XXX garden binary is moved to separate module

%files tests
%python_sitelibdir/kivy/tests

%changelog
* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10.0-alt2
- Fixed build.
- Split tests into separate package.

* Sun Jul 30 2017 Denis Medvedev <nbr@altlinux.org> 1.10.0-alt1
- version bump to 1.10.0

* Mon Apr 11 2016 Fr. Br. George <george@altlinux.ru> 1.9.1-alt1
- Autobuild version bump to 1.9.1
- Fix documentation build

* Tue Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 1.8.0-alt2
- cleanup buildreq
- switchoff html generation

* Thu Apr 23 2015 Fr. Br. George <george@altlinux.ru> 1.9.0-alt1
- Autobuild version bump to 1.9.0

* Mon Aug 25 2014 Fr. Br. George <george@altlinux.ru> 1.8.0-alt1
- Autobuild version bump to 1.8.0
- The garden binary is gone
- Hack out some unexpected python3 and android stuff

* Wed Jan 29 2014 Fr. Br. George <george@altlinux.ru> 1.7.2-alt2
- Fix build and dependencies

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 1.7.2-alt1
- Autobuild version bump to 1.7.2
- Move examples and docs to the newly introduced devel package

* Mon Jun 10 2013 Fr. Br. George <george@altlinux.ru> 1.7.1-alt1
- Autobuild version bump to 1.7.1

* Sun Mar 31 2013 Fr. Br. George <george@altlinux.ru> 1.6.0-alt1
- Autobuild version bump to 1.6.0

* Tue Dec 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt2
- Set examples as noarch package

* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 1.5.1-alt1
- Autobuild version bump to 1.5.1
- Remove android-specific jnius dependency

* Mon Oct 22 2012 Fr. Br. George <george@altlinux.ru> 1.4.1-alt1
- Autobuild version bump to 1.4.1

* Sun Jul 22 2012 Fr. Br. George <george@altlinux.ru> 1.3.0-alt1
- Autobuild version bump to 1.3.0

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
