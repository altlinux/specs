Epoch: 0
Group: Development/Other
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           javassist
Version:        3.28.0
Release:        alt1_2jpp11
Summary:        Java Programming Assistant for Java bytecode manipulation
License:        MPLv1.1 or LGPLv2+ or ASL 2.0

%global upstream_version rel_%(sed s/\\\\./_/g <<<"%{version}")_ga

URL:            https://www.javassist.org/
Source0:        https://github.com/jboss-%{name}/%{name}/archive/%{upstream_version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-all)
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
Group: Development/Java
Summary:        Javadocs for javassist
BuildArch: noarch

%description javadoc
javassist development documentation.


%prep
%setup -q -n %{name}-%{upstream_version}

# remove unnecessary maven plugins
%pom_remove_plugin :maven-source-plugin

# disable profiles that only add com.sun:tools dependency
%pom_xpath_remove "pom:profiles"

# add compatibility alias for old maven artifact coordinates
%mvn_alias : %{name}:%{name}

# add compatibility symlink for old classpath
%mvn_file : %{name}


%build
%mvn_build -f

# remove bundled jar and class files *after* they were used for running tests
rm javassist.jar src/test/resources/*.jar
find src/test -name "*.class" -print -delete


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference License.html
%doc Readme.html

%files javadoc -f .mfiles-javadoc
%doc --no-dereference License.html


%changelog
* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 0:3.28.0-alt1_2jpp11
- new version

* Sun Jun 13 2021 Igor Vlasenko <viy@altlinux.org> 0:3.27.0-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:3.21.0-alt1_3jpp8
- new version

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.18.1-alt1_12jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.18.1-alt1_10jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.18.1-alt1_9jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.18.1-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.18.1-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.18.1-alt1_6jpp8
- new jpp release

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

