BuildRequires: docbook-dtds
%define _without_tests 1
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with bootstrap
%bcond_with bootstrap
#def_with gcj_support
%bcond_with gcj_support
#def_with tests
%bcond_with tests

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define jmx_version 1.2.1


Name:           mx4j
Version:        3.0.2
Release:        alt1_1jpp6
Epoch:          0
Summary:        Open source implementation of JMX Java API
License:        ASL 1.1
Group:          Development/Java
URL:            http://mx4j.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/mx4j/MX4J%%20Source/3.0.2/mx4j-3.0.2-src.tar.gz
Source1:        %{name}-build.policy
Source2:        CatalogManager.properties
Source3:        http://mirrors.ibiblio.org/pub/mirrors/maven2/mx4j/mx4j/3.0.2/mx4j-3.0.2.pom
Source4:        http://mirrors.ibiblio.org/pub/mirrors/maven2/mx4j/mx4j-remote/3.0.2/mx4j-remote-3.0.2.pom
Patch0:         mx4j-javaxssl.patch
Patch2:         mx4j-build.patch
Patch3:         mx4j-docbook.patch
Patch5:         mx4j-caucho-build.patch
Patch7:         mx4j-split-tools.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jpackage-utils
Requires(pre): coreutils
Requires(post): alternatives >= 0:0.4
Requires(postun): alternatives >= 0:0.4
BuildRequires: jpackage-utils > 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: ant-trax
%if %without bootstrap
BuildRequires: ant-apache-resolver
BuildRequires: jaf
BuildRequires: javamail
BuildRequires: xjavadoc
BuildRequires: xdoclet
BuildRequires: wsdl4j
BuildRequires: jakarta-commons-discovery
%endif
BuildRequires: bcel >= 0:5.0
BuildRequires: log4j >= 0:1.2.7
BuildRequires: jakarta-commons-logging >= 0:1.0.1
BuildRequires: jetty5
BuildRequires: coreutils
BuildRequires: %{_bindir}/xmlcatalog
BuildRequires: docbook-style-xsl >= 0:1.61
BuildRequires: xml-commons-resolver11
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xerces-j2
%if %with tests
BuildRequires: ant-junit
BuildRequires: junit >= 0:3.7.1
BuildRequires: xmlunit
%endif
%if ! %{gcj_support}
Buildarch:      noarch
%endif
%if %without bootstrap
Requires: jaf
Requires: javamail
%endif
Requires: log4j >= 0:1.2.7
Requires: jakarta-commons-logging >= 0:1.0.1
Requires: bcel >= 0:5.0
Requires: xml-commons-resolver11
Requires: xml-commons-jaxp-1.3-apis
Obsoletes:      openjmx
Provides:       jmxri

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif
Source44: import.info

%description
OpenJMX is an open source implementation of the
Java(TM) Management Extensions (JMX).

%if %without bootstrap
%package tools-extra
Group:          Development/Java
Summary:        Additional protocols and scripting for %{name}
BuildRequires: jython >= 0:2.1
BuildRequires: axis >= 0:1.1
BuildRequires: burlap >= 0:3.0.8
BuildRequires: caucho-services
BuildRequires: hessian >= 0:3.0.8
Requires: jython >= 0:2.1
Requires: axis >= 0:1.1
Requires: burlap >= 0:3.0.8
Requires: caucho-services
Requires: hessian >= 0:3.0.8

%description tools-extra
%{summary}.
%endif

%if %without bootstrap
%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
Obsoletes:      openjmx-javadoc
BuildArch: noarch

%description javadoc
%{summary}.
%endif

%if %without bootstrap
%package manual
Group:          Development/Documentation
Summary:        Documentation for %{name}
BuildArch: noarch

%description    manual
%{summary}.
%endif

%prep
%setup -q

%patch0 -p1 -b .sav0
%patch2 -p0 -b .sav2
%patch3 -p1 -b .sav3
%if %{gcj_support}
%patch5 -p1 -b .sav5
%endif
%patch7 -p0 -b .sav7

