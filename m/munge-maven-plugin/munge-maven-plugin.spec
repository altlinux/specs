Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           munge-maven-plugin
Version:        1.0
Release:        alt1_10jpp8
Summary:        Munge Maven Plugin
License:        CDDL-1.0
URL:            http://github.com/sonatype/munge-maven-plugin
BuildArch:      noarch

Source0:        https://github.com/sonatype/munge-maven-plugin/archive/munge-maven-plugin-1.0.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.plugins:plugins-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
Source44: import.info

%description
Munge is a purposely-simple Java preprocessor. It only supports
conditional inclusion of source based on defined strings of the
form "if[tag]", "if_not[tag]", "else[tag]", and "end[tag]".
Unlike traditional preprocessors, comments, and formatting are all
preserved for the included lines. This is on purpose, as the output
of Munge will be distributed as human-readable source code.

To avoid creating a separate Java dialect, the conditional tags are
contained in Java comments. This allows one build to compile the
source files without pre-processing, to facilitate faster incremental
development. Other builds from the same source have their code contained
within that comment. The format of the tags is a little verbose, so
that the tags won't accidentally be used by other comment readers
such as javadoc. Munge tags must be in C-style comments;
C++-style comments may be used to comment code within a comment.

Like any preprocessor, developers must be careful not to abuse its
capabilities so that their code becomes unreadable. Please use it
as little as possible.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE
%doc README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_10jpp8
- new fc release

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_9jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_8jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_1jpp7
- new release

