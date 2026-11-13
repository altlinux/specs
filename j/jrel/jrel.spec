%define _unpackaged_files_terminate_build 1

Name: jrel
Version: 0.1.0
Release: alt1

Summary: Type-safe binary relations and identity collections for Java
License: Apache-2.0
Group: Development/Java
URL: https://github.com/veithen/jrel
VCS: https://github.com/veithen/jrel.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: LICENSE

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(com.github.veithen.checkt:checkt-annotations)
BuildRequires: mvn(com.github.veithen.checkt:checkt-annotation-processor)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(org.mockito:mockito-core)

%description
Java relations with type-safe references, bidirectional associations, identity
collections, composition and transitive closures.

%javadoc_package

%prep
%setup
cp %SOURCE1 LICENSE
# The parent supplies unavailable release and lint conventions.
%pom_remove_parent
%pom_xpath_inject pom:project "<groupId>com.github.veithen</groupId>"
%pom_remove_plugin org.codehaus.mojo:license-maven-plugin
%mvn_package :* %name

%build
%mvn_build -s -- -Dmaven.compiler.source=8 -Dmaven.compiler.target=8

%install
%mvn_install

%files -f .mfiles-%name
%doc LICENSE

%changelog
* Tue Nov 10 2026 Ivan Khanas <xeno@altlinux.org> 0.1.0-alt1
- Initial build for ALT.
