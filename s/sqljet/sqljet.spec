Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           sqljet
Version:        1.0.4
Release:        alt1_8jpp7
Summary:        Pure Java SQLite

Group:          Development/Java
License:        GPLv2
URL:            http://sqljet.com/
# Obtained by sh fetch-sqljet.sh
Source0:        %{name}-%{version}.tar.xz
Source1:        fetch-sqljet.sh
Source2:        %{name}-browser.sh
Source3:        %{name}-browser.desktop
Patch0:         %{name}-javadoc.patch
Patch1:         %{name}-1.0.4-suppressdupes.patch

BuildRequires:  ant
BuildRequires:  antlr
BuildRequires:  antlr3-java
BuildRequires:  antlr3-tool
BuildRequires:  easymock2
BuildRequires:  netbeans-platform
BuildRequires:  junit4
BuildRequires:  desktop-file-utils
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
%setup -q
%patch0
%patch1 -p1

find \( -name '*.class' -o -name '*.jar' \) -delete

pushd sqljet-examples/browser/lib
ln -s %{_javadir}/netbeans/swing-outline.jar org-netbeans-swing-outline.jar
popd

# versions in pom xml are to be processed by ant, but we don't need that so just fix them here
sed -i 's/%sqljet.version%/%{version}/;s/%antlr.version%/3.1.3/' pom.xml sqljet/osgi/MANIFEST.MF

%build
export CLASSPATH=$(build-classpath antlr3-runtime antlr3 antlr stringtemplate4 easymock2 junit4)

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jars osgi javadoc

jar umf sqljet/osgi/MANIFEST.MF build/sqljet.jar

%install
# jars
mkdir -p %{buildroot}%{_javadir}
install -m 755  build/sqljet.jar %{buildroot}%{_javadir}/%{name}.jar
install -m 755  build/sqljet-browser.jar  %{buildroot}%{_javadir}/%{name}-browser.jar

# maven metadata
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
%doc COPYING README.txt
%{_javadir}/%{name}.jar

%files browser
%{_javadir}/%{name}-browser.jar
%{_bindir}/%{name}-browser
%{_datadir}/applications/%{name}-browser.desktop

%files javadoc
%doc COPYING
%doc %{_javadocdir}/*

%changelog
* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_8jpp7
- fixed build with antlr3

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_4_redhat_1jpp6
- new jpp relase

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp6
- new version

