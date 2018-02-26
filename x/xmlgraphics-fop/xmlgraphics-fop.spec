AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2011, JPackage Project
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


%global bname fop

Name:           xmlgraphics-fop
Version:        1.0
Release:        alt1_4jpp6
Epoch:          0
Summary:        XSL-driven print formatter
License:        ASL 2.0
Group:          Development/Java
URL:            http://xmlgraphics.apache.org/fop/
# svn export http://svn.apache.org/repos/asf/xmlgraphics/fop/tags/fop-1_0/ fop-1.0 && tar cvzf fop-1.0-src.tar.gz fop-1.0
Source0:        http://www.apache.org/dist/xmlgraphics/fop/fop-1.0-src.tar.gz
Source1:        %{name}.script
Patch0:         xmlgraphics-fop-build.patch
Patch1:         xmlgraphics-fop-cli.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
Requires:       xmlgraphics-batik >= 0:1.7-13
Requires:       excalibur-avalon-logkit
Requires:       excalibur-avalon-framework-api
Requires:       excalibur-avalon-framework-impl
Requires:       qdox
Requires:       xalan-j2
Requires:       xmlgraphics-commons
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  java-javadoc
BuildRequires:  ant >= 0:1.8.0
BuildRequires:  ant-junit
BuildRequires:  junit
BuildRequires:  fonts-ttf-liberation
BuildRequires:  xmlgraphics-batik >= 0:1.7-13
BuildRequires:  xmlgraphics-batik-javadoc >= 0:1.7-13
BuildRequires:  excalibur-avalon-logkit
BuildRequires:  excalibur-avalon-framework-api
BuildRequires:  excalibur-avalon-framework-impl
BuildRequires:  qdox >= 0:1.11
BuildRequires:  servlet_api
BuildRequires:  xalan-j2
BuildRequires:  xmlgraphics-commons >= 0:1.4-4
BuildRequires:  xmlunit
BuildArch:       noarch
Source44: import.info
Source45: fop.jar-OSGi-MANIFEST.MF
Requires: commons-io commons-logging xmlgraphics-commons

Provides: fop = %{epoch}:%version-%release
Obsoletes: fop <= 0.21
Conflicts: fop <= 0:0.21

%description
FOP is the world's first print formatter driven by XSL formatting
objects. It is a Java application that reads a formatting object tree
and then turns it into a PDF document. The formatting object tree, can
be in the form of an XML document (output by an XSLT engine like XT or
Xalan) or can be passed in memory as a DOM Document or (in the case of
XT) SAX events.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{bname}-%{version}
%{_bindir}/find -type f -name '*.jar' | %{_bindir}/xargs -t %{__rm}

%patch0 -p0 -b .sav0
%patch1 -p1 -b .sav1

pushd lib
ln -s `%{_bindir}/build-classpath excalibur/avalon-framework-api`
ln -s `%{_bindir}/build-classpath excalibur/avalon-framework-impl`
ln -s `%{_bindir}/build-classpath commons-io`
ln -s `%{_bindir}/build-classpath commons-logging`
ln -s `%{_bindir}/build-classpath qdox`
ln -s `%{_bindir}/build-classpath servlet_api`
ln -s `%{_bindir}/build-classpath xml-commons-jaxp-1.3-apis-ext`
ln -s `%{_bindir}/build-classpath xmlgraphics-batik/batik-anim`
ln -s `%{_bindir}/build-classpath xmlgraphics-batik/batik-awt-util`
ln -s `%{_bindir}/build-classpath xmlgraphics-batik/batik-bridge`
ln -s `%{_bindir}/build-classpath xmlgraphics-batik/batik-css`
ln -s `%{_bindir}/build-classpath xmlgraphics-batik/batik-dom`
ln -s `%{_bindir}/build-classpath xmlgraphics-batik/batik-ext`
ln -s `%{_bindir}/build-classpath xmlgraphics-batik/batik-extension`
ln -s `%{_bindir}/build-classpath xmlgraphics-batik/batik-gvt`
ln -s `%{_bindir}/build-classpath xmlgraphics-batik/batik-parser`
ln -s `%{_bindir}/build-classpath xmlgraphics-batik/batik-svg-dom`
ln -s `%{_bindir}/build-classpath xmlgraphics-batik/batik-svggen`
ln -s `%{_bindir}/build-classpath xmlgraphics-batik/batik-script`
ln -s `%{_bindir}/build-classpath xmlgraphics-batik/batik-transcoder`
ln -s `%{_bindir}/build-classpath xmlgraphics-batik/batik-util`
ln -s `%{_bindir}/build-classpath xmlgraphics-batik/batik-xml`
ln -s `%{_bindir}/build-classpath xalan-j2`
ln -s `%{_bindir}/build-classpath xalan-j2-serializer`
ln -s `%{_bindir}/build-classpath xmlgraphics-commons`
ln -s `%{_bindir}/build-classpath xmlunit`
popd

