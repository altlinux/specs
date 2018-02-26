Name: cuetools
Version: 1.3.1
Release: alt4

Summary: cue and toc file parsers and utilities
Group: Sound
License: GPL
Url: http://developer.berlios.de/projects/cuetools/
Packager: Pavlov Konstantin <thresh@altlinux.ru>

Source0: http://prdownload.berlios.de/cuetools/%name-%version.tar.gz
Patch: %name-%version-%release-alt-changes.patch

# Automatically added by buildreq on Thu Jul 27 2006
BuildRequires: flex

%description
cuetools is a set of utilities for working with Cue Sheet (cue) and Table of
Contents (toc) files.

It includes:

* cueconvert - convert between the cue and toc formats
* cuebreakpoints - print the breakpoints from a cue or toc file
* cueprint - print disc and track infomation for a cue or toc file

%prep
%setup -q
%patch -p1

mv -f COPYING COPYING.orig
ln -s $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
install -pD extras/cuetag.sh %buildroot%_bindir/cuetag

%files
%doc AUTHORS ChangeLog NEWS README TODO
%doc extras/formats.txt extras/index.txt
%doc --no-dereference COPYING

%_bindir/cue*
%_man1dir/cue*.1*

%changelog
* Wed Feb 11 2009 Afanasov Dmitry <ender@altlinux.org> 1.3.1-alt4
- install cuetag.sh in %_bindir as cuetag

* Wed Feb 11 2009 Afanasov Dmitry <ender@altlinux.org> 1.3.1-alt3
- fix cuetag.sh errors:
  + change old metaflac options
  + handle filenames with blanks

* Sat Jan 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.3.1-alt2
- Fixed URL field.
- Changed packager.
- Minor spec cleanup.

* Fri Jul 28 2006 Andrei Bulava <abulava@altlinux.ru> 1.3.1-alt1
- initial build for ALT Linux

