Name: python-module-sdl2
Version: 0.9.5
Release: alt1
Group: Development/Python
License: Public Domain
Summary: SDL2 python wrapper
Source: PySDL2-%version.tar.gz
BuildArch: noarch

%setup_python_module sdl2

# Automatically added by buildreq on Mon Mar 03 2014
# optimized out: python-base python-modules python-modules-compiler python-modules-email
BuildRequires: python-devel
Requires: libSDL2_gfx libSDL2_image libSDL2_mixer libSDL2_ttf libSDL2

%description
PySDL2 is a wrapper around the SDL2 library and as such similar to the
discontinued PySDL project. In contrast to PySDL, it has no licensing
restrictions, nor does it rely on C code, but uses ctypes instead.

%prep
%setup -n PySDL2-%version

%build
%python_build

%install
%python_install

%files
%doc examples doc
%python_sitelibdir_noarch/sdl2*

%changelog
* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 0.9.5-alt1
- Autobuild version bump to 0.9.5

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 0.9.4-alt1
- Autobuild version bump to 0.9.4

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 0.9.3-alt1
- Autobuild version bump to 0.9.3

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 0.9.2-alt1
- Autobuild version bump to 0.9.2

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 0.9.1-alt1
- Autobuild version bump to 0.9.1

* Mon Mar 03 2014 Fr. Br. George <george@altlinux.ru> 0.8.0-alt1
- Autobuild version bump to 0.8.0

* Mon Mar 03 2014 Fr. Br. George <george@altlinux.ru> 0.7.0-alt1
- Initial build from scratch

