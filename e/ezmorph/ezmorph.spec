Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          ezmorph
Version:       1.0.6
Release:       alt1_17jpp8
Summary:       Object transformation library for Java
License:       ASL 2.0
URL:           http://ezmorph.sourceforge.net/
# A plain jarball with the source is provided by upstream.  We could use
# it, but we choose to build with maven for the sake of consistency.
# Therefore we pull the tree with maven metadata from VCS.
# cvs -d:pserver:anonymous@ezmorph.cvs.sourceforge.net:/cvsroot/ezmorph login
# cvs -z3 -d:pserver:anonymous@ezmorph.cvs.sourceforge.net:/cvsroot/ezmorph co -r REL_1_0_6 -d ezmorph-1.0.6 -P ezmorph
# tar czf ezmorph-1.0.6.tar.gz --exclude CVS ezmorph-1.0.6
Source0:       %{name}-%{version}.tar.gz
# License is not in tarball, but has since been added to upstream's source control:
Source1:       http://ezmorph.cvs.sourceforge.net/viewvc/ezmorph/ezmorph/LICENSE.txt

#BuildRequires: jakarta-oro
BuildRequires: maven-local
BuildRequires: mvn(commons-beanutils:commons-beanutils)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:12)

BuildArch:     noarch
Source44: import.info

%description
EZMorph is simple java library for transforming an Object to another
Object. It supports transformations for primitives and Objects and
multidimensional arrays.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q

cp -p %{SOURCE1} .

%pom_change_dep :log4j ::12

%pom_xpath_remove "pom:plugins"

%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_17jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_16jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_15jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_7jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_5jpp7
- fc update

* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_1jpp6
- new version

