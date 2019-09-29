Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           docker-client-java
Version:        8.11.7
Release:        alt1_5jpp8
Summary:        Docker Client

# Obsoletes/Provides added in F27
Provides:       docker-client = %{version}-%{release}
Obsoletes:      docker-client < %{version}-%{release}

License:        ASL 2.0
URL:            https://github.com/spotify/docker-client
Source0:        https://github.com/spotify/docker-client/archive/v%{version}.tar.gz

Patch0: 0001-Port-to-latest-version-of-Google-AutoValue.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.datatype:jackson-datatype-guava)
BuildRequires:  mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider)
BuildRequires:  mvn(com.github.jnr:jnr-unixsocket)
BuildRequires:  mvn(com.google.auto.value:auto-value) >= 1.4.1
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.guava:guava:20.0)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires:  mvn(org.glassfish.hk2:hk2-api)
BuildRequires:  mvn(org.glassfish.jersey.connectors:jersey-apache-connector)
BuildRequires:  mvn(org.glassfish.jersey.core:jersey-client)
BuildRequires:  mvn(org.glassfish.jersey.media:jersey-media-json-jackson)
BuildRequires:  mvn(org.slf4j:slf4j-api)

BuildArch: noarch
Source44: import.info

%description
The Docker Client is a Java API library for accessing a Docker daemon.

%prep
%setup -q -n docker-client-%{version}
%patch0 -p1

# The parent pom doen't add anything we can't live without
%pom_remove_parent
sed -i -e '/<packaging>/a<groupId>com.spotify</groupId>' pom.xml

# Plugins unnecessary for RPM builds
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :jacoco-maven-plugin

# Unnecessary static ananlysis stuff
%pom_remove_dep com.google.code.findbugs:annotations
sed -i -e '/SuppressFBWarnings/d' src/main/java/com/spotify/docker/client/DefaultDockerClient.java \
  src/main/java/com/spotify/docker/client/messages/{Host,Container}Config.java

# Missing dep for google cloud support
%pom_remove_dep :google-auth-library-oauth2-http
rm -rf src/{main,test}/java/com/spotify/docker/client/auth/gcr

# Add dep on hk2 api
%pom_add_dep org.glassfish.hk2:hk2-api

# Generate OSGi metadata
%pom_add_plugin "org.apache.felix:maven-bundle-plugin" pom.xml \
"<configuration>
  <instructions>
    <Bundle-SymbolicName>\${project.groupId}.docker.client</Bundle-SymbolicName>
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
%pom_add_plugin "org.apache.maven.plugins:maven-jar-plugin" pom.xml \
"<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>"

%build
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE
%doc README.md

%changelog
* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 8.11.7-alt1_5jpp8
- new version

