Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit f159b88a16be4d103c7e7beb90e07a92617980b9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global zipcommit %(c=%{commit}; echo ${c:0:12})

Name:           jFormatString
Version:        0
Release:        alt1_0.41.20131227gitf159b88jpp11
Summary:        Java format string compile-time checker

License:        GPLv2 with exceptions
URL:            http://code.google.com/p/j-format-string/

Source0:        http://j-format-string.googlecode.com/archive/%{commit}.zip
Source1:        http://search.maven.org/remotecontent?filepath=com/google/code/findbugs/jFormatString/2.0.2/jFormatString-2.0.2.pom

# This patch has not been sent upstream, since it is Fedora specific.
Patch0:         %{name}-build.patch

Patch1:         %{name}-java8.patch

BuildRequires:  javapackages-local

BuildRequires:  ant java-1.8.0-javadoc jpackage-utils junit
Requires:       jpackage-utils

BuildArch:      noarch
Source44: import.info

Obsoletes: jformatstring <= 0:0-alt1_0.3.20081016svnjpp6
Conflicts: jformatstring <= 0:0-alt1_0.3.20081016svnjpp6


%description
This project is derived from Sun's implementation of java.util.Formatter.  It
is designed to allow compile time checks as to whether or not a use of a
format string will be erroneous when executed at runtime.

%package javadoc
Group: Development/Java
Summary:        Javadoc documentation for %{name}
Requires:       java-1.8.0-javadoc
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n j-format-string-%{zipcommit}
%patch0 -p1
%patch1 -p1

cp %{SOURCE1} pom.xml

# delete test code - it requires FindBugs to compile
rm -rfv src/junit

# delete JARs
rm -v lib/*

%mvn_file com.google.code.findbugs:%{name} %{name}

%build
# Build the JAR
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  jarFile

# Create the javadocs
mkdir docs
javadoc -d docs -source 1.8 -sourcepath src/java \
  -classpath build/classes \
  -link file://%{_javadocdir}/java edu.umd.cs.findbugs.formatStringChecker

%mvn_artifact pom.xml build/%{name}.jar

%install

%mvn_install -J docs

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 0-alt1_0.41.20131227gitf159b88jpp11
- java11 build

* Mon Jun 06 2022 Igor Vlasenko <viy@altlinux.org> 0-alt1_0.39.20131227gitf159b88jpp8
- migrated to %%mvn_artifact

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.33.20131227gitf159b88jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.31.20131227gitf159b88jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.28.20131227gitf159b88jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.27.20131227gitf159b88jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.24.20131227gitf159b88jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.23.20131227gitf159b88jpp8
- new fc release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.22.20131227gitjpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.21.20131227gitjpp8
- java 8 mass update

