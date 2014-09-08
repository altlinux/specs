# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

Name:              args4j
%global tools_name %{name}-tools
%global site_name  %{name}-site

Version:          2.0.25
Release:          alt1_1jpp7
Summary:          Small Java lib that makes it easy to parse command line options/args in CUI apps
License:          MIT and BSD
Group:            Development/Java
# http://args4j.java.net/
URL:              http://%{name}.java.net/
Source0:          https://github.com/kohsuke/%{name}/archive/%{site_name}-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-shade-plugin
BuildRequires:    mockito

Requires:         jpackage-utils
Source44: import.info

%description
args4j is a small Java class library that makes it easy
to parse command line options/arguments in your CUI application.
- It makes the command line parsing very easy by using annotations.
- You can generate the usage screen very easily.
- You can generate HTML/XML that lists all options for your documentation.
- Fully supports localization.
- It is designed to parse javac like options (as opposed to GNU-style
  where ls -lR is considered to have two options l and R.)

args4j-tools are development-time tools for generating additional artifacits.

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{site_name}-%{version}

# removing classpath addition
sed -i 's/<addClasspath>true/<addClasspath>false/g' %{tools_name}/pom.xml

# fix ant group id
sed -i 's/<groupId>ant/<groupId>org.apache.ant/g' %{tools_name}/pom.xml

# removing bundled stuff
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%pom_xpath_remove "pom:parent"

%build
mvn-rpmbuild -pl :args4j-site,:args4j,:args4j-tools install javadoc:aggregate

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 %{name}/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
install -p -m 644 %{tools_name}/target/%{tools_name}-%{version}.jar %{buildroot}%{_javadir}/%{tools_name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{site_name}.pom
install -pm 644 %{name}/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 %{tools_name}/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{tools_name}.pom

%add_maven_depmap JPP-%{site_name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap JPP-%{tools_name}.pom %{tools_name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc %{name}/LICENSE.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{tools_name}.jar
%{_mavenpomdir}/JPP-%{site_name}.pom
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavenpomdir}/JPP-%{tools_name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{name}/LICENSE.txt
%doc %{_javadocdir}/%{name}

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.25-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.16-alt2_11jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.16-alt2_8jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.16-alt1_8jpp7
- new version

