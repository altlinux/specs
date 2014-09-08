Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-docck-plugin
Version:        1.0
Release:        alt2_14jpp7
Summary:        Maven Documentation Checker Plugin
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-docck-plugin/
#svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-docck-plugin-1.0/
#tar jcf maven-docck-plugin-1.0.tar.bz2 maven-docck-plugin-1.0/
Source0:        %{name}-%{version}.tar.bz2
BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-plugin-descriptor)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

%description
Checks for violations of the Plugin Documentation Standard.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q 

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_11jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_8jpp7
- new fc release

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7jpp7
- fc version

