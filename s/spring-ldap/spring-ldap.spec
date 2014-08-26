Epoch: 0
Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          spring-ldap
Version:       1.3.1
Release:       alt2_7jpp7
Summary:       Java library for simplifying LDAP operations
License:       ASL 2.0
URL:           http://www.springframework.org/ldap
# svn export https://src.springframework.org/svn/spring-ldap/tags/spring-ldap-1.3.1.RELEASE spring-ldap-1.3.1
# tar cfJ spring-ldap-1.3.1.tar.xz spring-ldap-1.3.1
Source0:       %{name}-%{version}.tar.xz
# Don't use ldapbp.jar, as I couldn't find the source and I doubt it has a valid
# open source license:
Patch0:        %{name}-remove-ldapbp.patch
# Use Java 5 to build the core as the JavaCC generated source code uses Java 5
# features like generics and annotations:
Patch1:        %{name}-use-java-5-to-build-core.patch
# Remove the dependency on spring-orm:
Patch2:        %{name}-remove-spring-orm.patch

BuildArch:     noarch

BuildRequires: dos2unix
BuildRequires: maven-local
BuildRequires: maven-release-plugin
BuildRequires: maven-shade-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: javacc-maven-plugin
BuildRequires: springframework
BuildRequires: springframework-beans
BuildRequires: springframework-context
BuildRequires: springframework-tx
BuildRequires: springframework-jdbc
Source44: import.info

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

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep

# Unpack and patch the source:
%setup -q
# Build the core only
%pom_disable_module test-support
%pom_disable_module test
%pom_disable_module ldif
%pom_disable_module odm
# Disable the AWS extension
%pom_xpath_remove "pom:build/pom:extensions" parent
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Remove binary files:
find . -name '*.jar' -print -delete

# Fix line endings in documentation files:
dos2unix notice.txt
dos2unix license.txt
dos2unix readme.txt

%build

# Skip the tests for now, as they bring dependencies that are not available in
# the distribution right now:
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc license.txt
%doc notice.txt
%doc readme.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt
%doc notice.txt

%changelog
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

