Epoch: 0
Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           json-lib
Version:        2.3
Release:        alt2_12jpp7
Summary:        JSON library for Java
License:        ASL 2.0
URL:            http://json-lib.sourceforge.net/
# NOTE: newer release (> 2.4) is available here https://github.com/aalmiray/Json-lib/
# A plain jarball with the source is provided by upstream.  We could use
# it, but we choose to build with maven for the sake of consistency.
# Therefore we pull the tree with maven metadata from VCS.
# cvs -d:pserver:anonymous@json-lib.cvs.sourceforge.net:/cvsroot/json-lib login
# cvs -z3 -d:pserver:anonymous@json-lib.cvs.sourceforge.net:/cvsroot/json-lib co -r REL_2_3 -d json-lib-2.3 -P json-lib
# tar czf json-lib-2.3.tar.gz --exclude CVS json-lib-2.3
Source0:        %{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}-antrun-plugin.patch

# compile dep
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.sf.ezmorph:ezmorph)
BuildRequires:  mvn(org.codehaus.groovy:groovy)
BuildRequires:  mvn(oro:oro)
BuildRequires:  mvn(xom:xom)
# runtime deps
BuildRequires:  mvn(log4j:log4j)

# test deps
BuildRequires:  mvn(xmlunit:xmlunit)

BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  maven-surefire-provider-junit

BuildRequires:  maven-antrun-plugin
# antrun-plugin deps for groovy ant task
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(asm:asm-all)
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(org.slf4j:slf4j-nop)

BuildArch:      noarch
Source44: import.info

%description
JSON-lib is a java library for transforming beans, maps, collections, java
arrays and XML to JSON and back again to beans and DynaBeans.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q

# Not strictly needed, but it makes no harm to be on the safe side
find -name '*.jar' -delete 
find -name '*.class' -delete

%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:groupId = 'org.codehaus.groovy']/pom:artifactId" groovy
%pom_remove_dep :jruby

%pom_remove_plugin :maven-compiler-plugin
%pom_remove_plugin :gmaven-plugin

%pom_xpath_remove "pom:project/pom:prerequisites"
%pom_xpath_remove "pom:project/pom:reporting"

# compile: src/main/groovy/net/sf/json/groovy/GJson.groovy
#          src/main/jdk15/net/sf/json/util/EnumMorpher.java
%patch0 -p0

# error: duplicate class
rm -r src/main/jdk15/net/sf/json/JSON*.java \
 src/main/jdk15/net/sf/json/util/JSONUtils.java
%pom_add_plugin org.apache.maven.plugins:maven-javadoc-plugin . '
<configuration>
  <charset>UTF-8</charset>
  <docencoding>UTF-8</docencoding>
  <sourcepath>${basedir}/src/main</sourcepath>
</configuration>'

# should be removed from distribution
%pom_remove_dep :commons-httpclient

%build

%mvn_file : %{name}
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_12jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_10jpp7
- new release

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_8jpp7
- fc update

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_5jpp7
- fixed build

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_5jpp7
- fc version

* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_1jpp6
- new version

