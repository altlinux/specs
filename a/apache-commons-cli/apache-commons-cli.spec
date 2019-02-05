Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           apache-commons-cli
Version:        1.4
Release:        alt1_5jpp8
Summary:        Command Line Interface Library for Java
License:        ASL 2.0
URL:            http://commons.apache.org/cli/
BuildArch:      noarch

Source0:        http://www.apache.org/dist/commons/cli/source/commons-cli-%{version}-src.tar.gz

# workaround for https://issues.apache.org/jira/browse/CLI-253
Patch0:         CLI-253-workaround.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
Source44: import.info
Provides: jakarta-commons-cli = %version

%description
The CLI library provides a simple and easy to use API for working with the
command line arguments and options.

%{?javadoc_package}

%prep
%setup -q -n commons-cli-%{version}-src
%patch0 -p1

# Compatibility links
%mvn_alias : org.apache.commons:commons-cli
%mvn_file : commons-cli %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt
%doc README.md RELEASE-NOTES.txt

%changelog
* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_5jpp8
- fc29 update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_4jpp8
- java update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_2jpp8
- new jpp release

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_2jpp8
- java 8 mass update

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sun Sep 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_9jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_7jpp7
- fc update

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_6jpp6
- add obsoletes

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_6jpp6
- fixed repolib

