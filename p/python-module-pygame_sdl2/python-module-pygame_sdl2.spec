Name: python-module-pygame_sdl2
Version: 6.99.10.1227
Release: alt1
%setup_python_module pygame_sdl2

Summary: A reimplementation of the Pygame API using SDL2

Group: Development/Python
License: LGPL
Url: https://github.com/renpy/pygame_sdl2

# NB! name is "renpy", yes!
Source: renpy-%version.tar.gz

%define python_includedir %_includedir/python%_python_version

#add_python_req_skip AppKit Foundation py2app

# Automatically added by buildreq on Thu Apr 23 2015
# optimized out: ipython libSDL2-devel libcloog-isl4 python-base python-devel python-module-BeautifulSoup python-module-PyStemmer python-module-Pygments python-module-docutils python-module-enum34 python-module-matplotlib python-module-ndg-httpsclient python-module-numpy python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pyglet python-module-pygobject3 python-module-pyparsing python-module-setuptools python-module-snowballstemmer python-module-terminado python-module-tornado_xstatic python-module-xstatic python-module-xstatic-term.js python-module-zope.interface python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-json python-modules-wsgiref python-modules-xml python3-base zlib-devel
BuildRequires: ctags libSDL2-devel libSDL2_gfx-devel libSDL2_image-devel libSDL2_mixer-devel libSDL2_ttf-devel libjpeg-devel libpng-devel python-module-Cython python-module-cssselect python-module-html5lib time

%description
Pygame_sdl2 is a reimplementation of the Pygame API using SDL2 and
related libraries. The initial goal of this project are to allow games
written using the pygame API to run on SDL2 on desktop and mobile
platforms. We will then evolve the API to expose SDL2-provided
functionality in a pythonic manner.

%package devel
Summary: Pygame_SDL2 development headers
Group: Development/Python
BuildArch: noarch

%description devel
Pygame_sdl2 is a reimplementation of the Pygame API using SDL2 and
related libraries. The initial goal of this project are to allow games
written using the pygame API to run on SDL2 on desktop and mobile
platforms. We will then evolve the API to expose SDL2-provided
functionality in a pythonic manner.

Install %name-devel if you need the API development environment.

%prep
%setup -n %modulename-renpy-%version
sed -i 's/sdl_libs = /sdl_libs = ["m"]+/' setup.py

%build
%python_build_debug

%install
%python_install

%files
%doc README*
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%files devel
%python_includedir/%modulename/

%changelog
* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 6.99.10.1227-alt1
- Autobuild version bump to 6.99.10.1227

* Mon Nov 23 2015 Fr. Br. George <george@altlinux.ru> 6.99.6.739-alt2
- Synchronize with Nov 3, 2015 version

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 6.99.6.739-alt1
- Autobuild version bump to 6.99.6.739

* Thu Apr 23 2015 Fr. Br. George <george@altlinux.ru> 6.99.0.303-alt1
- Initial build for ALT

