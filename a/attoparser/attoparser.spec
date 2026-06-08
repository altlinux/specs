Name:          attoparser
Version:       2.0.7
Release:       alt1
Summary:       Java parser for XML and HTML markup
License:       ASL 2.0
Group:         Development/Java
Url:           http://www.attoparser.org
Vcs:           https://github.com/attoparser/attoparser.git
BuildArch:     noarch

Source0:       %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-11-compat
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin
BuildRequires: maven-assembly-plugin

%description
Attoparser is a SAX-style event-based parser - though
it does not implement the SAX standard - but it can
also act as a DOM-style parser.

%prep
%setup
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles

%changelog
* Mon Jun 08 2026 Ilfat Aminov <aminov@altlinux.org> 2.0.7-alt1
- First build for ALT.
