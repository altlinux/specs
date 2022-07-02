Epoch: 0
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

Name:           apache-commons-collections
Version:        3.2.2
Release:        alt1_27jpp11
Summary:        Provides new interfaces, implementations and utilities for Java Collections
License:        ASL 2.0
URL:            http://commons.apache.org/collections/
BuildArch:      noarch

Source0:        http://www.apache.org/dist/commons/collections/source/commons-collections-%{version}-src.tar.gz

Patch0:         0001-Port-to-Java-8.patch
Patch1:         0002-Port-to-OpenJDK-11.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
%endif
Source44: import.info

%description
The introduction of the Collections API by Sun in JDK 1.2 has been a
boon to quick and effective Java programming. Ready access to powerful
data structures has accelerated development by reducing the need for
custom container classes around each core object. Most Java2 APIs are
significantly easier to use because of the Collections API.
However, there are certain holes left unfilled by Sun's
implementations, and the Jakarta-Commons Collections Component strives
to fulfill them. Among the features of this package are:
- special-purpose implementations of Lists and Maps for fast access
- adapter classes from Java1-style containers (arrays, enumerations) to
Java2-style collections.
- methods to test or create typical set-theory properties of collections
such as union, intersection, and closure.

%package testframework
Group: Development/Java
Summary:        Testframework for %{name}
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description testframework
%{summary}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n commons-collections-%{version}-src

# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;

%patch0 -p1
%patch1 -p1

# Port to maven-antrun-plugin 3.0.0
sed -i s/tasks/target/ pom.xml

# Fix file eof
sed -i 's/\r//' LICENSE.txt PROPOSAL.html README.txt NOTICE.txt

%mvn_package :commons-collections-testframework testframework
%mvn_file ':commons-collections{,-testframework}' %{name}@1 commons-collections@1

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.compiler.source=1.7 -Dmaven.compiler.target=1.7 -Dcommons.osgi.symbolicName=org.apache.commons.collections

%install
%mvn_artifact commons-collections:commons-collections-testframework:%{version} target/commons-collections-testframework-%{version}.jar
%mvn_install

%files -f .mfiles
%doc PROPOSAL.html README.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%files testframework -f .mfiles-testframework

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:3.2.2-alt1_27jpp11
- update

* Wed Jun 08 2022 Igor Vlasenko <viy@altlinux.org> 0:3.2.2-alt1_24jpp11
- support of new antrun plugin

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:3.2.2-alt1_20jpp11
- update

* Mon May 10 2021 Igor Vlasenko <viy@altlinux.org> 0:3.2.2-alt1_16jpp8
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.2.2-alt1_12jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.2.2-alt1_8jpp8
- java fc28+ update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.2.2-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.2.2-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.2.2-alt1_4jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.2.2-alt1_3jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt10_26jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt9jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt8_19jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt8_16jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt8_14jpp7
- fc update

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt8_6jpp6
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt7_6jpp6
- fixed build with new svgsalamander

* Sat Sep 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt6_6jpp6
- fixed build with lucene3

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt5_6jpp6
- new jpp relase

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt5_5jpp6
- fixed conflicts/obsoletes (closes: #24858)

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt4_5jpp6
- fixed repolib id

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt3_5jpp6
- fixed repolib

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt2_5jpp6
- add obsoletes

* Sat Jan 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_5jpp6
- new version

