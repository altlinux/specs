Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             solr3
Version:          3.6.2
Release:          alt1_19jpp8
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

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(com.google.guava:guava:20.0)
BuildRequires:  mvn(com.ibm.icu:icu4j)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-fileupload:commons-fileupload)
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(jakarta-regexp:jakarta-regexp)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpmime)
BuildRequires:  mvn(org.apache.lucene:lucene-analyzers:3.6.2)
BuildRequires:  mvn(org.apache.lucene:lucene-core:3.6.2)
BuildRequires:  mvn(org.apache.lucene:lucene-grouping:3.6.2)
BuildRequires:  mvn(org.apache.lucene:lucene-highlighter:3.6.2)
BuildRequires:  mvn(org.apache.lucene:lucene-icu:3.6.2)
BuildRequires:  mvn(org.apache.lucene:lucene-kuromoji:3.6.2)
BuildRequires:  mvn(org.apache.lucene:lucene-memory:3.6.2)
BuildRequires:  mvn(org.apache.lucene:lucene-misc:3.6.2)
BuildRequires:  mvn(org.apache.lucene:lucene-phonetic:3.6.2)
BuildRequires:  mvn(org.apache.lucene:lucene-queries:3.6.2)
BuildRequires:  mvn(org.apache.lucene:lucene-smartcn:3.6.2)
BuildRequires:  mvn(org.apache.lucene:lucene-solr-grandparent:pom:3.6.2)
BuildRequires:  mvn(org.apache.lucene:lucene-spatial:3.6.2)
BuildRequires:  mvn(org.apache.lucene:lucene-spellchecker:3.6.2)
BuildRequires:  mvn(org.apache.lucene:lucene-stempel:3.6.2)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)

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

mkdir -p parent
mv solr/* .
rm -rf solr

cp %{SOURCE1} parent/pom.xml

# Gmaven is retired
%pom_remove_plugin ":gmaven-plugin" parent/pom.xml
# Make it build
%pom_remove_plugin ":maven-enforcer-plugin" parent/pom.xml
%pom_remove_plugin ":buildnumber-maven-plugin" parent/pom.xml

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

%files -f .mfiles
%doc README.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_19jpp8
- new version

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_17jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_15jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_13jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_12jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_11jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_10jpp8
- java 8 mass update

