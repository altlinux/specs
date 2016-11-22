Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jsf-2.2-api
%define version 2.2.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-jsf-2.2-api
Version:       2.2.0
Release:       alt1_7jpp8
Summary:       JavaServer Faces 2.2 API
License:       (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:           http://www.jboss.org
Source0:       https://github.com/jboss/jboss-jsf-api_spec/archive/jboss-jsf-api_2.2_spec-%{namedversion}.tar.gz
Source1:       cddl.txt
Source2:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
BuildRequires: mvn(com.sun.faces:jsf-impl)
BuildRequires: mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.spec.javax.el:jboss-el-api_2.2_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet.jsp:jboss-jsp-api_2.2_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet.jstl:jboss-jstl-api_1.2_spec)

BuildArch:     noarch
Source44: import.info

%description
This package contains JSR-344: JavaServer Faces 2.2 API.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc	
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jsf-api_spec-jboss-jsf-api_2.2_spec-%{namedversion}

# We don't have this
%pom_remove_dep "org.jboss.spec:jboss-javaee-all-6.0"
# But we have this
%pom_add_dep "javax.inject:javax.inject"
%pom_add_dep "javax.enterprise:cdi-api"

cp %{SOURCE1} .
cp %{SOURCE2} .

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc cddl.txt LICENSE LICENSE-2.0.txt
%doc README

%files javadoc -f .mfiles-javadoc
%doc cddl.txt LICENSE LICENSE-2.0.txt
%doc README


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_7jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_4jpp8
- unbootsrap build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

