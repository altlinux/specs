%{!?runselftest:%global runselftest 0}

Name:		postgresql-jdbc
Version:	42.7.10
Release:	alt1

Summary:        JDBC driver for PostgreSQL
License:	BSD-2-Clause
Group:          Databases
URL:		http://jdbc.postgresql.org/

Source0:	postgresql-%version-jdbc-src.tar.gz

Provides:	pgjdbc = %version-%release

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(com.ongres.scram:scram-client)

BuildArch:      noarch

%if %runselftest
BuildRequires:	postgresql15-server
BuildRequires:	postgresql-test-rpm-macros
%endif

%description
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-jdbc package includes the .jar files needed for
Java programs to access a PostgreSQL database.

%javadoc_package

%prep
%setup -c

mv postgresql-%{version}-jdbc-src/* .

# remove any binary libs
find -type f \( -name "*.jar" -or -name "*.class" \) | xargs rm -f

# compat symlink: requested by dtardon (libreoffice), reverts part of
# 0af97ce32de877 commit.
%mvn_file org.postgresql:postgresql %name/postgresql %name postgresql

%mvn_alias org.postgresql:postgresql postgresql:postgresql

%build
# Include PostgreSQL testing methods and variables.
%if %runselftest
%postgresql_tests_init

PGTESTS_LOCALE=C.UTF-8

cat <<EOF > build.local.properties
server=localhost
port=$PGTESTS_PORT
database=test
username=test
password=test
privilegedUser=$PGTESTS_ADMIN
privilegedPassword=$PGTESTS_ADMINPASS
preparethreshold=5
loglevel=0
protocolVersion=0
EOF

# Start the local PG cluster.
%postgresql_tests_start
%else
# -f is equal to -Dmaven.test.skip=true
opts="-f"
%endif

%mvn_build $opts --xmvn-javadoc

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README.md

%changelog
* Mon Apr 06 2026 Evgeniy Serov <scala@altlinux.org> 42.7.10-alt1
- Updated to 42.7.10.

* Sat Nov 30 2024 Andrey Cherepanov <cas@altlinux.org> 0:42.6.2-alt1
- New version.
- Securiry fix: CVE-2024-1597 (ALT #51910).

* Mon Apr 17 2023 Igor Vlasenko <viy@altlinux.org> 0:42.6.0-alt1_1jpp11
- update

* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 0:42.3.1-alt1_3jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:42.2.18-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:42.2.16-alt1_1jpp8
- new version

* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 0:42.2.5-alt1_2jpp8
- new version

* Sat Jun 02 2018 Igor Vlasenko <viy@altlinux.ru> 0:42.2.2-alt1_4jpp8
- fc28+ update

* Wed May 16 2018 Igor Vlasenko <viy@altlinux.ru> 0:42.2.1-alt1_2jpp8
- java fc28 update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:42.1.4-alt1_1jpp8
- new version

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0:9.4.1212-alt1_4jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:9.4.1200-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:9.4.1200-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:9.2.1002-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:9.2.1002-alt1_2jpp7
- new release

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:9.2.1002-alt1_1jpp7
- fc update

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:9.1.902-alt1_1jpp7
- new version

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:9.1.901-alt1_1jpp6
- update to new release by jppimport

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:9.0.801-alt1_1jpp6
- new jpp release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:8.3.604-alt1_1jpp5
- new jpackage release

* Fri Nov 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:8.1.407-alt1_2jpp1.7
- converted from JPackage by jppimport script

