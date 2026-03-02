Name: gettext-maven-plugin
Version: 2.2.0
Release: alt1

Summary: Maven plugin to provide tasks to run gettext on project
License: Apache-2.0
Group: Development/Java
Url: https://github.com/cnhongwei/gettext-maven-plugin
BuildArch: noarch

Source0: https://github.com/cnhongwei/gettext-maven-plugin/archive/%name-%version.tar.gz
Patch: gettext-plugin-alt-fixes-compilation.patch

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default

BuildRequires: sonatype-oss-parent
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires: mvn(org.apache.maven.reporting:maven-reporting-impl)

%description
Maven plugin to provide tasks to run gettext on project.

%package javadoc
Group: Development/Java
Summary: Javadoc for %name
BuildArch: noarch

%description javadoc
This package contains the API documentation for %name.

%prep
%setup -n %name-%name-%version
%patch -p1

%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-gpg-plugin
%mvn_alias "io.github.cnhongwei:gettext-maven-plugin" "com.googlecode.gettext-commons:gettext-maven-plugin"

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Mar 02 2026 Anton Meleshnikov <alton@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus.
