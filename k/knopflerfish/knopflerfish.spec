Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2010, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#


Summary:        OSGI Framework
Name:           knopflerfish
Version:        2.4.0
Release:        alt2_1jpp6
Epoch:          0
License:        BSD Style
URL:            http://www.knopflerfish.org
Group:          Development/Java
Source0:        http://www.knopflerfish.org/releases/2.4.0/knopflerfish_osgi_2.4.0.jar
Source1:        knopflerfish-poms.tgz
Patch0:         knopflerfish-temp-BundleLocator.patch
Patch1:         knopflerfish-component-bundle-manifest.patch
Patch2:         knopflerfish-osgi-build.patch
Patch3:         knopflerfish-build.patch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7
BuildRequires: bindex
BuildRequires: crimson >= 0:1.1.3-20
BuildRequires: kxml2
BuildRequires: nanoxml
BuildRequires: objectweb-asm >= 0:3.2
BuildRequires: oldkxml
BuildRequires: oscar
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-commons-resolver12
BuildRequires: xml-commons-jaxp-1.3-apis
Requires: jpackage-utils >= 0:1.7.5

BuildArch:      noarch
Source44: import.info

%description
The Knopflerfish OSGi framework is a complete, 
open source, OSGi R4 framework.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -c -q -n %{name}_osgi_%{version}
tar xzf %{SOURCE1}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
mv knopflerfish.org/osgi/bundles/io/io/resources/javax.microedition.io.jar.no knopflerfish.org/osgi/bundles/io/io/resources/javax.microedition.io.jar
ln -sf $(build-classpath objectweb-asm/asm) knopflerfish.org/osgi/framework/libs/asm-3.2.jar
ln -sf $(build-classpath oscar/bundle/shell) knopflerfish.org/osgi/bundles/bundlerepository/libs/oscar-shell_api-1.0.0.jar
ln -sf $(build-classpath bindex) knopflerfish.org/ant/lib/bindex.jar
#
mkdir tmp
pushd tmp
jar xf $(build-classpath xerces-j2)
jar xf $(build-classpath xml-commons-resolver12)
jar xf $(build-classpath xml-commons-jaxp-1.3-apis)
jar cf ../xercesImpl.jar *
popd
ln -sf $(build-classpath kxml2) knopflerfish.org/osgi/bundles/component/resources/kxml2.jar
cp $(build-classpath oldkxml) knopflerfish.org/osgi/bundles/bundlerepository/resources/console_api.jar
ln -sf $(build-classpath oldkxml) knopflerfish.org/osgi/bundles/bundlerepository/resources/kxml-min.jar
ln -sf $(build-classpath nanoxml) knopflerfish.org/osgi/bundles/metatype/kf_metatype/resources/nanoxml-2.2.1.jar
ln -sf $(build-classpath xalan-j2) knopflerfish.org/osgi/bundles/xml/xalan/resources/xalan.jar
ln -sf $(build-classpath xml-commons-jaxp-1.3-apis) knopflerfish.org/osgi/bundles/xml/xalan/resources/xml-apis.jar
ln -sf $(build-classpath xml-commons-resolver12) knopflerfish.org/osgi/bundles/xml/xerces/resources/resolver.jar
#ln -sf $(build-classpath xerxes-j2) knopflerfish.org/osgi/bundles/xml/xerces/resources/xercesImpl.jar
cp xercesImpl.jar knopflerfish.org/osgi/bundles/xml/xerces/resources/xercesImpl.jar
ln -sf $(build-classpath xalan-j2-serializer) knopflerfish.org/osgi/bundles/xml/xerces/resources/serializer.jar
ln -sf $(build-classpath xml-commons-jaxp-1.3-apis) knopflerfish.org/osgi/bundles/xml/xerces/resources/xml-apis.jar
ln -sf $(build-classpath crimson) knopflerfish.org/osgi/bundles/xml/crimson/resources/crimson.jar

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3

### 
### hack!!! undo: this crimson implementation do not carry org.w3c.*
rm ./knopflerfish.org/osgi/bundles/xml/crimson/resources/crimson.jar
mv ./knopflerfish.org/osgi/bundles/xml/crimson/resources/crimson.jar.no \
./knopflerfish.org/osgi/bundles/xml/crimson/resources/crimson.jar
### end hack


