Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          classycle
Version:       1.4
Release:       alt2_9jpp8
Summary:       Analysing Tools for Java Class and Package Dependencies
License:       BSD
URL:           http://classycle.sourceforge.net/
# http://downloads.sourceforge.net/project/classycle/classycle1.4.zip without build file
# svn co -r209 https://classycle.svn.sourceforge.net/svnroot/classycle/trunk/Classycle/ classycle-1.4
# tar czf classycle-1.4-src-svn.tar.gz classycle-1.4
Source0:       %{name}-%{version}-src-svn.tar.gz
Source1:       http://repo1.maven.org/maven2/org/specs2/%{name}/%{version}/%{name}-%{version}.pom
# various fix
Patch0:        %{name}-%{version}-build.patch

Patch1:        %{name}-%{version}-disable-doclint.patch

BuildRequires: javapackages-local
BuildRequires: ant
BuildRequires: ant-testutil
BuildRequires: junit

BuildArch:     noarch
Source44: import.info

%description
Classycle tools analyse static class and package dependencies
of Java applications or libraries. Main features: Cyclic
dependency detection (beyond JDepend), XML report, checking layered
architectures. The tools runs from command line and as Ant tasks.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
cp -p %{SOURCE1} pom.xml
%pom_remove_dep "org.scala-lang:scala-library"

%build

# skip test for various reasons
ant jar apidoc

%install
%mvn_file org.specs2:%{name} %{name}
%mvn_artifact pom.xml target/%{name}-%{version}.jar
%mvn_install -J target/site/apidocs

%files -f .mfiles
%doc README.html
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_8jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2jpp7
- new version

