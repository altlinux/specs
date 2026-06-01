Name: pdfsam-injector
Version: 5.0.0
Release: alt1

Summary: A simple dependency injection engine based on Feather and used in PDFsam
License: Apache-2.0
Group: Development/Java
Url: https://github.com/torakiki/pdfsam-injector
Vcs: https://github.com/torakiki/pdfsam-injector.git
ExcludeArch: i586

Source: https://github.com/torakiki/pdfsam-injector/archive/v%version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: java-21-openjdk-devel

BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(jakarta.inject:jakarta.inject-api)

%description
A simple dependency injection engine based on Feather and used in PDFsam.

%javadoc_package

%prep
%setup

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Mon Jun 01 2026 Anton Meleshnikov <alton@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus.
