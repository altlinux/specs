Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:		truecommons-parent
Version:	67
Release:	alt1_8jpp8
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
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 67-alt1_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 67-alt1_7jpp8
- new version

