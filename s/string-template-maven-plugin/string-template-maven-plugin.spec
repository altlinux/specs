Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           string-template-maven-plugin
Version:        1.1
Release:        alt1_7jpp11
Summary:        Execute StringTemplate files during a maven build

License:        MIT
URL:            https://kevinbirch.github.io/%{name}/
BuildArch:      noarch
Source0:        https://github.com/kevinbirch/%{name}/archive/%{name}-%{version}.tar.gz
# The license file was added to git after the last release
Source1:        https://raw.githubusercontent.com/kevinbirch/%{name}/master/LICENSE
# Update org.sonatype.aether to org.eclipse.aether
# https://github.com/kevinbirch/string-template-maven-plugin/pull/12
Patch0:         %{name}-aether.patch
# Tell javadoc about maven mojo tags
# https://github.com/kevinbirch/string-template-maven-plugin/pull/13
Patch1:         %{name}-javadoc.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.antlr:ST4)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.twdata.maven:mojo-executor-maven-plugin)
Source44: import.info

%description
This plugin allows you to execute StringTemplate template files during
your build.  The values for templates can come from static declarations
or from a Java class specified to be executed.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
%patch1 -p1

cp -p %{SOURCE1} .

# Updated name
%pom_change_dep :stringtemplate :ST4

# We do not need the versions reports
%pom_remove_plugin :versions-maven-plugin

# We do not have the secret key for signing jars
%pom_remove_plugin :maven-gpg-plugin

# We do not create any soure JARs
%pom_remove_plugin :maven-source-plugin

# We use xmvn-javadoc instead of maven-javadoc-plugin
%pom_remove_plugin :maven-javadoc-plugin

# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent

# Require JDK 8 at a minimum
sed -i 's/1\.6/1.8/g' pom.xml tests/pom.xml \
  src/main/java/com/webguys/maven/plugin/st/Controller.java

%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles-%{name}
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Jun 12 2022 Igor Vlasenko <viy@altlinux.org> 1.1-alt1_7jpp11
- java11 build

* Thu Nov 12 2020 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2jpp8
- new version

