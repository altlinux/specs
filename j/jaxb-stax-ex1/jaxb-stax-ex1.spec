%define _unpackaged_files_terminate_build 1

Name: jaxb-stax-ex1
Version: 1.8.3
Release: alt1

Summary: Extended StAX API with Jakarta XML Binding support
License: BSD-3-Clause
Group: Development/Java
Url: https://github.com/eclipse-ee4j/jaxb-stax-ex
VCS: https://github.com/eclipse-ee4j/jaxb-stax-ex.git

Source: %name-%version.tar
Patch0: stax-ex1-activation-runtime.patch
Patch1: stax-ex1-jakarta.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: ee4j-parent
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: jakarta-activation
BuildRequires: jaxb-api
BuildRequires: junit

%description
Extensions to JSR-173 StAX using the system Jakarta Activation and JAXB APIs.
This package contains the complete upstream StAX Ex 1.8 project.

%package javadoc
Summary: API documentation for %name
Group: Development/Documentation
Requires: %name = %EVR

%description javadoc
API documentation for %name.

%prep
%setup -q
%autopatch -p1
# SCM-only maintenance plugins need a checkout; original headers remain intact.
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin
# Use the actual system API versions; all source and JPMS namespaces match.
activation_version=$(rpm -q --qf '%%{VERSION}' jakarta-activation)
jaxb_version=$(rpm -q --qf '%%{VERSION}' jaxb-api)
%pom_xpath_set "//pom:dependency[pom:groupId='jakarta.activation' and pom:artifactId='jakarta.activation-api']/pom:version" "$activation_version"
%pom_xpath_set "//pom:dependency[pom:groupId='jakarta.xml.bind' and pom:artifactId='jakarta.xml.bind-api']/pom:version" "$jaxb_version"
%mvn_compat_version org.jvnet.staxex:stax-ex %version
%mvn_package :stax-ex %name

%build
%mvn_build -s -- -DscmBranch=1.8.3 -DbuildNumber=eb4e2c15e3520c0b81b010923c1a94d484ff76aa

%install
%mvn_install
mkdir -p licenses
cp -p LICENSE.md NOTICE.md licenses/
if [ -d %buildroot%_javadocdir/%name/legal ]; then
    mv %buildroot%_javadocdir/%name/legal licenses/javadoc
    ln -s %_defaultdocdir/%name-%version/licenses/javadoc %buildroot%_javadocdir/%name/legal
fi

%files -f .mfiles-%name
%doc licenses

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 1.8.3-alt1
- Initial build for ALT.
