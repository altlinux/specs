%define _unpackaged_files_terminate_build 1
%define _localstatedir %{_var}

Name: mbrola
Version: 3.3
Release: alt4

Summary: MBROLA is a speech synthesizer based on the concatenation of diphones
License: AGPL-3.0
Group:   Sound
Url:     https://github.com/numediart/MBROLA

Source: %name-%version.tar

Requires:       sox-base
Requires: freespeech

BuildRequires: gcc
BuildRequires: make
BuildRequires: fdupes

%description
MBROLA is a speech synthesizer based on the concatenation of diphones.
It takes a list of phonemes as input, together with prosodic information
(duration of phonemes  and a piecewise linear description of pitch),
and produces speech samples on 16 bits (linear), at the sampling
frequency of the diphone database.

It is therefore NOT a Text-To-Speech  (TTS) synthesizer, since it does
not accept raw text as input.  In  order to obtain  a full TTS system,
you need to use this synthesizer in combination with a text processing
system that produces phonetic and prosodic commands such as festival
or freespeech.

%prep
%setup
sed -i 's/SYNTH_VERSION.*/SYNTH_VERSION \"%version\"/' Misc/common.h
%ifarch %e2k
# e2k: fix optlevel (lcc won't accept insane values)
sed -i 's,-O6,-O%_optlevel,g' Makefile
%endif

%build
export CFLAGS="%optflags"
%make_build -j1

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/mbrola
install -m 755 ./Bin/mbrola %buildroot%_bindir/mbrola
fdupes %buildroot%_datadir/%name

%files
%doc README.md
%doc --no-dereference LICENSE
%_bindir/mbrola
%_datadir/%name

%changelog
* Sat Nov 16 2024 Ilya Mashkin <oddity@altlinux.ru> 3.3-alt4
- fix build on Elbrus (Returned the fixline back in spec)

* Tue Oct 29 2024 Artem Semenov <savoptik@altlinux.org> 3.3-alt3
- Remove req to txt2pho
- Deleted say for txt2pho

* Fri Sep 13 2024 Artem Semenov <savoptik@altlinux.org> 3.3-alt2
- Build from gear
- Remove req to voices
- Move txt2pho to package

* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 3.3-alt1_1699.2.pm.49
- update by suseimport

* Wed Dec 01 2021 Igor Vlasenko <viy@altlinux.org> 3.3-alt1_2.12
- we have freespeech on arm/aarch64/ppc64le now

* Fri Oct 01 2021 Igor Vlasenko <viy@altlinux.org> 3.3-alt1_2.9
- fixed build with gcc11
- TODO: need freespeech on arm/aarch64/ppc64le

* Wed Aug 11 2021 Michael Shigorin <mike@altlinux.org> 3.3-alt1_1.10
- fix optlevel (lcc won't accept insane values)

* Fri Jun 11 2021 Igor Vlasenko <viy@altlinux.org> 3.3-alt1_1.9
- new version
- now open source
- TODO: need freespeech on arm/aarch64/ppc64le

* Wed Nov 17 2010 Michael Pozhidaev <msp@altlinux.ru> 3.01-alt6
- Added req to freespeech

* Wed Nov 17 2010 Michael Pozhidaev <msp@altlinux.ru> 3.01-alt5
- Removed VoiceMan configuration entry (now included into freespeech package)

* Mon Jun 28 2010 Michael Pozhidaev <msp@altlinux.ru> 3.01-alt4
- VoiceMan config entry updated to server version 1.5.0

* Fri Oct 17 2008 Igor Vlasenko <viy@altlinux.ru> 3.01-alt3.1
- added missing mbrola.voiceman

* Fri Sep 05 2008 Igor Vlasenko <viy@altlinux.ru> 3.01-alt3
- added voiceman support (thanks to Michael Pozhidaev)

* Thu Oct 26 2006 Igor Vlasenko <viy@altlinux.ru> 3.01-alt2
-  chosen proper mbrola binary

* Tue Oct 24 2006 Igor Vlasenko <viy@altlinux.ru> 3.01-alt1
 - first build for Sisyphus
