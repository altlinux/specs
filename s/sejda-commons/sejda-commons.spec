Name: sejda-commons
Version: 2.0.0
Release: alt1

Summary: A collection of utilities and common classes used by Sejda and PDFsam
License: Apache-2.0
Group: Development/Java
Url: https://sejda.org
Vcs: https://github.com/torakiki/sejda-commons.git
BuildArch: noarch

Source0: https://github.com/torakiki/%name/archive/v%version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: java-17-openjdk-devel

BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.slf4j:slf4j-api)
#Requires for the test scope
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(org.mockito:mockito-core)

%description
A collection of utilities and common classes used by Sejda and PDFsam.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-toolchains-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Mon Mar 23 2026 Anton Meleshnikov <alton@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus.
