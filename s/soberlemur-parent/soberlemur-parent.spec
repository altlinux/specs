Name: soberlemur-parent
Version: 1.0.21
Release: alt1

Summary: Parent POM for Sober Lemur Java projects

License: Apache-2.0
Group: Development/Java
Url: https://github.com/soberlemur/soberlemur-parent
BuildArch: noarch
ExcludeArch: %ix86

# Source-url: https://github.com/soberlemur/soberlemur-parent/archive/refs/tags/soberlemur-parent-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: maven-local
BuildRequires: java-25-openjdk-devel

%description
Shared Maven dependency and plugin configuration for Sober Lemur projects,
including PDFsam and Sejda.

%prep
%setup

%build
%mvn_artifact -Dtype=pom pom.xml

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE

%changelog
* Wed Sep 09 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.21-alt1
- Initial build for Sisyphus.
