Patch33:	ws-commons-axiom-1.2.8-alt-jdk7-support.patch
BuildRequires: sun-stax-1.0-api
BuildRequires: sun-jaxb-2.1-impl
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

#def_with gcj_support
%bcond_with gcj_support
%bcond_without maven

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           ws-commons-axiom
Version:        1.2.8
Release:        alt3_2jpp6
Epoch:          0
Summary:        AXIOM XML infoset model for Apache Axis2
License:        ASL 2.0
Url:            http://ws.apache.org/commons/axiom/
Group:          Development/Java
# svn -q export http://svn.apache.org/repos/asf/webservices/commons/tags/axiom/1.2.8/ ws-commons-axiom-1.2.8 && tar cjf ws-commons-axiom-1.2.8.tar.bz2 ws-commons-axiom-1.2.8
Source0:        ws-commons-axiom-%{version}.tar.bz2
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-build.xml
Source4:        %{name}-modules-axiom-api-build.xml
Source5:        %{name}-modules-axiom-dom-build.xml
Source6:        %{name}-modules-axiom-impl-build.xml
BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: ant >= 0:1.6
BuildRequires: junit >= 0:3.8.2
%if %with maven
BuildRequires: bcel
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven2 >= 2.0.4-10jpp
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-one
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven-release
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin
BuildRequires: maven2-default-skin
BuildRequires: mojo-maven2-plugin-jdepend
BuildRequires: mojo-maven2-plugin-xmlbeans
BuildRequires: ws-commons-axiom
%endif
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif
BuildRequires: crimson
BuildRequires: geronimo-specs-poms
BuildRequires: geronimo-stax-1.0-api
BuildRequires: geronimo-javamail-1.4-api
BuildRequires: geronimo-jaf-1.1-api
BuildRequires: glassfish-jaxb
BuildRequires: jakarta-commons-logging
BuildRequires: jaxen
BuildRequires: jdepend
BuildRequires: saxon8
BuildRequires: saxon8-dom
BuildRequires: wstx >= 0:3.1.1
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xml-commons-resolver12
BuildRequires: xmlunit
Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2
Requires: stax_1_0_api
Requires: xml-commons-jaxp-1.3-apis
Requires: javamail = 0:1.4
Requires: jaf = 0:1.1
Requires: jakarta-commons-logging
Requires: jaxen
Requires: glassfish-jaxb
Requires: saxon8
Requires: saxon8-dom
Requires: wstx >= 0:3.1.1
Requires: xerces-j2
Obsoletes:      apache-axiom < %{epoch}:%{version}-%{release}
Provides:       apache-axiom = %{epoch}:%{version}-%{release}
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info


%description
AXIOM stands for AXis Object Model (also known as OM - Object Model)
and refers to the XML infoset model that is initialy developed for
Apache Axis2.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Obsoletes:      apache-axiom-javadoc < %{epoch}:%{version}-%{release}
Provides:       apache-axiom-javadoc = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%if %with maven
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
%setup -q
cp -p %{SOURCE1} settings.xml

# fix eol
%{__perl} -pi -e 's/\r$//g' LICENSE.txt NOTICE.txt README.txt RELEASE-NOTE.txt

rm -f src/site/xdoc/download.*
cp -p %{SOURCE3} build.xml
cp -p %{SOURCE4} modules/axiom-api/build.xml
cp -p %{SOURCE5} modules/axiom-dom/build.xml
cp -p %{SOURCE6} modules/axiom-impl/build.xml

mkdir modules/axiom-api/src/site
cp -p src/site/site.xml modules/axiom-api/src/site
mkdir modules/axiom-dom/src/site
cp -p src/site/site.xml modules/axiom-dom/src/site
mkdir modules/axiom-impl/src/site
cp -p src/site/site.xml modules/axiom-impl/src/site

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%if %with maven
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

