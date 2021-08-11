Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

%global pkg_version     11b

Name:           java_cup
Version:        0.11b
Release:        alt4_18jpp11
Epoch:          2
Summary:        LALR parser generator for Java
License:        MIT
URL:            http://www2.cs.tum.edu/projects/cup/
BuildArch:      noarch

# svn export -r 65 https://www2.in.tum.de/repos/cup/develop/ java_cup-0.11b
# tar cjf java_cup-0.11b.tar.bz2 java_cup-0.11b/
Source0:        java_cup-%{version}.tar.bz2
# Add OSGi manifests
Source2:        %{name}-MANIFEST.MF
Source4:        %{name}-runtime-MANIFEST.MF

Patch0:         %{name}-build.patch

BuildRequires:  javapackages-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  ant
BuildRequires:  jflex
BuildRequires:  java_cup
%endif

# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Source44: import.info
Obsoletes: java-cup < 2:11b
Provides: java-cup = %{epoch}:%{version}-%release


%description
java_cup is a LALR Parser Generator for Java

%package javadoc
Group: Development/Java
Summary:       Javadoc for java_cup
BuildArch: noarch

%description javadoc
Javadoc for java_cup

%package manual
Group: Development/Java
Summary:        Documentation for java_cup
BuildArch: noarch

%description manual
Documentation for java_cup.

%prep
%setup -q
%patch0 -b .build

sed -i '/<javac/s/1.5/1.6/g' build.xml

# remove all binary files
find -name "*.class" -delete

%mvn_file ':{*}' @1

# remove prebuilt JFlex
rm -rf java_cup-%{version}/bin/JFlex.jar

# remove prebuilt java_cup, if not bootstrapping
rm -rf java_cup-%{version}/bin/java-cup-11.jar

%build
export CLASSPATH=$(build-classpath java_cup java_cup-runtime jflex)

%ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  -Dcupversion=20150326 -Dsvnversion=65
find -name parser.cup -delete
%ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  javadoc

# inject OSGi manifests
jar ufm dist/java-cup-%{pkg_version}.jar %{SOURCE2}
jar ufm dist/java-cup-%{pkg_version}-runtime.jar %{SOURCE4}

%install
%mvn_artifact %{name}:%{name}:%{version} dist/java-cup-%{pkg_version}.jar
%mvn_artifact %{name}:%{name}-runtime:%{version} dist/java-cup-%{pkg_version}-runtime.jar

%mvn_install -J dist/javadoc

# wrapper script for direct execution
%jpackage_script java_cup.Main "" "" java_cup cup true

%files -f .mfiles
%{_bindir}/cup
%doc changelog.txt
%doc --no-dereference licence.txt

%files manual
%doc manual.html
%doc --no-dereference licence.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference licence.txt

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 2:0.11b-alt4_18jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2:0.11b-alt4_15jpp11
- update

* Mon May 10 2021 Igor Vlasenko <viy@altlinux.org> 2:0.11b-alt4_12jpp8
- new version

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 2:0.11b-alt3_12jpp8
- fc update

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 2:0.11b-alt3_10jpp8
- fc update & java 8 build

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 2:0.11b-alt2_10jpp8
- fc update & java 8 build

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2:0.11b-alt1_10jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 2:0.11b-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2:0.11b-alt1_7jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2:0.11b-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2:0.11b-alt1_3jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 2:0.11b-alt1_1jpp8
- java 8 mass update

* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 2:0.11a-alt1_12jpp7
- new release

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 2:0.11a-alt1_9jpp7
- fc release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 2:0.11-alt2_0.a.2jpp5
- use default jpp profile

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 2:0.11-alt1_0.a.2jpp5
- new version

