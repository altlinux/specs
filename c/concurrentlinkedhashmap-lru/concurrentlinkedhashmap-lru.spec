Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          concurrentlinkedhashmap-lru
Version:       1.4.2
Release:       alt1_3jpp8
Summary:       A ConcurrentLinkedHashMap for Java
License:       ASL 2.0
Url:           https://github.com/ben-manes/concurrentlinkedhashmap
Source0:       https://github.com/ben-manes/concurrentlinkedhashmap/archive/%{name}-%{version}.tar.gz

# test deps
%if 0
BuildRequires: mvn(com.github.stephenc.high-scale-lib:high-scale-lib)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(net.sf.ehcache:ehcache)
BuildRequires: mvn(org.hamcrest:hamcrest-library) >= 1.3
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.testng:testng)
# unavailable test deps
BuildRequires: mvn(com.google.caliper:caliper)
BuildRequires: mvn(com.jayway.awaitility:awaitility)
# require cache-benchmark == r7903 from http://sourceforge.net/projects/cachebenchfwk/
BuildRequires: mvn(org.cachebench:cache-benchmark)
%endif

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-site-plugin

BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(com.google.code.findbugs:jsr305)

BuildArch:     noarch
Source44: import.info

%description
A high performance version of java.util.LinkedHashMap
for use as a software cache.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n concurrentlinkedhashmap-%{name}-%{version}
find . -name "*.class" -delete
find . -name "*.jar" -type f -print -delete

# Unavailable
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :taglist-maven-plugin
%pom_remove_plugin :emma-maven-plugin

# Unwanted
%pom_remove_plugin :maven-source-plugin

# Remove org.jvnet.wagon-svn:wagon-svn
%pom_xpath_remove "pom:build/pom:extensions"

%pom_xpath_remove "pom:dependencies/pom:dependency[pom:scope='test']"

# Fix http://jira.codehaus.org/browse/MCOMPILER-130
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:compilerArgument"
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration" "
<compilerArgument>-Werror</compilerArgument>"
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration" "
<compilerArgument>-Xlint:all</compilerArgument>"

# remove bundled Doug Lea JCP JSR-166
rm -r src/main/java/com/googlecode/concurrentlinkedhashmap/ConcurrentHashMapV8.java
sed -i "s|ConcurrentHashMapV8|java.util.concurrent.ConcurrentHashMap|" \
 src/main/java/com/googlecode/concurrentlinkedhashmap/ConcurrentLinkedHashMap.java

# Fix mojo-signatures aId
#sed -i "s|jdk.version}-sun</artifactId>|jdk.version}</artifactId>|" pom.xml
# Disabled currently is broken
%pom_remove_plugin :animal-sniffer-maven-plugin

%mvn_file :%{name} %{name}

%build

# test skipped for unavailable test deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1_2jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_1jpp7
- new release

