# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          concurrentlinkedhashmap-lru
Version:       1.3.2
Release:       alt1_1jpp7
Summary:       A ConcurrentLinkedHashMap for Java
Group:         Development/Java
License:       ASL 2.0
Url:           http://code.google.com/p/concurrentlinkedhashmap/
# git clone https://code.google.com/p/concurrentlinkedhashmap/ concurrentlinkedhashmap-lru-1.3.2
# (cd concurrentlinkedhashmap-lru-1.3.2 && git checkout concurrentlinkedhashmap-lru-1.3.2)
# find concurrentlinkedhashmap-lru-1.3.2 -name "*.class" -delete
# find concurrentlinkedhashmap-lru-1.3.2 -name "*.jar" -type f -delete
# lib/cache-benchmark/benchmark-fwk.jar
# rm -rf concurrentlinkedhashmap-lru-1.3.2/.git
# tar czf concurrentlinkedhashmap-lru-1.3.2-src-git.tar.gz concurrentlinkedhashmap-lru-1.3.2
Source0:       %{name}-%{version}-src-git.tar.gz

BuildRequires: sonatype-oss-parent

# test deps
%if 0
BuildRequires: apache-commons-lang
BuildRequires: ehcache-core
BuildRequires: ehcache-parent
BuildRequires: guava
BuildRequires: mockito
BuildRequires: testng
BuildRequires: mvn(org.hamcrest:hamcrest-library) >= 1.3
# unavailable test deps
# require cache-benchmark == r7903 from http://sourceforge.net/projects/cachebenchfwk/
BuildRequires: mvn(org.cachebench:cache-benchmark)
BuildRequires: mvn(com.google.caliper:caliper)
# https://bugzilla.redhat.com/show_bug.cgi?id=865893
BuildRequires: mvn(com.github.stephenc.high-scale-lib:high-scale-lib)
BuildRequires: mvn(com.jayway.awaitility:awaitility)
%endif
# com.google.code.findbugs:jsr305:2.0.1 scope: provided
BuildRequires: jsr-305

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-site-plugin
#BuildRequires: animal-sniffer
#BuildRequires: mojo-signatures

BuildArch:     noarch
Source44: import.info

%description
A high performance version of java.util.LinkedHashMap
for use as a software cache.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

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

# Fix mojo-signatures aId
sed -i "s|jdk.version}-sun</artifactId>|jdk.version}</artifactId>|" pom.xml
# Disabled currently is broken
%pom_remove_plugin :animal-sniffer-maven-plugin

%build

# test skipped for unavailable test deps
mvn-rpmbuild -Dmaven.test.skip=true package javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc README

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_1jpp7
- new release

