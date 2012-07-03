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
#


Name:           axis
Version:        1.4
Release:        alt3_6jpp6
Epoch:          0
Summary:        SOAP implementation in Java
License:        ASL 2.0
Group:          Development/Java
URL:            http://ws.apache.org/axis/
# svn export http://svn.apache.org/repos/asf/webservices/axis/branches/AXIS_1_4_FINAL/
Source0:        axis-1.4-src.tar.gz
Source1:        http://repo2.maven.org/maven2/axis/axis/1.4/axis-1.4.pom
Source2:        http://mirrors.ibiblio.org/pub/mirrors/maven2/org/apache/axis/axis-ant/1.4/axis-ant-1.4.pom
Source3:        http://mirrors.ibiblio.org/pub/mirrors/maven2/org/apache/axis/axis-jaxrpc/1.4/axis-jaxrpc-1.4.pom
Source4:        http://mirrors.ibiblio.org/pub/mirrors/maven2/org/apache/axis/axis-saaj/1.4/axis-saaj-1.4.pom
Source5:        axis-schema-1.4.pom
Patch0:         axis-java16.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils >= 0:1.6
Requires:       jaf
Requires:       jakarta-commons-discovery
Requires:       jakarta-commons-logging
Requires:       jakarta-commons-httpclient >= 1:3.0
Requires:       javamail
Requires:       jaxp_parser_impl
Requires:       log4j
Requires:       wsdl4j
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-nodeps
BuildRequires:  ant-junit
BuildRequires:  httpunit
BuildRequires:  junit
BuildRequires:  xmlunit
# Main requires
BuildRequires:  stax_1_0_api
BuildRequires:  bsf
BuildRequires:  castor >= 0:1.1
BuildRequires:  glassfish-javamail
BuildRequires:  jaf_1_1_api
BuildRequires:  geronimo-j2ee-1.4-apis
BuildRequires:  geronimo-servlet-2.4-api
BuildRequires:  jakarta-commons-discovery
BuildRequires:  jakarta-commons-httpclient >= 1:3.0
BuildRequires:  jakarta-commons-logging
BuildRequires:  jakarta-commons-net
BuildRequires:  oro
BuildRequires:  regexp
BuildRequires:  log4j
BuildRequires:  wsdl4j
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-jaxp-1.2-apis
BuildRequires:  xmlbeans
BuildRequires:  xml-security
# optional requires
#BuildRequires: jimi
BuildRequires:  jetty5
BuildArch:      noarch
Source44: import.info

%description
Apache AXIS is an implementation of the SOAP ("Simple Object Access Protocol")
submission to W3C.

From the draft W3C specification:

SOAP is a lightweight protocol for exchange of information in a decentralized,
distributed environment. It is an XML based protocol that consists of three
parts: an envelope that defines a framework for describing what is in a message
and how to process it, a set of encoding rules for expressing instances of
application-defined datatypes, and a convention for representing remote
procedure calls and responses.

This project is a follow-on to the Apache SOAP project.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description manual
Documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}-src
%{_bindir}/find -type f -name "*.[jrw]ar" | %{_bindir}/xargs -t %{__rm}
%patch0 -p0 -b .sav0

pushd lib
ln -s $(build-classpath stax_1_0_api) .
ln -s $(build-classpath bsf) .
ln -s $(build-classpath castor) .
ln -s $(build-classpath commons-discovery) .
ln -s $(build-classpath commons-httpclient) .
ln -s $(build-classpath commons-logging) .
ln -s $(build-classpath commons-net) .
ln -s $(build-classpath httpunit) .
ln -s $(build-classpath jetty5/jetty5) .
ln -s $(build-classpath log4j) .
ln -s $(build-classpath oro) .
ln -s $(build-classpath xml-security) .
ln -s $(build-classpath xmlbeans/xbean) .
ln -s $(build-classpath wsdl4j) .
pushd endorsed
ln -s $(build-classpath xerces-j2) .
ln -s $(build-classpath xml-commons-jaxp-1.2-apis) .
popd
ln -s $(build-classpath glassfish-javamail-monolithic) .
popd

ln -s %{_javadocdir}/%{name} docs/apiDocs

%build
export CLASSPATH=
export OPT_JAR_LIST=`cat %{_sysconfdir}/ant.d/{junit,nodeps}`
%{ant} \
    -Dant.build.javac.source=1.4 \
    -Dtest.functional.fail=no \
    -Dcommons-discovery.jar=$(build-classpath commons-discovery) \
    -Dcommons-httpclient.jar=$(build-classpath commons-httpclient) \
    -Dcommons-logging.jar=$(build-classpath commons-logging) \
    -Dlog4j-core.jar=$(build-classpath log4j) \
    -Dwsdl4j.jar=$(build-classpath wsdl4j) \
    -DxercesImpl.jar=$(build-classpath xerces-j2) \
    -DxmlParserAPIs.jar=$(build-classpath xml-commons-jaxp-1.2-apis) \
    -Dxalan.jar=$(build-classpath xalan-j2) \
    -Dxml-apis.jar=$(build-classpath xml-commons-jaxp-1.2-apis) \
    -Dxerces.jar=$(build-classpath xerces-j2) \
    -Dregexp.jar=$(build-classpath regexp) \
    -Dxmlunit.jar=$(build-classpath xmlunit) \
    -Djsse.jar=$(build-classpath jsse/jsse) \
    -Dtools.jar=%{_jvmdir}/java/lib/tools.jar \
    -Dj2ee.jar=$(build-classpath geronimo-j2ee-1.4-apis) \
    -Dactivation.jar=$(build-classpath jaf_1_1_api) \
    -Dmailapi.jar=$(build-classpath javamail/mailapi) \
    -Djunit.jar=$(build-classpath junit) \
    -Dservlet.jar=$(build-classpath geronimo-servlet-2.4-api) \
    -Dbsf.jar=$(build-classpath bsf) \
    -Dcastor.jar=$(build-classpath castor) \
    -Dcommons-net.jar=$(build-classpath commons-net) \
    -Djetty.jar=$(build-classpath jetty5) \
    -Dsecurity.jar=$(build-classpath xml-security) \
    -Dxmlbeans.jar=$(build-classpath xmlbeans) \
    -Dhttpunit.jar=$(build-classpath httpunit) \
    clean compile javadocs junit war

