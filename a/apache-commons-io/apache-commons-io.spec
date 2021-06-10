Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# unit tests do not finish or crash the JVM
%bcond_with tests

%global srcname commons-io

Name:           apache-commons-io
Epoch:          1
Version:        2.8.0
Release:        alt1_3jpp11
Summary:        Utilities to assist with developing IO functionality
License:        ASL 2.0

URL:            https://commons.apache.org/io
Source0:        https://archive.apache.org/dist/commons/io/source/%{srcname}-%{version}-src.tar.gz

Patch0: 0001-Fix-Files.size-failing-when-symlink-target-is-non-ex.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)

%if %{with tests}
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit-platform)
%endif
Source44: import.info

%description
Commons-IO contains utility classes, stream implementations,
file filters, and endian classes. It is a library of utilities
to assist with developing IO functionality.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{srcname}-%{version}-src
%patch0 -p1
sed -i 's/\r//' *.txt

%if %{with tests}
# com.google.jimfs:jimfs is not packaged for fedora
%pom_remove_dep com.google.jimfs:jimfs
rm src/test/java/org/apache/commons/io/input/ReversedLinesFileReaderTestParamFile.java

# junit-pioneer is not packaged for fedora
%pom_remove_dep :junit-pioneer
rm src/test/java/org/apache/commons/io/input/XmlStreamReaderTest.java
rm src/test/java/org/apache/commons/io/output/XmlStreamWriterTest.java
%endif

%mvn_file  : commons-io %{name}
%mvn_alias : org.apache.commons:


%build
%if %{with tests}
%mvn_build -- -Dmaven.test.skip.exec=true  -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dcommons.osgi.symbolicName=org.apache.commons.io
%else
%mvn_build -f -- -Dmaven.test.skip.exec=true  -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dcommons.osgi.symbolicName=org.apache.commons.io
%endif


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt


%changelog
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

