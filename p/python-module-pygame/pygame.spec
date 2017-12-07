%define oname pygame
%def_with python3

Name: python-module-%oname
Version: 1.9.3
Release: alt3

Summary: A Python module for interfacing with the SDL multimedia library
Summary(ru_RU.UTF-8): Расширение языка Python для работы с библиотекой SDL

Group: Development/Python
License: LGPL
Url: http://www.pygame.org

Source: %version.tar.gz
Patch: pygame-1.9.3-2to3.patch
%setup_python_module pygame
%define python_includedir %_includedir/python%_python_version
%define python3_includedir %_includedir/python%{_python3_version}m

Provides: python-pygame, %oname
Obsoletes: %oname

Requires: libSDL >= 1.2.7

# Automatically added by buildreq on Sun Jul 22 2007
BuildRequires: libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libsmpeg-devel libX11-devel python-devel python-modules-compiler libpng-devel libjpeg-devel libfreetype-devel libportmidi-devel

BuildPreReq: libnumpy-devel libv4l-devel rpm-build-intro

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel libnumpy-py3-devel python3-module-sphinx
BuildPreReq: python3-module-distribute python-tools-2to3
%endif

%add_python_req_skip AppKit Foundation py2app Numeric

%description
pygame is a Python wrapper module for the SDL multimedia library, written by
Pete Shinners.  It contains python functions and classes that will allow you
to use SDL's support for playing cdroms, audio and video output, and keyboard,
mouse and joystick input. pygame also includes support for the Numerical
Python extension. pygame is the successor to the pySDL wrapper project, written
by Mark Baker.

Install %name if you would like to write or play SDL games written in the
python language.

%description -l ru_RU.UTF-8
pygame - расширение языка программирования Python, позволяющее
использовать возможности мультимедийной библиотеки SDL (Simple
DirectMedia Layer), предоставляющей низкоуровневый доступ к звуковым
устройствам, клавиатуре, манипулятору мышь и к буферу экрана на
множестве различных платформ.

%if_with python3
%package -n python3-module-%oname
Summary: A Python 3 module for interfacing with the SDL multimedia library
Group: Development/Python3
%add_python3_req_skip AppKit Foundation py2app Numeric opencv

%description -n python3-module-%oname
pygame is a Python wrapper module for the SDL multimedia library, written by
Pete Shinners.  It contains python functions and classes that will allow you
to use SDL's support for playing cdroms, audio and video output, and keyboard,
mouse and joystick input. pygame also includes support for the Numerical
Python extension. pygame is the successor to the pySDL wrapper project, written
by Mark Baker.

Install %name if you would like to write or play SDL games written in the
python language.

%package -n python3-module-%oname-devel
Summary: Pygame development headers (Python 3)
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-devel
pygame is a Python wrapper module for the SDL multimedia library, written by
Pete Shinners.  It contains python functions and classes that will allow you
to use SDL's support for playing cdroms, audio and video output, and keyboard,
mouse and joystick input. pygame also includes support for Numerical Python
extension. pygame is the successor to the pySDL wrapper project, written by
Mark Baker.

Install python3-module-%oname-devel if you need the API documentation
and example programs.

%package -n python3-module-%oname-doc
Summary: Pygame documentation and example programs (Python3 version)
Group: Development/Python3
Requires: %name = %version-%release
BuildArch: noarch

%description -n python3-module-%oname-doc
Pygame documentation and example programs (Python3 version)
%endif

%package devel
Summary: Pygame development headers
Summary(ru_RU.UTF-8): Файлы для разработчика приложений, использующих pygame
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description devel
pygame is a Python wrapper module for the SDL multimedia library, written by
Pete Shinners.  It contains python functions and classes that will allow you
to use SDL's support for playing cdroms, audio and video output, and keyboard,
mouse and joystick input. pygame also includes support for Numerical Python
extension. pygame is the successor to the pySDL wrapper project, written by
Mark Baker.

Install %name-devel if you need the API documentation and example programs.

%description devel -l ru_RU.UTF-8
Пакет содержит заголовочные файлы, документацию и примеры программ,
использующих расширение pygame.

%package doc
Summary: Pygame documentation and example programs
Group: Development/Python
Requires: %name = %version-%release
BuildArch: noarch

