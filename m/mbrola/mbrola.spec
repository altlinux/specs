# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#
# spec file for package mbrola
#
# Copyright (c) 2021 Packman Team <packman@links2linux.de>
# Copyright (c) 2016-2019 Bernhard M. Wiedemann <bernhard+packman@lsmod.de>
# Copyright (c) 2005-2009 Manfred Tremmel <Manfred.Tremmel@iiv.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.links2linux.org/
#


%define tver    0.96
Name:           mbrola
Version:        3.3
Release:        alt1_1699.2.pm.49
Summary:        Speech Synthesis System
Summary(de):    Sprachsynthese System
License:        AGPL-3.0-or-later
Group:          Text tools
URL:            https://github.com/numediart/MBROLA
Source0:        https://github.com/numediart/MBROLA/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        https://github.com/GHPS/txt2pho/archive/%{tver}.tar.gz#/txt2pho-%{tver}.tar.gz
Source3:        say
Source4:        txt2phorc
# PATCH-FIX-OPENSUSE txt2pho-gcc11.patch
Patch0:         txt2pho-gcc11.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
Requires:       sox-base
Requires:     mbrola-voice
Source44: import.info
Requires: freespeech

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
%description -l de
Sprachsynthese System.
Für deutsche Sprachausgabe installieren Sie eines oder mehrere der
mbrola-de Pakete.

%prep
%setup -q -n MBROLA-%{version} -a 0 -a 2
%patch0 -p1
mkdir txt2pho-%{tver}/lib txt2pho-%{tver}/obj
sed -i 's/SYNTH_VERSION.*/SYNTH_VERSION \"%{version}\"/' Misc/common.h
# e2k: fix optlevel (lcc won't accept insane values)
sed -i 's,-O6,-O%_optlevel,g' Makefile MBROLA-%version/Makefile

%build
export CFLAGS="%{optflags}"
%make_build -j1
pushd txt2pho-%{tver}
# not parallel-safe
make CFLAGS="%{optflags}"
popd

%install
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/mbrola
install -m 755 ./Bin/mbrola %{buildroot}%{_bindir}/mbrola

pushd txt2pho-%{tver}
install -m 755 txt2pho %{buildroot}%{_bindir}/
cp -r data %{buildroot}%{_datadir}/mbrola/
install -m 755 pipefilt %{buildroot}%{_bindir}/
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/txt2pho
install -m 755 preproc %{buildroot}%{_bindir}/
install -m 644 data/PPRules/rules.lst %{buildroot}%{_datadir}/mbrola/
install -m 644 data/hadifix.abk %{buildroot}%{_datadir}/mbrola/
popd
install -m 755 %{SOURCE3} %{buildroot}%{_bindir}/mbrola-de6-say
fdupes %{buildroot}%{_datadir}/%{name}

%files
%doc README.md
%doc --no-dereference LICENSE
%config(noreplace) %{_sysconfdir}/txt2pho
%{_bindir}/mbrola
%{_bindir}/pipefilt
%{_bindir}/preproc
%{_bindir}/mbrola-de6-say
%{_bindir}/txt2pho
%{_datadir}/%{name}

%changelog
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

