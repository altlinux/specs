Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global pkg_version     11b
%global with_bootstrap  0

Name:           java_cup
Version:        0.11b
Release:        alt1_10jpp8
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

BuildRequires:  ant
BuildRequires:  javapackages-local
BuildRequires:  jflex
%if ! %{with_bootstrap}
BuildRequires:  java_cup >= 1:0.11a
%endif
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

# remove all binary files
find -name "*.class" -delete

%mvn_file ':{*}' @1

%if ! %{with_bootstrap}
# remove prebuilt JFlex
rm -rf java_cup-%{version}/bin/JFlex.jar

# remove prebuilt java_cup, if not bootstrapping
rm -rf java_cup-%{version}/bin/java-cup-11.jar
%endif

%build
%if ! %{with_bootstrap}
export CLASSPATH=$(build-classpath java_cup java_cup-runtime jflex)
%endif

ant -Dcupversion=20150326 -Dsvnversion=65
find -name parser.cup -delete
ant javadoc

# inject OSGi manifests
jar ufm dist/java-cup-%{pkg_version}.jar %{SOURCE2}
jar ufm dist/java-cup-%{pkg_version}-runtime.jar %{SOURCE4}

%install
%mvn_artifact %{name}:%{name}:%{version} dist/java-cup-%{pkg_version}.jar
%mvn_artifact %{name}:%{name}-runtime:%{version} dist/java-cup-%{pkg_version}-runtime.jar

%mvn_install -J dist/javadoc

%files -f .mfiles
%doc changelog.txt
%doc --no-dereference licence.txt

%files manual
%doc manual.html
%doc --no-dereference licence.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference licence.txt

%changelog
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

