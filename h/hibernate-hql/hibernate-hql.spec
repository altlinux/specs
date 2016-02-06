Name: hibernate-hql
Version: 1.0.0
Summary: Hibernate Query Parser
License: LGPLv2 and ASL 2.0
Url: https://github.com/hibernate/hibernate-hql-parser
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: hibernate-hql = 1.0.0-0.4.Alpha6.fc21
Provides: mvn(org.hibernate.hql:hibernate-hql-lucene) = 1.0.0.Alpha6
Provides: mvn(org.hibernate.hql:hibernate-hql-lucene:pom:) = 1.0.0.Alpha6
Provides: mvn(org.hibernate.hql:hibernate-hql-parent:pom:) = 1.0.0.Alpha6
Provides: mvn(org.hibernate.hql:hibernate-hql-parser) = 1.0.0.Alpha6
Provides: mvn(org.hibernate.hql:hibernate-hql-parser:pom:) = 1.0.0.Alpha6
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.antlr:antlr-runtime)
Requires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.0-api)
Requires: mvn(org.hibernate:hibernate-search-engine)
Requires: mvn(org.jboss.logging:jboss-logging)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: hibernate-hql-1.0.0-0.4.Alpha6.fc21.cpio

%description
Experimental new parser for HQL and JP-QL queries, to convert these into SQL
and other different targets such as Lucene queries, Map/Reduce queries for
NoSQL stores, make it possible to perform more sophisticated SQL
transformations.

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

