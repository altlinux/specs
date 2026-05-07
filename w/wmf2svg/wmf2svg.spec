Name:           wmf2svg
Version:        0.9.12
Release:        alt1

Summary:        WMF to SVG Converting Tool & Library for Java
License:        Apache-2.0
Group:          Development/Java
URL:            http://hidekatsu-izuno.github.io/wmf2svg/
VCS:            https://github.com/hidekatsu-izuno/wmf2svg

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

BuildArch:      noarch

%description
This project's goal is to make tool & library for converting wmf to svg.

%javadoc_package

%prep
%setup

%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-shade-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt README.md

%changelog
* Mon Apr 27 2026 Evgeniy Serov <scala@altlinux.org> 0.9.12-alt1
- Initial build for Sisyphus.
