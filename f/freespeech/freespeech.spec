Name: freespeech
Version: a10m
Release: alt3
Packager: Michael Pozhidaev <msp@altlinux.ru>

Summary: %name is a phonetic convertor for text strings
License: GPL
Group: Sound
Requires: tts-base
BuildPreReq: libgdbm-devel perl rpm-macros-tts
Url: http://tcts.fpms.ac.be/synthesis/mbrola.html

Source: http://tcts.fpms.ac.be/synthesis/mbrola/tts/English/fs.a10m.tar.gz
Source2: mbrola.voiceman
Source3: replacements.mbrola
Patch0: freespeech-a10m-alt-build.patch
Patch1: freespeech-a10m-alt-x86_64.patch
Patch2: freespeech-a10m-alt-externals.patch

%description
%name generates phonetic data used as input for speech synthesizers.
Usually it is used as a preprocessor for Mbrola.
So, you should install it if you are going to use Mbrola.

%prep
%setup -q -n distribution

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd lib
make clean
make CFLAGS='%optflags'
cd ../src
make clean
make CFLAGS='%optflags'
cd ..

%install
%__install -pD -m775 ./src/freephone %buildroot%_bindir/freephone
%__install -pD -m664 ./lib/lexicon.dir %buildroot%_datadir/%name/lexicon.dir
%__install -pD -m664 ./lib/lexicon.pag %buildroot%_datadir/%name/lexicon.pag
%__install -pD -m644 %SOURCE3 %buildroot%_datadir/%name/replacements.mbrola
%__install -pD -m644 %SOURCE2 %buildroot%_ttsdir/mbrola.voiceman

%preun
%tts_unregister mbrola

%files
%_bindir/*
%_datadir/*
%_ttsdir/*
%doc README INSTALLATION Copying ACKNOWLEDGEMENTS

%changelog
* Tue Apr 05 2011 Michael Pozhidaev <msp@altlinux.ru> a10m-alt3
- Added tts_unregister call to preun section
- tts-devel buildreq replaced by rpm-macros-tts

* Wed Nov 24 2010 Michael Pozhidaev <msp@altlinux.ru> a10m-alt2
- Added proper installation of mbrola.voiceman file

* Wed Aug 20 2008 Michael Pozhidaev <msp@altlinux.ru> a10m-alt1
- Fixed x86_64 compatibility

* Sun Feb 29 2004 Michael Pozhidaev <msp@altlinux.ru> 10.0-alt2
- Lexicon files are now included

* Thu Oct 23 2003 Michael Pozhidaev <msp@altlinux.ru> 10.0-alt1
- initial rpm
