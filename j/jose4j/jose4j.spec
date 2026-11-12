%define _unpackaged_files_terminate_build 1

Name: jose4j
Version: 0.9.7
Release: alt1

Summary: Java implementation of JWT and the JOSE specifications
License: Apache-2.0
Group: Development/Java
URL: https://bitbucket.org/b_c/jose4j/
VCS: https://bitbucket.org/b_c/jose4j.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: java-21-openjdk-devel
BuildRequires: slf4j2
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk18on)
BuildRequires: mvn(org.mockito:mockito-core)

%description
Jose4j implements JSON Web Token and the JOSE specification suite, including
JSON Web Signature, JSON Web Encryption and JSON Web Key, using Java JCA APIs.

%prep
%setup
# Use the actual parallel SLF4j2 provider's registered compatibility version.
%pom_change_dep org.slf4j:slf4j-api org.slf4j:slf4j-api:2
# Tests use the SLF4j API, without backend-specific imports or assertions.
%pom_remove_dep ch.qos.logback:logback-classic
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE.txt

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 0.9.7-alt1
- Initial build for ALT.
