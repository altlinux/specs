Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define parent plexus
%define subname i18n

Name:           plexus-i18n
Version:        1.0
Release:        alt7_0.8.b10.4jpp8
Summary:        Plexus I18N Component
License:        ASL 2.0
Group:          Development/Java
URL:            https://github.com/codehaus-plexus/plexus-i18n
BuildArch:      noarch

# svn export http://svn.codehaus.org/plexus/plexus-components/tags/plexus-i18n-1.0-beta-10/
# tar cjf plexus-i18n-1.0-beta-10-src.tar.bz2 plexus-i18n-1.0-beta-10/
Source0:        plexus-i18n-1.0-beta-10-src.tar.bz2

Patch0:         %{name}-migration-to-component-metadata.patch
Patch1:         %{name}-plexus-container-default-missing.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

%description
The Plexus project seeks to create end-to-end developer tools for 
writing applications. At the core is the container, which can be 
embedded or for a full scale application server. There are many 
reusable components for hibernate, form processing, jndi, i18n, 
velocity, etc. Plexus also includes an application server which 
is like a J2EE application server, without all the baggage.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n plexus-i18n-1.0-beta-10
%patch0 -p1
%patch1 -p1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.8.b10.4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.7.b10.4jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.b10.2.5jpp7
- rebuild with maven-local

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.b10.2.5jpp7
- new fc release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b10.2.5jpp7
- new fc release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b10.2.2jpp7
- fc version

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b10.1jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b6.5jpp5
- new jpackage release

* Sun Nov 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b6.5jpp1.7
- build with maven2

* Tue Oct 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.b6.5jpp1.7
- bootstrap build for maven2

* Wed Jun 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b6.5jpp1.7
- updated to new jpackage release

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b6.4jpp1.7
- converted from JPackage by jppimport script

