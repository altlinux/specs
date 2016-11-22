Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define parent plexus
%define subname bsh-factory

Name:           %{parent}-%{subname}
Version:        1.0
Release:        alt5_0.16.a7jpp8
Epoch:          0
Summary:        Plexus Bsh component factory
License:        MIT
URL:            http://plexus.codehaus.org/
BuildArch:      noarch
# svn export svn://svn.plexus.codehaus.org/plexus/tags/plexus-bsh-factory-1.0-alpha-7-SNAPSHOT plexus-bsh-factory/
# tar czf plexus-bsh-factory-src.tar.gz plexus-bsh-factory/
Source0:        %{name}-src.tar.gz
Source3:	plexus-bsh-factory-license.txt

Patch1:         %{name}-encodingfix.patch
Patch2:         0001-Migrate-to-plexus-containers-container-default.patch

BuildRequires:  maven-local
BuildRequires:  mvn(bsh:bsh)
BuildRequires:  mvn(classworlds:classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

%description
Bsh component class creator for Plexus.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}

%patch1 -b .sav
%patch2 -p1
cp release-pom.xml pom.xml
cp -p %{SOURCE3} .

%build
%mvn_file  : %{parent}/%{subname}
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc plexus-bsh-factory-license.txt

%files javadoc -f .mfiles-javadoc
%doc plexus-bsh-factory-license.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.16.a7jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.15.a7jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.13.a7jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.8.a7jpp7
- rebuild with maven-local

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.8.a7jpp7
- fc update

* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a7s.5jpp6
- fixed build with new plexus-containers

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a7s.5jpp6
- new jpp release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a7s.4jpp5
- new jpackage release

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a7s.2jpp1.7
- build with maven2

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a7s.2jpp1.7
- converted from JPackage by jppimport script

