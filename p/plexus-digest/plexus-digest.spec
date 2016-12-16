Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           plexus-digest
Version:        1.1
Release:        alt2_21jpp8
Epoch:          0
Summary:        Plexus Digest / Hashcode Components
License:        ASL 2.0
URL:            https://github.com/codehaus-plexus/plexus-digest
BuildArch:      noarch

# svn export http://svn.codehaus.org/plexus/plexus-components/tags/plexus-digest-1.1/ plexus-digest/
# tar czf plexus-digest-1.1-src.tar.gz plexus-digest/
Source0:        %{name}-%{version}-src.tar.gz

Patch0:         %{name}-migration-to-component-metadata.patch
Patch1:         %{name}-fix-test-dependencies.patch
Patch2:         0001-Do-not-use-algorithm-name-as-regular-expression.patch

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
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%mvn_file  : plexus/digest
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_21jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_20jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_19jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_14jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_12jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_9jpp7
- rebuild with maven-local

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_9jpp7
- new fc release

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_6jpp7
- new jpp release

* Sun Feb 26 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

