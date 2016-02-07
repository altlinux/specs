Name: spring-ldap
Version: 1.3.1
Summary: Java library for simplifying LDAP operations
License: ASL 2.0
Url: http://www.springframework.org/ldap
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.springframework.ldap.ldif:spring-ldap-ldif:pom:) = 1.3.1.RELEASE
Provides: mvn(org.springframework.ldap:spring-ldap-core) = 1.3.1.RELEASE
Provides: mvn(org.springframework.ldap:spring-ldap-core-tiger) = 1.3.1.RELEASE
Provides: mvn(org.springframework.ldap:spring-ldap-core-tiger:pom:) = 1.3.1.RELEASE
Provides: mvn(org.springframework.ldap:spring-ldap-core:pom:) = 1.3.1.RELEASE
Provides: mvn(org.springframework.ldap:spring-ldap-ldif-batch) = 1.3.1.RELEASE
Provides: mvn(org.springframework.ldap:spring-ldap-ldif-batch:pom:) = 1.3.1.RELEASE
Provides: mvn(org.springframework.ldap:spring-ldap-ldif-core) = 1.3.1.RELEASE
Provides: mvn(org.springframework.ldap:spring-ldap-ldif-core:pom:) = 1.3.1.RELEASE
Provides: mvn(org.springframework.ldap:spring-ldap-odm) = 1.3.1.RELEASE
Provides: mvn(org.springframework.ldap:spring-ldap-odm:pom:) = 1.3.1.RELEASE
Provides: mvn(org.springframework.ldap:spring-ldap-parent-tiger:pom:) = 1.3.1.RELEASE
Provides: mvn(org.springframework.ldap:spring-ldap-parent:pom:) = 1.3.1.RELEASE
Provides: mvn(org.springframework.ldap:spring-ldap:pom:) = 1.3.1.RELEASE
Provides: spring-ldap = 1.3.1-12.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-cli:commons-cli)
Requires: mvn(commons-lang:commons-lang)
Requires: mvn(commons-logging:commons-logging)
Requires: mvn(commons-pool:commons-pool)
Requires: mvn(log4j:log4j)
Requires: mvn(org.freemarker:freemarker)
Requires: mvn(org.springframework.batch:spring-batch-core)
Requires: mvn(org.springframework.batch:spring-batch-infrastructure)
Requires: mvn(org.springframework:spring-beans)
Requires: mvn(org.springframework:spring-context)
Requires: mvn(org.springframework:spring-core)
Requires: mvn(org.springframework:spring-tx)

BuildArch: noarch
Group: Development/Java
Release: alt3jpp
Source: spring-ldap-1.3.1-12.fc23.cpio

%description
Spring LDAP is a Java library for simplifying LDAP operations, based on the
pattern of Spring's JdbcTemplate. The framework relieves the user of common
chores, such as looking up and closing contexts, looping through results,
encoding/decoding values and filters, and more. The LdapTemplate class
encapsulates all the plumbing work involved in traditional LDAP programming,
such as creating a DirContext, looping through NamingEnumerations, handling
exceptions and cleaning up resources. This leaves the programmer to handle the
important stuff - where to find data (DNs and Filters) and what do do with it
(map to and from domain objects, bind, modify, unbind, etc.), in the same way
that JdbcTemplate relieves the programmer of all but the actual SQL and how the
data maps to the domain model. In addition to this, Spring LDAP provides
transaction support, a pooling library, exception translation from
NamingExceptions to a mirrored unchecked Exception hierarchy, as well as
several utilities for working with filters, LDAP paths and Attributes.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_3jpp7
- new version

* Fri Mar 18 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt3_1jpp5
- fixed build with new javacc5

* Sun Sep 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt2_1jpp5
- fixed build with new maven 2.0.8

* Sun Mar 15 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_1jpp5
- maven 2.0.7 build

* Sat Mar 14 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt0.1jpp
maven 2.0.7 bootstrap

