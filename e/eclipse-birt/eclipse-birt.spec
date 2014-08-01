# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
%define rlsdate %(date '+%%Y%%m%%d0000')
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name eclipse-birt
%define version 4.2.2
%global eclipse_dropin   %{_datadir}/eclipse/dropins

# Match the context qualifier with the upstream p2 repo
# 
# eclipse -consolelog -nosplash -application org.eclipse.equinox.p2.director \
#  -repository http://download.eclipse.org/birt/update-site/3.7 -list | \
#  grep org.eclipse.birt.feature.group | grep %%{version} | \
#  sed "s/org.eclipse.birt.feature.group=//" | \
#  sed "s/%%{version}.//" | \
#  sed "s/-.*//"
%global qualifier v201302161152
%global tag BIRT_4_2_2_Release_201302161152

Name:      eclipse-birt
Version:   4.2.2
Release:   alt1_1jpp7
Summary:   Eclipse-based reporting system
Group:     System/Libraries
License:   EPL
URL:       http://www.eclipse.org/birt/

# Generate Source0 using Source1
Source0:   %{name}-%{version}-fetched-src.tar.bz2
Source1:   fetch-birt.sh
Source2:   %{name}-fedora-data-feature.tar.bz2
# smil in Fedora is merged in xml-commons-apis-ext.jar, reflecting upstream changes
Patch0:    birt-remove-smil.patch
# 351482: BIRT does not work with Rhino (org.mozilla.javascript) 1.7R3
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=351482
#
# FIXME:  This is only a first-step patch to make it build with Rhino 1.7R3.
Patch1:    %{name}-build-with-rhino-1.7R3.patch

%if 0%{?rhel} >= 6
ExclusiveArch: %{ix86} x86_64
%else
BuildArch:        noarch
%endif
Source44: import.info


%description
BIRT is an Eclipse-based open source reporting system for web applications,
especially those based on Java and J2EE. BIRT has two main components: 
a report designer based on Eclipse, and a runtime component that you 
can add to your app server. BIRT also offers a charting engine that lets 
you add charts to your own application. 

%package chart
Group: System/Libraries
Summary:   Eclipse-based reporting system, the chart component
Obsoletes: eclipse-birt <= 4.2.0-0.1

BuildRequires:    jpackage-utils
BuildRequires:    eclipse-pde >= 1:4.2.0-0.4
BuildRequires:    eclipse-dtp >= 1.10
BuildRequires:    eclipse-emf
BuildRequires:    eclipse-gef
# 1.7-0.9.r2 is the first evr to contain OSGi metadata
BuildRequires:    rhino >= 1.7-0.9.r2
# FIXME:  should probably have a BuildRequires: rhino < 1.7-0.10.r3 here, but:
# 351482: Imported class removed in Rhino (org.mozilla.javascript) 1.7R3
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=351482
# This batik build contains OSGi manifests that BIRT needs
BuildRequires:    batik >= 1.7-12
BuildRequires:    fop >= 0.95-2
BuildRequires:    apache-commons-codec >= 1.3-9.4
BuildRequires:    sac >= 1.3-3.3

Requires:         jpackage-utils
Requires:         eclipse-platform >= 1:3.7.0
Requires:         eclipse-dtp >= 1.10
Requires:         eclipse-emf >= 2.6.0
Requires:         eclipse-gef >= 3.6.0
# 1.7-0.9.r2 is the first evr to contain OSGi metadata
Requires:    rhino >= 1.7-0.9.r2
# FIXME:  should probably have a Requires: rhino < 1.7-0.10.r3 here
# 351482: Imported class removed in Rhino (org.mozilla.javascript) 1.7R3
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=351482
# This batik build contains OSGi manifests that BIRT needs
Requires:         batik >= 1.7-12
Requires:         fop >= 0.95-2
Requires:         apache-commons-codec >= 1.3-9.4
Requires:         sac >= 1.3-3.3

%description chart
BIRT is an Eclipse-based open source reporting system for web applications,
especially those based on Java and J2EE. BIRT has two main components: 
a report designer based on Eclipse, and a runtime component that you 
can add to your app server. BIRT also offers a charting engine that lets 
you add charts to your own application.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p2

# add in a data feature to include birt data plugins
tar -xjf %{SOURCE2}

# make sure upstream hasn't snuck in any jars we don't know about
find -name "*.jar" -exec rm {} \; 

