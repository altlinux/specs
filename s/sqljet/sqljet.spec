Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           sqljet
Version:        1.1.7
Release:        alt1_2jpp7
Summary:        Pure Java SQLite

Group:          Development/Java
License:        GPLv2
URL:            http://sqljet.com/
Source0:        http://sqljet.com/files/%{name}-%{version}-src.zip

Source2:        %{name}-browser.sh
Source3:        %{name}-browser.desktop
Source4:        %{name}-build.xml
Source5:        %{name}-pom.xml

BuildRequires:  ant
BuildRequires:  antlr
BuildRequires:  antlr3-java
BuildRequires:  antlr3-tool
BuildRequires:  easymock3
BuildRequires:  netbeans-platform
BuildRequires:  junit
BuildRequires:  desktop-file-utils
BuildRequires:  stringtemplate4
Requires:       antlr3-java
BuildArch: noarch
Source44: import.info

%description
SQLJet is an independent pure Java implementation of a popular SQLite database
management system. SQLJet is a software library that provides API that enables
Java application to read and modify SQLite databases.

%package        browser
Group:          Development/Java
Summary:        SQLJet database browser
Requires:       %{name} = %{version}
Requires:       netbeans-platform

%description    browser
Utility for browsing SQLJet/SQLite databases.

%package        javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}

find \( -name '*.class' -o -name '*.jar' \) -delete

rm -rf gradlew.bat gradlew gradle

cp %{SOURCE4} build.xml

cat > sqljet.build.properties <<EOF
sqljet.version.major=1
sqljet.version.minor=1
sqljet.version.micro=4
sqljet.version.build=local

antlr.version=3.1.3
sqlite.version=3.6.10
EOF


%build
export CLASSPATH=$(build-classpath antlr3-runtime antlr3 antlr stringtemplate4 easymock3 junit)

ant jars osgi javadoc


%install
# jars
mkdir -p %{buildroot}%{_javadir}
install -m 755  build/sqljet.jar %{buildroot}%{_javadir}/%{name}.jar
install -m 755  build/sqljet-browser.jar  %{buildroot}%{_javadir}/%{name}-browser.jar

# maven metadata
cp %{SOURCE5} pom.xml
ant pom
mkdir -p %{buildroot}%{_mavenpomdir}
cp pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadocs
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/javadoc %{buildroot}%{_javadocdir}/%{name}

# browser scripts
install -d %{buildroot}%{_bindir}
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}-browser

desktop-file-install  --dir=%{buildroot}%{_datadir}/applications \
                      %{SOURCE3}

desktop-file-validate %{buildroot}/%{_datadir}/applications/sqljet-browser.desktop

%files
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom
%doc LICENSE.txt README.txt CHANGES.txt
%{_javadir}/%{name}.jar

%files browser
%doc LICENSE.txt
%{_javadir}/%{name}-browser.jar
%{_bindir}/%{name}-browser
%{_datadir}/applications/%{name}-browser.desktop

%files javadoc
%doc LICENSE.txt
%doc %{_javadocdir}/*

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt1_2jpp7
- new release

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_4jpp7
- fc update

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_8jpp7
- fixed build with antlr3

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_4_redhat_1jpp6
- new jpp relase

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp6
- new version

