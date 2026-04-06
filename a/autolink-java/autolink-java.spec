Name:           autolink-java
Version:        0.12.0
Release:        alt1

Summary:        Java library to extract links (URLs, email addresses) from plain text; fast, small and smart
License:        MIT
Group:          Development/Java
URL:            https://github.com/robinst/autolink-java
VCS:            https://github.com/robinst/autolink-java

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:      noarch

%description
Java library to extract links such as URLs and email addresses from plain text.
It's smart about where a link ends, such as with trailing punctuation.

%javadoc_package

%prep
%setup

%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :japicmp-maven-plugin

%build
# Tests are disabled due to some issues with JUnit
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE *.md

%changelog
* Fri Mar 13 2026 Evgeniy Serov <scala@altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus.
