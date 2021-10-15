# BEGIN SourceDeps(oneline):
BuildRequires: texinfo
# END SourceDeps(oneline)
Group: Sound
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 25

Name:           festival-freebsoft-utils
Version:        0.10
Release:        alt3_%autorelease
Summary:        Utilities that enhance Festival with some useful features

BuildArch:      noarch

License:        GPLv2+
URL:            https://www.freebsoft.org/festival-freebsoft-utils
Source0:        https://freebsoft.org/pub/projects/%{name}/%{name}-%{version}.tar.gz

# Fix a section level error in fdl.texi
# https://github.com/brailcom/festival-freebsoft-utils/pull/1
Patch0:         https://github.com/brailcom/festival-freebsoft-utils/pull/1.patch

Requires:       festival
# From docs/festival-freebsoft-utils.texi:
#   Having SoX (@url{http://sox.sourceforge.net}) installed is strongly
#   recommended, many festival-freebsoft-utils functions don't work without it.
Requires:     libsox-fmt-alsa libsox-fmt-ao libsox-fmt-caf libsox-fmt-fap libsox-fmt-flac libsox-fmt-mat4 libsox-fmt-mat5 libsox-fmt-mp3 libsox-fmt-opus libsox-fmt-oss libsox-fmt-paf libsox-fmt-pulseaudio libsox-fmt-pvf libsox-fmt-sd2 libsox-fmt-sndfile libsox-fmt-vorbis libsox-fmt-w64 libsox-fmt-wavpack libsox-fmt-xi libsox3 sox-base
# From docs/festival-freebsoft-utils.texi:
#   As Festival does not support UTF-8 encoding, festival-freebsoft-utils uses
#   the iconv utility for character coding conversions.
# Note that this is currently provided by glibc-common, so it should be
# available even without the explicit dependency.
Requires:     /usr/bin/iconv
Source44: import.info

%description
A collection of utilities that enhance Festival with some useful features. They
provide all that is needed for interaction with Speech Dispatcher.

Key festival-freebsoft-utils features are:

a.. Generalized concept of input events. festival-freebsoft-utils allows not only
  plain text synthesis, but also combining it with sounds. Additionally,
  mechanism of logical events mapped to other events is provided.
a.. Substitution of events for given words.
a.. High-level voice selection mechanism and setting of basic prosodic parameters.
a.. Spelling mode.
a.. Capital letter signalization.
a.. Punctuation modes, for explicit reading or not reading punctuation characters.
a.. Incremental synthesis of texts and events.
a.. Speech Dispatcher support.
a.. Rudimentary SSML support.
a.. Enhance the Festival extension language with functions commonly used in Lisp.
a.. Support for wrapping already defined Festival functions by your own code.
a.. Everything is written in the extension language, no patching of the Festival
  C++ sources is needed.


%package doc
Group: Sound
Summary:        Documentation for festival-freebsoft-utils

BuildRequires:  texi2dvi
BuildRequires:  tex(latex)
BuildArch: noarch

%description doc
Documentation for festival-freebsoft-utils in info, PDF, and HTML formats.


%prep
%setup -q
%patch0 -p1



%build
# Remove pre-built info page
%make_build clean
# Build info, PDF, and HTML docs from the texinfo sources.
%make_build info html


%install
install -t '%{buildroot}/%{_datadir}/festival' -D -p -m 0644 *.scm
install -t '%{buildroot}/%{_infodir}' -D -p -m 0644 doc/*.info
install -t '%{buildroot}/%{_docdir}/%{name}' -D -p -m 0644 \
    doc/*.html ANNOUNCE NEWS README


%files
%doc --no-dereference COPYING
%{_datadir}/festival/*.scm


%files doc
%doc --no-dereference COPYING
%doc %{_docdir}/%{name}/ANNOUNCE
%doc %{_docdir}/%{name}/NEWS
%doc %{_docdir}/%{name}/README

#doc %{_docdir}/%{name}/festival-freebsoft-utils.pdf
%doc %{_docdir}/%{name}/festival-freebsoft-utils.html

%doc %{_infodir}/festival-freebsoft-utils.info*


%changelog
* Fri Oct 15 2021 Igor Vlasenko <viy@altlinux.org> 0.10-alt3_25
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_11
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_6
- update to new release by fcimport

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_4
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2_3
- update to new release by fcimport

* Sun May 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2_2
- fixed festival_lib path

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_2
- initial release by fcimport

