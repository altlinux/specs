%define _unpackaged_files_terminate_build 1

Name: reactor-core
Version: 3.8.8
Release: alt1

Summary: Reactive Streams library for the JVM
License: Apache-2.0
Group: Development/Java
Url: https://github.com/reactor/reactor-core
VCS: https://github.com/reactor/reactor-core.git
BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt-build.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: biz-aQute-bnd-gradle-plugins
BuildRequires: gradle-mrjar-plugin
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: java-21-openjdk-devel
BuildRequires: shadow-gradle-plugin
BuildRequires: xgradle
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(io.micrometer:context-propagation)
BuildRequires: mvn(io.micrometer:micrometer-bom:pom:)
BuildRequires: mvn(io.micrometer:micrometer-commons)
BuildRequires: mvn(io.micrometer:micrometer-core)
BuildRequires: mvn(io.micrometer:micrometer-observation)
BuildRequires: mvn(io.projectreactor.tools:blockhound)
BuildRequires: mvn(io.projectreactor:jsr166)
BuildRequires: mvn(net.bytebuddy:byte-buddy)
BuildRequires: mvn(net.bytebuddy:byte-buddy-agent)
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(org.reactivestreams:reactive-streams)
BuildRequires: mvn(org.slf4j:slf4j-api)

%description
Project Reactor is a fully non-blocking foundation for JVM applications
with efficient demand management.

%prep
%setup -q
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register --artifacts=reactor-
%gradle_install

%files -f .mfiles
%doc README.md LICENSE

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 3.8.8-alt1
- Initial build for ALT.
