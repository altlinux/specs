# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           swt-chart
Version:        0.8.0
Release:        alt1_5jpp7
Summary:        SWTChart Feature

Group:          Development/Java
License:        EPL
URL:            http://www.swtchart.org/
# svn export https://swt-chart.svn.sourceforge.net/svnroot/swt-chart/tags/%%{version}/ %%{name}-%%{version}
# pushd %%{name}-%%{version} && rm -rf org.swtchart.{examples{,.ext},ext} && popd
# tar -cJf %%{name}-%%{version}.tar.xz %%{name}-%%{version}
Source0:        %{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  tycho >= 0.14.0

Requires:       jpackage-utils
Requires:       eclipse-platform >= 3.4.0
Source44: import.info

%description
SWTChart is a light-weight charting component for SWT.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q
# Create the poms
mvn-rpmbuild org.eclipse.tycho:tycho-pomgenerator-plugin:generate-poms -DgroupId=org.swtchart

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}

# Pom
install -p -m 644 org.swtchart/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Jar
install -p -m 644 org.swtchart/target/org.swtchart-%{version}-SNAPSHOT.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{_javadir}/%{name}.jar %{buildroot}%{_javadir}/org.swtchart_%{version}.jar

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# Javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs %{buildroot}%{_javadocdir}/%{name}


%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_5jpp7
- new version

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_4jpp7
- new version

