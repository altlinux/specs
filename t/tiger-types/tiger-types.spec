Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          tiger-types
Version:       1.4
Release:       alt1_8jpp8
Summary:       Type arithmetic library for Java5
License:       CDDL or GPLv2 with exceptions
Url:           http://java.net/projects/tiger-types
# svn export https://svn.java.net/svn/tiger-types~svn/tags/tiger-types-1.4
# tar czf tiger-types-1.4-src-svn.tar.gz tiger-types-1.4
Source0:       %{name}-%{version}-src-svn.tar.gz
# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# tiger-types package don't include the license file
Source1:       glassfish-LICENSE.txt

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

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
%setup -q
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
# removed some warning
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-compiler-plugin']" "
  <groupId>org.apache.maven.plugins</groupId>
  <version>any</version>"
%pom_xpath_inject "pom:reporting/pom:plugins/pom:plugin[pom:artifactId ='maven-javadoc-plugin']" "
  <groupId>org.apache.maven.plugins</groupId>
  <version>any</version>"

# Unneeded
%pom_remove_plugin :maven-idea-plugin
%pom_remove_plugin :maven-release-plugin

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
* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_8jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_3jpp7
- new release

