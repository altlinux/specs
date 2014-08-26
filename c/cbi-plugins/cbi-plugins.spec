# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven-local
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global tag cbi-plugins-1.0.3

Name:           cbi-plugins
Version:        1.0.3
Release:        alt1_1jpp7
Summary:        A set of helpers for Eclipse CBI

Group:          Development/Java
License:        EPL
URL:            http://git.eclipse.org/c/cbi/org.eclipse.cbi.maven.plugins.git/
Source0:        http://git.eclipse.org/c/cbi/org.eclipse.cbi.maven.plugins.git/snapshot/org.eclipse.cbi.maven.plugins-%{tag}.tar.bz2
BuildArch:      noarch

BuildRequires:  tycho
BuildRequires:  tycho-extras
BuildRequires:  xmvn
Requires:       tycho
Requires:       tycho-extras
Requires:       jpackage-utils
Source44: import.info

%description
A set of helpers for Eclipse CBI.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n org.eclipse.cbi.maven.plugins-%{tag}

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 eclipse-cbi-plugin/target/eclipse-cbi-plugin-*.jar \
        %{buildroot}%{_javadir}/eclipse-cbi-plugin.jar

install -m 644 eclipse-jarsigner-plugin/target/eclipse-jarsigner-plugin-*.jar \
        %{buildroot}%{_javadir}/eclipse-jarsigner-plugin.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}

install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-cbi-plugins-parent.pom
%add_maven_depmap JPP-cbi-plugins-parent.pom

install -pm 644 eclipse-cbi-plugin/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-eclipse-cbi-plugin.pom
%add_maven_depmap JPP-eclipse-cbi-plugin.pom eclipse-cbi-plugin.jar

install -pm 644 eclipse-jarsigner-plugin/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-eclipse-jarsigner-plugin.pom
%add_maven_depmap JPP-eclipse-jarsigner-plugin.pom eclipse-jarsigner-plugin.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/
rm -rf target/site/api*

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_1jpp7
- new release

