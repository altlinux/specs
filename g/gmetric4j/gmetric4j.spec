Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          gmetric4j
Version:       1.0.10
Release:       alt1_8jpp8
Summary:       JVM instrumentation to Ganglia
License:       BSD
URL:           https://github.com/ganglia/gmetric4j
Source0:       https://github.com/ganglia/gmetric4j/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.acplt.remotetea:remotetea-oncrpc)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: xmvn

BuildArch:     noarch
Source44: import.info

%description
Gmetric4j is a 100% java, configurable Ganglia agent that
periodically polls arbitrary attributes and reports their
values to Ganglia.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
find . -name "*.class" -delete
find . -name "*.jar" -type f -delete

%pom_remove_plugin :maven-jar-plugin
%pom_add_plugin "org.apache.maven.plugins:maven-jar-plugin:2.4" . '
<executions>
  <execution>
    <goals>
      <goal>test-jar</goal>
    </goals>
  </execution>
</executions>'

%pom_remove_plugin :maven-javadoc-plugin
# disable source jar
%pom_remove_plugin :maven-source-plugin

%pom_xpath_inject "pom:plugin[pom:artifactId ='maven-bundle-plugin']/pom:configuration/pom:instructions" "
 <Can-Redefine-Classes>false</Can-Redefine-Classes>"

rm src/main/resources/META-INF/MANIFEST.MF

rm -r src/test/java/info/ganglia/gmetric4j/gmetric/GMetricIT.java

%mvn_file : %{name}
%mvn_package :%{name}::tests:

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc --no-dereference COPYING

%files javadoc -f .mfiles-javadoc
%doc --no-dereference COPYING

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_3jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_2jpp8
- new version

