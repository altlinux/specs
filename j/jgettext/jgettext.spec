Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jgettext
Version:        0.14
Release:        alt1_7jpp8
Summary:        An ANTLR-based parser and generator for GNU Gettext PO/POT 

License:        LGPLv2
URL:            https://github.com/zanata/%{name}
Source0:        https://github.com/zanata/%{name}/archive/%{name}-%{version}.zip
Source1:        http://www.gnu.org/licenses/lgpl-2.1.txt

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.codehaus.mojo:antlr-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  gettext gettext-tools
Source44: import.info

%description
JGettext includes an ANTLR-based parser for GNU Gettext PO/POT files and a 
PO/POT generator as well.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p %{SOURCE1} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference lgpl-2.1.txt
%doc README.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference lgpl-2.1.txt

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_2jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_2jpp7
- new release

