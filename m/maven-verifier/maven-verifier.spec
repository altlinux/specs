Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-verifier
Version:        1.4
Release:        alt1_5jpp7
Summary:        Maven verifier
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-verifier
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
# Forwarded upstream, see MSHARED-284
Patch1:         0001-Update-to-maven-shared-utils-0.3.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-shared-utils

Obsoletes:      maven-shared-verifier < %{version}-%{release}
Provides:       maven-shared-verifier = %{version}-%{release}
Source44: import.info

%description
Provides a test harness for Maven integration tests.

This is a replacement package for maven-shared-verifier

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch1 -p1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_5jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

