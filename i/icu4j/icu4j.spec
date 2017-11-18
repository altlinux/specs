Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: perl(Output.pm) perl(Statistics/Descriptive.pm) perl(Statistics/Distributions.pm) perl(XML/LibXML.pm) rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           icu4j
Version:        59.1
Release:        alt2_2jpp8
Epoch:          1
Summary:        International Components for Unicode for Java
License:        MIT and EPL
URL:            http://site.icu-project.org/

#CAUTION
#to create a tarball use following procedure
#svn co http://source.icu-project.org/repos/icu/tags/release-59-1/icu4j/ icu4j-59.1
#tar caf icu4j-<version>.tar.xz icu4j-<version>/
Source0:        icu4j-%{version}.tar.xz

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
Summary:        Charset converter library of %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description charset
Charset converter library of %{name}.

%package localespi
Group: Development/Java
Summary:        Locale SPI library of %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description localespi
Locale SPI library of %{name}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
Requires:       java-javadoc
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n icu4j-%{version}

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

%build
export JAVA_HOME=%{_jvmdir}/java/
mkdir -p ~/.ant/lib
ant -Divy.mode=local -Doffline=true -Dicu4j.api.doc.jdk.link=%{_javadocdir}/java \
  all

%mvn_artifact pom.xml icu4j.jar

%install
%mvn_install -J doc

# No poms for these, so install manually
install -m 644 icu4j-charset.jar   %{buildroot}%{_javadir}/icu4j/
install -m 644 icu4j-localespi.jar %{buildroot}%{_javadir}/icu4j/

%files -f .mfiles
%doc main/shared/licenses/*
%doc readme.html APIChangeReport.html

%files charset
%{_javadir}/icu4j/icu4j-charset.jar

%files localespi
%{_javadir}/icu4j/icu4j-localespi.jar

%files javadoc -f .mfiles-javadoc
%doc main/shared/licenses/*

%changelog
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

