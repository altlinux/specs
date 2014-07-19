# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           opencsv
Version:        2.3
Release:        alt1_5jpp7
Summary:        A very simple csv (comma-separated values) parser library for Java
Group:          Development/Java
License:        ASL 2.0
URL:            http://opencsv.sourceforge.net/
Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}-src-with-libs.tar.gz
BuildArch:      noarch

BuildRequires:  jpackage-utils


BuildRequires:  maven-local

BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  junit

Requires:       jpackage-utils
Source44: import.info

%description
Support for all the basic csv-type things you're likely to want to do.


%package javadoc
Summary:           Javadocs for %{name}
Group:             Development/Java
Requires:          jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q # -n %{name}-%{version}

### making sure we dont use it
rm -rf lib/* doc deploy

%{__sed} -i 's/\r//' examples/MockResultSet.java
%{__sed} -i 's/\r//' examples/JdbcExample.java
%{__sed} -i 's/\r//' examples/addresses.csv
%{__sed} -i 's/\r//' examples/AddressExample.java

%build
# skip test because it is not jdk 1.6 compatible 
%global mvn_opts -Dgpg.skip=true -Dproject.build.sourceEncoding=UTF-8 -Dmaven.test.skip=true
mvn-rpmbuild package javadoc:aggregate %mvn_opts 


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files -f .mfiles
%doc examples

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_5jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_3jpp7
- new version