%build
cd knopflerfish.org
mkdir out
cp release_notes.txt out
ant -Dbuild.sysclasspath=first all htdocs javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/framework.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/framework-2.4.0.jar
install -m 644 knopflerfish.org/osgi/jars/basicdriverlocator/basicdriverlocator-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/bundlerepository/bundlerepository_all-2.0.4.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/cm/cm-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/cm/cm_all-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/cm/cm_api-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/cm_cmd/cm_cmd-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/cm_desktop/cm_desktop-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/component/component_all-2.0.2.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/component/component_api-2.0.2.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/connectors/connectors-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/console/console-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/console/console_all-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/console/console_api-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/consoletcp/consoletcp-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/consoletelnet/consoletelnet-2.0.4.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/consoletty/consoletty-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/crimson/crimson-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/demo1client/demo1client-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/demo1/demo1-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/demo1/demo1_all-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/demo1/demo1_api-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/desktop/desktop-2.3.17.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/desktop/desktop_all-2.3.17.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/desktop/desktop_api-2.3.17.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/device/device-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/device/device_all-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/device/device_api-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/event/event_all-2.0.9.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/event/event_api-2.0.9.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/frameworkcommands/frameworkcommands-2.0.5.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/httpconsole/httpconsole-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/http/http-2.1.8.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/http/http_all-2.1.8.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/http/http_api-2.1.8.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/httproot/httproot-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/io/io_all-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/io/io_api-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/jsdk/jsdk_api-2.5.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/kf_metatype/kf_metatype-2.0.3.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/kf_metatype/kf_metatype_all-2.0.3.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/logcommands/logcommands-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/log/log-2.0.2.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/log/log_all-2.0.2.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/log/log_api-2.0.2.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/measurement/measurement-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/metatype/metatype-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/position/position-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/prefs/prefs_all-2.0.4.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/prefs/prefs_api-2.0.4.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/provisioning/provisioning_api-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/remotefw/remotefw_api-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/sslj2sp/sslj2sp-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/trayicon_fw/trayicon_fw-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/trayicon/trayicon_all-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/trayicon/trayicon_api-2.0.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/upnp/upnp_api-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/useradmin/useradmin-2.0.2.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/useradmin/useradmin_all-2.0.2.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/useradmin/useradmin_api-2.0.2.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/util/util-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/wireadmin/wireadmin_api-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/xalan/xalan-2.7.1.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/xerces/xerces-2.9.1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 knopflerfish.org/osgi/jars/xml/xml-2.0.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}

