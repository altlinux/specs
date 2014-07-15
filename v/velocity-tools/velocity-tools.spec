Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          velocity-tools
Version:       2.0
Release:       alt2_2jpp7
Summary:       Collection of useful tools for Velocity template engine
Group:         Development/Java
License:       ASL 2.0
Url:           http://velocity.apache.org/tools/releases/2.0/
Source0:       http://www.apache.org/dist/velocity/tools/%{version}/%{name}-%{version}-src.tar.gz
# force tomcat 7.x apis
Source1:       velocity-tools-2.0-depmap
Patch0:        %{name}-%{version}-junit4.patch
# add org.apache.tomcat tomcat-jsp-api 7.0.27
Patch1:        %{name}-%{version}-pom.patch
Patch2:        %{name}-%{version}-dont_copy_test_lib.patch
# servlet 3.0 support thanks to mizdebsk
Patch3:        %{name}-%{version}-servlet.patch

BuildRequires: jpackage-utils

BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-chain
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-digester
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-validator
BuildRequires: jakarta-oro
BuildRequires: dom4j
BuildRequires: sslext
#  core taglib tiles
BuildRequires: struts
BuildRequires: tomcat-jsp-2.2-api
BuildRequires: tomcat-servlet-3.0-api
BuildRequires: velocity


# test deps
# httpunit httpunit 1.6.1
# org.mortbay.jetty jetty-embedded 6.0.1
# nekohtml nekohtml 0.9.5
# rhino js 1.6R5
# xerces xercesImpl 2.8.1
# xerces xmlParserAPIs 2.6.2
BuildRequires: junit

BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin

Requires:      apache-commons-beanutils
Requires:      apache-commons-chain
Requires:      apache-commons-collections
Requires:      apache-commons-digester
Requires:      apache-commons-lang
Requires:      apache-commons-logging
Requires:      apache-commons-validator
Requires:      jakarta-oro
Requires:      dom4j
Requires:      sslext
Requires:      struts
Requires:      tomcat-jsp-2.2-api
Requires:      tomcat-servlet-3.0-api
Requires:      velocity

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
The VelocityTools project is a collection of useful Java classes (aka tools),
as well as infrastructure to easily, automatically and transparently
make these tools available to Velocity templates.

Project include easy integration of Velocity into the view-layer of
web applications (via the VelocityViewTag and
VelocityViewServlet) and integration with Struts 1.x applications.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}-src
find . -name "*.jar" -delete
find . -name "*.class" -delete
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p0
sed -i 's/\r//' LICENSE NOTICE WHY_THREE_JARS.txt

%build
# tests skipped. cause: missing dependencies
mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 -Dmaven.local.depmap.file="%{SOURCE1}" -Dmaven.test.skip=true  install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -pm 644 dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "%{name}:%{name},org.apache.velocity:%{name}-generic,%{name}:%{name}-generic,%{name}:%{name}-view,org.apache.velocity:%{name}-view"

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc CONTRIBUTORS LICENSE NOTICE README.txt STATUS WHY_THREE_JARS.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_2jpp7
- fc version

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt4_2jpp6
- fixed build with maven3

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_2jpp6
- new jpp relase

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_1jpp5
- removed velocity from requires (temporally, due to v15/16 conlict)

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_1jpp5
- build with velocity15

* Wed Apr 01 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp5
- new version

* Fri Feb 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp5
- fixed build

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp1.7
- updated to new jpackage release

* Fri Nov 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

