Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
Name:           jchardet
Version:        1.1
Release:        alt2_12jpp8
Summary:        Java port of Mozilla's automatic character set detection algorithm

Group:          Development/Other
License:        MPLv1.1
URL:            http://jchardet.sourceforge.net/
Source0:        http://download.sourceforge.net/jchardet/%{version}/jchardet-%{version}.zip
Source1:        http://repo1.maven.org/maven2/net/sourceforge/%{name}/%{name}/1.0/%{name}-1.0.pom
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires: javapackages-tools rpm-build-java

Requires: javapackages-tools rpm-build-java
%if 0%{?fedora} >= 20 || 0%{?rhel} >= 7
%else
%endif
Source44: import.info

%description
jchardet is a java port of the source from Mozilla's automatic charset
detection algorithm. The original author is Frank Tang. What is available
here is the java port of that code. The original source in C++ can be found
from http://lxr.mozilla.org/mozilla/source/intl/chardet/. More information can
be found at http://www.mozilla.org/projects/intl/chardet.html.

%package javadoc
Summary:    API documentation for %{name}
Group:      Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

cp %{SOURCE1} pom.xml
# fix up the provided version
sed -i 's:<version>1.0</version>:<version>1.1</version>:' pom.xml

# remove distributionManagement.status from pom (maven stops build
# when it's there)
sed -i '/<distributionManagement>/,/<\/distributionManagement>/ d' pom.xml

# create proper dir structure
mkdir -p src/main/java/org/mozilla/intl/chardet
mv src/*java src/main/java/org/mozilla/intl/chardet

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_4jpp7
- new version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_3jpp6
- new jpp relase

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp5
- fixes for java6 support

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- converted from JPackage by jppimport script