for v in 2.0.0 2.0.1 2.0.2 2.0.3 2.0.4 2.0.5 2.0.9 2.1.8 2.3.17 2.4.0 2.5 2.7.1.1 2.9.1; do
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-${v}.jar; do ln -sf ${jar} `echo $jar| sed "s|-${v}||g"`; done)
done

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%add_to_maven_depmap org.knopflerfish knopflerfish-basicdriverlocator 2.0.1 JPP/knopflerfish basicdriverlocator
install -m 644 knopflerfish-poms/knopflerfish-basicdriverlocator-2.0.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-basicdriverlocator.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-bundlerepository_all 2.0.4 JPP/knopflerfish bundlerepository_all
install -m 644 knopflerfish-poms/knopflerfish-bundlerepository_all-2.0.4.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-bundlerepository_all.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-cm 2.0.1 JPP/knopflerfish cm
install -m 644 knopflerfish-poms/knopflerfish-cm-2.0.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-cm.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-cm_all 2.0.1 JPP/knopflerfish cm_all
install -m 644 knopflerfish-poms/knopflerfish-cm_all-2.0.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-cm_all.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-cm_api 2.0.1 JPP/knopflerfish cm_api
install -m 644 knopflerfish-poms/knopflerfish-cm_api-2.0.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-cm_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-cm_cmd 2.0.0 JPP/knopflerfish cm_cmd
install -m 644 knopflerfish-poms/knopflerfish-cm_cmd-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-cm_cmd.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-cm_desktop 2.0.1 JPP/knopflerfish cm_desktop
install -m 644 knopflerfish-poms/knopflerfish-cm_desktop-2.0.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-cm_desktop.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-component_all 2.0.2 JPP/knopflerfish component_all
install -m 644 knopflerfish-poms/knopflerfish-component_all-2.0.2.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-component_all.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-component_api 2.0.2 JPP/knopflerfish component_api
install -m 644 knopflerfish-poms/knopflerfish-component_api-2.0.2.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-component_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-connectors 2.0.1 JPP/knopflerfish connectors
install -m 644 knopflerfish-poms/knopflerfish-connectors-2.0.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-connectors.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-console 2.0.1 JPP/knopflerfish console
install -m 644 knopflerfish-poms/knopflerfish-console-2.0.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-console.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-console_api 2.0.1 JPP/knopflerfish console_api
install -m 644 knopflerfish-poms/knopflerfish-console_api-2.0.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-console_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-consoletcp 2.0.0 JPP/knopflerfish consoletcp
install -m 644 knopflerfish-poms/knopflerfish-consoletcp-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-consoletcp.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-consoletelnet 2.0.4 JPP/knopflerfish consoletelnet
install -m 644 knopflerfish-poms/knopflerfish-consoletelnet-2.0.4.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-consoletelnet.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-consoletty 2.0.1 JPP/knopflerfish consoletty
install -m 644 knopflerfish-poms/knopflerfish-consoletty-2.0.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-consoletty.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-crimson 2.0.1 JPP/knopflerfish crimson
install -m 644 knopflerfish-poms/knopflerfish-crimson-2.0.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-crimson.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-demo1 2.0.0 JPP/knopflerfish demo1
install -m 644 knopflerfish-poms/knopflerfish-demo1-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-demo1.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-demo1_all 2.0.0 JPP/knopflerfish demo1_all
install -m 644 knopflerfish-poms/knopflerfish-demo1_all-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-demo1_all.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-demo1_api 2.0.0 JPP/knopflerfish demo1_api
install -m 644 knopflerfish-poms/knopflerfish-demo1_api-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-demo1_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-demo1client 2.0.0 JPP/knopflerfish demo1client
install -m 644 knopflerfish-poms/knopflerfish-demo1client-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-demo1client.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-desktop 2.3.17 JPP/knopflerfish desktop
install -m 644 knopflerfish-poms/knopflerfish-desktop-2.3.17.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-desktop.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-desktop_all 2.3.17 JPP/knopflerfish desktop_all
install -m 644 knopflerfish-poms/knopflerfish-desktop_all-2.3.17.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-desktop_all.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-desktop_api 2.3.17 JPP/knopflerfish desktop_api
install -m 644 knopflerfish-poms/knopflerfish-desktop_api-2.3.17.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-desktop_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-device 2.0.0 JPP/knopflerfish device
install -m 644 knopflerfish-poms/knopflerfish-device-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-device.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-device_all 2.0.0 JPP/knopflerfish device_all
install -m 644 knopflerfish-poms/knopflerfish-device_all-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-device_all.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-device_api 2.0.0 JPP/knopflerfish device_api
install -m 644 knopflerfish-poms/knopflerfish-device_api-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-device_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-event_all 2.0.9 JPP/knopflerfish event_all
install -m 644 knopflerfish-poms/knopflerfish-event_all-2.0.9.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-event_all.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-event_api 2.0.9 JPP/knopflerfish event_api
install -m 644 knopflerfish-poms/knopflerfish-event_api-2.0.9.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-event_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-framework 2.4.0 JPP/knopflerfish framework
install -m 644 knopflerfish-poms/knopflerfish-framework-2.4.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-framework.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-frameworkcommands 2.0.5 JPP/knopflerfish frameworkcommands
install -m 644 knopflerfish-poms/knopflerfish-frameworkcommands-2.0.5.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-frameworkcommands.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-http 2.1.8 JPP/knopflerfish http
install -m 644 knopflerfish-poms/knopflerfish-http-2.1.8.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-http.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-http_all 2.1.8 JPP/knopflerfish http_all
install -m 644 knopflerfish-poms/knopflerfish-http_all-2.1.8.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-http_all.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-http_api 2.1.8 JPP/knopflerfish http_api
install -m 644 knopflerfish-poms/knopflerfish-http_api-2.1.8.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-http_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-httpconsole 2.0.1 JPP/knopflerfish httpconsole
install -m 644 knopflerfish-poms/knopflerfish-httpconsole-2.0.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-httpconsole.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-httproot 2.0.1 JPP/knopflerfish httproot
install -m 644 knopflerfish-poms/knopflerfish-httproot-2.0.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-httproot.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-io_all 2.0.0 JPP/knopflerfish io_all
install -m 644 knopflerfish-poms/knopflerfish-io_all-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-io_all.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-io_api 2.0.0 JPP/knopflerfish io_api
install -m 644 knopflerfish-poms/knopflerfish-io_api-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-io_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-jsdk_api 2.5 JPP/knopflerfish jsdk_api
install -m 644 knopflerfish-poms/knopflerfish-jsdk_api-2.5.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-jsdk_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-kf_metatype 2.0.3 JPP/knopflerfish kf_metatype
install -m 644 knopflerfish-poms/knopflerfish-kf_metatype-2.0.3.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-kf_metatype.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-kf_metatype_all 2.0.3 JPP/knopflerfish kf_metatype_all
install -m 644 knopflerfish-poms/knopflerfish-kf_metatype_all-2.0.3.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-kf_metatype_all.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-log 2.0.2 JPP/knopflerfish log
install -m 644 knopflerfish-poms/knopflerfish-log-2.0.2.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-log.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-log_all 2.0.2 JPP/knopflerfish log_all
install -m 644 knopflerfish-poms/knopflerfish-log_all-2.0.2.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-log_all.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-log_api 2.0.2 JPP/knopflerfish log_api
install -m 644 knopflerfish-poms/knopflerfish-log_api-2.0.2.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-log_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-logcommands 2.0.0 JPP/knopflerfish logcommands
install -m 644 knopflerfish-poms/knopflerfish-logcommands-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-logcommands.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-measurement 2.0.0 JPP/knopflerfish measurement
install -m 644 knopflerfish-poms/knopflerfish-measurement-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-measurement.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-metatype 2.0.0 JPP/knopflerfish metatype
install -m 644 knopflerfish-poms/knopflerfish-metatype-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-metatype.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-position 2.0.0 JPP/knopflerfish position
install -m 644 knopflerfish-poms/knopflerfish-position-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-position.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-prefs_all 2.0.4 JPP/knopflerfish prefs_all
install -m 644 knopflerfish-poms/knopflerfish-prefs_all-2.0.4.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-prefs_all.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-prefs_api 2.0.4 JPP/knopflerfish prefs_api
install -m 644 knopflerfish-poms/knopflerfish-prefs_api-2.0.4.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-prefs_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-provisioning_api 2.0.0 JPP/knopflerfish provisioning_api
install -m 644 knopflerfish-poms/knopflerfish-provisioning_api-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-provisioning_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-remotefw_api 2.0.0 JPP/knopflerfish remotefw_api
install -m 644 knopflerfish-poms/knopflerfish-remotefw_api-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-remotefw_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-sslj2sp 2.0.0 JPP/knopflerfish sslj2sp
install -m 644 knopflerfish-poms/knopflerfish-sslj2sp-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-sslj2sp.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-trayicon_all 2.0.1 JPP/knopflerfish trayicon_all
install -m 644 knopflerfish-poms/knopflerfish-trayicon_all-2.0.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-trayicon_all.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-trayicon_api 2.0.1 JPP/knopflerfish trayicon_api
install -m 644 knopflerfish-poms/knopflerfish-trayicon_api-2.0.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-trayicon_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-trayicon_fw 2.0.1 JPP/knopflerfish trayicon_fw
install -m 644 knopflerfish-poms/knopflerfish-trayicon_fw-2.0.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-trayicon_fw.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-upnp_api 2.0.0 JPP/knopflerfish upnp_api
install -m 644 knopflerfish-poms/knopflerfish-upnp_api-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-upnp_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-useradmin 2.0.2 JPP/knopflerfish useradmin
install -m 644 knopflerfish-poms/knopflerfish-useradmin-2.0.2.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-useradmin.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-useradmin_all 2.0.2 JPP/knopflerfish useradmin_all
install -m 644 knopflerfish-poms/knopflerfish-useradmin_all-2.0.2.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-useradmin_all.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-useradmin_api 2.0.2 JPP/knopflerfish useradmin_api
install -m 644 knopflerfish-poms/knopflerfish-useradmin_api-2.0.2.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-useradmin_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-util 2.0.0 JPP/knopflerfish util
install -m 644 knopflerfish-poms/knopflerfish-util-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-util.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-wireadmin_api 2.0.0 JPP/knopflerfish wireadmin_api
install -m 644 knopflerfish-poms/knopflerfish-wireadmin_api-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-wireadmin_api.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-xalan 2.7.1.1 JPP/knopflerfish xalan
install -m 644 knopflerfish-poms/knopflerfish-xalan-2.7.1.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-xalan.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-xerces 2.9.1 JPP/knopflerfish xerces
install -m 644 knopflerfish-poms/knopflerfish-xerces-2.9.1.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-xerces.pom
%add_to_maven_depmap org.knopflerfish knopflerfish-xml 2.0.0 JPP/knopflerfish xml
install -m 644 knopflerfish-poms/knopflerfish-xml-2.0.0.pom $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.knopflerfish-xml.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr knopflerfish.org/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# docs
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp *.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr knopflerfish.org/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%{_docdir}/%{name}-%{version}/*.txt
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%changelog
* Tue Dec 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt2_1jpp6
- use custom crimson.jar; current crimson.jar does not carry org.w3c.*

* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_1jpp6
- new version

