%define _unpackaged_files_terminate_build 1

Name: smallrye-common
Version: 2.15.0
Release: alt1

Summary: Common utilities for SmallRye projects
License: Apache-2.0
Group: Development/Java
Url: https://github.com/smallrye/smallrye-common
Vcs: https://github.com/smallrye/smallrye-common.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: jboss-logging
BuildRequires: jboss-logging-tools

%description
SmallRye Common provides shared utility libraries used across SmallRye
projects.

%package constraint
Summary: SmallRye Common constraints module
Group: Development/Java

%description constraint
Constraint utilities module from SmallRye Common.

%package cpu
Summary: SmallRye Common CPU module
Group: Development/Java

%description cpu
CPU detection and CPU-specific utilities module from SmallRye Common.

%package expression
Summary: SmallRye Common expression module
Group: Development/Java

%description expression
Expression processing module from SmallRye Common.

%package function
Summary: SmallRye Common functional helpers module
Group: Development/Java

%description function
Functional helper types module from SmallRye Common.

%package net
Summary: SmallRye Common networking module
Group: Development/Java

%description net
Networking utilities module from SmallRye Common.

%package os
Summary: SmallRye Common OS module
Group: Development/Java

%description os
Operating system utilities module from SmallRye Common.

%package ref
Summary: SmallRye Common references module
Group: Development/Java

%description ref
Reference utilities module from SmallRye Common.

%prep
%setup
%autopatch -p1

%pom_remove_parent
%pom_remove_dep org.jboss.shrinkwrap:shrinkwrap-bom

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r io.sundr:sundr-maven-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-surefire-plugin
%pom_remove_plugin -r :bridger
%pom_remove_plugin -r :impsort-maven-plugin

%pom_disable_module annotation
%pom_disable_module classloader
%pom_disable_module io
%pom_disable_module process
%pom_disable_module resource
%pom_disable_module search
%pom_disable_module version
%pom_disable_module vertx-context

%pom_add_dep_mgmt io.smallrye.common:smallrye-common-cpu:\${project.version} pom.xml
%pom_add_dep_mgmt io.smallrye.common:smallrye-common-ref:\${project.version} pom.xml
%pom_add_dep_mgmt org.jboss.logging:jboss-logging:\${version.org.jboss.logging} pom.xml
%pom_add_dep_mgmt org.jboss.logging:jboss-logging-annotations:\${version.org.jboss.logging} pom.xml
%pom_add_dep_mgmt org.jboss.logging:jboss-logging-processor:\${version.org.jboss.logging} pom.xml

%mvn_alias io.smallrye.common:smallrye-common-parent io.smallrye.common:smallrye-common-bom

%build
%mvn_build -s -f -j -- -Dmaven.compiler.source=11 -Dmaven.compiler.target=11

%install
%mvn_install

%files -f .mfiles-smallrye-common-parent
%doc --no-dereference LICENSE README.adoc

%files constraint -f .mfiles-smallrye-common-constraint
%files cpu -f .mfiles-smallrye-common-cpu
%files expression -f .mfiles-smallrye-common-expression
%files function -f .mfiles-smallrye-common-function
%files net -f .mfiles-smallrye-common-net
%files os -f .mfiles-smallrye-common-os
%files ref -f .mfiles-smallrye-common-ref

%changelog
* Fri Mar 27 2026 Ivan Khanas <xeno@altlinux.org> 2.15.0-alt1
- First build for ALT.
