Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           codehaus-parent
Version:        4
Release:        alt2_4jpp7
Summary:        Parent pom file for codehaus projects

Group:          Development/Java
License:        ASL 2.0
URL:            http://codehaus.org/
#Next version with license is at https://github.com/sonatype/codehaus-parent/blob/master/pom.xml
Source0:        http://repo1.maven.org/maven2/org/codehaus/codehaus-parent/%{version}/codehaus-parent-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Patch0:         %{name}-enforcer.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils

Requires:       jpackage-utils
Source44: import.info

%description
This package contains the parent pom file for codehaus projects.


%prep
%setup -q -c -T
cp -p %{SOURCE0} .
cp -p %{SOURCE1} LICENSE
%patch0

%build


%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 codehaus-parent-%{version}.pom \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom 


%files
%doc LICENSE
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:4-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:4-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:4-alt1_3jpp7
- shared FastInfoset.jar symlink as alternative

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:3-alt1_4jpp7
- fc version

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:3-alt1_1jpp6
- fixed build

