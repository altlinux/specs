Epoch: 0
Group: Development/Java
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           apache-commons-codec
Version:        1.15
Release:        alt1_4jpp11
Summary:        Implementations of common encoders and decoders
License:        ASL 2.0
URL:            https://commons.apache.org/codec/
BuildArch:      noarch

Source0:        https://archive.apache.org/dist/commons/codec/source/commons-codec-%{version}-src.tar.gz
# Data in DoubleMetaphoneTest.java originally has an inadmissible license.
# The author gives MIT in e-mail communication.
Source1:        aspell-mail.txt

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
%endif
Source44: import.info

%description
Commons Codec is an attempt to provide definitive implementations of
commonly used encoders and decoders. Examples include Base64, Hex,
Phonetic and URLs.

%{?javadoc_package}

%prep
%setup -q -n commons-codec-%{version}-src

cp %{SOURCE1} aspell-mail.txt
sed -i 's/\r//' RELEASE-NOTES*.txt LICENSE.txt NOTICE.txt

%mvn_file : commons-codec %{name}
%mvn_alias : commons-codec:commons-codec

%build
# Avoid running out of heap on s390x during test suite execution
export MAVEN_OPTS="-Xmx1024m"

%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dcommons.osgi.symbolicName=org.apache.commons.codec

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt aspell-mail.txt
%doc RELEASE-NOTES*

%changelog
* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 0:1.15-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:1.15-alt1_2jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 0:1.13-alt1_2jpp11
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_4jpp8
- fc29 update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_3jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_3jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_5jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_1jpp7
- new version

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_5jpp7
- new version

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_4jpp7
- added OSGi manifest

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_4jpp7
- new version

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_5jpp6
- fixed repolib

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_5jpp6
- fixed repolib

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_5jpp6
- new version

