%define _unpackaged_files_terminate_build 1

Name:    freespeech
Version: 2.0.0
Release: alt1
Epoch: 1
Summary: English text preprocessor for MBROLA speech synthesizer
License: GPL
Group: Other
Url: https://github.com/poretsky/freespeech
VCS: https://github.com/poretsky/freespeech.git

Source: %name-%version.tar
Patch: Fixed-include-pathes.patch

BuildRequires: libgdbm-devel
BuildRequires: perl-devel

%description
%name generates phonetic data used as input for speech synthesizers.
Usually it is used as a preprocessor for Mbrola where
freephone converts English text to phonemes.

%package -n enlex-data
Summary: English pronunciation dictionary
Group: Other
Requires: freephone = %EVR
Provides: %name = %EVR
Obsoletes: %name < %EVR

%description -n enlex-data
This package is aimed primarily for use together with the Freephone
 phonetizer for Mbrola. When it is installed you can instruct Freephone
 to use the pronunciation dictionary by the command line switch

%package -n freephone
Summary: English Text-To-Phoneme converter
Group: Other

%description -n freephone
freephone converts English text to phonemes for MBROLA.

 It can make use of an external dictionary in hash format,
 such as the one provided by enlex-data package.

%package doc
Summary: Doc files fore %name
Group: Documentation 
BuildArch: noarch

%description doc
%summary

%prep
%setup
%autopatch -p1

%build
%add_optflags -std=gnu14
%make_build LIBS=-lgdbm_compat -C lib

%install
%makeinstall_std

# installing debian man pages
install -d %buildroot%_man1dir

%files doc
%doc ACKNOWLEDGEMENTS Copying INSTALLATION README README.md
%_man1dir/*
%_docdir/enlex-data

%files -n freephone
%_bindir/freephone
%_bindir/lexholder-en

%files -n enlex-data
%_datadir/freespeech/enlex.dir
%_datadir/freespeech/enlex.pag

%changelog
* Tue May 19 2026 Artem Semenov <savoptik@altlinux.org> 1:2.0.0-alt1
- Updated to new version 2.0.0
- Removed debian patches
- Transition to GDBM (thx Igor B. Poretsky)
- Hardening (thx Samuel Thibault)
- Fixed man pages (thx Igor B. Poretsky)
- Added missed license info (thx Igor B. Poretsky)
- Add and update links (thx Nikita Tseykovets)

* Wed May 13 2026 Artem Semenov <savoptik@altlinux.org> r1.0m.21-alt2
- Applied debian patches

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
