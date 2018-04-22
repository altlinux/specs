Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jchardet
Version:        1.1
Release:        alt2_17jpp8
Summary:        Java port of Mozilla's automatic character set detection algorithm

License:        MPLv1.1 or GPLv2+ or LGPLv2+
URL:            http://jchardet.sourceforge.net/
Source0:        http://download.sourceforge.net/jchardet/%{version}/jchardet-%{version}.zip
Source1:        http://repo1.maven.org/maven2/net/sourceforge/%{name}/%{name}/1.0/%{name}-1.0.pom
BuildArch:      noarch

BuildRequires:  maven-local
Source44: import.info

%description
jchardet is a java port of the source from Mozilla's automatic charset
detection algorithm. The original author is Frank Tang. What is available
here is the java port of that code. The original source in C++ can be found
from http://lxr.mozilla.org/mozilla/source/intl/chardet/. More information can
be found at http://www.mozilla.org/projects/intl/chardet.html.

%package javadoc
Group: Development/Java
Summary:    API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

cp %{SOURCE1} pom.xml

# fix up the provided version
%pom_xpath_set /pom:project/pom:version %{version}

# remove distributionManagement.status from pom (maven stops build
# when it's there)
%pom_xpath_remove pom:distributionManagement

# create proper dir structure
mkdir -p src/main/java/org/mozilla/intl/chardet
mv src/*java src/main/java/org/mozilla/intl/chardet

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE


%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_17jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_16jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_14jpp8
- new jpp release

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

