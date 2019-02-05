Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          forbidden-apis
Version:       2.5
Release:       alt1_2jpp8
Summary:       Policeman's Forbidden API Checker
License:       ASL 2.0
URL:           https://github.com/policeman-tools/forbidden-apis
Source0:       https://github.com/policeman-tools/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Avoid bundling deps
Patch0:        avoid-jarjar-bundling.patch

# Port to latest versions of gradle and maven in Fedora
Patch1:        fix-gradle-maven-build.patch

BuildArch:     noarch

BuildRequires: gradle-local
BuildRequires: ivy-local
BuildRequires: maven-local
BuildRequires: ant
BuildRequires: ant-antunit
BuildRequires: ant-contrib
BuildRequires: ant-junit
BuildRequires: objectweb-asm
BuildRequires: plexus-utils
BuildRequires: maven-plugin-plugin
BuildRequires: sonatype-oss-parent
Source44: import.info

%description
Allows to parse Java byte code to find invocations of method/class/field
signatures and fail build (Apache Ant, Apache Maven, or Gradle).

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q
%patch0
%patch1

find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete

# Use system ivy settings
sed -i -e '/ivy:configure/d' build.xml

# Can't use missing maven-ant-tasks
%pom_xpath_remove "target/artifact:pom" build.xml
%pom_xpath_remove "target/artifact:mvn" build.xml
%pom_xpath_remove "target/artifact:install" build.xml
%pom_xpath_inject "target[@name='maven-descriptor']" \
"<exec executable='xmvn'>
  <arg value=\"-o\"/>
  <arg value=\"-f\"/>
  <arg value=\"\${maven-build-dir}/pom-build.xml\"/>
  <arg value=\"plugin:helpmojo\"/>
  <arg value=\"plugin:descriptor\"/>
  <arg value=\"plugin:report\"/>
  <arg value=\"-Dinjected.src.dir=src/main/java\"/>
  <arg value=\"-Dinjected.output.dir=../../build/main\"/>
  <arg value=\"-Dinjected.build.dir=\${maven-build-dir}\"/>
  <arg value=\"-Dinjected.maven-plugin-plugin.version=\${maven-plugin-plugin.version}\"/>
</exec>" build.xml
sed -i -e '/maven-ant-tasks/d' ivy.xml
sed -i -e '/uri="antlib:org.apache.maven.artifact.ant/d' build.xml

# Don't need to run RAT for RPM builds
sed -i -e '/apache-rat/d' ivy.xml
sed -i -e '/uri="antlib:org.apache.rat.anttasks/d' build.xml

%build
ant -Divy.mode=local jar documentation test-junit

%install
# Add deps on unbundled jars, taken from ivy.xml
%pom_add_dep org.apache.ant:ant:1.7.0:provided build/maven/pom-deploy.xml
%pom_add_dep org.ow2.asm:asm:6.1.1 build/maven/pom-deploy.xml
%pom_add_dep org.ow2.asm:asm-commons:6.1.1 build/maven/pom-deploy.xml
%pom_add_dep org.codehaus.plexus:plexus-utils:1.1 build/maven/pom-deploy.xml
%pom_add_dep commons-cli:commons-cli:1.3.1 build/maven/pom-deploy.xml

# Install maven artifacts
%mvn_artifact build/maven/pom-deploy.xml dist/forbiddenapis-2.5.jar
%mvn_install -J build/docs

# Install ant configuration
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "%{name} ant apache-commons-cli objectweb-asm/asm objectweb-asm/asm-commons plexus/utils" > %{name}-ant
install -pm 644 %{name}-ant %{buildroot}%{_sysconfdir}/ant.d/%{name}

%files -f .mfiles
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%doc --no-dereference LICENSE.txt NOTICE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_2jpp8
- fc29 update

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_1jpp8
- java update

* Tue Nov 07 2017 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_3jpp8
- fixed build

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_3jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_2jpp8
- java 8 mass update

