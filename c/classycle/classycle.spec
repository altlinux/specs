# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          classycle
Version:       1.4
Release:       alt2_3jpp7
Summary:       Analysing Tools for Java Class and Package Dependencies
Group:         Development/Java
License:       BSD
URL:           http://classycle.sourceforge.net/
# http://downloads.sourceforge.net/project/classycle/classycle1.4.zip without build file
# svn co -r209 https://classycle.svn.sourceforge.net/svnroot/classycle/trunk/Classycle/ classycle-1.4
# tar czf classycle-1.4-src-svn.tar.gz classycle-1.4
Source0:       %{name}-%{version}-src-svn.tar.gz
Source1:       http://repo1.maven.org/maven2/org/specs2/%{name}/%{version}/%{name}-%{version}.pom
# various fix
Patch0:        %{name}-%{version}-build.patch

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: ant-testutil
BuildRequires: junit4

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Classycle tools analyse static class and package dependencies
of Java applications or libraries. Main features: Cyclic
dependency detection (beyond JDepend), XML report, checking layered
architectures. The tools runs from command line and as Ant tasks.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p0
cp -p %{SOURCE1} pom.xml
%pom_remove_dep "org.scala-lang:scala-library"

%build

# skip test for various reasons
ant jar apidoc


%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt README.html

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2jpp7
- new version

