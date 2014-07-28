# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jsilver
Version:        1.0.0
Release:        alt1_4jpp7
Summary:        A pure-Java implementation of Clearsilver

Group:          Development/Java
License:        ASL 2.0 

URL:            http://code.google.com/p/jsilver/
# svn export http://jsilver.googlecode.com/svn/tags/jsilver-1.0.0 jsilver-1.0.0
# tar caf jsilver-1.0.0.tar.xz jsilver-1.0.0
Source0:        jsilver-1.0.0.tar.xz

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-plugin-exec
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  sablecc

Requires:       jpackage-utils
Source44: import.info

%description
A pure-Java implementation of Clearsilver, an HTML template system.

%package javadoc
Summary:        API docs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q 
find . -name *.jar -exec rm -f {} \;
ln -s %{_javadir}/sablecc.jar sablecc/

%build
mvn-rpmbuild install javadoc:javadoc

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p build/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- new version

