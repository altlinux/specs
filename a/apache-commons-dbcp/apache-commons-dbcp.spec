Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       dbcp
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.4
Release:          alt2_10jpp7
Summary:          Apache Commons DataBase Pooling Package
Group:            Development/Java
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

# Depmap needed to remove tomcat* deps (needed only for testing)
# and fix geronimo transaction
Source1:          %{short_name}.depmap
Patch0:           jdbc41.patch
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    apache-commons-parent
BuildRequires:    apache-commons-pool
BuildRequires:    geronimo-parent-poms
BuildRequires:    jta
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven

Requires:         jpackage-utils
Requires:         apache-commons-pool

# This should go away with F-17
Provides:         jakarta-%{short_name} = 0:%{version}-%{release}
Obsoletes:        jakarta-%{short_name} < 0:1.4-1
Obsoletes:        jakarta-%{short_name}-tomcat5 < 0:1.4-1
Obsoletes:        hibernate_jdbc_cache < 0:1.4-1
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
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires:         jpackage-utils
# This should go away with F-17
Obsoletes:        jakarta-%{short_name}-javadoc < 0:1.4-1
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
iconv -f iso8859-1 -t utf-8 RELEASE-NOTES.txt > RELEASE-NOTES.txt.conv && mv -f RELEASE-NOTES.txt.conv RELEASE-NOTES.txt

%patch0

%build
# Skip tests, tomcat:naming-java and tomcat:naming-common not available
mvn-rpmbuild \
        -Dmaven.local.depmap.file="%{SOURCE1}" \
        -Dmaven.test.skip=true \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.apache.commons:%{short_name}"

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :


%files
%doc LICENSE.txt NOTICE.txt README.txt RELEASE-NOTES.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{short_name}.jar
%{_javadir}/jakarta-%{short_name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_10jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_10jpp7
- new version

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt2_0.r830852.4jpp6
- build w/java6

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_0.r830852.4jpp6
- new version