%description doc
pygame is a Python  wrapper  module  for  the  SDL  multimedia  library,
written by Pete Shinners. It contains python functions and classes  that
will allow you to use SDL's support for playing cdroms, audio and  video
output, and keyboard, mouse and joystick  input.  pygame  also  includes
support for Numerical Python extension. pygame is the successor  to  the
pySDL wrapper project, written by Mark Baker.

Install %name-doc  if  you  need  the  API  documentation  and  example
programs.

%prep
%setup -n %oname-%version
%patch -p2
rm -f docs/LGPL
# fix find SDL libs on x86_64
subst "s|/lib|/%_lib|g" config_unix.py
# XXX
touch version.py.in

# remove due unliked dependences on MacOS modules
rm -f lib/macosx.py lib/mac_scrap.py

%build
export LOCALBASE=%prefix
python config.py
#sed -i 's|\(lpthread\)|\1 -lm|g' Setup
%add_optflags -fno-strict-aliasing

%python_build_debug
%if_with python3
	%python3_build_debug
	2to3 -w -n -j %__nprocs build/lib*%_python3_version
#	python3 -m sphinx -j %__nprocs -b html -d build/.doctrees3 -D headers_dest=src/doc -D headers_mkdirs=0 docs/reST build/%_python3_version
#else
#	python -m sphinx -j %__nprocs -b html -d build/.doctrees2 -D headers_dest=src/doc -D headers_mkdirs=0 docs/reST build/%_python_version
%endif

%install
%python_install
%if_with python3
%python3_install
%endif

%files
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%files devel
%python_includedir/%oname/

%files doc
%doc WHATSNEW install.html readme*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*

%files -n python3-module-%oname-devel
%python3_includedir/%oname

%files -n python3-module-%oname-doc
%doc WHATSNEW install.html readme*
%endif

%changelog
* Fri Dec 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1.9.3-alt3
- disable doc build

* Tue Jul 18 2017 Fr. Br. George <george@altlinux.ru> 1.9.3-alt2
- Fix 2to3 overthinking issue

* Sun Jul 02 2017 Fr. Br. George <george@altlinux.ru> 1.9.3-alt1
- Autobuild version bump to 1.9.3

* Wed Mar 08 2017 Fr. Br. George <george@altlinux.ru> 1.9.2-alt1
- New upstream
- Introduce Python3 module

* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt6
- build with new fixed libportmidi

* Sat Dec 13 2014 Dmitry Derjavin <dd@altlinux.org> 1.9.1-alt5
- Revision up for p7 rebuild.

* Thu Mar 13 2014 Dmitry Derjavin <dd@altlinux.org> 1.9.1-alt4.1
- NMU: rebuild with libopencv-2.4.8.1;

* Fri Jan 31 2014 Fr. Br. George <george@altlinux.ru> 1.9.1-alt4
- Fix spec encoding

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.1-alt3
- Rebuilt with libpng15

* Sun Jun 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.1-alt2
- Fixed build

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.1-alt1.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.1-alt1
- Version 1.9.1

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt7
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt6
- Fixed underlinking

* Sat Feb 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt5
- Rebuilt with reformed NumPy

* Sun Jan 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt4
- Rebuilt without python-module-Numeric
- Set doc package as noarch

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt3
- Rebuilt with python 2.6

* Mon Dec 15 2008 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt2
- fix file permissions (fix bug #18206, thanks to Nikolay Fetisov)

* Wed Nov 12 2008 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- new version 1.8.1 (with rpmrb script)
- update buildreq

* Sun Jan 13 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt2
- fix build on x86_64
- add patch for fix possible stack overwrite (thanks, Debian)
- cleanup spec

* Sun Jul 22 2007 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt1
- update buildreq

* Sat Feb 11 2006 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt0.1
- new version

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt2
- rebuild with python 2.4

* Sat Dec 04 2004 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- rename spec
- new version

* Fri Jul 02 2004 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt1
- new version
- rename to python-module-pygame
- rewrite spec for python policy accordance

* Sun Jun 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.5-alt1
- 1.5
- config.patch removed.

* Sat Feb 2 2002  Yuri N. Sedunov <aris@altlinux.ru> 1.4-alt1
- 1.4
- config patch

* Tue Jan 29 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.3-alt2
- Rebuilt with Python-2.2

* Mon Jan 7 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.3-alt1
- First build for Sisyphus.
