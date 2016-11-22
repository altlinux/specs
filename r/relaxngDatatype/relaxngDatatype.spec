Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           relaxngDatatype
Version:        2011.1
Release:        alt1_3jpp8
Summary:        RELAX NG Datatype API
License:        BSD
URL:            https://github.com/java-schema-utilities/relaxng-datatype-java
Source0:        https://github.com/java-schema-utilities/relaxng-datatype-java/archive/relaxngDatatype-%{version}.tar.gz
# License is not available in the tarball, this copy fetched from the tarball on the old sourceforge.net site
Source1:        copying.txt

BuildArch:      noarch
BuildRequires:  maven-local
Source44: import.info

%description
RELAX NG is a public space for test cases and other ancillary software
related to the construction of the RELAX NG language and its
implementations.

%package        javadoc
Group: Development/Documentation
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -n relaxng-datatype-java-relaxngDatatype-%{version}

cp -p %{SOURCE1} .

%pom_xpath_remove "pom:build/pom:extensions"

# For compatibility
%mvn_alias "com.github.relaxng:relaxngDatatype" "relaxngDatatype:relaxngDatatype"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/relaxngDatatype
%doc copying.txt

%files javadoc -f .mfiles-javadoc
%doc copying.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2011.1-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:2011.1-alt1_2jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_10.4jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_8.3jpp7
- rebuild to properly resolve msv conflict

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_8.3jpp7
- update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_4jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_3jpp5
- use default jpp profile

* Wed Sep 10 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_3jpp5
- converted from JPackage by jppimport script

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp1.7
- converted from JPackage by jppimport script

* Sun Apr 24 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt1
- Initial build for ALT Linux Sisyphus

