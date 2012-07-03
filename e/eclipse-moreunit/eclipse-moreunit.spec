BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global src_repo_tag   V_2_4_1
%global eclipse_base   %{_libdir}/eclipse
%global install_loc    %{_datadir}/eclipse/dropins/moreunit

Name:           eclipse-moreunit
Version:        2.4.1
Release:        alt1_1jpp6
Summary:        An Eclipse plugin that assists with writing more unit tests

Group:          Development/Java
License:        EPL
URL:            http://moreunit.sourceforge.net
## sh %{name}-fetch-src.sh V_2_4_1 2.4.1
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-fetch-src.sh

BuildArch: noarch

BuildRequires: eclipse-pde >= 1:3.6.0
Requires: eclipse-jdt >= 3.6.0
Source44: import.info

%description
MoreUnit is an Eclipse plugin that should assist with writing more unit tests.
It can decorate classes which have testcase(s) and mark methods in the editor
which are under test.  Renaming/moving classes/methods will cause moreUnit to
rename/move the corresponding test code.  Generation of test method stubs is
also possible.

%prep
%setup -q 

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
%{eclipse_base}/buildscripts/pdebuild -f org.moreunit

%install
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.moreunit.zip 

%files
%{install_loc}
%doc org.moreunit.plugin/help/documentation.html

%changelog
* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_1jpp6
- update to new release by jppimport

* Fri Mar 11 2011 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_1jpp6
- new version

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1_2jpp6
- new version

