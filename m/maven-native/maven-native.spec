%define version 1.0.0
%global namedreltag  %nil
%global namedversion %version%namedreltag

Name:           maven-native
Version:        1.0.0
Release:        alt4

Summary:        Compile c and c++ source under Maven
License:        Apache-2.0 and MIT
Group:          Development/Java
Url:            http://www.mojohaus.org/plugins.html
VCS:            https://github.com/mojohaus/maven-native.git
Source0:        %name-%namedversion-source-release.zip

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default
Buildrequires:  unzip

BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(bcel:bcel)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)

BuildArch:      noarch

%description
Maven Native - compile C and C++ source under Maven
with compilers such as GCC, MSVC, GCJ etc ...

%javadoc_package

%package components
Group: 	        Development/Java
Summary:        Maven Native Components

%description components
%summary.

%package -n native-maven-plugin
Group:          Development/Java
Summary:        Native Maven Plugin

%description -n native-maven-plugin
%summary.

%prep
%setup -n %name-%namedversion
%pom_add_dep org.apache.maven.plugin-tools:maven-plugin-annotations:3.9.0:compile

for d in LICENSE ; do
  iconv -f iso8859-1 -t utf-8 $d.txt > $d.txt.conv && mv -f $d.txt.conv $d.txt
  sed -i 's/\r//' $d.txt
done

%pom_remove_plugin com.github.ekryd.sortpom:sortpom-maven-plugin

%pom_remove_dep org.codehaus.mojo.natives:maven-native-mingw
%pom_remove_dep org.codehaus.mojo.natives:maven-native-mingw native-maven-plugin

%pom_add_dep org.apache.maven:maven-compat native-maven-plugin
%pom_add_dep org.apache.maven:maven-core native-maven-plugin

# missing test deps
%pom_add_dep aopalliance:aopalliance::test native-maven-plugin
%pom_add_dep net.sf.cglib:cglib::test native-maven-plugin

%mvn_package ":%name" %name
%mvn_package ":%name-api" %name
%mvn_package ":%name-components" components
%mvn_package ":%name-bcc" components
%mvn_package ":%name-generic-c" components
%mvn_package ":%name-javah" components
%mvn_package ":%name-manager" components
%mvn_package ":%name-msvc" components
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
%mvn_build -f -s

%install
%mvn_install

%files -f .mfiles-%name
%dir %_javadir/%name
%doc LICENSE.txt

%files components -f .mfiles-components
%doc LICENSE.txt

%files -n native-maven-plugin -f .mfiles-native-maven-plugin
%doc LICENSE.txt

%changelog
* Mon Jul 06 2026 Ivan A. Melnikov <iv@altlinux.org> 1.0.0-alt4
- Update to 1.0.0 release.

* Mon Mar 30 2026 Evgeniy Serov <scala@altlinux.org> 1.0-alt3
- Fix build with new sisu and plexus-containers.

* Mon Dec 08 2025 Ivan Khanas <xeno@altlinux.org> 1.0-alt2
- Return to the Sisyphus repository.

* Fri May 10 2024 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1_0.17
- rebuild with java 21.x

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.16.alpha.8jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.14.alpha.8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.13.alpha.8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.12.alpha.8jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.11.alpha.8jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.10.alpha.8jpp8
- new version

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.3.alpha.7jpp7
- new version

