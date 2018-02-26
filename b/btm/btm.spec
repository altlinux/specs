# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Summary:        Bitronix Transaction Manager
Name:           btm
Version:        2.1.2
Release:        alt1_1jpp7
Epoch:          0
License:        LGPLv3
URL:            http://bitronix.be
Group:          Development/Java
Source0:        http://bitronix.be/downloads/btm-dist-2.1.2.zip
Source1:        http://repo1.maven.org/maven2/org/codehaus/btm/btm-parent/2.1.2/btm-parent-2.1.2.pom
Source2:        http://repo1.maven.org/maven2/org/codehaus/btm/btm/2.1.2/btm-2.1.2.pom
Patch0:         %{name}-use-shared-jars.patch
Patch1:         btm-jdbc4.1.patch
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  junit
BuildRequires:  slf4j
BuildRequires:  geronimo-jms-1.1-api
BuildRequires:  geronimo-jta-1.1-api
BuildRequires:  xml-commons-apis
# Turn this on to make "ant test" work
# BuildRequires:  mockito
Requires:       jpackage-utils
Requires:       junit
Requires:       xml-commons-apis
Requires:       jpackage-utils >= 0:1.6
Requires:       slf4j
Requires:       geronimo-jms-1.1-api
Requires:       geronimo-jta-1.1-api

BuildArch:      noarch
Source44: import.info

%description
The Bitronix Transaction Manager (BTM) is a simple but complete
implementation of the JTA 1.1 API. It is a fully working XA transaction
manager that provides all services required by the JTA API while trying 
to keep the code as simple as possible for easier understanding of the 
XA semantics.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
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

%files
%doc license.txt release-notes-%{version}.txt
%{_javadir}/%{name}*.jar
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*.pom

%files javadoc
%doc license.txt
%doc %{_javadocdir}/*

%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.2-alt1_1jpp7
- fc build