# symlink orbit deps
mkdir orbitDeps
pushd orbitDeps
ln -s %{_javadir}/batik/batik-bridge.jar 
ln -s %{_javadir}/batik/batik-dom.jar 
ln -s %{_javadir}/batik/batik-svg-dom.jar
ln -s %{_javadir}/batik/batik-awt-util.jar 
ln -s %{_javadir}/batik/batik-extension.jar 
ln -s %{_javadir}/batik/batik-parser.jar 
ln -s %{_javadir}/batik/batik-svggen.jar 
ln -s %{_javadir}/batik/batik-swing.jar 
ln -s %{_javadir}/batik/batik-transcoder.jar
ln -s %{_javadir}/batik/batik-xml.jar 
ln -s %{_javadir}/xml-commons-jaxp-1.3-apis-ext.jar
ln -s %{_javadir}/fop.jar
ln -s %{_javadir}/js.jar
ln -s %{_javadir}/xerces-j2.jar
popd

%build
# build only chart feature and pared-down main feature until dependencies (full dtp and wtp) are ready
eclipse-pdebuild -a "-DforceContextQualifier=%{rlsdate} -DjavacSource=1.5 -DjavacTarget=1.5" -f org.eclipse.birt.chart \
                 -d "emf gef dtp-enablement dtp-connectivity dtp-modelbase dtp-sqldevtools" \
                 -o `pwd`/orbitDeps -v
# build the added birt feature to contain org.eclipse.birt.data and org.eclipse.birt.data.aggregation plugins
eclipse-pdebuild -a "-DforceContextQualifier=%{rlsdate} -DjavacSource=1.5 -DjavacTarget=1.5" -f org.eclipse.birt.data.fedora  \
                 -d "emf gef dtp-enablement dtp-connectivity dtp-modelbase dtp-sqldevtools" \
                 -o `pwd`/orbitDeps -v

%install
install -d -m 755 %{buildroot}%{eclipse_dropin}
unzip -q -d %{buildroot}%{eclipse_dropin}/birt build/rpmBuild/org.eclipse.birt.chart.zip
unzip -q -o -d %{buildroot}%{eclipse_dropin}/birt build/rpmBuild/org.eclipse.birt.data.fedora.zip

pushd %{buildroot}%{eclipse_dropin}/birt/eclipse/plugins
rm -fr org.apache.batik.bridge_*.jar
ln -s ../../../../../java/batik/batik-bridge.jar
rm -fr org.apache.batik.css_*.jar 
rm -fr org.apache.batik.dom_*.jar
ln -s ../../../../../java/batik/batik-dom.jar 
rm -fr org.apache.batik.dom.svg_*.jar
ln -s ../../../../../java/batik/batik-svg-dom.jar
rm -fr org.apache.batik.ext.awt_*.jar
ln -s ../../../../../java/batik/batik-awt-util.jar 
rm -fr org.apache.batik.parser_*.jar
ln -s ../../../../../java/batik/batik-parser.jar 
rm -fr org.apache.batik.pdf_*.jar
ln -s ../../../../../java/fop.jar
rm -fr org.apache.batik.svggen_*.jar
ln -s ../../../../../java/batik/batik-svggen.jar 
rm -fr org.apache.batik.transcoder_*.jar
ln -s ../../../../../java/batik/batik-transcoder.jar
rm -fr org.apache.batik.util_*.jar 
rm -fr org.apache.batik.util.gui_*.jar 
rm -fr org.apache.batik.xml_*.jar
ln -s ../../../../../java/batik/batik-xml.jar 
rm -fr org.w3c*.jar
ln -s ../../../../../java/xml-commons-jaxp-1.3-apis-ext.jar
rm -fr org.apache.commons.codec_*.jar
rm -fr org.mozilla.javascript_*.jar
ln -s ../../../../../java/js.jar
popd


%files chart
%{eclipse_dropin}/birt
%doc org.eclipse.birt.chart.feature/license.html
%doc org.eclipse.birt.chart.feature/epl-v10.html
%doc org.eclipse.birt.data.fedora.feature/license.html
%doc org.eclipse.birt.data.fedora.feature/epl-v10.html

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.2-alt1_1jpp7
- new version

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1_1jpp7
- fc update

* Fri Sep 28 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1_2jpp7
- new fc release

* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 3.7.0-alt1_4jpp6
- update to new release by jppimport

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_1jpp6
- new version

