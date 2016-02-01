Epoch: 0
Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define parent plexus
%define subname velocity

Name:           plexus-velocity
Version:        1.1.8
Release:        alt4_19jpp8
Summary:        Plexus Velocity Component
License:        ASL 2.0
URL:            https://github.com/codehaus-plexus/plexus-velocity
BuildArch:      noarch

# svn export http://svn.codehaus.org/plexus/plexus-components/tags/plexus-velocity-1.1.8/
# tar czf plexus-velocity-1.1.8-src.tar.gz plexus-velocity-1.1.8/
Source0:        plexus-velocity-%{version}-src.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(org.codehaus.plexus:plexus-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(velocity:velocity)
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
%setup -q -n plexus-velocity-%{version}
cp -p %{SOURCE1} LICENSE
for j in $(find . -name "*.jar"); do
        mv $j $j.no
done

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt4_19jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt2_15jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt2_14jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt2_11jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt1_11jpp7
- fc update

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt1_10jpp7
- new fc release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt1_9jpp7
- fc version

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt3_1jpp5
- explicit selection of java5 compiler

* Sat Feb 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt2_1jpp5
- fixed build with maven 2.0.7

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt1_1jpp5
- converted from JPackage by jppimport script

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt2_3jpp1.7
- build with maven2

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_3jpp1.7
- converted from JPackage by jppimport script

