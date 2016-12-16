Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          mybatis-parent
Version:       21
Release:       alt1_5jpp8
Summary:       The MyBatis parent POM
License:       ASL 2.0
URL:           http://www.mybatis.org/
Source0:       https://github.com/mybatis/parent/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)

BuildArch:     noarch
Source44: import.info

%description
The MyBatis parent POM which has to be inherited by all MyBatis modules.

%prep
%setup -q -n parent-%{name}-%{version}
# require com.github.stephenc.wagon:wagon-gitsite:0.4.1
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin
# unavailable plugins
%pom_remove_plugin org.apache.maven.plugins:maven-pdf-plugin
%pom_remove_plugin org.sonatype.plugins:jarjar-maven-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-maven-plugin
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin
%pom_remove_plugin org.codehaus.mojo:jdepend-maven-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin

# animal-sniffer is currently broken. it uses asm4, but asm3 is loaded
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

%pom_remove_plugin :maven-scm-plugin

# remove com.google.doclava:doclava:1.0.3
# javac.target.version is set 1.5
%pom_xpath_remove "pom:reporting/pom:plugins/pom:plugin[pom:artifactId ='maven-javadoc-plugin']/pom:configuration"
%pom_xpath_inject "pom:reporting/pom:plugins/pom:plugin[pom:artifactId ='maven-javadoc-plugin']" '
 <configuration>
  <minmemory>128m</minmemory>
  <maxmemory>1024m</maxmemory>
  <breakiterator>true</breakiterator>
  <quiet>true</quiet>
  <verbose>false</verbose>
  <source>${javac.target.version}</source>
  <linksource>true</linksource>
</configuration>'

%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-enforcer-plugin']/pom:executions/pom:execution/pom:configuration/pom:rules/pom:requirePluginVersions"

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc LICENSE NOTICE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 21-alt1_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 21-alt1_4jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 21-alt1_3jpp8
- java 8 mass update

