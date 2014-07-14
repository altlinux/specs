Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           mojo-parent
Version:        30
Release:        alt2_1jpp7
Summary:        Codehaus MOJO parent project pom file

Group:          Development/Java
License:        ASL 2.0
URL:            http://mojo.codehaus.org/
Source0:        http://repo1.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  codehaus-parent
BuildRequires:  maven
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-plugin-cobertura

Requires:       plexus-containers-component-javadoc
Requires:       maven-plugin-plugin
Requires:       junit
Requires:       codehaus-parent
Requires:       jpackage-utils
Source44: import.info

%description
Codehaus MOJO parent project pom file

%prep
%setup -q

%build
mvn-rpmbuild install

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:30-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Tue Aug 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:30-alt1_1jpp7
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:20-alt1_2jpp6
- new version

