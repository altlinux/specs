# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           anchorman
Version:        0.0.1
Release:        alt2_13
Summary:        The recording-studio-in-a-box

Group:          Sound
License:        GPLv2+
URL:            https://fedorahosted.org/anchorman/
Source0:        https://fedorahosted.org/released/anchorman/%{name}-%{version}.tar.gz

BuildRequires:  gstreamer1.0-devel gstreamer-gir-devel glib2-devel libgio libgio-devel libgudev-devel libgudev-gir-devel ctest cmake
Requires:       gst-plugins-good
Source44: import.info

%description
Ever wanted to run your own recording studio? Need to handle multiple streams of
audio, video, and possibly even subtitles? Anchorman can't do that. Yet.
However, it can stream a webcam to an icecast server. Included is support for
suspending/resuming the stream when the device is inserted/removed.


%prep
%setup -q


%build
%{fedora_cmake} .
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%{_bindir}/anchorman
%doc LICENSE README TODO


%changelog
* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt2_13
- rebuild with gstreamer

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt2_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt2_10
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt2_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt2_8
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt2_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt2_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt2_3
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt2_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_2
- update to new release by fcimport

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_1
- initial release by fcimport

