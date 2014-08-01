Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       dbutils
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.5
Release:          alt1_3jpp7
Summary:          Apache Commons DbUtils Package
Group:            Development/Java
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    hamcrest
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    mockito
Requires:         jpackage-utils
Source44: import.info

%description
DbUtils is a small set of classes designed to make working with JDBC easier. 
JDBC resource cleanup code is mundane, error prone work so these classes 
abstract out all of the cleanup tasks from your code leaving you with what you 
really wanted to do with JDBC in the first place: query and update data.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' *.txt

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{short_name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.apache.commons:%{short_name}"

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_3jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_3jpp7
- new version

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_5jpp6
- add obsoletes

