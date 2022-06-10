Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname dirq
Name:		java-dirq
Version:	1.8
Release:	alt1_15jpp11
Summary:	Directory based queue
License:	ASL 2.0
URL:		https://github.com/cern-mig/%{name}
Source0:	https://github.com/cern-mig/%{name}/archive/%{srcname}-%{version}.tar.gz
Patch0:		java-dirq-1.8-updated-pom.patch
BuildArch:	noarch
BuildRequires:	maven-local
BuildRequires:	mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(junit:junit)
Source44: import.info

%description
The goal of this module is to offer a simple queue system using the underlying
file system for storage, security and to prevent race conditions via atomic
operations. It focuses on simplicity, robustness and scalability.

This module allows multiple concurrent readers and writers to interact with
the same queue.

A Perl implementation (Directory::Queue) and a Python implementation (dirq)
of the same algorithm are available so readers and writers can be written in
different programming languages.

%package javadoc
Group: Development/Java
Summary:	Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{srcname}-%{version}
%patch0 -p1

# remove unnecessary plugins
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin

%mvn_file : %{name}

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc CHANGES readme.md todo.md

%changelog
* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 1.8-alt1_15jpp11
- update

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.8-alt1_13jpp11
- new version

