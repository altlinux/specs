# fake! killme!! see deps.notes
Provides: osgi(org.apache.xmlrpc)
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
Name:           oscar
Version:        1.0.5
Release:        alt2_2jpp6
Epoch:          0
License:        BSD Style
URL:            http://oscar.objectweb.org
Group:          Development/Java
Source0:        oscar-1.0.5.jar
Source1:        oscar-bundles.tar.gz
Source2:	oscar-insajmx-agent-build.xml
Source3:	oscar-insajmx-registry-build.xml
Source4:	oscar-insajmx-rmiconnector-build.xml
Source5:	oscar-insajmx-httpconnector.tar.gz

Patch0:         oscar-1.0.5-simple-build_xml.patch
Patch1:         oscar-osgi-util-build_xml.patch
Patch2:         oscar-wireadmincmd-build_xml.patch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7
BuildRequires: servlet
BuildRequires: mx4j

Requires: xml-commons-apis
BuildArch:      noarch
Source44: import.info

%description
Oscar is an open source implementation of the Open Services Gateway 
Initiative (OSGi) framework specification; the goal is to provide a 
completely compliant implementation of the OSGi framework specification. 
Oscar is currently compliant with a large portion of the OSGi 3 
specifications, although certain compliance work still needs to be 
completed. Despite this fact, the OSGi framework functionality provided 
by Oscar is very stable and is in use by many people.
Even though OSGi targets the embedded device market, the framework is 
ideally suited for experimenting with component-oriented and 
service-oriented computing in general. For example, Oscar can be 
easily embedded into other projects and used as a plugin or extension 
mechanism; it serves this purpose much better than other systems that 
are used for similar purposes, such as Java Management Extensions (JMX). 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.



%prep
%setup -c -q -n %{name}_%{version}
jar xf org/ungoverned/oscar/installer/resource/src.jar
# remove all binary libs
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
mkdir oscar-bundles
(cd oscar-bundles
gzip -dc %{SOURCE1} | tar xf -
rm oscar-shellplugin-src.jar
rm oscar-tv-1.0.3-src.jar
rm oscar-upnpbasedriver-2.0.0-src.jar
)
(cd src-bundle
for j in ../oscar-bundles/*.jar; do
	jar xf $j
done
gzip -dc %{SOURCE5} | tar xf -
rm -rf osgiprov
)
cp %{SOURCE2} src-bundle/insajmx/agent/build.xml
cp %{SOURCE3} src-bundle/insajmx/registry/build.xml
cp %{SOURCE4} src-bundle/insajmx/rmiconnector/build.xml

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav

%build
export LANG=en_US.ISO8859-1
rm -rf src-bundle/binarylight
rm -rf src-bundle/clock
rm -rf src-bundle/insajmx

export CLASSPATH=$(build-classpath mx4j/mx4j servlet)
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first all apidoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle

install -m 644 lib/moduleloader.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/moduleloader-%{version}.jar
install -m 644 lib/oscar.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/oscar-%{version}.jar
install -m 644 lib/osgi.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/osgi-%{version}.jar
install -m 644 bundle/bundlerepository.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/bundlerepository-%{version}.jar
install -m 644 bundle/contenthandler.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/contenthandler-%{version}.jar
install -m 644 bundle/controlpoint-1.1.2-bin.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/controlpoint-%{version}.jar
install -m 644 bundle/datastreamhandler.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/datastreamhandler-%{version}.jar
install -m 644 bundle/handlertest.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/handlertest-%{version}.jar
install -m 644 bundle/httpadmin.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/httpadmin-%{version}.jar
install -m 644 bundle/httpshell.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/httpshell-%{version}.jar
install -m 644 bundle/httptest.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/httptest-%{version}.jar
install -m 644 bundle/introspector.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/introspector-%{version}.jar
install -m 644 bundle/log.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/log-%{version}.jar
install -m 644 bundle/mbeanfactory.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/mbeanfactory-%{version}.jar
install -m 644 bundle/notification.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/notification-%{version}.jar
install -m 644 bundle/osgimbean_2.0.5.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/osgimbean_2.0.5-%{version}.jar
install -m 644 bundle/osgi-service.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/osgi-service-%{version}.jar
install -m 644 bundle/osgi-util.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/osgi-util-%{version}.jar
install -m 644 bundle/PermissionAdminCommands.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/PermissionAdminCommands-%{version}.jar
install -m 644 bundle/PermissionAdmin.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/PermissionAdmin-%{version}.jar
install -m 644 bundle/permissionmanager.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/permissionmanager-%{version}.jar
install -m 644 bundle/Preferences.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/Preferences-%{version}.jar
install -m 644 bundle/remotelogger_0.1.2.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/remotelogger-%{version}.jar
install -m 644 bundle/servicebinder.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/servicebinder-%{version}.jar
install -m 644 bundle/servicelookup.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/servicelookup-%{version}.jar
install -m 644 bundle/servicenotifier.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/servicenotifier-%{version}.jar
install -m 644 bundle/serviceregister.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/serviceregister-%{version}.jar
install -m 644 bundle/servlet.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/servlet-%{version}.jar
install -m 644 bundle/shellextension.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/shellextension-%{version}.jar
install -m 644 bundle/shellextra.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/shellextra-%{version}.jar
install -m 644 bundle/shellgui.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/shellgui-%{version}.jar
install -m 644 bundle/shell.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/shell-%{version}.jar
install -m 644 bundle/shellmbean.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/shellmbean-%{version}.jar
install -m 644 bundle/shelltui.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/shelltui-%{version}.jar
install -m 644 bundle/simple.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/simple-%{version}.jar
install -m 644 bundle/tablelayout.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/tablelayout-%{version}.jar
install -m 644 bundle/telnetd.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/telnetd-%{version}.jar
install -m 644 bundle/urlhandlers.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/urlhandlers-%{version}.jar
install -m 644 bundle/wireadmincmd.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/wireadmincmd-%{version}.jar
install -m 644 bundle/xmlrpc.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle/xmlrpc-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

(cd $RPM_BUILD_ROOT%{_javadir}/%{name}/bundle && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/%{name}
%doc src-bundle/*.txt

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.5-alt2_2jpp6
- fixed build with java 7

* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.5-alt1_2jpp6
- new version

