Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global base_name       collections
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        3.2.1
Release:        alt10_26jpp8
Summary:        Provides new interfaces, implementations and utilities for Java Collections
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        commons-collections-testframework.pom

Patch0:         java8-compat.patch
Patch1:         jakarta-%{short_name}-javadoc-nonet.patch

Patch4:         commons-collections-3.2-build_xml.patch


BuildArch:      noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: ant
BuildRequires: apache-commons-parent
BuildRequires: dos2unix
Requires:      jpackage-utils
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
Summary:        Testframework for %{name}
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description testframework
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
%{summary}.

%package testframework-javadoc
Summary:        Javadoc for %{name}-testframework
Group:          Development/Java

%description testframework-javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src

# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;
find . -name "*.java" |xargs dos2unix

%patch0 -p1
%patch1 -p1
%patch4 -b .sav

# Fix file eof
%{__sed} -i 's/\r//' LICENSE.txt
%{__sed} -i 's/\r//' PROPOSAL.html
%{__sed} -i 's/\r//' RELEASE-NOTES.html
%{__sed} -i 's/\r//' README.txt
%{__sed} -i 's/\r//' NOTICE.txt

# Substitute version into testframework pom
cp -p %{SOURCE1} pom-testframework.xml
sed -i 's/@VERSION@/%{version}/' pom-testframework.xml

%build
%mvn_build

ant tf.javadoc

%install

# jars
install -Dm 644 target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -Dm 644 target/%{short_name}-testframework-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-testframework.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *; do ln -sf ${jar} `echo $jar| sed  "s|apache-||g"`; done)


# poms
mkdir -p %{buildroot}%{_datadir}/maven-poms/
install -Dpm 644 pom.xml %{buildroot}%{_datadir}/maven-poms/%{short_name}.pom
install -Dpm 644 pom-testframework.xml %{buildroot}%{_datadir}/maven-poms/%{short_name}-testframework.pom


# fragments
%add_maven_depmap %{short_name}.pom %{short_name}.jar -a "org.apache.commons:%{short_name}"
%add_maven_depmap %{short_name}-testframework.pom %{short_name}-testframework.jar -f "testframework" -a "org.apache.commons:%{short_name}-testframework"


# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
rm -rf target/site/apidocs


# testframework-javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-testframework-%{version}
cp -pr build/docs/testframework/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-testframework-%{version}
ln -s %{name}-testframework-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-testframework


%files -f .mfiles
%doc PROPOSAL.html README.txt LICENSE.txt RELEASE-NOTES.html NOTICE.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{short_name}.jar

%files testframework -f .mfiles-testframework
%{_javadir}/%{name}-testframework.jar
%{_javadir}/%{short_name}-testframework.jar

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files testframework-javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}-testframework-%{version}
%{_javadocdir}/%{name}-testframework


%changelog
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

