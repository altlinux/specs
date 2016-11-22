# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jboss-classpool-scoped
Version:        1.0.0
Release:        alt2_11jpp8
Summary:        A custom class pool for several JBoss products

Group:          Development/Other
License:        LGPLv2+
URL:            http://www.jboss.org/jbossreflect

# svn export http://anonsvn.jboss.org/repos/jbossas/projects/jboss-classpool/tags/1.0.0.GA/scopedpool/ jboss-classpool-scoped-1.0.0
# tar cJf jboss-classpool-scoped-1.0.0.tar.xz jboss-classpool-scoped-1.0.0/
Source0:        jboss-classpool-scoped-1.0.0.tar.xz

BuildArch:      noarch

BuildRequires:  javassist
BuildRequires:  maven-local
Source44: import.info

%description
A custom class pool for several JBoss products.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -type f -name *.jar -delete
find -type f -name *.class -delete

%pom_set_parent org.jboss:jboss-parent:6
%pom_xpath_inject pom:project \
    "<groupId>org.jboss.classpool</groupId><version>1.0.0.GA</version>"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp7
- new version

