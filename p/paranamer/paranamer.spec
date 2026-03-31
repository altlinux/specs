%define _unpackaged_files_terminate_build 1

Name: paranamer
Version: 2.8.3
Release: alt1

Summary: Runtime access to constructor and method parameter names
License: BSD-3-Clause
Group: Development/Java
Url: https://github.com/paul-hammant/paranamer
Vcs: https://github.com/paul-hammant/paranamer.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-17-compat
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-antrun-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: atinject

%description
Paranamer allows runtime access to constructor and method parameter names.

%prep
%setup
%autopatch -p1

%pom_disable_module paranamer-generator
%pom_disable_module paranamer-ant
%pom_disable_module paranamer-maven-plugin

%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-surefire-report-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r org.codehaus.mojo:cobertura-maven-plugin
%pom_remove_plugin -r org.sonatype.plugins:nexus-staging-maven-plugin

%pom_remove_plugin com.thoughtworks.paranamer:paranamer-maven-plugin paranamer-core9
%pom_remove_plugin com.thoughtworks.paranamer:paranamer-maven-plugin paranamer

%pom_remove_dep org.mockito:mockito-all paranamer
%pom_remove_dep net.sourceforge.f2j:arpack_combined_all paranamer

%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE.txt

%changelog
* Mon Mar 30 2026 Ivan Khanas <xeno@altlinux.org> 2.8.3-alt1
- Initial build for ALT.
