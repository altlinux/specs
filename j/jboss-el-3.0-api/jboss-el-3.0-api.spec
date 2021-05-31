Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             jboss-el-3.0-api
Version:          1.0.13
Release:          alt1_5jpp11
Summary:          JSR-341 Expression Language 3.0 API
License:          (CDDL or GPLv2 with exceptions) and ASL 2.0

%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

URL:              https://github.com/jboss/jboss-el-api_spec
Source0:          %{url}/archive/jboss-el-api_3.0_spec-%{namedversion}.tar.gz
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:          cddl.txt

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)

BuildArch:        noarch
Source44: import.info

%description
The JSR-341 Expression Language 3.0 API classes.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-el-api_spec-jboss-el-api_3.0_spec-%{namedversion}

cp %{SOURCE1} .
cp %{SOURCE2} .

%pom_remove_plugin :maven-source-plugin

%pom_change_dep :javax.el-impl :javax.el

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%build
# tests are broken with the version of el in fedora 33+
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README
%doc --no-dereference LICENSE cddl.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE cddl.txt LICENSE-2.0.txt

%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.0.13-alt1_5jpp11
- update

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.0.13-alt1_2jpp11
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_5jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.5.Alpha1jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.4.Alpha1jpp8
- new version

