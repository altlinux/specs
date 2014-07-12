# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
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

Name:           slf4j
Version:        1.7.2
Release:        alt1_4jpp7
Epoch:          0
Summary:        Simple Logging Facade for Java
Group:          Development/Java
# the log4j-over-slf4j and jcl-over-slf4j submodules are ASL 2.0, rest is MIT
License:        MIT and ASL 2.0
URL:            http://www.slf4j.org/
Source0:        http://www.slf4j.org/dist/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  ant-junit >= 0:1.6.5
BuildRequires:  javassist >= 0:3.4
BuildRequires:  junit >= 0:3.8.2
BuildRequires:  maven
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-plugin-build-helper
BuildRequires:  log4j
BuildRequires:  apache-commons-logging
BuildRequires:  cal10n
Requires:       jpackage-utils
Requires:       cal10n
BuildArch:      noarch
Source44: import.info

%description
The Simple Logging Facade for Java or (SLF4J) is intended to serve
as a simple facade for various logging APIs allowing to the end-user
to plug in the desired implementation at deployment time. SLF4J also
allows for a gradual migration path away from
Jakarta Commons Logging (JCL).

Logging API implementations can either choose to implement the
SLF4J interfaces directly, e.g. NLOG4J or SimpleLogger. Alternatively,
it is possible (and rather easy) to write SLF4J adapters for the given
API implementation, e.g. Log4jLoggerAdapter or JDK14LoggerAdapter..

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildRequires:  java-javadoc
Requires:       java-javadoc
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package manual
Group:          Development/Java
Summary:        Documents for %{name}
BuildArch: noarch

%description manual
Manual for %{name}.

%prep
%setup -q
find . -name "*.jar" | xargs rm
cp -p %{SOURCE1} APACHE-LICENSE

%pom_disable_module integration
%pom_disable_module osgi-over-slf4j
%pom_remove_plugin :maven-source-plugin

# Because of a non-ASCII comment in slf4j-api/src/main/java/org/slf4j/helpers/MessageFormatter.java
%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>ISO-8859-1</project.build.sourceEncoding>"

# Fix javadoc links
%pom_xpath_remove "pom:links"
%pom_xpath_inject "pom:plugin[pom:artifactId[text()='maven-javadoc-plugin']]/pom:configuration" "
    <detectJavaApiLink>false</detectJavaApiLink>
    <isOffline>false</isOffline>
    <links><link>/usr/share/javadoc/java</link></links>"

# dos2unix
%{_bindir}/find -name "*.css" -o -name "*.js" -o -name "*.txt" | \
    %{_bindir}/xargs -t %{__perl} -pi -e 's/\r$//g'

# The general pattern is that the API package exports API classes and does
# not require impl classes. slf4j was breaking that causing "A cycle was
# detected when generating the classpath slf4j.api, slf4j.nop, slf4j.api."
# The API bundle requires impl package, so to avoid cyclic dependencies
# during build time, it is necessary to mark the imported package as an
# optional one.
sed -i "/Import-Package/s/.$/;resolution:=optional&/" slf4j-api/src/main/resources/META-INF/MANIFEST.MF

%build
mvn-rpmbuild \
        -P skipTests \
        -Dmaven.test.skip=true \
        install javadoc:aggregate

%install
# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}

install -m 644 jcl-over-slf4j/target/jcl-over-slf4j-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/jcl-over-slf4j.jar
install -m 644 jul-to-slf4j/target/jul-to-slf4j-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/jul-to-slf4j.jar
install -m 644 log4j-over-slf4j/target/log4j-over-slf4j-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/log4j-over-slf4j.jar
install -m 644 slf4j-api/target/%{name}-api-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/api.jar
install -m 644 slf4j-ext/target/%{name}-ext-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/ext.jar
install -m 644 slf4j-jcl/target/%{name}-jcl-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/jcl.jar
install -m 644 slf4j-jdk14/target/%{name}-jdk14-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/jdk14.jar
install -m 644 slf4j-log4j12/target/%{name}-log4j12-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/log4j12.jar
install -m 644 slf4j-migrator/target/%{name}-migrator-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/migrator.jar
install -m 644 slf4j-nop/target/%{name}-nop-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/nop.jar
install -m 644 slf4j-simple/target/%{name}-simple-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/simple.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-parent.pom
install -pm 644 jcl-over-slf4j/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-jcl-over-slf4j.pom
install -pm 644 jul-to-slf4j/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-jul-to-slf4j.pom
install -pm 644 log4j-over-slf4j/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-log4j-over-slf4j.pom
install -pm 644 slf4j-api/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-api.pom
install -pm 644 slf4j-ext/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-ext.pom
install -pm 644 slf4j-jcl/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-jcl.pom
install -pm 644 slf4j-jdk14/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-jdk14.pom
install -pm 644 slf4j-log4j12/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-log4j12.pom
install -pm 644 slf4j-migrator/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-migrator.pom
install -pm 644 slf4j-nop/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-nop.pom
install -pm 644 slf4j-simple/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-simple.pom

%add_maven_depmap JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-jcl-over-slf4j.pom %{name}/jcl-over-slf4j.jar
%add_maven_depmap JPP.%{name}-jul-to-slf4j.pom %{name}/jul-to-slf4j.jar
%add_maven_depmap JPP.%{name}-log4j-over-slf4j.pom %{name}/log4j-over-slf4j.jar
%add_maven_depmap JPP.%{name}-api.pom %{name}/api.jar
%add_maven_depmap JPP.%{name}-ext.pom %{name}/ext.jar
%add_maven_depmap JPP.%{name}-jcl.pom %{name}/jcl.jar
%add_maven_depmap JPP.%{name}-jdk14.pom %{name}/jdk14.jar
%add_maven_depmap JPP.%{name}-log4j12.pom %{name}/log4j12.jar
%add_maven_depmap JPP.%{name}-migrator.pom %{name}/migrator.jar
%add_maven_depmap JPP.%{name}-nop.pom %{name}/nop.jar
%add_maven_depmap JPP.%{name}-simple.pom %{name}/simple.jar

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/api*/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/
rm -rf target/site/api*

# manual
install -d -m 0755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -f target/site/.htaccess
cp -pr target/site $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/


%files -f .mfiles
%doc LICENSE.txt APACHE-LICENSE
%dir %{_javadir}/%{name}

%files javadoc
%doc LICENSE.txt APACHE-LICENSE
%{_javadocdir}/%{name}

%files manual
%doc LICENSE.txt APACHE-LICENSE
#%{_docdir}/%{name}-%{version}/site
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%changelog
* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt1_4jpp7
- update

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt1_1jpp7
- new version

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.6-alt1_2jpp7
- new version

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt3_5jpp7
- fc version

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_5jpp7
- fc version

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_5jpp6
- new version

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_4jpp6
- new version (full build)

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_4jpp6
- new version (bootstrap)

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.8-alt1_1jpp6
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_2jpp5
- converted from JPackage by jppimport script

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_2jpp1.7
- updated to new jpackage release

* Mon Dec 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_1jpp1.7
- added dependency on new excalibur

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

