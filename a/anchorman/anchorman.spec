# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           anchorman
Version:        0.0.1
Release:        alt2_2
Summary:        The recording-studio-in-a-box

Group:          Sound
License:        GPLv2+
URL:            https://fedorahosted.org/anchorman/
Source0:        https://fedorahosted.org/released/anchorman/%{name}-%{version}.tar.gz

BuildRequires:  gstreamer-devel libglib2-devel libgudev-devel ctest cmake
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
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%{_bindir}/anchorman
%doc LICENSE README TODO


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt2_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_2
- update to new release by fcimport

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_1
- initial release by fcimport

