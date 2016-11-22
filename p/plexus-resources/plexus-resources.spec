Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global namedversion 1.0-alpha-7

Name:           plexus-resources
Version:        1.0
Release:        alt7_0.20.a7jpp8
Summary:        Plexus Resource Manager
License:        MIT
URL:            https://github.com/codehaus-plexus/plexus-resources
BuildArch:      noarch

# svn export http://svn.codehaus.org/plexus/plexus-components/tags/plexus-resources-1.0-alpha-7/
# tar caf plexus-resources-1.0-alpha-7-src.tar.xz plexus-resources-1.0-alpha-7
Source0:        %{name}-%{version}-alpha-7-src.tar.xz

BuildRequires:  maven-local
BuildRequires:  mvn(org.codehaus.plexus:plexus-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info
Source45: plexus-resources-1.0-components.xml

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
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

mkdir -p target/classes/META-INF/plexus
cp -p %{SOURCE45} target/classes/META-INF/plexus/components.xml


%build
%mvn_file  : plexus/resources
%mvn_build -f

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.20.a7jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.19.a7jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.14.a7jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.13.a7jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.9.a7jpp7
- rebuild with maven-local

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.9.a7jpp7
- new fc release

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.8.a7jpp7
- fixed plexus component generation

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.8.a7jpp7
- fc version

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.1.a4.4jpp6
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.1.a4.4jpp6
- rebuild w/new maven2; disabled tests

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a4.2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a4.1jpp5
- converted from JPackage by jppimport script

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a3.1jpp1.7
- converted from JPackage by jppimport script

