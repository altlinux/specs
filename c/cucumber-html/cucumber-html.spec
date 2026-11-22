%define _unpackaged_files_terminate_build 1

Name: cucumber-html
Version: 0.2.7
Release: alt1

Summary: Cross-platform HTML formatter resources for Cucumber
License: MIT
Group: Development/Java
URL: https://github.com/cucumber-attic/cucumber-html
VCS: https://github.com/cucumber-attic/cucumber-html

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)

BuildArch: noarch

%description
Cucumber-HTML provides the static HTML, CSS and JavaScript resources used to
render Cucumber execution reports.

%prep
%setup -q
%pom_xpath_set 'pom:project/pom:version' %version
%pom_remove_plugin org.apache.felix:maven-bundle-plugin
%pom_xpath_set \
    'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:version' \
    3.2.2
%pom_xpath_remove 'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:configuration/pom:archive/pom:manifestFile'

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-cucumber-html
%doc LICENSE

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 0.2.7-alt1
- Initial build for ALT.
