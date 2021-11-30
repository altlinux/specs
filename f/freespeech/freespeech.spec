
Name: freespeech
Version: a10m
Release: alt4
Packager: Michael Pozhidaev <msp@altlinux.ru>

Summary: %name is a phonetic convertor for text strings
License: GPL
Group: Sound
Requires: tts-base
BuildRequires(pre): rpm-macros-tts
BuildRequires: libgdbm-devel perl libdb6.1-devel
Url: http://tcts.fpms.ac.be/synthesis/mbrola.html

Source: http://tcts.fpms.ac.be/synthesis/mbrola/tts/English/fs.a10m.tar.gz
# use new name enlex.db
Source2: mbrola.voiceman
Source3: replacements.mbrola
# use old name enlex.db
#Source4: mbrola.voiceman.lexicon

Patch0: http://poretsky.homelinux.net/packages/debian/pool/free/f/freespeech/freespeech_1.0m-16focal1.diff

# old msp@ patches:
# no need; overridden by poretsky@ debian patch
# Patch10: freespeech-a10m-alt-build.patch
# Patch11: freespeech-a10m-alt-x86_64.patch
# no need; deprecated by poretsky@ debian patch
# Patch12: freespeech-a10m-alt-externals.patch



%description
%name generates phonetic data used as input for speech synthesizers.
Usually it is used as a preprocessor for Mbrola where
freephone converts English text to phonemes.

Install it if you are going to use Mbrola.

It can make use of an external dictionary in hash format,
such as the one provided by enlex package.

%if_with enlex
%package -n enlex
Summary: English pronunciation dictionary
Requires: ${misc:Depends}

%description -n enlex
This package is aimed primarily for use together with the Freephone
phonetizer for Mbrola. When it is installed you can instruct Freephone
to use the pronunciation dictionary by the command line switch
"-h /usr/share/freespeech/enlex.db".
%endif

%prep
%setup -q -n distribution

%patch0 -p1

#patch10 -p1
#patch11 -p1
#patch12 -p1

%build
cd lib
make clean
make CFLAGS='%optflags'
cd ../src
make clean
make CFLAGS='%optflags'
cd ..

%install
install -pD -m775 ./src/freephone %buildroot%_bindir/freephone

# old names
#install -pD -m664 ./lib/lexicon.dir %buildroot%_datadir/%name/lexicon.dir
#install -pD -m664 ./lib/lexicon.pag %buildroot%_datadir/%name/lexicon.pag

install -pD -m755 ./lib/lexholder %buildroot%_bindir/lexholder-en
install -pD -m644 ./lib/lexicon %buildroot%_datadir/%name/enlex.db

install -pD -m644 %SOURCE3 %buildroot%_datadir/%name/replacements.mbrola
install -pD -m644 %SOURCE2 %buildroot%_ttsdir/mbrola.voiceman


# installing debian man pages
install -d %buildroot%_man1dir
install -m644 debian/freephone.1 debian/lexholder-en.1 %buildroot%_man1dir/

%preun
%tts_unregister mbrola

%files
%_bindir/freephone
%_man1dir/freephone.1*
%dir %_datadir/%name
%_datadir/%name/replacements.mbrola
%_ttsdir/mbrola.voiceman
%doc README INSTALLATION Copying ACKNOWLEDGEMENTS
%doc doc/minidesc.doc
%doc doc/OVERVIEW
%doc doc/phoncode.doc
%doc doc/spn_format.doc
%if_with enlex
%files -n enlex
%endif
%doc doc/phoncode.doc
%doc lib/text710.doc
%_bindir/lexholder-en
%_man1dir/lexholder-en.1*
%_datadir/%name/enlex.db

%changelog
* Wed Dec 01 2021 Igor Vlasenko <viy@altlinux.org> a10m-alt4
- switched to Igor Poretsky's debian release:
- lexholder is renamed to lexholder-en
- lexicon is now enlex.db
- freephone switch is now -h /usr/share/freespeech/enlex.db
- hopefully now builds on armh, aarch64 and ppc64le

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
