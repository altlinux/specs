Name: sejda-io
Version: 3.0.1
Release: alt1

Summary: An Input/Output layer built on top of Java standard io and nio packages
License: Apache-2.0
Group: Development/Java
Url: https://sejda.org
Vcs: https://github.com/torakiki/sejda-io.git
BuildArch: noarch

Source0: https://github.com/torakiki/%name/archive/v%version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: java-17-openjdk-devel

BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.sejda:sejda-commons)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.slf4j:slf4j-api)

%description
An Input/Output layer built on top of Java standard io and nio packages.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-toolchains-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Mon Mar 23 2026 Anton Meleshnikov <alton@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus.
