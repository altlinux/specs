# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             rmic-maven-plugin
Version:          1.2.1
Release:          alt1_4jpp7
Summary:          Uses the java rmic compiler to generate classes used in remote method invocation
License:          MIT
Group:            Development/Java
URL:              http://mojo.codehaus.org/%{name}

Source0:          http://repo2.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:           pom-compiler-source-target.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-invoker-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    maven-checkstyle-plugin

Requires:         maven
Source44: import.info

%description
This plugin works with Maven 2 and uses the java rmic compiler to generate
classes used in remote method invocation.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
sed -i -e "s|groupId>plexus|groupId>org.codehaus.plexus|g" pom.xml

%patch0 -p0

%build
mvn-rpmbuild  -Dmaven.test.failure.ignore=true install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc License.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc License.txt
%{_javadocdir}/%{name}

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_4jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt4_1jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt3_1jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1jpp7
- fixed build

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1jpp7
- new version

