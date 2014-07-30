# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		opticalraytracer
Version:	2.7
Release:	alt1_7jpp7
Summary:	Utility that analyzes systems of lenses

Group:		Toys
License:	GPLv2+	  
URL:		http://arachnoid.com/OpticalRayTracer/index.html
Source0:	http://arachnoid.com/OpticalRayTracer/OpticalRayTracer_source.tar.gz
Source1:	%{name}.desktop
BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	jpackage-utils
BuildRequires:	ant
BuildRequires:	ant-junit

Requires:	jpackage-utils
Source44: import.info

%description
OpticalRayTracer is a X Window GUI-based utility that analyzes systems of 
lenses. It uses optical principles and a virtual optical bench to predict
the behavior of many kinds of ordinary and exotic lens types.

OpticalRayTracer includes an advanced, easy-to-use interface that allows the
user to rearrange the optical configuration by simply dragging lenses around 
using the mouse.

%package javadoc
Summary:		Javadocs for %{name}
Group:			Development/Java
Requires:		%{name} = %{version}-%{release}
Requires:		jpackage-utils
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

mkdir -p $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/raytracer <<-EOF
	#!/bin/bash
	. /usr/share/java-utils/java-functions
	MAIN_CLASS=opticalraytracer.OpticalRayTracer
	set_classpath "%{name}-%{version}"
	run "$@"
EOF
chmod a+x $RPM_BUILD_ROOT%{_bindir}/raytracer

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/OpticalRayTracer.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar


mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp dist/javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%{_javadir}/*
%{_bindir}/raytracer
%{_datadir}/applications/*opticalraytracer.desktop
%{_datadir}/icons/hicolor/32x32/apps/OpticalRayTracer.png
%doc src/opticalraytracer/help_resources/*

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_7jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_5jpp7
- new version

