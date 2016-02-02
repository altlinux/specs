Group: Toys
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:		opticalraytracer
Version:	2.7
Release:	alt2_12jpp8
Summary:	Utility that analyzes systems of lenses

License:	GPLv2+	  
URL:		http://arachnoid.com/OpticalRayTracer/index.html
Source0:	http://arachnoid.com/OpticalRayTracer/OpticalRayTracer_source.tar.gz
Source1:	%{name}.desktop
BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	jpackage-utils
BuildRequires:	ant
BuildRequires:	ant-junit

Source44: import.info

%description
OpticalRayTracer is a X Window GUI-based utility that analyzes systems of 
lenses. It uses optical principles and a virtual optical bench to predict
the behavior of many kinds of ordinary and exotic lens types.

OpticalRayTracer includes an advanced, easy-to-use interface that allows the
user to rearrange the optical configuration by simply dragging lenses around 
using the mouse.

%package javadoc
Group: Development/Java
Summary:		Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c

%build
ant 

%install
desktop-file-install \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
%{SOURCE1}

install -D -p -m644 src/opticalraytracer/icons/OpticalRayTracer.png \
$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/OpticalRayTracer.png

%jpackage_script opticalraytracer.OpticalRayTracer '' '' %{name} raytracer true

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/OpticalRayTracer.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar


mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp dist/javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: http://arachnoid.com/messages/index.php
SentUpstream: 2014-09-22
-->
<application>
  <id type="desktop">opticalraytracer.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Analyze the optical properties of lenses</summary>
  <description>
    <p>
      Optical Ray Tracer is an application for analyzing the properties of lenses.
      You specify a single lens, or a series of lenses, then Optical Ray Tracer can
      simulate how light will behave when it passes through them.
    </p>
  </description>
  <url type="homepage">http://arachnoid.com/OpticalRayTracer/index.html</url>
  <screenshots>
    <screenshot type="default">http://arachnoid.com/OpticalRayTracer/images/optical_ray_tracer_image.png</screenshot>
  </screenshots>
</application>
EOF

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files
%{_javadir}/*
%{_bindir}/raytracer
%{_datadir}/appdata/*%{name}.appdata.xml
%{_datadir}/applications/*opticalraytracer.desktop
%{_datadir}/icons/hicolor/32x32/apps/OpticalRayTracer.png
%doc src/opticalraytracer/help_resources/*
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_12jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_12jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_7jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_5jpp7
- new version

