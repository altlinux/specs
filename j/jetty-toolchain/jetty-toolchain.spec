BuildRequires: maven-enforcer-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jetty-toolchain
Version:        1.4
Release:        alt3_4jpp7
Summary:        Jetty Toolchain main POM file

Group:          Development/Java
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
# rpmlint config file (fedpkg lint will use this)
Source1:        .rpmlint
BuildArch:      noarch

BuildRequires:  maven
BuildRequires:  jpackage-utils
BuildRequires:  jetty-parent

Requires:       maven
Requires:       jpackage-utils
Requires:       jetty-parent
Source44: import.info

%description
Jetty Toolchain main POM file

%prep
%setup -q

%build
pushd %{name}
mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  install

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
pushd %{name}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom
popd

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_4jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_4jpp7
- fixed build

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_4jpp7
- new version

