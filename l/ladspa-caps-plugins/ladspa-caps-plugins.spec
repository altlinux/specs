# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           ladspa-caps-plugins
Version:        0.9.24
Release:        alt3_4
Summary:        The C* Audio Plugin Suite
License:        GPLv3+
Group:          Sound
URL:            http://quitte.de/dsp/caps.html
Source0:        http://quitte.de/dsp/caps_%{version}.tar.bz2
Patch0:         caps-0.9.10-nostrip.patch
Patch1:         caps-0.9.24-gcc6.patch
Patch2:         caps-0.9.24-alt-compat.patch
BuildRequires:  ladspa_sdk
Requires:       ladspa_sdk
Obsoletes:      caps <= 0.3.0-2
Provides:       caps = %{version}-%{release}
Source44: import.info
Conflicts: ladspa-caps < 0.4.3
Obsoletes: ladspa-caps < 0.4.3
Provides: ladspa-caps = %version

%description
caps, the C* Audio Plugin Suite, is a collection of refined LADSPA
units including instrument amplifier emulation, stomp-box classics,
versatile 'virtual analog' oscillators, fractal oscillation, reverb,
equalization and others.


%prep
%setup -q -n caps-%{version}
%patch0 -p1 -z .nostrip
%patch1 -p1
%patch2 -p2
# use the system version of ladspa.h
rm ladspa.h


%build
%make_build OPTS="$RPM_OPT_FLAGS -fPIC"


%install
%makeinstall_std DEST=%{_libdir}/ladspa


%files
%doc CHANGES README*
%doc COPYING
%{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/*


%changelog
* Thu Feb 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.24-alt3_4
- Fixed build with new toolchain.

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.24-alt2_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.24-alt2_2
- update to new release by fcimport

* Wed Sep 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.24-alt2_1
- to Sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.24-alt1_1
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_5
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_3
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_2
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_1
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1_1
- update to new release by fcimport

* Wed May 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_9
- initial fc import

