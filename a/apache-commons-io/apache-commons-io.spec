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

Name:           apache-commons-io
Epoch:          1
Version:        2.8.0
Release:        alt1_5jpp11
Summary:        Utilities to assist with developing IO functionality
License:        ASL 2.0
URL:            https://commons.apache.org/io
BuildArch:      noarch

Source0:        https://archive.apache.org/dist/commons/io/source/commons-io-%{version}-src.tar.gz

Patch0:         0001-Fix-Files.size-failing-when-symlink-target-is-non-ex.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.mockito:mockito-core)
%endif
Source44: import.info

%description
Commons-IO contains utility classes, stream implementations,
file filters, and endian classes. It is a library of utilities
to assist with developing IO functionality.

%{?javadoc_package}

%prep
%setup -q -n commons-io-%{version}-src
%patch0 -p1
sed -i 's/\r//' *.txt

# Run tests in multiple reusable forks to improve test performance
sed -i -e /reuseForks/d -e /forkCount/d pom.xml
sed -i '/<argLine>/d' pom.xml

%mvn_file  : commons-io %{name}
%mvn_alias : org.apache.commons:

%pom_remove_dep org.junit-pioneer:junit-pioneer
%pom_remove_dep com.google.jimfs:jimfs

# Test depends on com.google.jimfs:jimfs
rm src/test/java/org/apache/commons/io/input/ReversedLinesFileReaderTestParamFile.java

# This annotation is part of junitpioneer
sed -i '/DefaultLocale/d' src/test/java/org/apache/commons/io/output/XmlStreamWriterTest.java
sed -i '/DefaultLocale/d' src/test/java/org/apache/commons/io/input/XmlStreamReaderTest.java

%build
# See "-DcommonsIoVersion" in maven-surefire for the tested version

# The following tests fail on tmpfs/nfs:
#  * PathUtilsDeleteDirectoryTest.testDeleteDirectory1FileSize0OverrideReadOnly:80->testDeleteDirectory1FileSize0:68 » FileSystem
#  * PathUtilsDeleteFileTest.testDeleteReadOnlyFileDirectory1FileSize1:114 » FileSystem
#  * PathUtilsDeleteFileTest.testSetReadOnlyFileDirectory1FileSize1:134 » FileSystem
#  * PathUtilsDeleteTest.testDeleteDirectory1FileSize0OverrideReadonly:97->testDeleteDirectory1FileSize0:69 » FileSystem
#  * PathUtilsDeleteTest.testDeleteDirectory1FileSize1OverrideReadOnly:145->testDeleteDirectory1FileSize1:117 » FileSystem

%mvn_build -f -- -Dmaven.test.skip.exec=true  -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dcommons.osgi.symbolicName=org.apache.commons.io

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%changelog
* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 1:2.8.0-alt1_5jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:2.8.0-alt1_3jpp11
- new version

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1:2.6-alt1_8jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1:2.6-alt1_6jpp8
- new version

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 1:2.6-alt1_3jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.6-alt1_1jpp8
- new version

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.5-alt2_3jpp8
- fc27 update

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.5-alt2_2jpp8
- fixed build with new testng

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.5-alt1_2jpp8
- new version

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt6_15jpp8
- fixed build

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt5_15jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt5_14jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt3_10jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt3_9jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt3_2jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt1_2jpp7
- new release

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_13jpp6
- added osgi manifest

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_12jpp6
- added compat mapping

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_12jpp6
- renamed

