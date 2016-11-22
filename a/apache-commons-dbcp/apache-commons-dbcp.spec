Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global base_name       dbcp
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.4
Release:          alt2_20jpp8
Summary:          Apache Commons DataBase Pooling Package
Group:            Development/Other
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
BuildArch:        noarch

Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

Patch0:           jdbc41.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(commons-pool:commons-pool)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
Source44: import.info

%description
Many Apache projects support interaction with a relational database. Creating a
new connection for each user can be time consuming (often requiring multiple
seconds of clock time), in order to perform a database transaction that might
take milliseconds. Opening a connection per user can be unfeasible in a
publicly-hosted Internet application where the number of simultaneous users can
be very large. Accordingly, developers often wish to share a "pool" of open
connections between all of the application's current users. The number of users
actually performing a request at any given time is usually a very small
percentage of the total number of active users, and during request processing
is the only time that a database connection is required. The application itself
logs into the DBMS, and handles any user account issues internally.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
iconv -f iso8859-1 -t utf-8 RELEASE-NOTES.txt > RELEASE-NOTES.txt.conv && mv -f RELEASE-NOTES.txt.conv RELEASE-NOTES.txt

%patch0

%mvn_alias : org.apache.commons:%{short_name}
%mvn_file : %{name} %{short_name}

%build
# Skip tests, tomcat:naming-java and tomcat:naming-common not available
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_20jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_19jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_12jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_10jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_10jpp7
- new version

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt2_0.r830852.4jpp6
- build w/java6

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_0.r830852.4jpp6
- new version

