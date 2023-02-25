Group: Sound
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           gt
Version:        0.4
Release:        alt1_39
Summary:        Modified Timidity which supportes enhanced gus format patches
License:        GPLv2+
URL:            http://alsa.opensrc.org/GusSoundfont
# This is ftp://ling.lll.hawaii.edu/pub/greg/gt-0.4.tar.gz
# with the examples/patch and sfz directories removed as the license of the
# samples in these dirs is unclear. Also the src/ac3* files have been removed
# as these contain patented code.
Source0:        %{name}-%{version}-clean.tar.gz
Patch0:         gt-0.4-noac3.patch
Patch1:         gt-0.4-compile-fix.patch
Patch2:         gt-0.4-optflags.patch
Patch3:         gt-0.4-config-default-velocity-layer.patch
Patch4:         gt-0.4-ppc-compile-fix.patch
Patch5:         gt-0.4-unsf-bigendian-fix.patch
Patch6:         gt-0.4-unsf-tremolo.patch
Patch7:         gt-0.4-gcc10.patch
BuildRequires:  gcc
BuildRequires:  libalsa-devel libvorbis-devel flex
Requires:       timidity-instruments
Source44: import.info

%description
Modified timidity midi player which supportes enhanced gus format patches and
surround audio output.


%package -n soundfont-utils
Group: Sound
Summary:        Utilities for converting from / to various soundfont formats

%description -n soundfont-utils
Utilities for converting from / to various soundfont formats and a midi file
disassembler.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

cp -p src/README README.timidity


%build
export CFLAGS="$RPM_OPT_FLAGS -fsigned-char -std=gnu89"
%configure
make


%install
%makeinstall_std
# rename somewhat genericly named dim to midi-disasm
mv $RPM_BUILD_ROOT%{_bindir}/dim $RPM_BUILD_ROOT%{_bindir}/midi-disasm
mv $RPM_BUILD_ROOT%{_mandir}/man1/dim.1 \
   $RPM_BUILD_ROOT%{_mandir}/man1/midi-disasm.1
sed -i 's/dim/midi-disasm/g' $RPM_BUILD_ROOT%{_mandir}/man1/midi-disasm.1
touch -r utils/midifile.c $RPM_BUILD_ROOT%{_mandir}/man1/midi-disasm.1
 

%files
%doc AUTHORS COPYING ChangeLog FEATURES NEWS README*
%{_bindir}/gt
%{_mandir}/man1/gt.1*

%files -n soundfont-utils
%doc COPYING utils/README* utils/GUSSF2-SPEC
%{_bindir}/*
%exclude %{_bindir}/gt
%{_mandir}/man1/*
%exclude %{_mandir}/man1/gt.1*


%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 0.4-alt1_39
- update to new release by fcimport

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_32
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_26
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_24
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_23
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_22
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_21
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_20
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_19
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_18
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_17
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_16
- update to new release by fcimport

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_15
- new version

