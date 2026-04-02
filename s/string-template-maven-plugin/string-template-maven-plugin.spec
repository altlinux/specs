Name:           string-template-maven-plugin
Version:        1.1
Release:        alt3.1

Summary:        Execute StringTemplate files during a maven build
License:        MIT
Group:          Development/Java
URL:            https://kevinbirch.github.io/string-template-maven-plugin
VCS:            https://github.com/kevinbirch/string-template-maven-plugin

Source0:        %name-%version.tar.gz
Source1:        LICENSE

Patch0:         %name-aether.patch
Patch2:         %name-descriptor.patch
Patch3:         %name-annotations.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.antlr:ST4)
BuildRequires:  mvn(org.twdata.maven:mojo-executor-maven-plugin)

BuildArch:      noarch

%description
This plugin allows you to execute StringTemplate template files during
your build.  The values for templates can come from static declarations
or from a Java class specified to be executed.

%javadoc_package

%prep
%setup -n %name-%name-%version
%autopatch -p1

cp -p %SOURCE1 .

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

# This only enforces use of ancient maven and java versions
%pom_remove_plugin :maven-enforcer-plugin

# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent

# Require JDK 8 at a minimum
sed -i 's/1\.6/1.8/g' pom.xml tests/pom.xml \
  src/main/java/com/webguys/maven/plugin/st/Controller.java

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%name
%doc README.md
%doc LICENSE

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 1.1-alt3.1
- Cosmetic fixes.

* Thu Feb 12 2026 Evgeniy Serov <scala@altlinux.org> 1.1-alt3
- FTBFS fix
- updated patches
- use maven plugin annotations
- removed import.info

* Mon Nov 17 2025 Anton Meleshnikov <alton@altlinux.org> 1.1-alt2
- FTBFS fix (thanks fedora for the patch)

* Sun Jun 12 2022 Igor Vlasenko <viy@altlinux.org> 1.1-alt1_7jpp11
- java11 build

* Thu Nov 12 2020 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2jpp8
- new version

