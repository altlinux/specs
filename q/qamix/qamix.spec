Packager: Alex Negulescu <alecs@altlinux.org>
Name: qamix
Version: 0.0.7
Release: alt3.1

Summary: QAMix is a configurable mixer for ALSA
Group: Sound
License: GPL
Url: http://alsamodular.sourceforge.net

Source: %name-%{version}e.tar.bz2
#Source1: %name-48x48.xpm
#Source2: %name-32x32.xpm
#Source3: %name-16x16.xpm
Patch0: qamix-0.0.7-alt-DSO.patch

BuildRequires: gcc-c++ libalsa-devel libqt3-devel desktop-file-utils ImageMagick

%description
QAMix is a configurable mixer for ALSA.

%prep
%setup -n %name-%{version}e
%patch0 -p2
find -type f -print0 |xargs -r0 %__subst 's,sys/\(asoundlib.h\),alsa/\1,' --
find -type f -print0 |xargs -r0 %__subst 's,^[[:blank:]]*$,,g' --
%__subst 's,\(^CXXFLAGS.*\),\1 \$(RPM_OPT_FLAGS),' make_%name

%build
%make_build QT_BASE_DIR=%_libdir/qt3 -f make_%name

%install
install -pD %name %buildroot%_bindir/%name
mkdir -p %buildroot%_datadir/%name
install -m644 *.xml %buildroot%_datadir/%name/

# menu
desktop-file-install \
		     --dir %buildroot%_desktopdir \
		     --add-category=Mixer \
		     --add-category=Audio \
		     --add-category=AudioVideo \
		      --remove-key=Encoding \
		     %name.desktop
echo "Comment=A configurable mixer for ALSA" >> %buildroot%_desktopdir/%name.desktop

# icons
mkdir -p %buildroot{%_niconsdir,%_miconsdir,%_liconsdir}
install -pD -m644 multimedia.png %buildroot%_liconsdir/%name.png
convert -size 32x32 multimedia.png %buildroot%_niconsdir/%name.png
convert -size 16x16 multimedia.png %buildroot%_niconsdir/%name.png
install -pD -m644 mini-kamix.png %buildroot%_iconsdir/hicolor/22x22/apps/mini-kamix.png
convert -size 16x16 mini-kamix.png %buildroot%_miconsdir/mini-kamix.png

%files
%doc README
%_bindir/%name
%_datadir/%name
%_iconsdir/hicolor/*/apps/*.png
%_desktopdir/%name.desktop

# TODO(php-coder) for new maintainer:
# - add THANKS file to documentation
# - make .mo files and install them
# - make and install kamix
# - update BuildRequires

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt3.1
- Fixed build

* Wed Aug 10 2011 Alex Negulescu <alecs@altlinux.org> 0.0.7-alt3
- replaced references to kamix.png -> mini-kamix.png (#25781)

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.7-alt2.qa1
- NMU: converted menu to desktop file; installed pixmaps

* Fri Sep 04 2009 Alex Negulescu <alecs@altlinux.org> 0.0.7-alt2
- Cleanup spec
- Initial build for Sisyphus

* Sun Jun 03 2007 Slava Semushin <php-coder@altlinux.ru> 0.0.7-alt1e
- NMU
- Trying to fix build under x86_64

* Sun Jun 03 2007 Slava Semushin <php-coder@altlinux.ru> 0.0.7-alt0e
- NMU
- Updated to version 0.0.7e
- Fixed bad encoding specification in Summary and %%description (#5122)
- Updated Url tag
- Spec cleanup:
  + s/%%setup -q/%%setup/
  + Removed trailing spaces
  + Don't use macroses for cat, install and mkdir command

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.0.6-alt0.5.1
- Rebuilt with libstdc++.so.6.

* Fri Aug 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.6-alt0.5
- 0.0.6
- summary, description by avp.

* Thu Jun 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.1-alt0.5
- First build for Sisyphus.

