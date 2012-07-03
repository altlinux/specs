Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.3.1
%define name apiviz
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             apiviz
Version:          1.3.1
Release:          alt1_4jpp7
Summary:          APIviz is a JavaDoc doclet to generate class and package diagrams
Group:            Development/Java
License:          LGPLv2+
URL:              http://code.google.com/p/apiviz/
Source0:          http://%{name}.googlecode.com/files/%{name}-%{namedversion}-dist.tar.gz
Patch0:           %{name}-%{namedversion}-pom.patch
Patch1:           %{name}-%{namedversion}-jdk7.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    java-1.7.0-devel
BuildRequires:    maven

BuildRequires:    maven-antrun-plugin
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    maven-plugin-jxr
BuildRequires:    jdepend
BuildRequires:    ant-contrib
BuildRequires:    junit4
BuildRequires:    ant

Requires:         jdepend
Requires:         jpackage-utils
Source44: import.info

%description
APIviz is a JavaDoc doclet which extends the Java standard doclet.
It generates comprehensive UML-like class and package diagrams for
quick understanding of the overall API structure. 

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1
%patch1 -p1

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
mvn-rpmbuild install javadoc:aggregate

%install
# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/jboss
cp -p target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/jboss/%{name}.jar

# APIDOCS
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.jboss-%{name}.pom

%add_maven_depmap JPP.jboss-%{name}.pom jboss/%{name}.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc COPYRIGHT.txt LICENSE.jdepend.txt LICENSE.txt NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_4jpp7
- fc version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_3.GA_jpackage_1jpp6
- new jpp relase

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_1jpp6
- new version

