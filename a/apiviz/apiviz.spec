Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 28
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.3.2
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             apiviz
Version:          1.3.2
Release:          alt2_18jpp8
Summary:          APIviz is a JavaDoc doclet to generate class and package diagrams
Group:            Development/Other
License:          LGPLv2+
URL:              http://code.google.com/p/apiviz/
Source0:          http://apiviz.googlecode.com/files/apiviz-%{namedversion}-dist.tar.gz
Patch0:           0001-JDK7-compatibility.patch
Patch1:           0002-JDK8-compatibility.patch
Patch2:           0003-fix-deprecated-assembly-goal.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(ant-contrib:ant-contrib)
BuildRequires:    mvn(com.sun:tools)
BuildRequires:    mvn(jdepend:jdepend)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
Source44: import.info

%description
APIviz is a JavaDoc doclet which extends the Java standard doclet.
It generates comprehensive UML-like class and package diagrams for
quick understanding of the overall API structure. 

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n apiviz-%{namedversion}
%patch0 -p1

%if 0%{?fedora} || 0%{?rhel} > 7
%patch1 -p1
%patch2 -p0
%endif

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

#%pom_xpath_remove "pom:dependencies/pom:dependency[pom:artifactId = 'tools']/pom:scope"
#%pom_xpath_remove "pom:dependencies/pom:dependency[pom:artifactId = 'tools']/pom:systemPath"

%pom_remove_dep com.sun:tools
%pom_add_dep com.sun:tools

%mvn_alias "org.jboss.apiviz:apiviz" "net.gleamynode.apiviz:apiviz"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc COPYRIGHT.txt LICENSE.jdepend.txt LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt2_18jpp8
- fc29 update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt2_17jpp8
- java fc28+ update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt2_16jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt2_13jpp8
- added BR: maven-assembly-plugin for javapackages 5

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt1_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt1_10jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt1_9jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt1_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt1_4jpp7
- new release

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

