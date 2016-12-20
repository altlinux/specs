Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          glassfish-jaxrpc-api
Version:       1.1.1
Release:       alt1_3jpp8
Summary:       The Java API for XML-Based RPC (JAX-RPC)
License:       CDDL or GPLv2 with exceptions
URL:           https://metro.java.net/
# svn export https://svn.java.net/svn/glassfish~svn/tags/javax.xml.rpc-api-1.1.1 glassfish-jaxrpc-api-1.1.1
# tar cJf glassfish-jaxrpc-api-1.1.1.tar.xz glassfish-jaxrpc-api-1.1.1
Source0:       %{name}-%{version}.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(javax.servlet:javax.servlet-api)
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

Java APIs for XML based RPC 1.1 Design Specification.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin

%pom_change_dep :servlet-api :javax.servlet-api:3.1.0 . "<optional>true</optional>"

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
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_3jpp8
- new version

