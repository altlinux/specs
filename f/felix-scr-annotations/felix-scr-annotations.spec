Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
%global project   felix
%global bundle    org.apache.felix.scr.annotations
Name:          felix-scr-annotations
Version:       1.9.6
Release:       alt1_4jpp7
Summary:       Annotations for SCR
License:       ASL 2.0
URL:           http://felix.apache.org/
Source0:       http://www.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildRequires: mvn(org.apache.felix:felix-parent)
BuildRequires: mvn(org.apache.felix:org.apache.felix.scr.generator)

BuildRequires: maven-local
BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-surefire-plugin
# i dont know which package as missing this required...
BuildRequires: mvn(org.mockito:mockito-all)

%if %{?fedora} == 20
Requires:      mvn(org.apache.felix:org.apache.felix.scr.generator)
%endif

BuildArch:     noarch
Source44: import.info

%description
Annotations for generating OSGi service descriptors.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%build

%mvn_file :%{bundle} %{project}/%{bundle}
# no test to run
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%if %{?fedora} != 20
%mvn_install
%else

mkdir -p %{buildroot}%{_javadir}/%{project}
install -m 644 target/%{bundle}-%{version}.jar  \
  %{buildroot}%{_javadir}/%{project}/%{bundle}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{project}-%{bundle}.pom
%add_maven_depmap JPP.%{project}-%{bundle}.pom %{project}/%{bundle}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%endif

%if %{?fedora} != 20
%files -f .mfiles
%else
%files
%{_javadir}/%{project}/%{bundle}.jar
%{_mavenpomdir}/JPP.%{project}-%{bundle}.pom
%{_mavendepmapfragdir}/%{name}
%endif
%doc LICENSE NOTICE changelog.txt

%if %{?fedora} != 20
%files javadoc -f .mfiles-javadoc
%else
%files javadoc
%{_javadocdir}/%{name}
%endif
%doc LICENSE NOTICE

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.6-alt1_4jpp7
- new release

