Name:           reload4j
Version:        1.2.26
Release:        alt1.1

Summary:        Reload4j is a drop-in replacement for log4j 1.2.17
License:        Apache-2.0
Group:          Development/Java
URL:            https://reload4j.qos.ch/
VCS:            https://github.com/qos-ch/reload4j

Source0:        %name-%version.tar

Patch0:         0001-Replace-javax-with-jakarta-mail.patch
Patch1:         0002-Replace-javax-with-jakarta-jms.patch
Patch2:         0003-reload4j-remove-internal-sun-api.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(jakarta.mail:jakarta.mail-api)
BuildRequires:  mvn(jakarta.jms:jakarta.jms-api)

BuildArch:      noarch

%description
The reload4j project is a fork of Apache log4j version 1.2.17 in order to fix
most pressing security issues. It is intended as a drop-in replacement for
log4j version 1.2.17. By drop-in, we mean the replacement of log4j.jar with
reload4j.jar in your build without needing to make changes to source code,
i.e. to your java files.

With release 1.2.18.0 and later, the reload4j project offers a clear and easy
migration path for the thousands of users who have an urgent need to fix
vulnerabilities in log4j 1.2.17.

%javadoc_package

%prep
%setup
%autopatch -p1

%pom_remove_plugin :maven-toolchains-plugin
%pom_remove_plugin :maven-source-plugin

%pom_change_dep javax.mail:mail jakarta.mail:jakarta.mail-api
%pom_change_dep javax.jms:javax.jms-api jakarta.jms:jakarta.jms-api

%pom_remove_dep :h2

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.compiler.source=1.5 -Dmaven.compiler.target=1.5

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE *.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 1.2.26-alt1.1
- Cosmetic fixes.

* Sun Feb 22 2026 Evgeniy Serov <scala@altlinux.org> 1.2.26-alt1
- Initial build for Sisyphus.
