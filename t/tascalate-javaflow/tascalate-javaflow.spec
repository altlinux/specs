%define _unpackaged_files_terminate_build 1

Name: tascalate-javaflow
Version: 2.7.5
Release: alt1

Summary: Continuations / Coroutines library for Java
License: Apache-2.0
Group: Development/Java
Url: https://github.com/vsilaev/tascalate-javaflow
Vcs: https://github.com/vsilaev/tascalate-javaflow.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-default
BuildRequires: slf4j
BuildRequires: moditect-maven-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-shade-plugin

%description
Tascalate JavaFlow provides continuations/coroutines support for Java.
This package ships the API artifact required by dependent Java projects.

%package parent
Summary: Parent POM for %name
Group: Development/Java

%description parent
%summary.

%prep
%setup

# Build only API module needed by downstream jasperreports.
%pom_disable_module net.tascalate.javaflow.spi
%pom_disable_module net.tascalate.javaflow.providers.asm3
%pom_disable_module net.tascalate.javaflow.providers.asm4
%pom_disable_module net.tascalate.javaflow.providers.asm5
%pom_disable_module net.tascalate.javaflow.providers.asmx
%pom_disable_module net.tascalate.javaflow.providers.core
%pom_disable_module net.tascalate.javaflow.providers.proxy
%pom_disable_module net.tascalate.javaflow.tools.jar
%pom_disable_module net.tascalate.javaflow.tools.ant
%pom_disable_module net.tascalate.javaflow.tools.maven
%pom_disable_module net.tascalate.javaflow.tools.gradle
%pom_disable_module net.tascalate.javaflow.tools.runtime
%pom_disable_module net.tascalate.javaflow.agent.common
%pom_disable_module net.tascalate.javaflow.agent.core
%pom_disable_module net.tascalate.javaflow.agent.proxy

%pom_remove_plugin -r -f org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin -r -f :maven-javadoc-plugin
%pom_remove_plugin -r -f :maven-gpg-plugin

sed -i -e 's#<source>1.6</source>#<source>1.8</source>#g' -e 's#<target>1.6</target>#<target>1.8</target>#g' pom.xml

%build
%mvn_build -s -f -j

%install
%mvn_install

%files parent -f .mfiles-net.tascalate.javaflow.parent

%files -f .mfiles-net.tascalate.javaflow.api
%doc LICENSE NOTICE README.md

%changelog
* Tue Apr 14 2026 Ivan Khanas <xeno@altlinux.org> 2.7.5-alt1
- First build for ALT.
