Name: thumbnailator
Version: 0.4.21
Release: alt1

Summary: Thumbnailator - a thumbnail generation library for Java
License: MIT
Group: Development/Java
Url: https://github.com/coobird/thumbnailator
Vcs: https://github.com/coobird/thumbnailator.git
BuildArch: noarch

Source0: https://github.com/coobird/thumbnailator/archive/%version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)

%description
Thumbnailator - a thumbnail generation library for Java.
Thumbnailator is a single JAR file with no dependencies
to external libraries, making development and deployment simple and easy.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-javadoc-plugin
#replace source and target on the 11
%pom_xpath_replace "pom:source" "<source>11</source>"
%pom_xpath_replace "pom:target" "<target>11</target>"

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Thu Mar 26 2026 Anton Meleshnikov <alton@altlinux.org> 0.4.21-alt1
- Initial build for Sisyphus.
