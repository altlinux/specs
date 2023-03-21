Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 71.1
%global gittag %(v=%{version}; echo "release-$v" | sed 's/\\./-/')
%global srctgz %(v=%{version}; echo "icu4j-$v" | sed 's/\\./_/')

Name:           icu4j
Version:        71.1
Release:        alt1_3jpp11
Epoch:          1
Summary:        International Components for Unicode for Java
# ICU itself is now covered by Unicode license, but still has contributed
# components covered by MIT and BSD licenses
# Data from the Timezone Database is Public Domain
License:        Unicode and MIT and BSD and Public Domain
URL:            https://icu.unicode.org/

Source0:        https://github.com/unicode-org/icu/releases/download/%{gittag}/%{srctgz}.tgz

# Add better OSGi metadata to core jar
Patch0:         0001-Improve-OSGi-manifest.patch

# Use default Doclet due to Doclet API changes in Java 9+
# that prevent ICU's custom one from being built
Patch1:         0002-Use-default-doclet.patch

# Update the code for Java 8.  Patch courtesy of OpenSuSE.
Patch2:         0003-java8.patch

# Ivy is no longer available from Fedora
Patch3:         0004-remove-ivy.patch

# Fix some invalid javadoc characters
Patch4:         0005-javadoc.patch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  javapackages-local

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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1


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
rm main/tests/core/src/com/ibm/icu/dev/test/util/LocaleMatcherTest.java
rm main/tests/charset/src/com/ibm/icu/dev/test/charset/TestConversion.java
rm main/tests/translit/src/com/ibm/icu/dev/test/translit/TransliteratorDisorderedMarksTest.java

%build
#export JAVA_HOME=%{_jvmdir}/java/
mkdir -p ~/.ant/lib
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  -Djavac.source=8 -Djavac.target=8 -Divy.mode=local -Doffline=true -Ddoclint.option='-Xdoclint:none' -Dicu4j.api.doc.jdk.link= all

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
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1:71.1-alt1_3jpp11
- new version

* Sat Jul 02 2022 Igor Vlasenko <viy@altlinux.org> 1:70.1-alt1_3jpp11
- new version

* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 1:69.1-alt1_1jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:68.2-alt1_1jpp11
- new version

* Sun Oct 11 2020 Igor Vlasenko <viy@altlinux.ru> 1:65.1-alt1_5jpp8
- new version

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

