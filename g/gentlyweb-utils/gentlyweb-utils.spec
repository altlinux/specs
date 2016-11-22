Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          gentlyweb-utils
# there are no differences in the debian source taraball
# http://ftp.de.debian.org/debian/pool/main/g/gentlyweb-utils/gentlyweb-utils_1.5.orig.tar.gz
# the version is changed only in the activemq package see activemq-5.6.0/pom.xml
Version:       1.5
Release:       alt1_9jpp8
Summary:       Java utility library used by JoSQL for I/O
License:       ASL 2.0
Url:           http://josql.sourceforge.net/
Source0:       http://sourceforge.net/projects/josql/files/josql/stable-2.2/gentlyWEB-src-utils-1.1.tar.gz
Source1:       http://repo.fusesource.com/nexus/content/groups/public/net/sf/josql/%{name}/%{version}/gentlyweb-utils-%{version}.pom
# use system libraries
# fix javac target/source 1.5, encoding
# fix version
# add javadoc task
Patch0:        %{name}-%{version}-build.patch

BuildRequires: ant
BuildRequires: javapackages-local
BuildRequires: jdom

BuildArch:     noarch
Source44: import.info

%description
Simple java utility library used mainly by JoSQL for I/O.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n gentlyWEB-src-utils-1.1
%patch0 -p0

%mvn_file : %{name} gentlyWEB-utils

%build

%ant -f build-utils.xml createUtilsJar javadoc

%install

%mvn_artifact %{SOURCE1} gentlyWEB-utils-%{version}.jar
%mvn_install -J apidocs

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_8jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_3jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_2jpp7
- new version

