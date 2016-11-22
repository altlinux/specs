Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jgettext
Version:        0.14
Release:        alt1_3jpp8
Summary:        An ANTLR-based parser and generator for GNU Gettext PO/POT 

License:        LGPLv2
URL:            https://github.com/zanata/%{name}
Source0:        https://github.com/zanata/%{name}/archive/%{name}-%{version}.zip
Source1:        http://www.gnu.org/licenses/lgpl-2.1.txt

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  antlr-maven-plugin
BuildRequires: gettext gettext-tools gettext-tools-python

Requires:       antlr-tool
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
%doc lgpl-2.1.txt README.txt
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc lgpl-2.1.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_2jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_2jpp7
- new release