%build
export ANT_OPTS="-Djava.awt.headless=true -Xms1g"
export CLASSPATH=
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbatik.javadoc=%{_javadocdir}/batik package junit maven-artifacts

%install

# jars
mkdir -p %{buildroot}%{_javadir}/%{name}
install -p -m 644 build/%{bname}.jar %{buildroot}%{_javadir}/%{name}/%{bname}-%{version}.jar
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}*; do ln -s ${jar} `echo $jar | sed "s|-%{version}||g"`; done)

# pom
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 build/maven/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-%{bname}.pom
%add_to_maven_depmap org.apache.xmlgraphics %{bname} %{version} JPP/%{name} %{bname}

# script
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# data
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr hyph %{buildroot}%{_datadir}/%{name}
cp -pr conf %{buildroot}%{_datadir}/%{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# inject OSGi manifest fop.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE45} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-fop/fop.jar META-INF/MANIFEST.MF

mkdir -p $RPM_BUILD_ROOT`dirname /etc/fop.conf`
touch $RPM_BUILD_ROOT/etc/fop.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/xmlgraphics-fop.conf`
touch $RPM_BUILD_ROOT/etc/xmlgraphics-fop.conf

# avalon-framework is not in requires
subst 's,excalibur/avalon-framework,excalibur/avalon-framework-api excalibur/avalon-framework-impl,' %buildroot%_bindir/%name
# add xmlgraphics-commons to classpath
grep xmlgraphics-commons %buildroot%_bindir/xmlgraphics-fop || sed -i 's,xmlgraphics-batik,xmlgraphics-batik-all xmlgraphics-commons commons-io commons-logging,' %buildroot%_bindir/xmlgraphics-fop

# fop compat symlinks
pushd $RPM_BUILD_ROOT/%_javadir
ln -s xmlgraphics-fop/fop.jar fop.jar
ln -s xmlgraphics-fop/fop.jar xmlgraphics-fop.jar
popd
pushd $RPM_BUILD_ROOT/%_bindir
ln -s xmlgraphics-fop fop
popd
pushd $RPM_BUILD_ROOT/%_datadir
ln -s xmlgraphics-fop fop
popd
# end inject OSGi manifest fop.jar-OSGi-MANIFEST.MF

%files
%doc NOTICE LICENSE README known-issues.xml status.xml
%attr(0755,root,root) %{_bindir}/%{name}
%dir %{_javadir}*/%{name}
%exclude %dir %{_javadocdir}/%{name}
%{_javadir}*/%{name}/%{bname}-%{version}.jar
%{_javadir}*/%{name}/%{bname}.jar
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/conf
%{_datadir}/%{name}/conf/fop.xconf
%dir %{_datadir}/%{name}/hyph
%{_datadir}/%{name}/hyph/hyphenation.dtd
%{_datadir}/%{name}/hyph/readme
%{_datadir}/maven2/poms/JPP.%{name}-%{bname}.pom
%{_mavendepmapfragdir}/%{name}
%config(noreplace,missingok) /etc/fop.conf
%config(noreplace,missingok) /etc/xmlgraphics-fop.conf
# compat symlinks
%_javadir/fop.jar
%_javadir/xmlgraphics-fop.jar
%_bindir/fop
%_datadir/fop

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sun Jan 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_4jpp6
- new jpp relase

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt5_6jpp6
- added commons-logging to the classpath

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt4_6jpp6
- add xmlgraphics-commons to classpath

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt3_6jpp6
- added OSGi provides

* Thu May 28 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt3_6jpp5
- new jpp release

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt3_5jpp5
- obsoletes fop 0.20.5

* Tue Oct 28 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt2_5jpp5
- fixed #17536

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt1_5jpp5
- added config

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt1_4jpp5
- converted from JPackage by jppimport script

