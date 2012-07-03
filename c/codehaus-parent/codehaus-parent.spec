Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           codehaus-parent
Version:        3
Release:        alt1_4jpp7
Summary:        Parent pom file for codehaus projects

Group:          Development/Java
License:        ASL 2.0
URL:            http://codehaus.org/
#Next version with license is at https://github.com/sonatype/codehaus-parent/blob/master/pom.xml
Source0:        http://repo1.maven.org/maven2/org/codehaus/codehaus-parent/3/codehaus-parent-3.pom
BuildArch:      noarch

BuildRequires:  jpackage-utils

Requires:       jpackage-utils
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils
Source44: import.info

%description
This package contains the parent pom file for codehaus projects.


%prep
%setup -q -c -T


%build


%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %SOURCE0 \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_to_maven_depmap org.codehaus codehaus-parent %{version} JPP %{name}


%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:3-alt1_4jpp7
- fc version

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:3-alt1_1jpp6
- fixed build

