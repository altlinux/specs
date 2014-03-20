Name: quakespasm
Version: 0.85.9
Release: alt1

Summary: Quake engine
License: GPL
Group: Graphics
Url: http://quakespasm.sf.net

Packager: %packager
Source: %name-%version.tar

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

%files
%_bindir/quakespasm
%dir %docdir
%docdir/README.music
%docdir/*.txt

%changelog
* Thu Mar 20 2014 Andrey Bergman <vkni@altlinux.org> 0.85.9-alt1
- Initial release for Sisyphus.

