Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global artifactId javax.servlet-api

Name:           glassfish-servlet-api
Version:        3.1.0
Release:        alt3_10jpp8
Summary:        Java Servlet API
License:        (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:            http://servlet-spec.java.net
# svn export https://svn.java.net/svn/glassfish~svn/tags/javax.servlet-api-3.1.0 javax.servlet-api-3.1.0
# tar cvJf javax.servlet-api-3.1.0.tar.xz javax.servlet-api-3.1.0/
Source0:        %{artifactId}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  jvnet-parent
BuildRequires:  maven-local
BuildRequires:  maven-source-plugin
Source44: import.info


%description
The javax.servlet package contains a number of classes 
and interfaces that describe and define the contracts between 
a servlet class and the runtime environment provided for 
an instance of such a class by a conforming servlet container.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{artifactId}-%{version}
%pom_remove_plugin :maven-remote-resources-plugin
%pom_remove_plugin :maven-javadoc-plugin
cp -p %{SOURCE1} .
# README contains also part of javax.servlet-api license
cp -p src/main/resources/META-INF/README .
%mvn_file :%{artifactId} %{name}

%build
%mvn_alias : javax.servlet:servlet-api
%mvn_alias : org.apache.geronimo.specs:geronimo-servlet_3.0_spec
%mvn_alias : org.eclipse.jetty.orbit:javax.servlet
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc README
%doc LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt3_10jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt3_9jpp8
- new version

* Mon Jan 25 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_2jpp7
- new release

