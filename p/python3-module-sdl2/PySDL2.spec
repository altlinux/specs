%define _unpackaged_files_terminate_build 1

Name:       python3-module-sdl2
Version:    0.9.6
Release:    alt1

Group:      Development/Python3
License:    Public Domain
Summary:    SDL2 python wrapper

Url:        https://bitbucket.org/marcusva/py-sdl2
Source:     PySDL2-%version.tar.gz
BuildArch:  noarch


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

Requires: libSDL2_gfx libSDL2_image libSDL2_mixer libSDL2_ttf libSDL2

%description
PySDL2 is a wrapper around the SDL2 library and as such similar to the
discontinued PySDL project. In contrast to PySDL, it has no licensing
restrictions, nor does it rely on C code, but uses ctypes instead.

%prep
%setup -n PySDL2-%version

%build
%python3_build

%install
%python3_install

%files
%doc examples doc
%python3_sitelibdir_noarch/*


%changelog
* Tue Oct 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.6-alt1
- Version updated to 0.9.6
- disable python2, enable python3

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.5-alt1.1
- NMU: added URL

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
