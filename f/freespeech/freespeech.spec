%define _unpackaged_files_terminate_build 1

Name:    freespeech
Version: r1.0m.21
Release: alt1

Summary: English text preprocessor for MBROLA speech synthesizer
License: GPL
Group:   Other
Url:     https://github.com/poretsky/freespeech

Source: %name-%version.tar
Patch0: Alt.patch

BuildRequires: libgdbm-devel
BuildRequires: perl
BuildRequires: libdb6.1-devel

%description
%name generates phonetic data used as input for speech synthesizers.
Usually it is used as a preprocessor for Mbrola where
freephone converts English text to phonemes.

%prep
%setup
%patch0 -p1

%build
%make_build

%install
%makeinstall_std

# installing debian man pages
install -d %buildroot%_man1dir
install -m644 debian/freephone.1 debian/lexholder-en.1 %buildroot%_man1dir/

%files
%doc *.md
%_bindir/freephone
%_bindir/lexholder-en
%_man1dir/*
%dir %_datadir/freespeech
%_datadir/freespeech/enlex.db
%_datadir/doc/enlex-data

%changelog
* Tue Aug 27 2024 Artem Semenov <savoptik@altlinux.org> r1.0m.21-alt1
- Rebuild from new repo (ALT bug: 51043)

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
