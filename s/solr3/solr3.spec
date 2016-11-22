Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             solr3
Version:          3.6.2
Release:          alt1_11jpp8
Summary:          Apache Solr
License:          ASL 2.0
Url:              http://lucene.apache.org/solr/

# wget http://archive.apache.org/dist/lucene/solr/3.6.2/apache-solr-3.6.2-src.tgz
# tar -xf apache-solr-3.6.2-src.tgz apache-solr-3.6.2/solr/
# rm -rf apache-solr-3.6.2/solr/lib 
# find apache-solr-3.6.2/solr/ -name "*.jar" -delete
# find apache-solr-3.6.2/solr/ -name "*.class" -delete
# tar -cvjf apache-solr-3.6.2.tar.gz apache-solr-3.6.2/solr/
Source0:          apache-solr-%{version}.tar.gz

Source1:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/apache/lucene/lucene-solr-grandparent/%{version}/lucene-solr-grandparent-%{version}.pom
Source2:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/apache/solr/solr-parent/%{version}/solr-parent-%{version}.pom
Source3:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/apache/solr/solr-core/%{version}/solr-core-%{version}.pom
Source4:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/apache/solr/solr-solrj/%{version}/solr-solrj-%{version}.pom

Source10:         https://repository.jboss.org/nexus/service/local/repositories/central/content/org/apache/solr/solr-analysis-extras/%{version}/solr-analysis-extras-%{version}.pom

Source20:         solr-contrib.pom

BuildRequires:    lucene3
BuildRequires:    lucene3-contrib
BuildRequires:    maven-local
BuildRequires:    maven-plugin-build-helper
BuildRequires:    woodstox-core
BuildRequires:    apache-commons-fileupload
BuildRequires:    icu4j
BuildRequires:    jcl-over-slf4j
# tmp, see below
BuildRequires:    xmlstarlet

BuildRequires:    regexp

BuildArch:        noarch
Source44: import.info

%description
Solr is the popular, blazing fast open source enterprise search platform from
the Apache LuceneTM project. Its major features include powerful full-text
search, hit highlighting, faceted search, near real-time indexing, dynamic
clustering, database integration, rich document (e.g., Word, PDF) handling, and
geospatial search. Solr is highly reliable, scalable and fault tolerant,
providing distributed indexing, replication and load-balanced querying,
automated failover and recovery, centralized configuration and more. Solr
powers the search and navigation features of many of the world's largest
internet sites.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
# Unpack manually only the solr directory
tar -xf %{SOURCE0} apache-solr-%{version}/solr

%setup -D -T -n apache-solr-%{version}

mkdir parent
mv solr/* .
rm -rf solr

cp %{SOURCE1} parent/pom.xml

# Gmaven is retired
%pom_remove_plugin ":gmaven-plugin" parent/pom.xml
# Make it build
%pom_remove_plugin ":maven-enforcer-plugin" parent/pom.xml

cp %{SOURCE2} pom.xml

# Make sure the relative path is valid
sed -i "s|../pom.xml|parent/pom.xml|" pom.xml

# Disable test deps
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:scope = 'test']"

# Disable modules
%pom_disable_module webapp
%pom_disable_module test-framework

# Copy POMs
cp %{SOURCE3} core/pom.xml
cp %{SOURCE4} solrj/pom.xml
cp %{SOURCE10} contrib/analysis-extras/pom.xml
cp %{SOURCE20} contrib/pom.xml

%pom_xpath_remove "pom:build/pom:directory" pom.xml
%pom_xpath_remove "pom:build/pom:directory" parent/pom.xml

for m in core contrib/analysis-extras solrj; do
%pom_xpath_remove "pom:build/pom:directory" ${m}/pom.xml
%pom_xpath_remove "pom:build/pom:outputDirectory" ${m}/pom.xml
done

# Remove Jetty support
%pom_remove_dep "org.mortbay.jetty:" core/pom.xml
rm core/src/java/org/apache/solr/client/solrj/embedded/JettySolrRunner.java

# Use proper woodstox aid
sed -i "s|wstx-asl|woodstox-core-asl|" solrj/pom.xml

%mvn_compat_version : %{version} 3

%build

%mvn_build -f

%install
%mvn_install

# Worakround for https://bugzilla.redhat.com/show_bug.cgi?id=1019670
#for aid in solr-core solr-solrj; do
#  xmlstarlet ed -L -s "dependencyMap/autoRequires[artifactId = '${aid}']" -t elem -n version -v %{version} %{buildroot}%{_mavendepmapfragdir}/solr3.xml
#done

%files -f .mfiles
%doc README.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_11jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_10jpp8
- java 8 mass update

