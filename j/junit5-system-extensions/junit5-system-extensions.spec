%define _unpackaged_files_terminate_build 1

Name: junit5-system-extensions
Version: 1.2.3
Release: alt1

Summary: JUnit Jupiter extensions for testing System streams and exit calls
License: EPL-2.0
Group: Development/Java
URL: https://github.com/itsallcode/junit5-system-extensions
VCS: https://github.com/itsallcode/junit5-system-extensions.git

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: junit5
BuildRequires: mvn(org.apiguardian:apiguardian-api)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)

%description
JUnit Jupiter extensions for testing code that reads or writes System
streams or calls System.exit.

%package javadoc
Summary: API documentation for %name
Group: Development/Documentation

%description javadoc
API documentation for JUnit5 System Extensions.

%prep
%setup -q
# The system compiler supports the upstream Java 11 bytecode target.
%pom_remove_plugin org.apache.maven.plugins:maven-toolchains-plugin
# Release metadata, signing and analysis do not belong to the offline build.
%pom_remove_plugin io.github.git-commit-id:git-commit-id-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-artifact-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin
%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin org.sonarsource.scanner.maven:sonar-maven-plugin
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
# JUnit API annotation classes are needed with upstream -Werror.
%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:provided
%mvn_file : %name

%build
%mvn_build -s -- -Dmaven.compiler.release=11 \
    -Dgit.commit.time="$SOURCE_DATE_EPOCH" \
    -DargLine=-Djava.security.manager=allow

%install
%mvn_install

%files -f .mfiles-%name
%doc LICENSE.md LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 03 2026 Ivan Khanas <xeno@altlinux.org> 1.2.3-alt1
- Initial build for ALT.
