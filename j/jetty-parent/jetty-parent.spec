# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jetty-parent
Version:        19
Release:        alt2_7jpp7
Summary:        Jetty parent POM file

Group:          Development/Java
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://repo1.maven.org/maven2/org/eclipse/jetty/%{name}/%{version}/%{name}-%{version}.pom
# rpmlint config file (fedpkg lint will use this)
Source1:        .rpmlint
Source2:        http://www.eclipse.org/legal/epl-v10.html
Source3:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local

Requires:       jpackage-utils
Source44: import.info

%description
Jetty parent POM file

%prep
%setup -q -c -T
cp -p %{SOURCE2} %{SOURCE3} .

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE0} \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom

%files
%doc epl-v10.html LICENSE-2.0.txt
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 19-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 19-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 19-alt1_4jpp7
- new version

