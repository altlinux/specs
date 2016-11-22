Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          gmetric4j
Version:       1.0.10
Release:       alt1_3jpp8
Summary:       JVM instrumentation to Ganglia
License:       BSD
URL:           https://github.com/ganglia/gmetric4j
Source0:       https://github.com/ganglia/gmetric4j/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.acplt.remotetea:remotetea-oncrpc)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

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

# disable javadoc jar
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"
%pom_xpath_inject "pom:plugin[pom:artifactId ='maven-javadoc-plugin']" '
 <configuration>
   <doctitle>Gmetric4j ${project.version} API</doctitle>
   <windowtitle>Gmetric4j ${project.version} API</windowtitle>
</configuration>'
# disable source jar
%pom_remove_plugin :maven-source-plugin

sed -i '/Class-Path/d' src/main/resources/META-INF/MANIFEST.MF

rm -r src/test/java/info/ganglia/gmetric4j/gmetric/GMetricIT.java

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

install -m 644 target/%{name}-%{version}-tests.jar \
  %{buildroot}%{_javadir}/%{name}-tests.jar

%files -f .mfiles
%{_javadir}/%{name}-tests.jar
%doc README
%doc COPYING

%files javadoc -f .mfiles-javadoc
%doc COPYING

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_3jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_2jpp8
- new version

