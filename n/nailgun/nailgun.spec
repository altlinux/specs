Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define debug_package %{nil}

Name:     nailgun
Version:  0.9.1
Release:  alt2_11jpp8
Summary:  Framework for running Java from the cli without the JVM startup overhead
License:  ASL 2.0
URL:      http://martiansoftware.com/nailgun/

# https://github.com/martylamb/nailgun/archive/nailgun-all-0.9.1.zip
Source0:  %{name}-%{name}-all-%{version}.zip

BuildRequires:  maven-local
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info
BuildArch: noarch

%description
Nailgun is a client, protocol, and server for running Java programs from the 
command line without incurring the JVM startup overhead. Programs run in the 
server (which is implemented in Java), and are triggered by the client 
(written in C), which handles all I/O.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-all-%{version}

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Jun 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_11jpp8
- fixed arch build

* Wed May 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_7jpp8
- fixed build with maven-javadoc-plugin 3

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_7jpp8
- fc update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_5jpp8
- new jpp release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_7jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_6jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_5jpp7
- new version

