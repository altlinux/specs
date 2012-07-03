Name: terminatorx
Version: 3.83
Release: alt2.qa2
Summary: realtime audio synthesizer

Group: Sound
License: GPL
Url: http://www.terminatorx.org

Source: terminatorX-%version.tar
Patch0: %name-%version-%release.patch
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: libalsa-devel libpng-devel ladspa_sdk libxml2-devel libgtk+2-devel liblrdf-devel libaudiofile-devel libmad-devel libsox-devel libvorbis-devel libcap-devel libXxf86dga-devel librarian libXi-devel gcc-c++ gnome-libs-devel vorbis-tools mpg123 libjack-devel
Requires: ladspa_sdk vorbis-tools
BuildRequires: desktop-file-utils

%description
terminatorX is a realtime audio synthesizer that allows you to "scratch"
on digitally sampled audio data (*.wav, *.au, *.ogg, *.mp3, etc.) the
way hiphop-DJs scratch on vinyl records. It features multiple
turntables, realtime effects (buit-in as well as LADSPA plugin effects),
a sequencer and MIDI interface - all accessible through an easy-to-use
gtk+ GUI.

%prep
%setup -q -n terminatorX-%version
%patch0 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Audio \
	--add-category=AudioVideoEditing \
	%buildroot%_desktopdir/terminatorX.desktop

%files -f %name.lang
%_bindir/terminatorX
%_man1dir/terminatorX.1*
%_datadir/omf/terminatorX
%_datadir/terminatorX
%_desktopdir/terminatorX.desktop
%_liconsdir/terminatorX-app.png
%_iconsdir/hicolor/48x48/mimetypes/terminatorX-mime.png
%_datadir/mime-info/terminatorX.*
%doc AUTHORS COPYING COPYING-DOCS ChangeLog

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.83-alt2.qa2
- Fixed build

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 3.83-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for terminatorx

* Wed Mar 09 2011 Vladimir Lettiev <crux@altlinux.ru> 3.83-alt2
- updated buildreqs

* Wed Feb 09 2011 Vladimir Lettiev <crux@altlinux.ru> 3.83-alt1
- initial build

