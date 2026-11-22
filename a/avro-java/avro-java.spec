%define _unpackaged_files_terminate_build 1

Name: avro-java
Version: 1.11.5
Release: alt1

Summary: Apache Avro Java serialization runtime
License: Apache-2.0
Group: Development/Java
Url: https://avro.apache.org/
Vcs: https://github.com/apache/avro
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(com.fasterxml.jackson:jackson-bom:pom:)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(org.apache.commons:commons-compress)
BuildRequires: mvn(org.xerial.snappy:snappy-java)
BuildRequires: mvn(org.tukaani:xz)
BuildRequires: mvn(com.github.luben:zstd-jni)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)

%description
Apache Avro Java core runtime and its upstream Maven parent POMs.

%prep
%setup
rm .mvn/extensions.xml
%pom_xpath_set pom:parent/pom:version 40
%pom_xpath_inject pom:properties '<maven.compiler.release/>'
%pom_xpath_inject pom:properties '<remoteresources.skip>true</remoteresources.skip>'
resource='<resource><directory>../../..</directory><targetPath>META-INF</targetPath>'
resource="$resource<includes><include>LICENSE.txt</include><include>NOTICE.txt</include></includes></resource>"
%pom_xpath_inject pom:build/pom:resources "$resource" lang/java/avro
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-checkstyle-plugin lang/java
%pom_remove_plugin :spotless-maven-plugin . lang/java
%pom_remove_plugin :cyclonedx-maven-plugin lang/java
%pom_remove_plugin :maven-javadoc-plugin lang/java
# Package the Java core and its Maven parent POMs.
%pom_xpath_remove 'pom:modules/pom:module[text()!="avro"]' lang/java
%mvn_package 'org.apache.avro:avro:jar:tests:*' __noinstall
%mvn_package 'org.apache.avro:*'
%mvn_file 'org.apache.avro:{*}' avro/@1

%build
%mvn_build -s -j -- -pl :avro-toplevel,:avro-parent,:avro

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%changelog
* Fri Nov 20 2026 Ivan Khanas <xeno@altlinux.org> 1.11.5-alt1
- Initial build for ALT.
