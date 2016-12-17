Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global project_version 1.0-beta-2

Name:           plexus-active-collections
Version:        1.0
Release:        alt2_0.20.beta2jpp8
Summary:        Plexus Container-Backed Active Collections

License:        ASL 2.0
URL:            http://plexus.codehaus.org/
#svn export http://svn.codehaus.org/plexus/tags/plexus-active-collections-1.0-beta-2/
#tar zcf plexus-active-collections-1.0-beta-2.tar.gz plexus-active-collections-1.0-beta-2/
Source0:        plexus-active-collections-1.0-beta-2.tar.gz
Source1:        http://apache.org/licenses/LICENSE-2.0.txt

Patch0:         %{name}-migration-to-component-metadata.patch

BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
Source44: import.info


%description
Plexus Container-Backed Active Collections

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{project_version}
%patch0 -p1
cp %{SOURCE1} .

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.20.beta2jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.19.beta2jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.18.beta2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.13.beta2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.12.beta2jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.9.beta2jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.9.beta2jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.8.beta2jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.7.beta2jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