cp -p %{SOURCE1} build
cp -p %{SOURCE2} %{_builddir}/%{name}-%{version}/build/
# use the one from docbook-dtds instead of getting it from the net
catalogfile=`%{_bindir}/xmlcatalog /usr/share/sgml/docbook/xmlcatalog "-//OASIS//DTD DocBook XML V4.1.2//EN"`
sed -i -e 's|http://www.oasis-open.org/docbook/xml/4.1.2/docbookx.dtd|'$catalogfile'|' src/docs/index.xml
catalogfile=`%{_bindir}/xmlcatalog /etc/xml/catalog "http://docbook.sourceforge.net/release/xsl/current/html/chunk.xsl" | sed -e 's|file://||'`
sed -i -e 's|http://docbook.sourceforge.net/release/xsl/current/html/chunk.xsl|'$catalogfile'|' src/docs/xsl/mx4j-chunk.xsl

pushd lib
%if %with tests
   ln -sf $(build-classpath junit) .
   ln -sf $(build-classpath xmlunit) .
%endif
   ln -sf $(build-classpath xml-commons-jaxp-1.3-apis) xml-apis.jar
   ln -sf $(build-classpath xerces-j2) xercesImpl.jar
   ln -sf $(build-classpath xalan-j2) xalan.jar
   ln -sf $(build-classpath commons-logging) .
   ln -sf $(build-classpath log4j) .
%if %without bootstrap
   ln -sf $(build-classpath burlap) .
   ln -sf $(build-classpath caucho-services) .
   ln -sf $(build-classpath hessian) .
   ln -sf $(build-classpath axis/axis) .
   ln -sf $(build-classpath axis/jaxrpc) .
   ln -sf $(build-classpath axis/saaj) .
   ln -sf $(build-classpath wsdl4j) .
   ln -sf $(build-classpath jython) .
   ln -sf $(build-classpath xdoclet/xdoclet) .
   ln -sf $(build-classpath xdoclet/xdoclet-jmx-module) .
   ln -sf $(build-classpath xdoclet/xdoclet-mx4j-module) .
   ln -sf $(build-classpath javamail/mailapi) .
   ln -sf $(build-classpath javamail/smtp) .
   ln -sf $(build-classpath jaf) .
#
   ln -sf $(build-classpath commons-discovery) .
   ln -sf $(build-classpath jetty5/jetty5) org.mortbay.jetty.jar
%endif
   ln -sf $(build-classpath bcel) .
   ln -sf $(build-classpath servletapi5) servlet.jar
   ln -sf $(build-classpath jsse) .
   ln -sf $(build-classpath jsse/jcert) jcert.jar
   ln -sf $(build-classpath jsse/jnet) jnet.jar
   ln -sf $(build-classpath jaas) .
   ln -sf $(build-classpath xml-commons-resolver11) .
popd

%build
export OPT_JAR_LIST="ant/ant-junit junit xmlunit ant/ant-trax jaxp_transform_impl xalan-j2-serializer ant/ant-apache-resolver xml-commons-resolver11"

cd build
%if %without bootstrap
%if %with tests
%{ant} -Dbuild.sysclasspath=first compile.jmx compile.rjmx compile.tools tests-report javadocs docs
%else
%{ant} -Dbuild.sysclasspath=first compile.jmx compile.rjmx compile.tools javadocs docs
%endif
%else
%{ant} -Dbuild.sysclasspath=first compile.jmx compile.rjmx
%endif

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 dist/lib/%{name}-impl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/mx4j-impl-%{version}.jar
install -m 644 dist/lib/%{name}-jmx.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/mx4j-jmx-%{version}.jar
install -m 644 dist/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/mx4j-%{version}.jar
%if %without bootstrap
install -m 644 dist/lib/%{name}-tools.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/mx4j-tools-%{version}.jar
install -m 644 dist/lib/%{name}-tools-extra.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/mx4j-tools-extra-%{version}.jar
%endif
install -m 644 dist/lib/%{name}-rjmx.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/mx4j-rjmx-%{version}.jar
install -m 644 dist/lib/%{name}-rimpl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/mx4j-rimpl-%{version}.jar
install -m 644 dist/lib/%{name}-remote.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/mx4j-remote-%{version}.jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}/boa
install -m 644 dist/lib/boa/%{name}-rjmx-boa.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/boa/%{name}-rjmx-boa-%{version}.jar
install -m 644 dist/lib/boa/%{name}-rimpl-boa.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/boa/%{name}-rimpl-boa-%{version}.jar
install -m 644 dist/lib/boa/%{name}-remote-boa.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/boa/%{name}-remote-boa-%{version}.jar

pushd $RPM_BUILD_ROOT%{_javadir}/%{name}
   for jar in *-%{version}.jar ; do
      ln -fs ${jar} $(echo $jar | sed "s|-%{version}.jar|.jar|g")
   done
