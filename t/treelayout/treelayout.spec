Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global core org.abego.treelayout
Name:          treelayout
Version:       1.0.3
Release:       alt1_5jpp8
Summary:       Efficient and customizable Tree Layout Algorithm in Java
License:       BSD
URL:           http://treelayout.sourceforge.net/
Source0:       https://github.com/abego/treelayout/archive/v%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
Efficiently create compact, highly customizable
tree layouts. The software builds tree layouts
in linear time. I.e. even trees with many nodes
are built fast.

%package demo
Group: Development/Java
Summary:       TreeLayout Core Demo

%description demo
Demo for "org.abego.treelayout.core".

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

# This is a dummy POM added just to ease building in the RPM platforms:
cat > pom.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project
  xmlns="http://maven.apache.org/POM/4.0.0"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <modelVersion>4.0.0</modelVersion>
  <groupId>org.abego.treelayout</groupId>
  <artifactId>org.abego.treelayout.project</artifactId>
  <packaging>pom</packaging>
  <version>%{version}</version>

  <modules>
    <module>org.abego.treelayout</module>
    <module>org.abego.treelayout.demo</module>
    <!-- Use org.netbeans.api:org-netbeans-api-visual:RELEASE67: -->
    <!--module>org.abego.treelayout.netbeans</module-->
    <!--module>org.abego.treelayout.netbeans.demo</module-->
  </modules>

</project>
EOF

# fix non ASCII chars
native2ascii -encoding UTF8 %{core}/src/main/java/org/abego/treelayout/package-info.java \
 %{core}/src/main/java/org/abego/treelayout/package-info.java

%mvn_package :%{core}.project __noinstall

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{core}.core
%doc %{core}/CHANGES.txt README.md
%doc %{core}/src/LICENSE.TXT

%files demo -f .mfiles-%{core}.demo
%doc %{core}.demo/CHANGES.txt
%doc %{core}.demo/src/LICENSE.TXT

%files javadoc -f .mfiles-javadoc
%doc %{core}/src/LICENSE.TXT

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_3jpp8
- new fc release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2jpp8
- new version

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp8
- new version

