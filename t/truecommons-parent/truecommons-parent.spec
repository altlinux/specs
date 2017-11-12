Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		truecommons-parent
Version:	67
Release:	alt1_10jpp8
Summary:	Parent Pom for OSS Projects

License:	ASL 2.0
URL:		http://schlichtherle.de

Source0:	http://central.maven.org/maven2/net/java/truecommons/%{name}/%{version}/%{name}-%{version}.pom

Provides:	schlichtherle-oss-parent = %{version}-%{release}
Obsoletes:	schlichtherle-oss-parent <= 21-4

BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	maven-enforcer-plugin
BuildRequires:	sonatype-oss-parent
BuildRequires:	findbugs
Source44: import.info

%description
Parent POM for Open Source Software projects hosted on java.net.

%prep
cp %{SOURCE0} pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 67-alt1_10jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 67-alt1_9jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 67-alt1_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 67-alt1_7jpp8
- new version

