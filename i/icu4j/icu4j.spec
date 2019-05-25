Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 63.1
%global gittag %(v=%{version}; echo "release-$v" | sed 's/\\./-/')
%global srctgz %(v=%{version}; echo "icu4j-$v" | sed 's/\\./_/')

Name:           icu4j
Version:        63.1
Release:        alt1_2jpp8
Epoch:          1
Summary:        International Components for Unicode for Java
# ICU itself is now covered by Unicode license, but still has contributed
# components covered by MIT and BSD licenses
# Data from the Timezone Database is Public Domain
License:        Unicode and MIT and BSD and Public Domain
URL:            http://site.icu-project.org/

Source0:        https://github.com/unicode-org/icu/releases/download/%{gittag}/%{srctgz}.tgz

# These pom templates are missing from the upstream source archive
# See https://github.com/unicode-org/icu/pull/294
Source1:        https://repo1.maven.org/maven2/com/ibm/icu/icu4j/%{version}/icu4j-%{version}.pom
Source2:        https://repo1.maven.org/maven2/com/ibm/icu/icu4j-charset/%{version}/icu4j-charset-%{version}.pom
Source3:        https://repo1.maven.org/maven2/com/ibm/icu/icu4j-localespi/%{version}/icu4j-localespi-%{version}.pom

# Add better OSGi metadata to core jar
Patch0:         improve-osgi-manifest.patch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-javadoc
BuildRequires:  javapackages-local
BuildRequires:  ivy-local

BuildArch:      noarch
Source44: import.info
%define java_bin %_jvmdir/java/bin

%description
The International Components for Unicode (ICU) library provides robust and
full-featured Unicode services on a wide variety of platforms. ICU supports
the most current version of the Unicode standard, and provides support for
supplementary characters (needed for GB 18030 repertoire support).

Java provides a very strong foundation for global programs, and IBM and the
ICU team played a key role in providing globalization technology into Sun's
Java. But because of its long release schedule, Java cannot always keep
up-to-date with evolving standards. The ICU team continues to extend Java's
Unicode and internationalization support, focusing on improving
performance, keeping current with the Unicode standard, and providing
richer APIs, while remaining as compatible as possible with the original
Java text and internationalization API design.

%package charset
Group: Development/Java
Summary: Charset converter library of %{name}

%description charset
Charset converter library of %{name}.

%package localespi
Group: Development/Java
Summary: Locale SPI library of %{name}

%description localespi
Locale SPI library of %{name}.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
Requires: java-javadoc
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -c
%patch0

# Ivy local does not name these libs as icu4j expects
sed -i -e 's/junit-4.12/junit-SYSTEM/' \
       -e 's/hamcrest-core-1.3/hamcrest-core-SYSTEM/' build.xml

# Missing dep on pl.pragmatists:JUnitParams for tests, so delete tests that
# requires it for now
sed -i -e '/pl.pragmatists/d' ivy.xml
rm main/tests/core/src/com/ibm/icu/dev/test/format/DataDrivenFormatTest.java
rm main/tests/core/src/com/ibm/icu/dev/test/calendar/DataDrivenCalendarTest.java
rm main/tests/core/src/com/ibm/icu/dev/test/serializable/CompatibilityTest.java
rm main/tests/core/src/com/ibm/icu/dev/test/serializable/CoverageTest.java
rm main/tests/charset/src/com/ibm/icu/dev/test/charset/TestConversion.java
rm main/tests/translit/src/com/ibm/icu/dev/test/translit/TransliteratorDisorderedMarksTest.java

%build
export JAVA_HOME=%{_jvmdir}/java/
mkdir -p ~/.ant/lib
ant -Divy.mode=local -Doffline=true -Dicu4j.api.doc.jdk.link=%{_javadocdir}/java \
  all check

# Temporary hack until https://github.com/unicode-org/icu/pull/294 is merged
mkdir -p maven/icu4j{,-charset,-localespi}
cp -p %{SOURCE1} maven/icu4j/pom.xml
cp -p %{SOURCE2} maven/icu4j-charset/pom.xml
cp -p %{SOURCE3} maven/icu4j-localespi/pom.xml

for jar in icu4j icu4j-charset icu4j-localespi ; do
  sed -i -e 's/@POMVERSION@/%{version}/' maven/$jar/pom.xml
  %mvn_artifact maven/$jar/pom.xml $jar.jar
  %mvn_package :$jar $jar
done

%install
%mvn_install -J doc

# No poms for these, so install manually
install -m 644 icu4j-charset.jar   %{buildroot}%{_javadir}/icu4j/
install -m 644 icu4j-localespi.jar %{buildroot}%{_javadir}/icu4j/

%files -f .mfiles-icu4j
%doc --no-dereference main/shared/licenses/*
%doc readme.html APIChangeReport.html

%files charset -f .mfiles-icu4j-charset

%files localespi -f .mfiles-icu4j-localespi

%files javadoc -f .mfiles-javadoc
%doc --no-dereference main/shared/licenses/*

%changelog
* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1:63.1-alt1_2jpp8
- new version

* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 1:59.1-alt3_3jpp8
- fixed build

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:59.1-alt2_3jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:59.1-alt2_2jpp8
- fixed build

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 1:59.1-alt1_2jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:59.1-alt1_1jpp8
- new version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:54.1.1-alt1_8jpp8
- new fc release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1:54.1.1-alt1_7jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1:54.1.1-alt1_6jpp8
- java 8 mass update

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.4.2.2-alt2_12jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.4.2.2-alt1_12jpp7
- new version

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.4.2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

