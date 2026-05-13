Name:           maven-resolver
Epoch:          1
Version:        1.6.3
Release:        alt4

License:        Apache-2.0
Summary:        Apache Maven Artifact Resolver library
Group:          Development/Java
URL:            https://maven.apache.org/resolver/
VCS:            https://github.com/apache/maven-resolver
Source0:        %name-%version-source-release.zip

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default
BuildRequires:  unzip

BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)

BuildArch:      noarch

%description
Apache Maven Artifact Resolver is a library for working with artifact
repositories and dependency resolution. Maven Artifact Resolver deals with the
specification of local repository, remote repository, developer workspaces,
artifact transports and artifact resolution.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-enforcer-plugin

%pom_disable_module maven-resolver-synccontext-redisson

# generate OSGi manifests
for pom in $(find -mindepth 2 -name pom.xml) ; do
  %pom_add_plugin "org.apache.felix:maven-bundle-plugin" $pom \
  "<configuration>
    <instructions>
      <Bundle-SymbolicName>\${project.groupId}$(sed 's:./maven-resolver::;s:/pom.xml::;s:-:.:g' <<< $pom)</Bundle-SymbolicName>
      <Export-Package>!org.eclipse.aether.internal*,org.eclipse.aether*</Export-Package>
      <_nouses>true</_nouses>
    </instructions>
  </configuration>
  <executions>
    <execution>
      <id>create-manifest</id>
      <phase>process-classes</phase>
      <goals><goal>manifest</goal></goals>
    </execution>
  </executions>"
done


%mvn_alias 'org.apache.maven.resolver:maven-resolver{*}' 'org.eclipse.aether:aether@1'
%mvn_file ':maven-resolver{*}' %name/maven-resolver@1 aether/aether@1

%build
# tests are disabled cause jetty is built with 17 java
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
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

