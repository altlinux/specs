Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name apiviz
%define version 1.3.2
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             apiviz
Version:          1.3.2
Release:          alt1_2jpp7
Summary:          APIviz is a JavaDoc doclet to generate class and package diagrams
Group:            Development/Java
License:          LGPLv2+
URL:              http://code.google.com/p/apiviz/
Source0:          http://apiviz.googlecode.com/files/apiviz-%{namedversion}-dist.tar.gz
Patch0:           apiviz-pom.patch

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
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    maven-plugin-jxr
BuildRequires:    jdepend
BuildRequires:    ant-contrib
BuildRequires:    junit4
BuildRequires:    ant

Requires:         jdepend
Requires:         jpackage-utils
Requires:         graphviz
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
This package contains the API documentation for %%{name}.

%prep
%setup -q -n apiviz-%{namedversion}
%patch0 -p1

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
mvn-rpmbuild install javadoc:aggregate

%install
# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# APIDOCS
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "net.gleamynode.apiviz:apiviz"

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc COPYRIGHT.txt LICENSE.jdepend.txt LICENSE.txt NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt1_2jpp7
- fc update

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_8jpp7
- new fc release

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_7jpp7
- new release

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_4jpp7
- fc version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_3.GA_jpackage_1jpp6
- new jpp relase

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_1jpp6
- new version

