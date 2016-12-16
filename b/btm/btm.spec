Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Summary:        Bitronix Transaction Manager
Name:           btm
Version:        2.1.2
Release:        alt1_9jpp8
Epoch:          0
License:        LGPLv3
URL:            http://bitronix.be
Source0:        http://bitronix.be/downloads/btm-dist-2.1.2.zip
Source1:        http://repo1.maven.org/maven2/org/codehaus/btm/btm-parent/2.1.2/btm-parent-2.1.2.pom
Source2:        http://repo1.maven.org/maven2/org/codehaus/btm/btm/2.1.2/btm-2.1.2.pom
Patch0:         %{name}-use-shared-jars.patch
Patch1:         btm-jdbc4.1.patch

BuildRequires:  ant >= 0:1.6
BuildRequires:  geronimo-jta
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  xml-commons-apis
#BuildRequires:  mvn(javax.transaction:jta)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires:  mvn(org.codehaus:codehaus-parent:pom:)
BuildRequires:  mvn(org.slf4j:slf4j-api)

# Turn this on to make "ant test" work
# BuildRequires:  mockito
Requires:       junit
Requires:       xml-commons-apis
Requires:       java >= 1.6.0
Requires:       geronimo-jms
Requires:       geronimo-jta

BuildArch:      noarch
Source44: import.info

%description
The Bitronix Transaction Manager (BTM) is a simple but complete
implementation of the JTA 1.1 API. It is a fully working XA transaction
manager that provides all services required by the JTA API while trying 
to keep the code as simple as possible for easier understanding of the 
XA semantics.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-dist-%{version}
# remove all binary libs
find -name '*.jar' -exec rm -f '{}' \;


%patch0 -p1
%patch1 -p1

%mvn_file org.codehaus.%{name}:%{name} %{name}

%build

ant build

%install
%mvn_artifact %{SOURCE1}
%mvn_artifact %{SOURCE2} dist/%{name}-%{version}.jar
%mvn_install -J doc/api

%files -f .mfiles
%doc release-notes-%{version}.txt
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt


%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.2-alt1_9jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.2-alt1_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.2-alt1_7jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.2-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.2-alt1_3jpp7
- new release

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.2-alt1_2jpp7
- use fc geronimo

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.2-alt1_1jpp7
- fc build

