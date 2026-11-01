%define _unpackaged_files_terminate_build 1

Name: escapevelocity
Version: 1.1
Release: alt1

Summary: Lightweight Velocity-compatible Java template engine
License: Apache-2.0
Group: Development/Java
Url: https://github.com/google/escapevelocity
VCS: https://github.com/google/escapevelocity.git
BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-private-entry-test.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.guava:guava-testlib)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires: mvn(org.apache.velocity:velocity-engine-core)

%description
EscapeVelocity implements the Velocity template language subset used by
Java annotation processors, including AutoValue.

%prep
%setup
%autopatch -p1
%pom_remove_parent
%pom_xpath_inject pom:project '<properties><project.build.sourceEncoding>UTF-8</project.build.sourceEncoding></properties>'
%pom_change_dep org.apache.velocity:velocity org.apache.velocity:velocity-engine-core:2.4.1

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE README.md

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 1.1-alt1
- Initial build for ALT.
