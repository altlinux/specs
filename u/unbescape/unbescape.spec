Name:          unbescape
Version:       1.1.6
Release:       alt1
Summary:       Advanced yet easy to use escaping library for Java
License:       ASL 2.0
Group:         Development/Java
Url:           http://www.unbescape.org/
Vcs:           https://github.com/unbescape/unbescape.git
BuildArch:     noarch

Source0:       %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-11-compat
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: maven-source-plugin
BuildRequires: maven-assembly-plugin

%description
Unbescape is a Java library aimed at performing fully-featured and
high-performance escape and unescape operations for:

- HTML (HTML5 and HTML 4)
- XML (XML 1.0 and XML 1.1)
- JavaScript
- JSON
- URI/URL
- CSS
- CSV (Comma-Separated Values)
- Java literals
- Java .properties files

%prep
%setup
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles

%changelog
* Fri May 22 2026 Ilfat Aminov <aminov@altlinux.org> 1.1.6-alt1
- First build for ALT.
