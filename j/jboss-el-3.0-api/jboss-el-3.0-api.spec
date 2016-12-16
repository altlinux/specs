Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-el-3.0-api
%define version 1.0.5
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-el-3.0-api
Version:          1.0.5
Release:          alt1_1jpp8
Summary:          JSR-341 Expression Language 3.0 API
License:          (CDDL or GPLv2 with exceptions) and ASL 2.0
Url:              https://github.com/jboss/jboss-el-api_spec
Source0:          https://github.com/jboss/jboss-el-api_spec/archive/jboss-el-api_3.0_spec-%{namedversion}.tar.gz
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

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc LICENSE cddl.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE cddl.txt LICENSE-2.0.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.5.Alpha1jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.4.Alpha1jpp8
- new version

