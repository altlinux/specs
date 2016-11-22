Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:      brazil
Version:   2.3
Release:   alt3_15jpp8
Summary:   Extremely small footprint Java HTTP stack
Group:     Development/Other
License:   SPL
URL:       https://github.com/mbooth101/brazil

Source0:   https://github.com/mbooth101/brazil/archive/%{name}-%{version}.tar.gz

# upsteam's build script doesn't build javadocs, so use our own, better script
Source2:   brazil-build.xml

BuildArch:        noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    ant
Requires: javapackages-tools rpm-build-java
Source44: import.info

%description
Brazil is as an extremely small footprint HTTP stack and flexible architecture 
for adding URL-based interfaces to arbitrary applications and devices from Sun 
Labs. This package contains the core set of classes that are not dependent on 
any other external Java libraries.

%package javadoc
Summary:   Java-docs for %{name}
Group:     Development/Java
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package demo
Summary:   Demos for %{name}
Group:     Development/Other
Requires:  %{name} = %{version}
Requires:  tcl

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# fix permissions and interpreter in sample scripts
grep -lR -e ^\#\!/usr/sfw/bin/tclsh8.3 samples | xargs sed --in-place "s|/usr/sfw/bin/tclsh8.3|/usr/bin/tclsh|"
grep -lR -e ^\#\!/usr/bin/tclsh        samples | xargs chmod 755
grep -lR -e ^\#\!/bin/sh               samples | xargs chmod 755

%build
cp -p %{SOURCE2} build.xml
ant all

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p build/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# samples
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr samples %{buildroot}%{_datadir}/%{name}

%files
%doc README.md srcs/license.terms
%{_javadir}/%{name}.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%files demo
%doc %{_datadir}/%{name}/samples/README
%{_datadir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt3_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt3_14jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt3_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt3_10jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt3_9jpp7
- new fc release

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt3_8jpp7
- applied repocop patches

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_8jpp7
- fc version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_9jpp6
- new jpp relase

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_6jpp5
- updated from f13

* Mon Jul 28 2008 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_3jpp5
- converted from JPackage by jppimport script

