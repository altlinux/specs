Name: cuetools
Version: 1.4.0
Release: alt1.git20131123

Summary: cue and toc file parsers and utilities
Group: Sound
License: GPL
Url: http://developer.berlios.de/projects/cuetools/

Source0: http://prdownload.berlios.de/cuetools/%name-%version.tar.gz

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
%setup

mv -f COPYING COPYING.orig
ln -s $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
mv %buildroot%_bindir/cuetag.sh %buildroot%_bindir/cuetag
install -p -m644 doc/cuetag.1 %buildroot%_man1dir/

%files
%doc AUTHORS ChangeLog NEWS README TODO
%doc doc/formats.txt extras/index.txt
%doc --no-dereference COPYING

%_bindir/cue*
%_man1dir/cue*.1*

%changelog
* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.git20131123
- Version 1.4.0

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.1-alt4.qa1
- NMU: rebuilt for debuginfo.

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

