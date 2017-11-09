Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.1.0
%global namedreltag .RELEASE
%global namedversion %{version}%{?namedreltag}
%global oname spring-plugin
Name:          springframework-plugin
Version:       1.1.0
Release:       alt1_8jpp8
Summary:       Simple plugin infrastructure
License:       ASL 2.0
URL:           https://github.com/SpringSource/spring-plugin
Source0:       https://github.com/spring-projects/spring-plugin/archive/%{namedversion}.tar.gz
# https://github.com/spring-projects/spring-plugin/issues/12
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.hamcrest:hamcrest-library)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.springframework:spring-aop)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-test)

BuildArch:     noarch
Source44: import.info

%description
Spring Plugin provides a more pragmatic approach to plugin
development by providing the core flexibility of having
plugin implementations extending a core system's functionality
but of course not delivering core OSGi features like dynamic
class loading or run-time installation and deployment of plugins.
Although Spring Plugin thus is not nearly as powerful as OSGi,
it servers poor man's requirements to build a modular extensible
application.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{namedversion}

%pom_remove_plugin :com.springsource.bundlor.maven
%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"

for p in core metadata; do
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>" ${p}
done

%pom_add_plugin org.apache.felix:maven-bundle-plugin . '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>${project.artifactId}</Bundle-SymbolicName>
    <Bundle-Name>${project.name}</Bundle-Name>
    <Bundle-Vendor>SpringSource, a division of VMware</Bundle-Vendor>
    <Bundle-Version>${project.version}</Bundle-Version>
    <Bundle-RequiredExecutionEnvironment>J2SE-1.6</Bundle-RequiredExecutionEnvironment>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

%mvn_file :%{oname}-core %{oname}-core
%mvn_file :%{oname}-metadata %{oname}-metadata

%build
# Problem with new cglib: NoSuchFieldError: HASH_ASM_TYPE
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
%doc README.markdown

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_6jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_4jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_3jpp8
- new version

