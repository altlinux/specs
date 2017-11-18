Name: gst-plugins-espeak1.0
Version: 0.5.0
Release: alt1
Summary: Simple gstreamer plugin to use espeak by way of sound source
License: LGPLv2+
Group: System/Libraries
Url: http://sugarlabs.org/go/DevelopmentTeam/gst-plugins-espeak
Packager: Sugar Development Team <sugar@packages.altlinux.org>


Source: http://download.sugarlabs.org/sources/honey/gst-plugins-espeak/gst-plugins-espeak-%version.tar

Requires: libespeak
Requires: gst-plugins-base1.0
Requires: gst-plugins-good1.0
Requires: gstreamer1.0-utils

BuildRequires: libespeak-devel  
BuildRequires: gst-plugins1.0-devel
BuildRequires: gstreamer1.0-utils  

%description
Simple gstreamer plugin to use espeak by way of sound source.
It was developed to simplify espeak usage in Sugar Speak activity.

%prep
%setup -v -n gst-plugins-espeak-%version


%build
# make sure to build the plugin for release                                     
sed -i 's/NANO=1/NANO=0/g' configure                                            
%define __libtoolize true
%configure
make

%install
make DESTDIR=%{buildroot} install

%files 
%{_libdir}/gstreamer*/*
%doc AUTHORS COPYING NEWS README

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1
- new version

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- update to 0.4.0 for gstreamer1

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1
- update to 0.3.5 version for old gstreamer

* Sun Apr 11 2010 Aleksey Lim <alsroot@altlinux.org> 0.3.4-alt1
- update to 0.3.4 version

* Wed Apr 29 2009 Aleksey Lim <alsroot@altlinux.org> 0.3.3-alt1
- update to 0.3.3 version

* Tue Apr 28 2009 Aleksey Lim <alsroot@altlinux.org> 0.3.1-alt1
- update to 0.3.1 version

* Tue Mar 17 2009 Aleksey Lim <alsroot@altlinux.org> 0.3-alt1
- update to 0.3 version

* Tue Feb 17 2009 Aleksey Lim <alsroot@altlinux.org> 0.1-alt1
- first build for ALT Linux Sisyphus
