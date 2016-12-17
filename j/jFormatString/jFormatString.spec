# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global commit f159b88a16be4d103c7e7beb90e07a92617980b9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global zipcommit %(c=%{commit}; echo ${c:0:12})

Name:           jFormatString
Version:        0
Release:        alt1_0.23.20131227gitf159b88jpp8
Summary:        Java format string compile-time checker

Group:          Development/Other
License:        GPLv2 with exceptions
URL:            http://code.google.com/p/j-format-string/

Source0:        http://j-format-string.googlecode.com/archive/%{commit}.zip
Source1:        http://search.maven.org/remotecontent?filepath=com/google/code/findbugs/jFormatString/2.0.2/jFormatString-2.0.2.pom

# This patch has not been sent upstream, since it is Fedora specific.
Patch0:         %{name}-build.patch

BuildRequires:  ant java-devel java-javadoc jpackage-utils junit
Requires: jpackage-utils

BuildArch:      noarch
Source44: import.info

Obsoletes: jformatstring <= 0:0-alt1_0.3.20081016svnjpp6
Conflicts: jformatstring <= 0:0-alt1_0.3.20081016svnjpp6


%description
This project is derived from Sun's implementation of java.util.Formatter.  It
is designed to allow compile time checks as to whether or not a use of a
format string will be erroneous when executed at runtime.

%package javadoc
Summary:        Javadoc documentation for %{name}
Group:          Development/Java
Requires:       java-javadoc
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n j-format-string-%{zipcommit}
%patch0 -p1

cp %{SOURCE1} pom.xml

# delete test code - it requires FindBugs to compile
rm -rfv src/junit

# delete JARs
rm -v lib/*

%build
# Build the JAR
ant jarFile

# Create the javadocs
mkdir docs
javadoc -d docs -source 1.5 -sourcepath src/java \
  -classpath build/classes \
  -link file://%{_javadocdir}/java edu.umd.cs.findbugs.formatStringChecker

%install

# JAR files
mkdir -p %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
cp -p build/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# Javadocs
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp docs/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{name}*

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.23.20131227gitf159b88jpp8
- new fc release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.22.20131227gitjpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.21.20131227gitjpp8
- java 8 mass update

