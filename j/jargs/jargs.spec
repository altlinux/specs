Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jargs
Version:        1.0
Release:        alt1_17jpp8
Summary:        Java command line option parsing suite

Group:          Development/Other
License:        BSD
URL:            http://jargs.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://repository.jboss.org/nexus/content/repositories/thirdparty-releases/net/sf/jargs/1.0/jargs-1.0.pom
BuildArch:      noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant
BuildRequires:  junit
Source44: import.info


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
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
ant runtimejar javadoc


%install
# jar
mkdir -p %{buildroot}%{_javadir}
cp -p lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr doc/* %{buildroot}%{_javadocdir}/%{name}
# pom
mkdir -p %{buildroot}%{_mavenpomdir}
cp -p %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "%{name}:%{name}"


%files -f .mfiles
%doc README LICENCE TODO doc/CHANGES 


%files javadoc
%doc LICENCE
%{_javadocdir}/%{name}/


%changelog
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

