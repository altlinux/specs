%define _unpackaged_files_terminate_build 1

Name: pragmatists-junitparams
Version: 1.1.1
Release: alt2

Summary:  Parameterised tests that don't suck
License: Apache-2.0
Group: Development/Java
Url: https://pragmatists.github.io/JUnitParams
Vcs: https://github.com/Pragmatists/JUnitParams.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: sonatype-oss-parent
BuildRequires: junit
BuildRequires: assertj-core
BuildRequires: maven-source-plugin

%description
%summary.

%prep
%setup
#fix with java17
sed -i 's|<source>1.6<|<source>1.8<|' pom.xml
sed -i 's|<target>1.6<|<target>1.8<|' pom.xml

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin

%build
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Mon Aug 17 2026 Anton Meleshnikov <alton@altlinux.org> 1.1.1-alt2
- FTBFS fix with java17.

* Wed Dec 03 2025 Ivan Khanas <xeno@altlinux.org> 1.1.1-alt1
- First build for ALT.
