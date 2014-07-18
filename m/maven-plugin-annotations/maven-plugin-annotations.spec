BuildRequires: maven-plugin-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
# Not to be confused with maven-annotation-plugin from code.google!
Name:           maven-plugin-annotations
Version:        3.1
Release:        alt2_2jpp7
Summary:        Maven Plugin Java 5 Annotations

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugin-tools/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugin-tools/%{name}/%{version}/%{name}-%{version}-sources.jar
Source1:        http://repo2.maven.org/maven2/org/apache/maven/plugin-tools/%{name}/%{version}/%{name}-%{version}.pom
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven

Requires:       jpackage-utils
Requires:       maven
Source44: import.info

%description
This package provides Java 5 annotations to use in Mojos in plugins for
Apache Maven.

%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package provides %{summary}.


%prep
%setup -q -c
mkdir -p src/main/java
cp META-INF/{LICENSE,NOTICE} .
mv META-INF src/main/resources
mv org src/main/java
cp %{SOURCE1} pom.xml

find -name '*.java' -exec sh -c 'mv $0 $0.orig && native2ascii $0.orig $0' {} \;

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}

install -m 644 target/%{name}-*.jar %{buildroot}%{_javadir}/%{name}.jar
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE NOTICE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}


%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_2jpp7
- fixed build

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_2jpp7
- new release

