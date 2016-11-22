Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           plexus-cli
Version:        1.6
Release:        alt1_3jpp8
Epoch:          0
Summary:        Command Line Interface facilitator for Plexus
License:        ASL 2.0
URL:            https://github.com/codehaus-plexus/plexus-cli
BuildArch:      noarch

# git clone git://github.com/codehaus-plexus/plexus-cli.git
# git --git-dir plexus-cli/.git archive --prefix plexus-cli-1.6/ 8927458e81 | xz >plexus-cli-1.6.tar.xz
Source0:        %{name}-%{version}.tar.xz
Source1:        LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(commons-cli:commons-cli)
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
%setup -q
cp -p %{SOURCE1} .

%mvn_file : plexus/cli

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_18jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_17jpp7
- new release

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_12jpp7
- fc update

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_5jpp6
- new version

* Thu Jan 06 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_5jpp6
- jpp 6 releases

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_5jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_1jpp5
- converted from JPackage by jppimport script

