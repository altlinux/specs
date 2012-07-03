Summary: Recording tool for Skype Calls
Name: skype-call-recorder
Version: 0.8
Release: alt2.qa2
Source: %name-%version.tar.gz
Patch: %name-desktop.patch
Patch1: %name-0.8-alt-DSO.patch
License: GPL
URL: http://atdot.ch/scr/
Packager: Stanislav Yadykin <tosick@altlinux.ru>
Group: Networking/Instant messaging

# Automatically added by buildreq on Tue Dec 09 2008
BuildRequires: ImageMagick-tools cmake gcc-c++ id3lib-devel liblame-devel libqt4-devel libvorbis-devel
BuildRequires: desktop-file-utils

%description
Skype Call recorder allows you to record Skype calls to MP3, Ogg Vorbis or WAV files.

%prep
%setup -q
%patch -p1
%patch1 -p2

%build
CMAKE_INSTALL_PREFIX=/usr /usr/bin/cmake .
%make
for I in 16x16 32x32 48x48; do 
    /usr/bin/convert -resample $I icon.png icon-$I.png
done

%install
%make_install
install -D -m644 icon-16x16.png %buildroot/%_miconsdir/%name.png
install -D -m644 icon-32x32.png %buildroot/%_miconsdir/%name.png
install -D -m644 icon-48x48.png %buildroot/%_miconsdir/%name.png
install -D -m755 %name %buildroot/%_bindir/%name
install -D -m644 %name.desktop %buildroot/%_desktopdir/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=VideoConference \
	%buildroot%_desktopdir/skype-call-recorder.desktop

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_miconsdir/%name.png
%_miconsdir/%name.png
%doc INSTALL COPYING 

%changelog
* Tue Jun 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt2.qa2
- Fixed build

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.8-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for skype-call-recorder
  * postclean-03-private-rpm-macros for the spec file

* Thu Jan 15 2009 Stanislav Yadykin <tosick@altlinux.org> 0.8-alt2
- spec improvements
- desktop file improvements

* Tue Dec 09 2008 Stanislav Yadykin <tosick@altlinux.org> 0.8-alt1
- initial release

