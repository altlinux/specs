# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          plexus-pom
Version:       3.3.3
Release:       alt1_5jpp8
Summary:       Root Plexus Projects POM
Group:         Development/Other
License:       ASL 2.0
URL:           https://github.com/codehaus-plexus/plexus-pom
Source0:       https://github.com/codehaus-plexus/plexus-pom/archive/plexus-%{version}.tar.gz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: forge-parent
Source44: import.info

%description
The Plexus project provides a full software stack for creating and
executing software projects.  This package provides parent POM for
Plexus packages.

%prep
%setup -q -n plexus-pom-plexus-%{version}
# require: maven-site-plugin *
%pom_xpath_remove "pom:profile[pom:id='maven-3']"
# * require: org.codehaus.plexus plexus-stylus-skin 1.0
# org.apache.maven.wagon wagon-webdav-jackrabbit 1.0
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin

%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin
cp -p %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.3-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.3-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.3-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.3-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt1_5jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt1_4jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt3_3jpp7
- rebuild with maven-local

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_3jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_3jpp7
- fc update

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_2jpp7
- new version

