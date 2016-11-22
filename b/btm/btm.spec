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
Release:        alt1_8jpp8
Epoch:          0
License:        LGPLv3
URL:            http://bitronix.be
Source0:        http://bitronix.be/downloads/btm-dist-2.1.2.zip
Source1:        http://repo1.maven.org/maven2/org/codehaus/btm/btm-parent/2.1.2/btm-parent-2.1.2.pom
Source2:        http://repo1.maven.org/maven2/org/codehaus/btm/btm/2.1.2/btm-2.1.2.pom
Patch0:         %{name}-use-shared-jars.patch
Patch1:         btm-jdbc4.1.patch
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant >= 0:1.6
BuildRequires:  junit
BuildRequires:  slf4j
BuildRequires:  geronimo-jms
BuildRequires:  geronimo-jta
BuildRequires:  xml-commons-apis
# Turn this on to make "ant test" work
# BuildRequires:  mockito
Requires: javapackages-tools rpm-build-java
Requires:       junit
Requires:       xml-commons-apis
Requires: javapackages-tools rpm-build-java
Requires:       slf4j
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

%build
ant build

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}-parent.pom
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files -f .mfiles
%doc release-notes-%{version}.txt
%doc license.txt

%files javadoc
%doc license.txt
%doc %{_javadocdir}/*

%changelog
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

