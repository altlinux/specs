Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           mojo-parent
Version:        30
Release:        alt4_2jpp7
Summary:        Codehaus MOJO parent project pom file

Group:          Development/Java
License:        ASL 2.0
URL:            http://mojo.codehaus.org/
Source0:        http://repo1.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  codehaus-parent
BuildRequires:  maven-local
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
# hack for proper compliation of maven plugins
sed -i -e 's,<mojo.java.target>1.4</mojo.java.target>,<mojo.java.target>${maven.compiler.target}</mojo.java.target>,' pom.xml

%build
mvn-rpmbuild install

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom -a org.codehaus.mojo:mojo

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:30-alt4_2jpp7
- rebuild with maven-local

* Sat Jul 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:30-alt3_2jpp7
- fixed 1.4 java mojo target in pom

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:30-alt2_2jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:30-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Tue Aug 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:30-alt1_1jpp7
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:20-alt1_2jpp6
- new version

