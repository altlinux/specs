Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global base_name  discovery
%global short_name commons-%{base_name}

Name:           apache-%{short_name}
Version:        0.5
Release:        alt3_15jpp8
Epoch:          2
Summary:        Apache Commons Discovery
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:         %{name}-addosgimanifest.patch
Patch1:         %{name}-remove-unreliable-test.patch
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  apache-commons-logging >= 1.1.1
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

%build
%mvn_file  : %{short_name} %{name}
%mvn_build -X

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
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

