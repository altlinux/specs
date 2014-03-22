Name: quakespasm
Version: 0.85.9
Release: alt2

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
install -pm644 gnu.txt %buildroot%docdir/
install -pm644 README.txt %buildroot%docdir/
install -pm644 README.music %buildroot%docdir/
install -pm644 %SOURCE1 %buildroot%docdir/

%files
%_bindir/quakespasm
%dir %docdir
%docdir/README.music
%docdir/README.maintainer
%docdir/*.txt

%changelog
* Sat Mar 22 2014 Andrey Bergman <vkni@altlinux.org> 0.85.9-alt2
- Corrected Group, added README.maintainer.

* Thu Mar 20 2014 Andrey Bergman <vkni@altlinux.org> 0.85.9-alt1
- Initial release for Sisyphus.