# maven3 support 
mv modules/* .
rmdir modules
ln -s . modules
sed -i s,modules/,, pom.xml
%patch33
# end maven3 support

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

export MAVEN_SETTINGS=$(pwd)/settings.xml
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e -s ${MAVEN_SETTINGS} -Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -Dmaven.test.skip=true install javadoc:javadoc 
 #site

%if 0
pushd modules/axiom-tests
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e -s ${MAVEN_SETTINGS} -Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=$MAVEN_REPO_LOCAL install
popd
%endif
%else
export OPT_JAR_LIST=:
export CLASSPATH=$(build-classpath \
commons-logging \
jaxen \
geronimo-javamail-1.4-api \
geronimo-jaf-1.1-api \
xml-commons-jaxp-1.3-apis \
geronimo-stax-1.0-api \
)
pushd modules/axiom-api
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar test javadoc
popd
AXIOM_API_JAR=`ls $(pwd)/modules/axiom-api/target/axiom-api-*.jar`
CLASSPATH=$CLASSPATH:${AXIOM_API_JAR}
pushd modules/axiom-impl
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar test javadoc
popd
AXIOM_IMPL_JAR=`ls $(pwd)/modules/axiom-impl/target/axiom-impl-*.jar`
CLASSPATH=$CLASSPATH:${AXIOM_IMPL_JAR}
pushd modules/axiom-dom
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar test javadoc
popd

# Yes, create target
mkdir target
%endif

mkdir tmp
pushd tmp
%{jar} xf ../modules/axiom-api/target/axiom-api-%{version}.jar
%{jar} xf ../modules/axiom-c14n/target/axiom-c14n-%{version}.jar
%{jar} xf ../modules/axiom-dom/target/axiom-dom-%{version}.jar
%{jar} xf ../modules/axiom-impl/target/axiom-impl-%{version}.jar
%{jar} xf ../modules/axiom-integration/target/axiom-integration-%{version}.jar
%{jar} xf ../modules/axiom-tests/target/axiom-tests-%{version}.jar
%{jar} cf ../target/axiom-%{version}.jar *
popd
rm -r tmp

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -p -m 644 target/axiom-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -p -m 644 modules/axiom-api/target/axiom-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-api-%{version}.jar
install -p -m 644 modules/axiom-c14n/target/axiom-c14n-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-c14n-%{version}.jar
install -p -m 644 modules/axiom-dom/target/axiom-dom-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-dom-%{version}.jar
install -p -m 644 modules/axiom-impl/target/axiom-impl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-impl-%{version}.jar
install -p -m 644 modules/axiom-integration/target/axiom-integration-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-integration-%{version}.jar
install -p -m 644 modules/axiom-tests/target/axiom-tests-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tests-%{version}.jar
%add_to_maven_depmap org.apache.ws.commons.axiom axiom %{version} JPP %{name}
%add_to_maven_depmap org.apache.ws.commons.axiom axiom-api %{version} JPP %{name}-api
%add_to_maven_depmap org.apache.ws.commons.axiom axiom-c14n %{version} JPP %{name}-c14n
%add_to_maven_depmap org.apache.ws.commons.axiom axiom-dom %{version} JPP %{name}-dom
%add_to_maven_depmap org.apache.ws.commons.axiom axiom-impl %{version} JPP %{name}-impl
%add_to_maven_depmap org.apache.ws.commons.axiom axiom-integration %{version} JPP %{name}-integration
%add_to_maven_depmap org.apache.ws.commons.axiom axiom-tests %{version} JPP %{name}-tests
# create unprefixed and unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done
)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom
install -pm 644 modules/axiom-api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-api.pom
install -pm 644 modules/axiom-c14n/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-c14n.pom
install -pm 644 modules/axiom-dom/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-dom.pom
install -pm 644 modules/axiom-impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-impl.pom
install -pm 644 modules/axiom-integration/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-integration.pom
install -pm 644 modules/axiom-tests/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-tests.pom

# javadocs
%if 0
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
#cp -pr modules/axiom-api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/c14n
#cp -pr modules/axiom-c14n/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/c14n
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/dom
#cp -pr modules/axiom-dom/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/dom
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/impl
#cp -pr modules/axiom-impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/impl
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/integration
#cp -pr modules/axiom-integration/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/integration
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/tests
#cp -pr modules/axiom-tests/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/tests
%else
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
#cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
%if %with maven
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/apidocs
pushd $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
ln -s %{_javadocdir}/%{name}-%{version} apidocs
popd
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt NOTICE.txt README.txt RELEASE-NOTE.txt 
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-api-%{version}.jar
%{_javadir}/%{name}-api.jar
%{_javadir}/%{name}-c14n-%{version}.jar
%{_javadir}/%{name}-c14n.jar
%{_javadir}/%{name}-dom-%{version}.jar
%{_javadir}/%{name}-dom.jar
%{_javadir}/%{name}-impl-%{version}.jar
%{_javadir}/%{name}-impl.jar
%{_javadir}/%{name}-integration-%{version}.jar
%{_javadir}/%{name}-integration.jar
%{_javadir}/%{name}-tests-%{version}.jar
%{_javadir}/%{name}-tests.jar
%{_datadir}/maven2/poms/JPP.%{name}.pom
%{_datadir}/maven2/poms/JPP.%{name}-api.pom
%{_datadir}/maven2/poms/JPP.%{name}-c14n.pom
%{_datadir}/maven2/poms/JPP.%{name}-dom.pom
%{_datadir}/maven2/poms/JPP.%{name}-impl.pom
%{_datadir}/maven2/poms/JPP.%{name}-integration.pom
%{_datadir}/maven2/poms/JPP.%{name}-tests.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with maven
%files manual
%{_docdir}/%{name}-%{version}
%endif

%changelog
* Wed Mar 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.8-alt3_2jpp6
- fixed build with maven3

* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.8-alt2_2jpp6
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.8-alt1_2jpp6
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.7-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.7-alt1_2jpp5
- converted from JPackage by jppimport script

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.4-alt1_1jpp1.7
- converted from JPackage by jppimport script

