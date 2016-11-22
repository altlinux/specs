Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           plexus-interactivity
Version:        1.0
Release:        alt6_0.22.alpha6jpp8
Epoch:          0
Summary:        Plexus Interactivity Handler Component
License:        MIT
URL:            https://github.com/codehaus-plexus/plexus-interactivity
BuildArch:      noarch
# svn export \
#   http://svn.codehaus.org/plexus/plexus-components/tags/plexus-interactivity-1.0-alpha-6/
# tar caf plexus-interactivity-1.0-alpha-6-src.tar.xz \
#   plexus-interactivity-1.0-alpha-6
Source0:        plexus-interactivity-1.0-alpha-6-src.tar.xz
Patch1:         plexus-interactivity-dependencies.patch
Patch2:         plexus-interactivity-jline2.patch

BuildRequires:  maven-local
BuildRequires:  mvn(jline:jline) >= 2
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-components:pom:)
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
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%package api
Group: Development/Java
Summary:        API for %{name}

%description api
API module for %{name}.

%package jline
Group: Development/Java
Summary:        jline module for %{name}

%description jline
jline module for %{name}.

%prep
%setup -q -n plexus-interactivity-1.0-alpha-6
%patch1 -p1
%patch2 -p1

%mvn_file ":{plexus}-{*}" @1/@2

%build
%mvn_package ":plexus-interactivity"

%mvn_build -f -s

%install
%mvn_install

%files -f .mfiles
%files api -f .mfiles-plexus-interactivity-api
%files jline -f .mfiles-plexus-interactivity-jline

%files javadoc -f .mfiles-javadoc


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_0.22.alpha6jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_0.21.alpha6jpp8
- unbootsrap build

* Mon Jan 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.11.alpha6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.10.alpha6jpp7
- new release

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.7.alpha6jpp7
- fc update

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a6.1jpp6
- new version

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a5.6jpp5
- fixed build

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a5.6jpp5
- new jpackage release

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a5.5jpp1.7
- build with maven2

* Wed Jun 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a5.5jpp1.7
- updated to new jpackage release

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a5.4jpp1.7
- converted from JPackage by jppimport script

* Sun Dec 04 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt0.1.alpha5
- Rebuild for ALTLinux Sisyphus
- spec cleanup

* Mon Nov 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.a5.1jpp
- First JPackage build

