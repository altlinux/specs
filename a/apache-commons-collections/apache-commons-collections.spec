Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global base_name       collections
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        3.2.2
Release:        alt1_3jpp8
Summary:        Provides new interfaces, implementations and utilities for Java Collections
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

Patch0:         0001-Port-to-Java-8.patch

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
Source44: import.info
Obsoletes: jakarta-%{short_name} < 1:%{version}-%{release}
Conflicts: jakarta-%{short_name} < 1:%{version}-%{release}

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
Requires:       %{name} = %{version}

%description testframework
%{summary}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
Provides:       %{name}-testframework-javadoc = %{version}-%{release}
Obsoletes:      %{name}-testframework-javadoc < %{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src

# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;

%patch0 -p1

# Fix file eof
sed -i 's/\r//' LICENSE.txt PROPOSAL.html README.txt NOTICE.txt

%mvn_package :%{short_name}-testframework testframework
%mvn_file ':%{short_name}{,-testframework}' %{name}@1 %{short_name}@1

%build
%mvn_build -- -Dmaven.test.skip.exec=true

ant tf.javadoc -Dtf.build.docs=target/site/apidocs/

%mvn_artifact %{short_name}:%{short_name}-testframework:%{version} target/%{short_name}-testframework-%{version}.jar

%install
%mvn_install

# Workaround for RPM bug #646523 - can't change symlink to directory
%files -f .mfiles
%doc PROPOSAL.html README.txt LICENSE.txt NOTICE.txt

%files testframework -f .mfiles-testframework

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
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

