%define fix_permissions \
find -type d -print0 | xargs -0 chmod 0775 \
find -type f -print0 | xargs -0 chmod 0664
%define oname pygame

%def_without python3

Name: python-module-%oname
Version: 1.9.1
Release: alt2

Summary: A Python module for interfacing with the SDL multimedia library
Summary(ru_RU.KOI8-R): Расширение языка Python для работы с библиотекой SDL

Group: Development/Python
License: LGPL
Url: http://pygame.seul.org

Source: http://pygame.seul.org/ftp/pygame-%{version}release.tar.bz2
#Patch: pygame-1.7.1.patch

%setup_python_module pygame
%define python_includedir %_includedir/python%_python_version

Provides: python-pygame, %modulename
Obsoletes: %modulename

Requires: libSDL >= 1.2.7

# FIXME: buildreq is broken
# manually removed: eric
# Automatically added by buildreq on Sun Jul 22 2007
BuildRequires: libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libsmpeg-devel libX11-devel python-devel python-modules-compiler libpng-devel libjpeg-devel

BuildPreReq: libnumpy-devel libv4l-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel libnumpy-py3-devel
BuildPreReq: python3-module-distribute python-tools-2to3
%endif

%add_python_req_skip AppKit Foundation py2app

%description
pygame is a Python wrapper module for the SDL multimedia library, written by
Pete Shinners.  It contains python functions and classes that will allow you
to use SDL's support for playing cdroms, audio and video output, and keyboard,
mouse and joystick input. pygame also includes support for the Numerical
Python extension. pygame is the successor to the pySDL wrapper project, written
by Mark Baker.

Install %name if you would like to write or play SDL games written in the
python language.

%description -l ru_RU.KOI8-R
pygame - расширение языка программирования Python, позволяющее
использовать возможности мультимедийной библиотеки SDL (Simple
DirectMedia Layer), предоставляющей низкоуровневый доступ к звуковым
устройствам, клавиатуре, манипулятору мышь и к буферу экрана на
множестве различных платформ.

%if_with python3
%package -n python3-module-%oname
Summary: A Python 3 module for interfacing with the SDL multimedia library
Group: Development/Python3
%add_python3_req_skip AppKit Foundation py2app

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
%endif

%package devel
Summary: Pygame development headers
Summary(ru_RU.KOI8-R): Файлы для разработчика приложений, использующих pygame
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

%description devel -l ru_RU.KOI8-R
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
%setup -n %modulename-%{version}release
%fix_permissions
#%patch -p1
rm -f docs/LGPL
# fix find SDL libs on x86_64
subst "s|/lib|/%_lib|g" config_unix.py

# remove due unliked dependences on MacOS modules
rm -f lib/macosx.py lib/mac_scrap.py

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
export LOCALBASE=%_prefix
python config.py
sed -i 's|\(lpthread\)|\1 -lm|g' Setup
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
python3 config.py
sed -i 's|\(lpthread\)|\1 -lm|g' Setup
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build_debug
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%files devel
%python_includedir/%modulename/

%files doc
%doc WHATSNEW install.html README.txt docs examples

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*

%files -n python3-module-%oname-devel
%{python3_includedir}mu/*
%endif

%changelog
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
