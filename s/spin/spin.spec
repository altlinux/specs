# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           spin
Version:        1.5
Release:        alt2_7jpp7
Summary:        A transparent threading solution for non-freezing Swing applications
License:        LGPLv2
Group:          Development/Java
Url:            http://spin.sourceforge.net/
BuildArch:      noarch

Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-all.zip
Patch0:         %{name}-pom_xml.patch

BuildRequires:  maven
BuildRequires:  jpackage-utils

BuildRequires:  cglib
BuildRequires:  objectweb-asm


Requires:       jpackage-utils

Requires:       cglib
Requires:       objectweb-asm
Source44: import.info


%description
Spin is a small library that concentrates on offering a powerful solution
to build non-freezing Swing applications. Spin enforces good application
design by separating the GUI and non-visual components through interfaces.
If it is used wisely in an application framework, the GUI programmers will
never have to think about threads again.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch
%description javadoc
Documentation for the spin Java library.

%prep
%setup -q
# Remove pre-build jar files
%{__rm} -rf lib
# Compile against the correct version of cglib
%patch0 -p1

%build
# One of the tests tries to access the X display
mvn-rpmbuild install javadoc:aggregate -DskipTests

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 target/%{name}-%{version}.jar $RPM_BUILD_ROOT/%{_javadir}/%{name}.jar
install -d -m 755 ${RPM_BUILD_ROOT}%{_javadocdir}/
cp -r target/site/apidocs ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}
%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%doc license.txt
%{_javadir}/*.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%files javadoc
%doc license.txt
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_7jpp7
- new version

