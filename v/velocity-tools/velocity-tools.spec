Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          velocity-tools
Version:       2.0
Release:       alt2_17jpp8
Summary:       Collection of useful tools for Velocity template engine
License:       ASL 2.0
Url:           http://velocity.apache.org/tools/releases/2.0/
Source0:       http://www.apache.org/dist/velocity/tools/%{version}/%{name}-%{version}-src.tar.gz
Patch0:        %{name}-%{version}-junit4.patch
Patch1:        %{name}-%{version}-dont_copy_test_lib.patch
# servlet 3.0 support thanks to mizdebsk
# servlet 3.1 support
Patch2:        %{name}-%{version}-servlet.patch
Patch3:        %{name}-%{version}-port-to-dom4j-2.0.patch

BuildRequires: maven-local
BuildRequires: mvn(commons-beanutils:commons-beanutils)
BuildRequires: mvn(commons-chain:commons-chain)
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(commons-digester:commons-digester)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(commons-validator:commons-validator)
BuildRequires: mvn(dom4j:dom4j)
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)
# required by resources-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-filtering)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires: mvn(org.apache.struts:struts-core)
BuildRequires: mvn(org.apache.struts:struts-taglib)
BuildRequires: mvn(org.apache.struts:struts-tiles)
BuildRequires: mvn(org.apache.tomcat:tomcat-jsp-api)
BuildRequires: mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires: mvn(org.apache.velocity:velocity)
BuildRequires: mvn(oro:oro)
BuildRequires: mvn(sslext:sslext)
# required by tomcat-jsp-api
BuildRequires: mvn(org.apache.tomcat:tomcat-el-api)

# test deps
%if 0
BuildRequires: mvn(httpunit:httpunit) = 1.6.1
BuildRequires: mvn(nekohtml:nekohtml) = 0.9.5
BuildRequires: mvn(org.mortbay.jetty:jetty-embedded) = 6.0.1
BuildRequires: mvn(rhino:js) = 1.6R5
BuildRequires: mvn(xerces:xercesImpl) = 2.8.1
BuildRequires: mvn(xerces:xmlParserAPIs) = 2.6.2
%endif
BuildRequires: mvn(junit:junit)
BuildRequires: xmvn

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
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}-src
find . -name "*.jar" -delete
find . -name "*.class" -delete
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

sed -i 's/\r//' LICENSE NOTICE WHY_THREE_JARS.txt

# force tomcat 7.x apis
%pom_remove_dep javax.servlet:servlet-api
%pom_add_dep org.apache.tomcat:tomcat-servlet-api::provided
%pom_add_dep org.apache.tomcat:tomcat-jsp-api::provided
# remove non standard build structure
%pom_xpath_remove "pom:project/pom:build/pom:outputDirectory"
%pom_xpath_remove "pom:project/pom:build/pom:directory"

%pom_remove_dep org.mortbay.jetty:jetty-embedded

%mvn_file :%{name} %{name}
%mvn_alias :%{name} %{name}:%{name}
%mvn_alias :%{name} org.apache.velocity:%{name}-generic
%mvn_alias :%{name} %{name}:%{name}-generic
%mvn_alias :%{name} %{name}:%{name}-view
%mvn_alias :%{name} org.apache.velocity:%{name}-view

%build

# tests skipped. cause: missing dependencies
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc CONTRIBUTORS README.txt STATUS WHY_THREE_JARS.txt
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_17jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_15jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_13jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_12jpp8
- java 8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_5jpp7
- new release

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

