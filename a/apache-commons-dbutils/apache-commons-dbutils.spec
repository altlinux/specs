Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global short_name      commons-dbutils

Name:             apache-%{short_name}
Version:          1.5
Release:          alt1_11jpp8
Summary:          Apache Commons DbUtils Package
License:          ASL 2.0
URL:              http://commons.apache.org/dbutils/
BuildArch:        noarch

Source0:          http://www.apache.org/dist/commons/dbutils/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.hamcrest:hamcrest-all)
BuildRequires:  mvn(org.mockito:mockito-core)
Source44: import.info

%description
DbUtils is a small set of classes designed to make working with JDBC easier. 
JDBC resource cleanup code is mundane, error prone work so these classes 
abstract out all of the cleanup tasks from your code leaving you with what you 
really wanted to do with JDBC in the first place: query and update data.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' *.txt

# Compatibility links
%mvn_alias "%{short_name}:%{short_name}" "org.apache.commons:%{short_name}"
%mvn_file :commons-dbutils %{short_name} %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_11jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_10jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_9jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_5jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_3jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_3jpp7
- new version

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_5jpp6
- add obsoletes