#    -Djimi.jar=$(build-classpath jimi) \

%install

### Jar files

install -d -m 755 %{buildroot}%{_javadir}/%{name}

pushd build/lib
   install -p -m 644 axis.jar axis-ant.jar axis-schema.jar saaj.jar jaxrpc.jar \
           %{buildroot}%{_javadir}/%{name}/
popd

pushd %{buildroot}%{_javadir}/%{name}
   for jar in *.jar ; do
      vjar=$(echo $jar | sed s+.jar+-%{version}.jar+g)
      mv $jar $vjar
      ln -s $vjar $jar
   done
popd

# pom
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-axis.pom
cp -p %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-axis-ant.pom
cp -p %{SOURCE5} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-axis-schema.pom
cp -p %{SOURCE3} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jaxrpc.pom
cp -p %{SOURCE4} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-saaj.pom
%add_to_maven_depmap org.apache.axis axis %{version} JPP/%{name} axis
%add_to_maven_depmap axis axis %{version} JPP/%{name} axis
%add_to_maven_depmap org.apache.axis axis-ant %{version} JPP/%{name} axis-ant
%add_to_maven_depmap axis axis-ant %{version} JPP/%{name} axis-ant
%add_to_maven_depmap org.apache.axis axis-saaj %{version} JPP/%{name} axis-schema
%add_to_maven_depmap axis axis-saaj %{version} JPP/%{name} axis-schema
%add_to_maven_depmap org.apache.axis axis-jaxrpc %{version} JPP/%{name} jaxrpc
%add_to_maven_depmap axis axis-jaxrpc %{version} JPP/%{name} jaxrpc
%add_to_maven_depmap org.apache.axis axis-saaj %{version} JPP/%{name} saaj
%add_to_maven_depmap axis axis-saaj %{version} JPP/%{name} saaj

### Javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/webapps
install -p -m 644 build/axis.war %{buildroot}%{_datadir}/%{name}-%{version}/webapps

%files
%doc LICENSE README release-notes.html changelog.html
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/axis-%{version}.jar
%{_javadir}/%{name}/axis-ant-%{version}.jar
%{_javadir}/%{name}/axis-ant.jar
%{_javadir}/%{name}/axis-schema-%{version}.jar
%{_javadir}/%{name}/axis-schema.jar
%{_javadir}/%{name}/axis.jar
%{_javadir}/%{name}/jaxrpc-%{version}.jar
%{_javadir}/%{name}/jaxrpc.jar
%{_javadir}/%{name}/saaj-%{version}.jar
%{_javadir}/%{name}/saaj.jar
%{_datadir}/%{name}-%{version}
%{_datadir}/maven2/poms/JPP.%{name}-axis.pom
%{_datadir}/maven2/poms/JPP.%{name}-axis-ant.pom
%{_datadir}/maven2/poms/JPP.%{name}-axis-schema.pom
%{_datadir}/maven2/poms/JPP.%{name}-jaxrpc.pom
%{_datadir}/maven2/poms/JPP.%{name}-saaj.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc --no-dereference docs/*

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_6jpp6
- new jpp relase

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_5jpp6
- new jpp release

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_4jpp5
- selected java5 compiler explicitly

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_4jpp5
- new jpp release

* Mon Feb 23 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_2jpp5
- fixed build

* Tue Oct 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_2jpp1.7
- removed jaf conflict

* Wed Aug 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_2jpp1.7
- updated to new jpackage version

* Mon Jul 04 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2.1-alt1
- 1.2.1
- changed dependency: jakarta-oro -> jakarta-regexp
- changed rpmgroup of packages with documentation

* Sun Mar 27 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2-alt0.2
- rpm-build-java macroces
- version from cvs 20050327

* Tue Sep 21 2004 Vladimir Lettiev <crux@altlinux.ru> 1.2-alt0.1.beta3
- 1.2beta3
- Rebuild for ALT Linux Sisyphus
- spec cleanup

* Fri Aug 20 2004 Ralph Apel <r.apel at r-apel.de>  0:1.1-3jpp
- Build with ant-1.6.2

* Thu Jun 26 2003 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net>  0:1.1-2jpp
- fix javadoc versionning

* Thu Jun 26 2003 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net>  0:1.1-1jpp
- Initial packaging
- no xml security for now since xml-security is not packaged yet
- functional tests not executed yet - seems they need some setup and do not
  run out of the box
- no webapp right now - file layout is too messy if hidden into a war file
  since jpp installs webapps expanded, this matters
