BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-logging
%define version 3.1.2
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jboss-logging
Version:          3.1.2
Release:          alt1_1jpp7
Summary:          The JBoss Logging Framework
Group:            Development/Java
License:          ASL 2.0
URL:              https://github.com/jboss-logging/jboss-logging

# git clone git://github.com/jboss-logging/jboss-logging.git
# cd jboss-logging/ && git archive --format=tar --prefix=jboss-logging-3.1.2.GA/ 3.1.2.GA | xz > jboss-logging-3.1.2.GA.tar.xz
Source0:          jboss-logging-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local

BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    jboss-logmanager
BuildRequires:    slf4j
BuildRequires:    log4j
BuildRequires:    apiviz
BuildRequires:    jboss-parent
BuildRequires:    maven-surefire-provider-junit

Requires:         log4j
Requires:         slf4j
Requires:         jboss-logmanager
Requires:         jpackage-utils
Source44: import.info

%description
This package contains the JBoss Logging Framework.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-logging-%{namedversion}

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc src/main/resources/META-INF/LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc src/main/resources/META-INF/LICENSE.txt

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.2-alt1_1jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt3_4jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_4jpp7
- new version

