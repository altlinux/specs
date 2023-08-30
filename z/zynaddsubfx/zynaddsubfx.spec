Name: zynaddsubfx
Version: 3.0.6
Release: alt4

Summary: %name is a open source software synthesizer
License: GPLv2+
Group: Sound
Url: http://zynaddsubfx.sourceforge.net/

Source0: %name-%version-%release.tar
Source1: DPF.tar
Source2: pugl.tar
Source3: instruments.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(mxml)
BuildRequires: pkgconfig(rtosc)
BuildRequires: pkgconfig(zlib)

BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xrandr)

%description
%name is a open source software synthesizer capable of making a countless
number of instruments, from some common heard from expensive hardware to
interesting sounds that you'll boost to an amazing universe of sounds.

%prep
%setup -a1 -a2 -a3
sed -i '/^#include <string>/ a#include <cstdint>' \
    src/Misc/Bank.h src/Nio/Engine.h
sed -i 's,/opt/zyn-fusion,%_libdir/zyn-fusion,' \
    src/Plugin/ZynAddSubFX/ZynAddSubFX-UI-Zest.cpp

%build
%cmake -DGuiModule=zest -DDefaultOutput=jack -DPluginLibDir=%_lib
%cmake_build

%install
%cmakeinstall_std

%global _customdocdir %_defaultdocdir/%name

%files
%_bindir/zynaddsubfx
%_libdir/lv2/*
%_libdir/vst/*
%_datadir/bash-completion/*/zynaddsubfx
%_datadir/doc/zynaddsubfx
%_datadir/zynaddsubfx
%_desktopdir/*.desktop
%_pixmapsdir/zynaddsubfx.*

%changelog
* Wed Aug 30 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.6-alt4
- fix ui plugin search path (closes: 47068)

* Fri Jun 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.6-alt3
- rebuilt with gcc13

* Tue Feb 01 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.6-alt2
- 3.0.6 released

* Wed Dec 01 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.6-alt1
- 3.0.6-rc4-38-g4b591948

* Thu Apr 28 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.4.1-alt2.1.qa4
- Fixed build with libfltk13-1.3.3-alt1.

* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt2.1.qa3
- Rebuilt with updated libfltk

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt2.1.qa2
- Rebuilt with new FLTK

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.4.1-alt2.1.qa1
- NMU: rebuilt for updated dependencies.

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt2.1
- Rebuilt with FLTK 1.3.0.r8575

* Mon Feb 28 2011 Egor Glukhov <kaman@altlinux.org> 2.4.1-alt2
- Fixed to build against fltk 1.3

* Sun Jul 18 2010 Egor Glukhov <kaman@altlinux.org> 2.4.1-alt1
- 2.4.1 from upstream tarball

