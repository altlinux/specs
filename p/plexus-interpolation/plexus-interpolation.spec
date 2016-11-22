Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           plexus-interpolation
Version:        1.22
Release:        alt1_5jpp8
Summary:        Plexus Interpolation API
License:        ASL 2.0 and ASL 1.1 and MIT
URL:            https://github.com/codehaus-plexus/plexus-interpolation
BuildArch:      noarch

Source0:        https://github.com/sonatype/%{name}/archive/%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-components:pom:)
Source44: import.info

%description
Plexus interpolator is the outgrowth of multiple iterations of development
focused on providing a more modular, flexible interpolation framework for
the expression language style commonly seen in Maven, Plexus, and other
related projects.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%mvn_file : plexus/interpolation
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.22-alt1_5jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.22-alt1_4jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.22-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt3_7jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt3_6jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt3_2jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt1_2jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt1_3jpp7
- fc version

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt1_1jpp6
- new jpp relase

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.12-alt1_1jpp6
- new version

