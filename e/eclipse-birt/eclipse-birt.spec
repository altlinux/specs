%define rlsdate %(date '+%%Y%%m%%d0000')
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
# required for install
BuildRequires: unzip
%global eclipse_base     %{_libdir}/eclipse
%global eclipse_dropin   %{_datadir}/eclipse/dropins

Name:      eclipse-birt
Version:   3.7.0
Release:   alt1_4jpp6
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

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    eclipse-pde >= 1:3.4.1
BuildRequires:    eclipse-dtp
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
BuildRequires:    jakarta-commons-codec >= 1.3-9.4
BuildRequires:    sac >= 1.3-3.3

Requires:         jpackage-utils
Requires:         eclipse-platform >= 1:3.7.0
Requires:         eclipse-dtp >= 1.9.0
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
Requires:         jakarta-commons-codec >= 1.3-9.4
Requires:         sac >= 1.3-3.3
Source44: import.info

%description
BIRT is an Eclipse-based open source reporting system for web applications,
especially those based on Java and J2EE. BIRT has two main components: 
a report designer based on Eclipse, and a runtime component that you 
can add to your app server. BIRT also offers a charting engine that lets 
you add charts to your own application. 

%prep
%setup -q
%patch0

# add in a data feature to include birt data plugins
pushd features
tar -xjf %{SOURCE2}
popd

# make sure upstream hasn't snuck in any jars we don't know about
find -name "*.jar" -exec rm {} \; 

# symlink orbit deps
mkdir orbitDeps
pushd orbitDeps
ln -s %{_javadir}/commons-codec.jar org.apache.commons.codec_1.3.0.jar
ln -s %{_javadir}/batik/batik-bridge.jar 
ln -s %{_javadir}/batik/batik-css.jar 
ln -s %{_javadir}/batik/batik-dom.jar 
ln -s %{_javadir}/batik/batik-svg-dom.jar
ln -s %{_javadir}/batik/batik-awt-util.jar 
ln -s %{_javadir}/batik/batik-extension.jar 
ln -s %{_javadir}/batik/batik-parser.jar 
ln -s %{_javadir}/batik/batik-svggen.jar 
ln -s %{_javadir}/batik/batik-swing.jar 
ln -s %{_javadir}/batik/batik-transcoder.jar
ln -s %{_javadir}/batik/batik-gui-util.jar 
ln -s %{_javadir}/batik/batik-util.jar 
ln -s %{_javadir}/batik/batik-xml.jar 
ln -s %{_javadir}/xml-commons-jaxp-1.3-apis-ext.jar
ln -s %{_javadir}/fop.jar
ln -s %{_javadir}/sac.jar
ln -s %{_javadir}/js.jar
popd

%build
# build only chart feature and pared-down main feature until dependencies (full dtp and wtp) are ready
%{eclipse_base}/buildscripts/pdebuild -a "-DforceContextQualifier=%{rlsdate} -DjavacSource=1.5 -DjavacTarget=1.5" -f org.eclipse.birt.chart \
                       -d "emf gef dtp-enablement dtp-connectivity dtp-modelbase dtp-sqldevtools" \
                       -o `pwd`/orbitDeps -v
# build the added birt feature to contain org.eclipse.birt.data and org.eclipse.birt.data.aggregation plugins
%{eclipse_base}/buildscripts/pdebuild -a "-DforceContextQualifier=%{rlsdate} -DjavacSource=1.5 -DjavacTarget=1.5" -f org.eclipse.birt.data.fedora  \
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
ln -s ../../../../../java/batik/batik-css.jar 
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
ln -s ../../../../../java/sac.jar
rm -fr org.apache.batik.svggen_*.jar
ln -s ../../../../../java/batik/batik-svggen.jar 
rm -fr org.apache.batik.transcoder_*.jar
ln -s ../../../../../java/batik/batik-transcoder.jar
rm -fr org.apache.batik.util_*.jar
ln -s ../../../../../java/batik/batik-util.jar 
rm -fr org.apache.batik.util.gui_*.jar
ln -s ../../../../../java/batik/batik-gui-util.jar 
rm -fr org.apache.batik.xml_*.jar
ln -s ../../../../../java/batik/batik-xml.jar 
rm -fr org.w3c*.jar
ln -s ../../../../../java/xml-commons-jaxp-1.3-apis-ext.jar
rm -fr org.apache.commons.codec_*.jar
ln -s ../../../../../java/commons-codec.jar org.apache.commons.codec_1.3.0.jar
popd

%files
%{eclipse_dropin}/birt
%doc features/org.eclipse.birt.chart.feature/license.html
%doc features/org.eclipse.birt.chart.feature/epl-v10.html
%doc features/org.eclipse.birt.data.fedora.feature/license.html
%doc features/org.eclipse.birt.data.fedora.feature/epl-v10.html

%changelog
* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 3.7.0-alt1_4jpp6
- update to new release by jppimport

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_1jpp6
- new version

