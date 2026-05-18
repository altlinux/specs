Name:           sisu
Epoch:          2
Version:        0.9.0.M3
Release:        alt2

Summary:        Eclipse dependency injection framework
# sisu is EPL-1.0, the bundled asm is BSD
License:        EPL-1.0 and BSD
Group:          Development/Java
URL:            https://eclipse.org/sisu/
VCS:            https://github.com/eclipse-sisu/sisu-project

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires:  mvn(com.google.inject.extensions:guice-servlet)
Buildrequires:  mvn(org.testng:testng)
BuildRequires:  mvn(com.google.inject.extensions:guice-assistedinject)
BuildRequires:  mvn(cglib:cglib)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(javax.enterprise:cdi-api)

BuildArch:      noarch

%description
Java dependency injection framework with backward support for plexus and bean
style dependency injection.

%javadoc_package

%package        maven-plugin
Summary:        Sisu plugin for Apache Maven
Group:          Development/Java
Obsoletes:      sisu-mojos < 1:0.9.0~M3

%description    maven-plugin
The Sisu Plugin for Maven provides mojos to generate
META-INF/sisu/javax.inject.Named index files for the Sisu container.

%prep
%setup

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin -r :maven-clean-plugin

find . -name pom.xml -type f -exec sed -i '/<classifier>classes<\/classifier>/d' {} +

%mvn_alias :org.eclipse.sisu.inject :::no_asm:
%mvn_alias :org.eclipse.sisu.plexus org.sonatype.sisu:sisu-inject-plexus org.codehaus.plexus:plexus-container-default

%mvn_package :sisu-maven-plugin maven-plugin

%build
%mvn_build -f

%install
%mvn_install
ln -s sisu/org.eclipse.sisu.inject.jar %buildroot%_javadir/org.eclipse.sisu.inject.jar
ln -s sisu/org.eclipse.sisu.plexus.jar %buildroot%_javadir/org.eclipse.sisu.plexus.jar
echo %_javadir/org.eclipse.sisu.inject.jar >> .mfiles
echo %_javadir/org.eclipse.sisu.plexus.jar >> .mfiles

%files -f .mfiles
%doc LICENSE.txt README.md

%files maven-plugin -f .mfiles-maven-plugin

%changelog
* Sun May 17 2026 Evgeniy Serov <scala@altlinux.org> 2:0.9.0.M3-alt2
- Fixed FTBFS: added missing dependency.

* Sat Mar 30 2026 Evgeniy Serov <scala@altlinux.org> 2:0.9.0.M3-alt1
- Updated to 0.9.0.M3.

* Mon Apr 17 2023 Igor Vlasenko <viy@altlinux.org> 2:0.3.5-alt1_2jpp11
- update

* Sun Jul 10 2022 Igor Vlasenko <viy@altlinux.org> 2:0.3.4-alt2_7jpp11
- added proper Obsoletes/Confilcts:

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 2:0.3.4-alt1_7jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2:0.3.4-alt1_3jpp11
- new version

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 2:0.3.3-alt1_8jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 2:0.3.3-alt1_7jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 2:0.3.3-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 2:0.3.3-alt1_2jpp8
- new version

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 2:0.3.2-alt1_7jpp8
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt1_6jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

