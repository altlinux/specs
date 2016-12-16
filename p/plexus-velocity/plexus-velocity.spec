Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           plexus-velocity
Version:        1.2
Release:        alt1_1jpp8
Summary:        Plexus Velocity Component
License:        ASL 2.0
URL:            https://codehaus-plexus.github.io/plexus-velocity/
BuildArch:      noarch

Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(org.codehaus.plexus:plexus-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(velocity:velocity)
Source44: import.info

%description
This package provides Plexus Velocity component - a wrapper for
Apache Velocity template engine, which allows easy use of Velocity
by applications built on top of Plexus container.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}

find -name '*.jar' -delete

cp -p %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt4_21jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt4_19jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt2_15jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt2_14jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt2_11jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt1_11jpp7
- fc update

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt1_10jpp7
- new fc release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt1_9jpp7
- fc version

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt3_1jpp5
- explicit selection of java5 compiler

* Sat Feb 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt2_1jpp5
- fixed build with maven 2.0.7

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt1_1jpp5
- converted from JPackage by jppimport script

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt2_3jpp1.7
- build with maven2

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_3jpp1.7
- converted from JPackage by jppimport script

