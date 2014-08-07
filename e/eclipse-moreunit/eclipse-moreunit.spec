# BEGIN SourceDeps(oneline):
BuildRequires: maven-local unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global src_repo_tag   v3.0.2
%global install_loc    %{_datadir}/eclipse/dropins/moreunit

Name:           eclipse-moreunit
Version:        3.0.2
Release:        alt2_1jpp7
Summary:        An Eclipse plugin that assists with writing more unit tests

Group:          Development/Java
License:        EPL
URL:            http://moreunit.sourceforge.net
## sh %{name}-fetch-src.sh v3.0.2 3.0.2
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-fetch-src.sh

BuildArch: noarch

BuildRequires: eclipse-pde >= 1:3.6.0
BuildRequires: tycho
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
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
pushd org.moreunit.build
%pom_disable_module ../org.moreunit.test.dependencies
%pom_disable_module ../org.moreunit.core.test
%pom_disable_module ../org.moreunit.test
%pom_disable_module ../org.moreunit.mock.test
%pom_disable_module ../org.moreunit.mock.it
mvn-rpmbuild -DskipTychoVersionCheck=true clean install
popd

%install
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     org.moreunit.updatesite/target/org.moreunit-%{version}.zip 
pushd %{buildroot}%{install_loc}
mv org.moreunit-%{version}/features/ .
mv org.moreunit-%{version}/plugins/ .
rm -fr org.moreunit-%{version}
pushd features
for f in `ls -1 * | grep jar$`; do
    unzip $f -d ./${f/.jar//};
done
rm -fr ./*.jar
popd

popd

%files
%{install_loc}
%doc org.moreunit.plugin/help/documentation.html

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_1jpp7
- rebuild with maven-local

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1_1jpp7
- new version

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 2.4.6-alt1_2jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt2_1jpp6
- fixed build

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_1jpp6
- update to new release by jppimport

* Fri Mar 11 2011 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_1jpp6
- new version

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1_2jpp6
- new version

