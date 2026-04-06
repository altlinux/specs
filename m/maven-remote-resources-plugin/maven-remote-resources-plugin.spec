Name:           maven-remote-resources-plugin
Version:        3.3.0
Release:        alt1

Summary:        Apache Maven Remote Resources Plugin
License:        Apache-2.0
Group:          Development/Java
URL:            http://maven.apache.org/plugins/maven-remote-resources-plugin/
VCS:            https://github.com/apache/maven-remote-resources-plugin

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-resources)
BuildRequires:  mvn(org.apache.velocity:velocity-engine-core)
BuildRequires:  mvn(org.apache.maven.shared:maven-verifier)

BuildArch:      noarch

%description
Process resources packaged in JARs that have been deployed to
a remote repository. The primary use case being satisfied is
the consistent inclusion of common resources in a large set of
projects. Maven projects at Apache use this plug-in to satisfy
licensing requirements at Apache where each project much include
license and notice files for each release.

%javadoc_package

%prep
%setup

%pom_remove_parent
%pom_xpath_inject pom:project "<groupId>org.apache.maven.plugins</groupId>"

%pom_remove_plugin :maven-dependency-plugin

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Thu Mar 19 2026 Evgeniy Serov <scala@altlinux.org> 3.3.0-alt1
- Updated to 3.3.0.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.7.0-alt1_7jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.7.0-alt1_3jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_6jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_4jpp8
- new version

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1jpp8
- unbootstrap build

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_13jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_11jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_10jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_5jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_4jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_2jpp7
- fixed build

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_2jpp7
- new release

* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_4jpp7
- new version

