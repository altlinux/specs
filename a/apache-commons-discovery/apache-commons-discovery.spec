Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global base_name  discovery
%global short_name commons-%{base_name}

Name:           apache-%{short_name}
Version:        0.5
Release:        alt3_22jpp8
Epoch:          2
Summary:        Apache Commons Discovery
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:         %{name}-addosgimanifest.patch
Patch1:         %{name}-remove-unreliable-test.patch
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
Source44: import.info

%description
The Discovery component is about discovering, or finding, implementations for
pluggable interfaces.  Pluggable interfaces are specified with the intent that
multiple implementations are, or will be, available to provide the service
described by the interface.  Discovery provides facilities for finding and
instantiating classes, and for lifecycle management of singleton (factory)
classes.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0
%patch1 -p1
%mvn_file : %{short_name} %{name}

%build
%mvn_build -- -Dcommons.osgi.symbolicName=org.apache.commons.discovery

%install
%mvn_install

%files -f .mfiles
%doc RELEASE-NOTES.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt


%changelog
* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 2:0.5-alt3_22jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 2:0.5-alt3_19jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2:0.5-alt3_18jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2:0.5-alt3_17jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2:0.5-alt3_16jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2:0.5-alt3_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2:0.5-alt3_14jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2:0.5-alt3_9jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2:0.5-alt3_7jpp7
- new release

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 2:0.5-alt3_4jpp7
- added BR: for xmvn

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2:0.5-alt2_4jpp7
- rebuild with maven-local

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 2:0.5-alt1_4jpp7
- fc update

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 1:0.5-alt1_0.r830999.4jpp6
- new version

