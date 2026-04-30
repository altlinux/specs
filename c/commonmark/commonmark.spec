%define _unpackaged_files_terminate_build 1

Name: commonmark
Version: 0.28.0
Release: alt1

Summary: Java CommonMark library for parsing and rendering Markdown text
Group: Development/Java
License: BSD-2-Clause
Url: https://commonmark.org/
Vcs: https://github.com/commonmark/commonmark-java
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin
BuildRequires: autolink-java

%package javadoc
Summary: API documentation for commonmark
Group: Development/Java

%package ext-autolink
Summary: commonmark extension for autolinking
Group: Development/Java

%package ext-footnotes
Summary: commonmark extension for footnotes
Group: Development/Java

%package ext-gfm-alerts
Summary: commonmark extension for alerts
Group: Development/Java

%package ext-gfm-strikethrough
Summary: commonmark extension for strikethrough
Group: Development/Java

%package ext-gfm-tables
Summary: commonmark extension for tables
Group: Development/Java

%package ext-heading-anchor
Summary: commonmark extension for adding id attributes to h tags
Group: Development/Java

%package ext-image-attributes
Summary: commonmark extension for adding attributes to images
Group: Development/Java

%package ext-ins
Summary: commonmark extension for <ins>; using ++.
Group: Development/Java

%package ext-task-list-items
Summary: commonmark extension for task list items
Group: Development/Java

%package ext-yaml-front-matter
Summary: commonmark extension for YAML front matter
Group: Development/Java

%description
Java library for parsing and rendering Markdown text according to the
CommonMark specification (and some extensions). Provides classes for
parsing input to an abstract syntax tree (AST), visiting and
manipulating nodes, and rendering to HTML or back to Markdown.

%description javadoc
This package contains API documentation for CommonMark library.

%description ext-autolink
CommonMark extension for turning plain URLs and email addresses into links.

%description ext-footnotes
CommonMark extension for footnotes using [^1] syntax.

%description ext-gfm-alerts
Commonmark extension for GFM alerts (admonition blocks) using [!TYPE]
syntax (GitHub Flavored Markdown).

%description ext-gfm-strikethrough
CommonMark extension for GFM strikethrough using ~~ (GitHub Flavored Markdown).

%description ext-gfm-tables
CommonMark extension for GFM tables using "|" pipes (GitHub Flavored
Markdown).

%description ext-heading-anchor
CommonMark extension for adding unique id attributes to header tags.

%description ext-image-attributes
CommonMark extension for adding attributes to images.

%description ext-ins
CommonMark extension for <ins>; using ++.

%description ext-task-list-items
CommonMark extension for task list items.

%description ext-yaml-front-matter
CommonMark extension for YAML front matter.

%prep
%setup

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-gpg-plugin

# Now there is a problem with JPMS of assertj-core and its transitive dependency byte-buddy.
%pom_disable_module commonmark-integration-test
%pom_disable_module commonmark-test-util

# No need to package
%mvn_package :commonmark-parent __noinstall

%build
%mvn_build -sf

%install
%mvn_install

%files -f .mfiles-commonmark

%files javadoc -f .mfiles-javadoc

%files ext-autolink -f .mfiles-commonmark-ext-autolink

%files ext-footnotes -f .mfiles-commonmark-ext-footnotes

%files ext-gfm-alerts -f .mfiles-commonmark-ext-gfm-alerts

%files ext-gfm-strikethrough -f .mfiles-commonmark-ext-gfm-strikethrough

%files ext-gfm-tables -f .mfiles-commonmark-ext-gfm-tables

%files ext-heading-anchor -f .mfiles-commonmark-ext-heading-anchor

%files ext-image-attributes -f .mfiles-commonmark-ext-image-attributes

%files ext-ins -f .mfiles-commonmark-ext-ins

%files ext-task-list-items -f .mfiles-commonmark-ext-task-list-items

%files ext-yaml-front-matter -f .mfiles-commonmark-ext-yaml-front-matter

%changelog
* Thu Apr 30 2026 Arseniy Kostevich <faux@altlinux.org> 0.28.0-alt1
- New version.
- Add package ext-gfm-alerts.

* Tue Apr 07 2026 Arseniy Kostevich <faux@altlinux.org> 0.27.1-alt2
- Fix dependency name.

* Tue Mar 24 2026 Arseniy Kostevich <faux@altlinux.org> 0.27.1-alt1
- Initial build for ALT.
