Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
%define project_version 1.0-alpha-15

Name:           plexus-component-api
Version:        1.0
Release:        alt4_0.13.alpha15jpp7
Summary:        Plexus Component API

License:        ASL 2.0
URL:            http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-15/plexus-component-api/
#svn export http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-15/plexus-component-api/ plexus-component-api-1.0-alpha-15
#tar zcf plexus-component-api-1.0-alpha-15.tar.gz plexus-component-api-1.0-alpha-15/
Source0:        plexus-component-api-1.0-alpha-15.tar.gz

BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  plexus-classworlds
Source44: import.info

%description
Plexus Component API

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-%{project_version}

%build
%mvn_build

%install
%mvn_install

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files -f .mfiles
%files javadoc -f .mfiles-javadoc

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_0.13.alpha15jpp7
- update

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_0.10.alpha15jpp7
- BR: maven-local

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.10.alpha15jpp7
- added compat symlink

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.10.alpha15jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.10.alpha15jpp7
- new release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.7.alpha15jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

