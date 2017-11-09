Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          tiger-types
Version:       2.2
Release:       alt1_4jpp8
Summary:       Type arithmetic library for Java5
License:       CDDL or GPLv2 with exceptions
Url:           https://github.com/kohsuke/tiger-types
Source0:       https://github.com/kohsuke/%{name}/archive/%{name}-%{version}.tar.gz
# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# tiger-types package don't include the license file
Source1:       glassfish-LICENSE.txt

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:     noarch
Source44: import.info

%description
Tiger-types is a type arithmetic library for Java5.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
# add OSGi support required by glassfish hk2
%pom_add_plugin org.apache.felix:maven-bundle-plugin . '
<configuration>
  <instructions>
      <Embed-Dependency>*;scope=provided;inline=true</Embed-Dependency>
      <Export-Package>org.jvnet.tiger_types.*</Export-Package>
  </instructions>
  <unpackBundle>true</unpackBundle>
</configuration>
<executions>
  <execution>
      <id>osgi-bundle</id>
      <phase>package</phase>
      <goals>
          <goal>bundle</goal>
      </goals>
  </execution>
</executions>'

# not needed
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-site-plugin
%pom_xpath_remove "pom:build/pom:extensions"


%mvn_file :%{name} %{name}

cp -p %{SOURCE1} LICENSE.txt
sed -i 's/\r//' LICENSE.txt

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_2jpp8
- new fc release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_1jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_8jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_8jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_3jpp7
- new release

