Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name javassist
%define version 3.18.1
%global upstream_version rel_%(sed s/\\\\./_/g <<<"%{version}")_ga

Name:           javassist
Version:        3.18.1
Release:        alt1_5jpp8
Summary:        The Java Programming Assistant provides simple Java bytecode manipulation
Group:          Development/Other
License:        MPLv1.1 or LGPLv2+ or ASL 2.0
URL:            http://www.csg.is.titech.ac.jp/~chiba/%{name}/
BuildArch:      noarch

Source0:        http://github.com/jboss-%{name}/%{name}/archive/%{upstream_version}.tar.gz

Patch0:         0001-Remove-usage-of-junit.awtui-and-junit.swingui.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
Source44: import.info

%description
Javassist enables Java programs to define a new class at runtime and to
modify a class file when the JVM loads it. Unlike other similar
bytecode editors, Javassist provides two levels of API: source level
and bytecode level. If the users use the source-level API, they can
edit a class file without knowledge of the specifications of the Java
bytecode. The whole API is designed with only the vocabulary of the
Java language. You can even specify inserted bytecode in the form of
source text; Javassist compiles it on the fly. On the other hand, the
bytecode-level API allows the users to directly edit a class file as
other editors.

%package javadoc
Summary:           Javadocs for javassist
Group:             Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
javassist development documentation.

%prep
%setup -q -n %{name}-%{upstream_version}
find . -name \*.jar -type f -delete
mkdir runtest
%patch0 -p1
%pom_xpath_remove "pom:profile[pom:id='default-tools']"
%pom_add_dep com.sun:tools

%mvn_file : %{name}
%mvn_alias : %{name}:%{name}

%build
# TODO: enable tests
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc License.html Readme.html

%files javadoc -f .mfiles-javadoc
%doc License.html

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.18.1-alt1_5jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.18.1-alt1_4jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.16.1-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.16.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.16.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.16.1-alt1_2jpp7
- new version

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.9.0-alt1_3jpp6
- new versuin

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.8.0-alt1_2jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.8.0-alt1_1jpp5
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_0.cr1.2jpp1.7
- converted from JPackage by jppimport script

* Sat Apr 23 2005 Vladimir Lettiev <crux@altlinux.ru> 3.0-alt1
- Initial build for ALT Linux Sisyphus

