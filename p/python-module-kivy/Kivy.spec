Name: python-module-kivy
Version: 1.8.0
Release: alt2
Summary: Open source library for rapid development of applications
License: LGPLv3
Group: Development/Python
Url: http://kivy.org
Source: Kivy-%version.tar.gz

%setup_python_module kivy
%add_python_req_skip AppKit
%add_python_req_skip freenect
%add_python_req_skip jnius
%add_python_req_skip android

BuildRequires: libGL-devel libGLES-devel python-module-Cython0.18 python-module-Pyrex python-module-docutils python-module-html5lib python-module-nss python-module-numpy-testing python-module-pygame

%description
Kivy - Open source library for rapid development of applications
that make use of innovative user interfaces, such as multi-touch apps.

%package devel
Group: Development/Python
Summary: Development environment for Kivy, %summary
BuildArch: noarch

%description devel
Example files, documentation and packaging tool for Kivy, %summary

%prep
%setup -n Kivy-%version
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
sleep 1
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
  #make html

%install
%python_install

%files
%doc doc/README PKG-INFO
%python_sitelibdir/kivy

%files devel
#%doc doc/build/html
%_datadir/kivy-examples
## XXX garden binary is moved to separate module

%changelog
* Tue Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 1.8.0-alt2
- cleanup buildreq
- switchoff html generation

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
