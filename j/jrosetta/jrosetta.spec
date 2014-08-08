# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jrosetta
Version:        1.0.4
Release:        alt1_7jpp7
Summary:        A common base to build a graphical console

Group:          Development/Java
License:        GPLv2
URL:            http://dev.artenum.com/projects/JRosetta
Source0:        http://maven.artenum.com/content/groups/public/com/artenum/%{name}/%{version}/%{name}-%{version}-sources.jar

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local

BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-clean-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit4

Requires:       jpackage-utils
Source44: import.info

%description
JRosetta provides a common base for graphical component that could be used
to build a graphical console in Swing with the latest requirements, such as
command history, completion and so on for instance for scripting language
or command line.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
# remove jar format related directory
rm -fr ../META-INF
#wrong-file-end-of-line-encoding
cp -p CHANGE.txt CHANGE.txt.CRLF
sed -i -e 's/\r//' CHANGE.txt
touch -r CHANGE.txt.CRLF CHANGE.txt
rm CHANGE.txt.CRLF
# remove deployement dependency
%pom_xpath_remove "pom:build/pom:extensions" pom.xml

%build
mvn-rpmbuild -e install javadoc:aggregate

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp -p modules/%{name}-api/target/%{name}-api-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-API-%{version}.jar
ln -s %{name}-API-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-API.jar
cp -p modules/%{name}-engine/target/%{name}-engine-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-engine-%{version}.jar
ln -s %{name}-engine-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-engine.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 modules/%{name}-api/pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-API.pom
install -pm 644 modules/%{name}-engine/pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-engine.pom

%add_maven_depmap JPP-%{name}.pom
%add_maven_depmap JPP-%{name}-API.pom %{name}-API.jar
%add_maven_depmap JPP-%{name}-engine.pom %{name}-engine.jar

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavenpomdir}/JPP-%{name}-*.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}-*.jar
%doc LICENSE.txt COPYRIGHT.txt CHANGE.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_7jpp7
- re-imported for xmvn migration

* Fri Apr 19 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- New version (ALT #28870)
- Build by maven

* Thu Sep 10 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt2
- Fix BuildRequires (ALT #21518)

* Thu Jul 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1
- initial from Fedora

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 kwizart < kwizart at gmail.com > - 1.0.2-1
- Fix License (GPLv2 only)
- Fix Summary
- Update to 1.0.2 - previous patch merged upstream

* Mon Oct 27 2008 kwizart < kwizart at gmail.com > - 1.0.1-1
- Initial Package

