Name: jakarta-validation-api
Version: 3.1.1
Release: alt1

Summary: Jakarta Validation API
License: Apache-2.0
Group: Development/Java
Url: https://beanvalidation.org/
Vcs: https://github.com/jakartaee/validation.git
BuildArch: noarch

Source0: https://github.com/jakartaee/validation/archive/%version.tar.gz

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: testng

BuildRequires: mvn(org.eclipse.ee4j:project:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

%description
Jakarta Validation defines a metadata model and API for JavaBean and method validation.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :license-maven-plugin

%build
%mvn_build

%install
rm -rf .xmvn/apidocs/module-source-path
rm -f .xmvn/apidocs/args
cp -a src/main/javadoc/doc-files .xmvn/apidocs/
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference license.txt NOTICE.md

%changelog
* Mon Nov 16 2026 Ivan Khanas <xeno@altlinux.org> 3.1.1-alt1
- New version.

* Mon Mar 23 2026 Anton Meleshnikov <alton@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus.
