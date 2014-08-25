Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
Name:           maven-reporting-impl
Version:        2.2
Release:        alt1_5jpp7
Summary:        Abstract classes to manage report generation
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-reporting-impl
# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-reporting-impl-2.2 maven-reporting-impl-2.2
# tar caf maven-reporting-impl-2.2.tar.xz maven-reporting-impl-2.2/
Source0:        %{name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-shared
%{?fedora:BuildRequires: junit-addons}

Obsoletes:      maven-shared-reporting-impl < %{version}-%{release}
Provides:       maven-shared-reporting-impl = %{version}-%{release}
Source44: import.info

%description
Abstract classes to manage report generation, which can be run both:

* as part of a site generation (as a maven-reporting-api's MavenReport),
* or as a direct standalone invocation (as a maven-plugin-api's Mojo).

This is a replacement package for maven-shared-reporting-impl

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.

%prep
%setup -q
cp -p %{SOURCE1} LICENSE.txt

%build
%mvn_build %{!?fedora:-f}

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_5jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_0jpp7
- new version

