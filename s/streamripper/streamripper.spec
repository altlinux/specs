Name: streamripper
Version: 1.64.6
Release: alt1

Summary: A tool to rip shoutcast radio streams to mp3/ogg/aac files
Group: Networking/Other
License: GPL
Url: http://streamripper.sourceforge.net/
Packager: Evgenii Terechkov <evg@altlinux.org>

Source0: http://dl.sourceforge.net/sourceforge/streamripper/%name-%version.tar.gz

BuildRequires: binutils-devel libmad-devel libvorbis-devel glib2-devel

%description
Streamripper records shoutcast and icecast compatible streams. It uses
meta data within a shoutcast stream to determine the beginning and end
of each song, and stores the songs on your hard disk as individual
mp3/ogg/aac files. In addition, streamripper includes a relay server
for listening to the station while you are recording.

%prep
%setup -q

mv -f COPYING COPYING.orig
ln -s $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%configure \
	--without-included-libmad \
	--without-included-argv

%make_build

%install
%makeinstall_std

%files
%doc CHANGES THANKS fake_external_metadata.pl fetch_external_metadata.pl parse_rules.txt
%doc --no-dereference COPYING

%_bindir/%name
%_man1dir/%name.1*

%changelog
* Sat Jan  7 2012 Terechkov Evgenii <evg@altlinux.org> 1.64.6-alt1
- 1.64.6

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.63.5-alt1
- 1.63.5 release.

* Tue May 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.62.0-alt1
- 1.62.0 release.

* Mon Jan 29 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.61.27-alt2
- Changed Packager: field.
- Minor spec cleanup.

* Mon Oct 16 2006 Andrei Bulava <abulava@altlinux.ru> 1.61.27-alt1
- 1.61.27

* Mon Aug 28 2006 Andrei Bulava <abulava@altlinux.ru> 1.61.26-alt1
- 1.61.26

* Wed Jul 19 2006 Andrei Bulava <abulava@altlinux.ru> 1.61.24-alt1
- initial build for ALT Linux
