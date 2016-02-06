Name: hibernate-search
Version: 4.5.1
Summary: Hibernate Search
License: LGPLv2+
Url: http://search.hibernate.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: hibernate-search = 4.5.1-5.fc23
Provides: mvn(org.hibernate:hibernate-search-analyzers) = 4.5.1.Final
Provides: mvn(org.hibernate:hibernate-search-analyzers:pom:) = 4.5.1.Final
Provides: mvn(org.hibernate:hibernate-search-build-config) = 4.5.1.Final
Provides: mvn(org.hibernate:hibernate-search-build-config:pom:) = 4.5.1.Final
Provides: mvn(org.hibernate:hibernate-search-engine) = 4.5.1.Final
Provides: mvn(org.hibernate:hibernate-search-engine:pom:) = 4.5.1.Final
Provides: mvn(org.hibernate:hibernate-search-infinispan) = 4.5.1.Final
Provides: mvn(org.hibernate:hibernate-search-infinispan:pom:) = 4.5.1.Final
Provides: mvn(org.hibernate:hibernate-search-orm) = 4.5.1.Final
Provides: mvn(org.hibernate:hibernate-search-orm:pom:) = 4.5.1.Final
Provides: mvn(org.hibernate:hibernate-search-parent:pom:) = 4.5.1.Final
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.puppycrawl.tools:checkstyle)
Requires: mvn(junit:junit)
Requires: mvn(org.apache.avro:avro)
Requires: mvn(org.apache.lucene:lucene-analyzers:3)
Requires: mvn(org.apache.lucene:lucene-core:3)
Requires: mvn(org.apache.lucene:lucene-facet:3)
Requires: mvn(org.apache.solr:solr-analysis-extras:3)
Requires: mvn(org.apache.tika:tika-core)
Requires: mvn(org.hibernate.common:hibernate-commons-annotations)
Requires: mvn(org.hibernate:hibernate-core)
Requires: mvn(org.infinispan:infinispan-lucene-directory)
Requires: mvn(org.jboss.logging:jboss-logging)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: hibernate-search-4.5.1-5.fc23.cpio

%description
Full text search engines like Apache Lucene are very powerful technologies to
add efficient free text search capabilities to applications. However, Lucene
suffers several mismatches when dealing with object domain models. Amongst
other things indexes have to be kept up to date and mismatches between index
structure and domain model as well as query mismatches have to be avoided.

Hibernate Search addresses these shortcomings - it indexes your domain model
with the help of a few annotations, takes care of database/index
synchronization and brings back regular managed objects from free text queries.

Hibernate Search is using Apache Lucene under the cover.

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 4.5.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

