Name: quakespasm
Version: 0.93
Release: alt1

Summary: Quake engine
License: GPL
Group: Games/Arcade
Url: http://quakespasm.sf.net

Packager: %packager
Source: %name-%version.tar
Source1: README.maintainer

# Automatically added by buildreq on Thu Mar 20 2014
# optimized out: libGL-devel libGLU-devel libX11-devel libcloog-isl4 libogg-devel
BuildRequires: libSDL-devel libmad-devel libvorbis-devel

%description
An engine for iD software's Quake.

%description -l ru_RU.UTF-8
quakespasm - современный движок для игры Quake.

%prep
%setup -q

%build
cd Quake
%make

%install
mkdir -p %buildroot/%_bindir/
install -pm755 Quake/quakespasm %buildroot/%_bindir/

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir

install -pm644 LICENSE.txt %buildroot%docdir/
install -pm644 Quakespasm.html %buildroot%docdir/
install -pm644 Quakespasm.txt %buildroot%docdir/
install -pm644 Quakespasm-Music.txt %buildroot%docdir/

install -pm644 %SOURCE1 %buildroot%docdir/

%files
%_bindir/quakespasm
%dir %docdir
%docdir/LICENSE.txt
%docdir/Quakespasm.html
%docdir/Quakespasm.txt
%docdir/Quakespasm-Music.txt
%docdir/README.maintainer

%changelog
* Sat Dec 02 2017 Andrey Bergman <vkni@altlinux.org> 0.93-alt1
- Version update.

* Wed Aug 24 2016 Andrey Bergman <vkni@altlinux.org> 0.92.1-alt1
- Version update.

* Sat Jul 02 2016 Andrey Bergman <vkni@altlinux.org> 0.92.0-alt1
- Version update.

* Fri Jan 29 2016 Andrey Bergman <vkni@altlinux.org> 0.91.0-alt1
- Version update.

* Tue Jun 23 2015 Andrey Bergman <vkni@altlinux.org> 0.90.1-alt1
- Version update.

* Tue Oct 28 2014 Andrey Bergman <vkni@altlinux.org> 0.90.0-alt1
- Version update.

* Sat Mar 22 2014 Andrey Bergman <vkni@altlinux.org> 0.85.9-alt2
- Corrected Group, added README.maintainer.

* Thu Mar 20 2014 Andrey Bergman <vkni@altlinux.org> 0.85.9-alt1
- Initial release for Sisyphus.

