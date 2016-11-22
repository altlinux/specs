Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name maven-native
%define version 1.0
%global namedreltag  -alpha-8
%global namedversion %{version}%{?namedreltag}
%global dotreltag    %(echo %{namedreltag} | tr - .)

Name:          maven-native
Version:       1.0
Release:       alt1_0.11.alpha.8jpp8
Summary:       Compile c and c++ source under Maven
License:       ASL 2.0 and MIT
Url:           http://www.mojohaus.org/plugins.html
# Source code available @ https://github.com/mojohaus/maven-native
Source0:       http://repo2.maven.org/maven2/org/codehaus/mojo/natives/%{name}/%{namedversion}/%{name}-%{namedversion}-source-release.zip

BuildRequires: maven-local
BuildRequires: mojo-parent
BuildRequires: mvn(aopalliance:aopalliance)
BuildRequires: mvn(bcel:bcel)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.sf.cglib:cglib)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires: mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-api)
BuildRequires: mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch:     noarch
Source44: import.info

%description
Maven Native - compile C and C++ source under Maven
with compilers such as GCC, MSVC, GCJ etc ...

%package components
Group: Development/Java
Summary:       Maven Native Components

%description components
%{summary}.

%package -n native-maven-plugin
Group: Development/Java
Summary:       Native Maven Plugin

%description -n native-maven-plugin
%{summary}.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

for d in LICENSE ; do
  iconv -f iso8859-1 -t utf-8 $d.txt > $d.txt.conv && mv -f $d.txt.conv $d.txt
  sed -i 's/\r//' $d.txt
done

# use jvm apis
%pom_remove_dep backport-util-concurrent:backport-util-concurrent
%pom_remove_dep backport-util-concurrent:backport-util-concurrent maven-native-api
sed -i "s|edu.emory.mathcs.backport.java.util.concurrent|java.util.concurrent|" \
 maven-native-api/src/main/java/org/codehaus/mojo/natives/compiler/AbstractCompiler.java

sed -i 's|<artifactId>maven-project|<artifactId>maven-compat|' pom.xml
%pom_remove_dep :maven-project native-maven-plugin
%pom_add_dep org.apache.maven:maven-compat native-maven-plugin
%pom_add_dep org.apache.maven:maven-core native-maven-plugin

# missing test deps
%pom_add_dep aopalliance:aopalliance::test native-maven-plugin
%pom_add_dep net.sf.cglib:cglib::test native-maven-plugin

%mvn_package ":%{name}" %{name}
%mvn_package ":%{name}-api" %{name}
%mvn_package ":%{name}-components" components
%mvn_package ":%{name}-bcc" components
%mvn_package ":%{name}-generic-c" components
%mvn_package ":%{name}-javah" components
%mvn_package ":%{name}-manager" components
%mvn_package ":%{name}-msvc" components
%mvn_package ":native-maven-plugin" native-maven-plugin

%build

#  junit.framework.AssertionFailedError: Failed to create plexus container.
# native-maven-plugin with maven3 test failures:
# Caused by: java.lang.ClassNotFoundException: org.apache.maven.artifact.repository.Authentication
#  java.lang.VerifyError: (class: org/apache/maven/project/MavenProject, 
# method: getSnapshotArtifactRepository signature: ()Lorg/apache/maven/artifact/repository/ArtifactRepository;)
# Incompatible argument to function
# force org.codehaus.plexus plexus-container-default 1.5.5 apis
# test skipped cause: [ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.15:test (default-test) on project native-maven-plugin: Execution default-test of goal org.apache.maven.plugins:maven-surefire-plugin:2.15:test failed: There was an error in the forked process
# [ERROR] java.lang.NoClassDefFoundError: org/sonatype/aether/RepositorySystemSession
%mvn_build -f -s -- -Dmojo.java.target=1.7 -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles-%{name}
%dir %{_javadir}/%{name}
%doc LICENSE.txt

%files components -f .mfiles-components
%doc LICENSE.txt

%files -n native-maven-plugin -f .mfiles-native-maven-plugin
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.11.alpha.8jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.10.alpha.8jpp8
- new version

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.3.alpha.7jpp7
- new version

