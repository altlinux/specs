Name:           maven-resolver
Epoch:          1
Version:        1.9.27
Release:        alt1

License:        Apache-2.0
Summary:        Apache Maven Artifact Resolver
Group:          Development/Java
URL:            https://maven.apache.org/resolver/
VCS:            https://github.com/apache/maven-resolver

Source0:        %name-%version.tar

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server:9.4)
BuildRequires:  mvn(org.eclipse.jetty:jetty-util:9.4)
BuildRequires:  mvn(org.eclipse.jetty:jetty-http:9.4)

BuildArch:      noarch

%description
Apache Maven Artifact Resolver is a library for working with artifact
repositories and dependency resolution. Maven Artifact Resolver deals with the
specification of local repository, remote repository, developer workspaces,
artifact transports and artifact resolution.

%javadoc_package

%prep
%setup

%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :japicmp-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

%pom_disable_module maven-resolver-named-locks-hazelcast
%pom_disable_module maven-resolver-named-locks-redisson
%pom_disable_module maven-resolver-demos

%pom_xpath_set "pom:properties/pom:jettyVersion" "9.4" \
    maven-resolver-transport-http

%pom_xpath_set \
    "pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration/pom:systemPropertyVariables/pom:java.io.tmpdir" \
    "%_tmppath"

find . -name pom.xml -type f -exec sed -i '/classes<\/classifier>/d' {} +

# requires internet connection
rm maven-resolver-supplier/src/test/java/org/eclipse/aether/supplier/RepositorySystemSupplierTest.java

%mvn_alias 'org.apache.maven.resolver:maven-resolver{*}' 'org.eclipse.aether:aether@1'
%mvn_file ':maven-resolver{*}' %name/maven-resolver@1 aether/aether@1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Sun Aug 23 2026 Evgeniy Serov <scala@altlinux.org> 1:1.9.27-alt1
- Automatically updated to 1.9.27.

* Fri Aug 21 2026 Evgeniy Serov <scala@altlinux.org> 1:1.9.22-alt1
- Updated to 1.9.22.

* Mon Aug 17 2026 Evgeniy Serov <scala@altlinux.org> 1:1.9.10-alt1
- Updated to 1.9.10.

* Tue May 12 2026 Evgeniy Serov <scala@altlinux.org> 1:1.6.3-alt4
- Removed maven-enforcer-plugin from build.

* Sun Apr 05 2026 Evgeniy Serov <scala@altlinux.org> 1:1.6.3-alt3
- Cleanup spec.
- Enabled previously disabled modules.

* Tue Dec 09 2025 Anton Meleshnikov <alton@altlinux.org> 1:1.6.3-alt2
- fixed FTBFS (disabled tests)

* Fri Apr 18 2025 Anton Meleshnikov <alton@altlinux.org> 1:1.6.3-alt1
- new version

* Wed Apr 16 2025 Anton Meleshnikov <alton@altlinux.org> 1:1.6.2-alt1jpp11
- new version

* Sun Jul 10 2022 Igor Vlasenko <viy@altlinux.org> 1:1.6.1-alt2_5jpp11
- added proper Obsoletes/Confilcts:

* Wed Aug 18 2021 Igor Vlasenko <viy@altlinux.org> 1:1.6.1-alt1_5jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:1.4.2-alt1_5jpp11
- fc34 update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1:1.4.2-alt1_3jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 1:1.4.1-alt1_2jpp8
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.3.3-alt1_2jpp8
- new version

* Wed Jul 10 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.3.1-alt1_2jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.1.1-alt1_2jpp8
- java update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.1.0-alt1_2jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.1.0-alt1_1jpp8
- new version

* Sun Nov 19 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0.3-alt1_7jpp8
- new version

