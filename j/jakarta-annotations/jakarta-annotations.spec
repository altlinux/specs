%define _unpackaged_files_terminate_build 1

Name: jakarta-annotations
Version: 3.0.0
Release: alt1

Summary: Jakarta Annotations
License: EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
Group: Development/Java
Url: https://github.com/jakartaee/common-annotations-api
Vcs: https://github.com/jakartaee/common-annotations-api.git
BuildArch: noarch

Source0: %name-%version.tar
# Jakarta v3+ does not provide javax imports required by xmvn.
Patch0: 0001-Add-maven-antrun-plugin-for-providing-javax-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: maven-enforcer-plugin
BuildRequires: spec-version-maven-plugin
BuildRequires: maven-antrun-plugin
BuildRequires: objectweb-asm
BuildRequires: jarjar

%description
Jakarta Annotations defines a collection of annotations representing
common semantic concepts that enable a declarative style of programming
that applies across a variety of Java technologies.

%{?javadoc_package}

%prep
%setup
%autopatch -p1

# remove unnecessary dependency on parent POM
# org.eclipse.ee4j:project is not packaged and isn't needed
%pom_remove_parent api

# remove plugins not needed for RPM builds
%pom_remove_plugin :maven-javadoc-plugin api
%pom_remove_plugin :maven-source-plugin api

# provide aliases for the old artifact coordinates
%mvn_alias jakarta.annotation:jakarta.annotation-api \
  javax.annotation:javax.annotation-api \
  javax.annotation:jsr250-api

%build
%mvn_build -- --file=api/pom.xml \
  -Dmaven.compiler.source=9 \
  -Dmaven.compiler.target=9 \
  -Dmaven.javadoc.source=9 \
  -Dmaven.compiler.release=9 \
  #

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md

%changelog
* Tue Nov 12 2025 Ivan Khanas <xeno@altlinux.org> 3.0.0-alt1
- New version.

* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 1.3.5-alt1_11jpp11
- update

* Wed Jun 02 2021 Igor Vlasenko <viy@altlinux.org> 1.3.5-alt1_6jpp11
- new version
