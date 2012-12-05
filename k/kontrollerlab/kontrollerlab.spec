Summary:	AVR microcontrollers IDE
Name:		kontrollerlab
Version:	0.8.0beta1
Release:	alt3.qa3
License:	GPL
Group:		Development/Tools
URL:		http://sourceforge.net/projects/kontrollerlab/
Source:		%name-%version.tar.bz2
Packager:	Evgeny Sinelnikov <sin@altlinux.ru>

%def_without arts

BuildRequires:	gcc-c++
BuildRequires:	libqt3-devel
BuildRequires:	kdelibs-devel
BuildRequires(pre):	rpm-build-compat

Patch: %name-0.8.0beta1-kshortcut.patch
Patch1: %name-0.8.0beta1-alt-DSO.patch
Patch2: %name-0.8.0beta1-alt-glibc-2.16.patch

%description
The KontrollerLab is an IDE for developing software for Atmel(r) 
AVR(c) microcontrollers using the avr-gcc compiler, the uisp and 
the avrdude upload software.

%prep
%setup
%patch -p2
%patch1 -p2
%patch2 -p2
sed -i 's|/usr/lib/|%_libdir/|' configure

%build
%add_optflags -I%_includedir/tqtinterface
%K3configure --without-arts

%install
%K3install

%files
%doc AUTHORS ChangeLog NEWS README TODO INSTALL COPYING
%_K3bindir/*
%_K3datadir/icons/*/*/*/*.png
%_K3mimelnk/application/*
%_K3applnk/Utilities/*
%_K3apps/*
%_K3doc/*/*

%changelog
* Wed Dec 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0beta1-alt3.qa3
- Fixed build with glibc 2.16

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0beta1-alt3.qa2
- Fixed build

* Tue May 10 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.0beta1-alt3.qa1
- Disable aRts
- Adapt to new KDE3 placement

* Sat Feb 19 2011 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.0beta1-alt3
- Fix build for x86_64 with --enable-libsuffix=64

* Fri Feb 18 2011 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.0beta1-alt2
- Update for new compiler and environment restrictions:
+ Build with tqtinterface includes cxxflags
+ Fix redundant classname for KShortcut
+ Change kde_docdir to _K3doc
+ Build without arts

* Sun Jan 24 2010 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.0beta1-alt1
- Update to last beta version

* Fri Apr 17 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.7.1-alt3
- Add build requires pre for rpm-build-compat

* Thu Apr 16 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.7.1-alt2
- Fix build requires
- Fix intersections with system packages

* Mon Apr 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.7.1-alt1
- Build for Sisyphus

* Sat Feb 24 2008 kontrollerlab 0.7.1
- Created package structure for kontrollerlab
