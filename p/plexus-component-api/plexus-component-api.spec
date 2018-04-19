Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define project_version 1.0-alpha-15

Name:           plexus-component-api
Version:        1.0
Release:        alt4_0.24.alpha15jpp8
Summary:        Plexus Component API

License:        ASL 2.0
URL:            http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-15/plexus-component-api/
#svn export http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-15/plexus-component-api/ plexus-component-api-1.0-alpha-15
#tar zcf plexus-component-api-1.0-alpha-15.tar.gz plexus-component-api-1.0-alpha-15/
Source0:        %{name}-%{project_version}.tar.gz

BuildArch: noarch

BuildRequires:  java-devel >= 1.6.0
BuildRequires:  maven-local
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  plexus-classworlds
# requires as parent pom
BuildRequires:  plexus-containers
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
%dir %{_javadir}/%{name}
%files javadoc -f .mfiles-javadoc

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_0.24.alpha15jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_0.23.alpha15jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_0.22.alpha15jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_0.20.alpha15jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_0.19.alpha15jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_0.15.alpha15jpp7
- new release

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

