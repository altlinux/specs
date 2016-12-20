Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          glassfish-ejb-api
Version:       3.2
Release:       alt1_3jpp8
Summary:       Java EJB 3.2 API Design Specification
License:       CDDL or GPLv2 with exceptions
URL:           https://java.net/projects/ejb-spec/
# svn export https://svn.java.net/svn/glassfish~svn/tags/javax.ejb-api-3.2 glassfish-ejb-api-3.2
# tar cJf glassfish-ejb-api-3.2.tar.xz glassfish-ejb-api-3.2
Source0:       %{name}-%{version}.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(javax.transaction:javax.transaction-api)
BuildRequires: mvn(javax.xml.rpc:javax.xml.rpc-api)
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.glassfish:legal)
BuildRequires: mvn(org.glassfish.build:spec-version-maven-plugin)

BuildArch:     noarch
Source44: import.info

%description
Project GlassFish Enterprise JavaBean API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :glassfishbuild-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin

%pom_xpath_remove "pom:Embed-Dependency"

# fix build failure. 'useDefaultManifestFile' has been removed from the maven-jar-plugin >= 3.0.0
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration/pom:useDefaultManifestFile"
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration" '
<archive>
  <manifestFile>${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
</archive>'

%mvn_file : %{name}

%build

%mvn_build

cp -p target/classes/META-INF/LICENSE.txt .
sed -i 's/\r//' LICENSE.txt

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_3jpp8
- new version

