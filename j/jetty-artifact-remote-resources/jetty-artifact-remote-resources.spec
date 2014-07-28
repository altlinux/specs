# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jetty-artifact-remote-resources
Version:        1.0
Release:        alt3_8jpp7
Summary:        Jetty toolchain artifact remote resources

Group:          Development/Java
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
# rpmlint config file (fedpkg lint will use this)
Source1:        .rpmlint
BuildArch:      noarch

Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source3:        http://www.eclipse.org/legal/epl-v10.html

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-remote-resources-plugin >= 1.2.1-3
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  jetty-toolchain

Requires:       maven
Requires:       jetty-toolchain
Source44: import.info

%description
Jetty toolchain artifact remote resources

%prep
%setup -q
cp -p %{SOURCE2} %{SOURCE3} .

%build
mvn-rpmbuild -X install

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -Dp -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE-2.0.txt epl-v10.html
%{_mavenpomdir}/JPP-%{name}.pom
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_8jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_5jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_5jpp7
- fixed build

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5jpp7
- new version

