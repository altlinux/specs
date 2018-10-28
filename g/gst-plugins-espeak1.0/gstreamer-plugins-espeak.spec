Group: System/Libraries
%define oldname gstreamer-plugins-espeak
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           gst-plugins-espeak1.0
Version:        0.5.0
Release:        alt1_5
Summary:        A simple gstreamer plugin to use espeak
License:        LGPLv2+
URL:            http://wiki.sugarlabs.org/go/Activity_Team/gst-plugins-espeak
Source0:        http://download.sugarlabs.org/sources/honey/gst-plugins-espeak/gst-plugins-espeak-%{version}.tar.gz

Patch0:		fix-export-regex.patch

BuildRequires:  gcc
BuildRequires:  libespeak-devel
BuildRequires:  glib2-devel libgio libgio-devel
BuildRequires:  gst-plugins1.0-devel gst-plugins1.0-gir-devel
BuildRequires:  gstreamer1.0-devel libgstreamer1.0-gir-devel
Source44: import.info

%description
A simple gstreamer plugin to use espeak as a sound source.
It was developed to simplify the espeak usage in the Sugar Speak activity.
The plugin uses given text to produce audio output. 

%prep
%setup -q -n gst-plugins-espeak-%{version}
%patch0 -p1

%build
# make sure to build the plugin for release
sed -i 's/NANO=1/NANO=0/g' configure
%configure
%make_build V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT

# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/gstreamer-espeak.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2013 Richard Hughes <richard@hughsie.com> -->
<component type="codec">
  <id>gstreamer-espeak</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>eSpeak GStreamer Multimedia Codec</name>
  <summary>Multimedia playback for eSpeak</summary>
  <description>
    <p>
      eSpeak is a compact open source text-to-speech synthesizer for English
      and other languages.
      This codec includes different voices, whose characteristics can be altered.
    </p>
    <p>
      A codec decodes audio and video for for playback or editing and is also
      used for transmission or storage.
      Different codecs are used in video-conferencing, streaming media and
      video editing applications.
    </p>
  </description>
  <url type="homepage">http://gstreamer.freedesktop.org/</url>
  <url type="bugtracker">https://bugzilla.gnome.org/enter_bug.cgi?product=GStreamer</url>
  <url type="donation">http://www.gnome.org/friends/</url>
  <url type="help">http://gstreamer.freedesktop.org/documentation/</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

# remove libtool archives
find %{buildroot} -name '*.la' -delete

%files
%doc --no-dereference COPYING
%doc AUTHORS README NEWS
%{_datadir}/appdata/*.appdata.xml
%{_libdir}/gstreamer-1.0/libgstespeak.so


%changelog
* Sun Oct 28 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_5
- fixed build

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
