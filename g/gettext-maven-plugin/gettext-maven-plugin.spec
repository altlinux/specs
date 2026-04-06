Name:           gettext-maven-plugin
Version:        2.2.0
Release:        alt2

Summary:        Maven plugin to provide tasks to run gettext on project
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/cnhongwei/gettext-maven-plugin
VCS:            https://github.com/cnhongwei/gettext-maven-plugin

Source0:        %name-%version.tar.gz

Patch0:         gettext-plugin-alt-fixes-compilation.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:) 
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)

BuildArch:      noarch

%description
Maven plugin to provide tasks to run gettext on project.

%javadoc_package

%prep
%setup -n %name-%name-%version
%patch -p1

%pom_add_dep org.apache.maven:maven-core

%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-gpg-plugin
%mvn_alias "io.github.cnhongwei:gettext-maven-plugin" "com.googlecode.gettext-commons:gettext-maven-plugin"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Mon Apr 06 2026 Evgeniy Serov <scala@altlinux.org> 2.2.0-alt2
- Fix build with missing dep.

* Mon Mar 02 2026 Anton Meleshnikov <alton@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus.
