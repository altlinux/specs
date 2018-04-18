Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jargs
Version:        1.0
Release:        alt2_21jpp8
Summary:        Java command line option parsing suite

License:        BSD
URL:            http://jargs.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://repository.jboss.org/nexus/content/repositories/thirdparty-releases/net/sf/jargs/1.0/jargs-1.0.pom
BuildArch:      noarch

BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  junit
Source44: import.info


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.


%description
This project provides a convenient, compact, pre-packaged and 
comprehensively documented suite of command line option parsers 
for the use of Java programmers. 
Initially, parsing compatible with GNU-style 'getopt' is provided.

%prep
%setup -q
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;


%build
%ant runtimejar javadoc


%install
%mvn_artifact %{SOURCE1} lib/%{name}.jar
%mvn_alias net.sf:%{name} %{name}:%{name}
%mvn_install -J doc


%files -f .mfiles
%doc README TODO doc/CHANGES
%doc --no-dereference LICENCE


%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENCE


%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_21jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_18jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_18jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_17jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_16jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_12jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_10jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_9jpp7
- fc update

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp6
- new version

