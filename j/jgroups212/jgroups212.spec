# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:     jgroups212
Version:  2.12.3
Release:  alt1_5jpp7
Summary:  A toolkit for reliable multicast communication

Group:    Development/Java
License:  LGPLv2
URL:      http://www.jgroups.org
# git clone git://github.com/belaban/JGroups.git
# cd JGroups && git checkout Branch_JGroups_2_12 && git checkout-index -f -a --prefix=jgroups212-2.12.3.Final
# find jgroups212-2.12.3.Final/ -name '*.jar' -type f -delete
# tar -cJf jgroups212-2.12.3.Final.tar.xz jgroups212-2.12.3.Final
Source0:  %{name}-%{version}.Final.tar.xz
Patch0:   %{name}-groupid.patch
BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: bsh
BuildRequires: log4j

Requires:      jpackage-utils
Requires:      bsh
Requires:      log4j
Source44: import.info

%description
A toolkit for reliable multicast communication.
It allows developers to create reliable multipoint (multicast) applications
where reliability is a deployment issue, and does not have to be implemented
by the application developer. This saves application developers significant
amounts of time, and allows for the application to be deployed in different
environments, without having to change code.

%package javadoc
Summary:    Javadoc for %{name}
Group:      Development/Java
Requires:   jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}.Final
find . -name \*.jar -exec rm -f {} \;

%patch0 -p1

%build
# Tests to not current run under maven for this project
mvn-rpmbuild -Dmaven.test.skip=true install \
    -Dproject.build.sourceEncoding=UTF-8 \
    javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/jgroups-%{version}.Final.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Fix incorrect permissions on documentation
chmod 644 README

%files
%doc LICENSE README INSTALL.html
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.12.3-alt1_5jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.12.3-alt1_3jpp7
- new fc release

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.12.3-alt1_2jpp7
- new version

