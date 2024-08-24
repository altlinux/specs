Name: quakespasm
Version: 0.96.3
Release: alt1

Summary: Quake engine
License: GPLv2
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
* Sat Aug 24 2024 Andrey Bergman <vkni@altlinux.org> 0.96.3-alt1
- Version update.

* Thu Jun 20 2024 Andrey Bergman <vkni@altlinux.org> 0.96.2-alt1
- Version update.

* Tue Oct 31 2023 Andrey Bergman <vkni@altlinux.org> 0.96.1-alt1
- Version update.

* Mon Sep 11 2023 Andrey Bergman <vkni@altlinux.org> 0.96.0-alt1
- Version update.

* Sun Nov 06 2022 Andrey Bergman <vkni@altlinux.org> 0.95.1-alt1
- Version update.

* Sun Oct 02 2022 Andrey Bergman <vkni@altlinux.org> 0.95.0-alt1
- Version update.

* Sun May 22 2022 Andrey Bergman <vkni@altlinux.org> 0.94.4-alt1
- Version update.

* Wed Dec 29 2021 Andrey Bergman <vkni@altlinux.org> 0.94.3-alt1
- Version update.

* Sat Mar 07 2020 Andrey Bergman <vkni@altlinux.org> 0.93.2-alt1
- Version update.

* Sun Jun 10 2018 Andrey Bergman <vkni@altlinux.org> 0.93.1-alt1
- Version update.

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