popd

pushd $RPM_BUILD_ROOT%{_javadir}/%{name}/boa
   for jar in *-%{version}.jar ; do
      ln -fs ${jar} $(echo $jar | sed "s|-%{version}.jar|.jar|g")
   done
popd

# poms

mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p %{SOURCE3} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-mx4j.pom
cp -p %{SOURCE4} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-mx4j-remote.pom
%add_to_maven_depmap mx4j mx4j %{version} JPP/%{name} mx4j
%add_to_maven_depmap mx4j mx4j-remote %{version} JPP/%{name} mx4j-remote

%if %without bootstrap
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -r dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jmxri_mx4j<<EOF
%{_javadir}/jmxri.jar	%{_javadir}/%{name}/mx4j-jmx.jar	10
EOF

%pre
%{__rm} -f %{_javadir}/%{name}.jar

%files
%_altdir/jmxri_mx4j
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/mx4j-%{version}.jar
%{_javadir}/%{name}/mx4j.jar
%{_javadir}/%{name}/mx4j-impl-%{version}.jar
%{_javadir}/%{name}/mx4j-impl.jar
%{_javadir}/%{name}/mx4j-jmx-%{version}.jar
%{_javadir}/%{name}/mx4j-jmx.jar
%{_javadir}/%{name}/mx4j-remote-%{version}.jar
%{_javadir}/%{name}/mx4j-remote.jar
%{_javadir}/%{name}/mx4j-rimpl-%{version}.jar
%{_javadir}/%{name}/mx4j-rimpl.jar
%{_javadir}/%{name}/mx4j-rjmx-%{version}.jar
%{_javadir}/%{name}/mx4j-rjmx.jar
%if %without bootstrap
%{_javadir}/%{name}/mx4j-tools-%{version}.jar
%{_javadir}/%{name}/mx4j-tools.jar
%endif
%dir %{_javadir}/%{name}/boa
%{_javadir}/%{name}/boa/mx4j-remote-boa-%{version}.jar
%{_javadir}/%{name}/boa/mx4j-remote-boa.jar
%{_javadir}/%{name}/boa/mx4j-rimpl-boa-%{version}.jar
%{_javadir}/%{name}/boa/mx4j-rimpl-boa.jar
%{_javadir}/%{name}/boa/mx4j-rjmx-boa-%{version}.jar
%{_javadir}/%{name}/boa/mx4j-rjmx-boa.jar
%{_datadir}/maven2/poms/JPP.%{name}-mx4j.pom
%{_datadir}/maven2/poms/JPP.%{name}-mx4j-remote.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/mx4j-%{version}.jar.*
%{_libdir}/gcj/%{name}/mx4j-tools-%{version}.jar.*
%{_libdir}/gcj/%{name}/mx4j-remote-boa-%{version}.jar.*
%endif

%if %without bootstrap
%files tools-extra
%{_javadir}/%{name}/mx4j-tools-extra-%{version}.jar
%{_javadir}/%{name}/mx4j-tools-extra.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/mx4j-tools-extra-3.0.1.jar.*
%endif
%endif

%if %without bootstrap
%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%endif

%if %without bootstrap
%files manual
%doc dist/docs/*
%endif

%changelog
* Tue Jan 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.0.2-alt1_1jpp6
- new version

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt7_9jpp5
- fixed 0-priority alternative

* Sat Jan 24 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt6_9jpp5
- rebuild for repocop

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt6_8jpp5
- converted from JPackage by jppimport script

* Thu Aug 14 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt6_7jpp1.7
- fixed unpackaged dir

* Fri Mar 07 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt5_7jpp1.7
- added mx4j-3.0.1-alt-local-xsl-stylesheets.patch

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt4_7jpp1.7
- full-fledged build

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt3_7jpp1.7
- updated to new jpackage release

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt3
- provides jmxri; jpp compatible symlinks

* Wed Aug 10 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.0.1-alt2
- Added /proc to BuildRequires

* Sat Jul 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.0.1-alt1
- New upstream release

* Fri Feb 25 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.0.0-alt1
- New upstream release

* Thu Jan 20 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.1.1-alt1
- New upstream release

* Tue Nov 23 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.1.0-alt1
- New upstream release
- Package the all-in-one jars containing both API and implementation
- Provided jmx_impl alternative (thanks to Vladimir Lettiev for insight)

* Tue Jul 13 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.0.1-alt1
- New package for Sisyphus.
