BuildRequires: javapackages-local
Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global project_name MultithreadedTC
Name:           multithreadedtc
Version:        1.01
Release:        alt4_21jpp8
Summary:        A framework for testing concurrent Java application
License:        BSD 
URL:            http://www.cs.umd.edu/projects/PL/multithreadedtc
#http://multithreadedtc.googlecode.com/files/MultithreadedTC-1.01-source.zip
Source0:        %{project_name}-%{version}-source.zip
Source1:        %{name}.pom
Patch0:         %{name}-build.patch

BuildArch: noarch

BuildRequires: java-devel >= 1.6.0
BuildRequires: jpackage-utils
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit
BuildRequires: junit

Requires:      jpackage-utils
Requires:      junit
Source44: import.info

%description
MultithreadedTC is a framework for testing concurrent applications. 
It features a metronome that is used to provide fine control over
the sequence of activities in multiple threads.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{project_name}-%{version}-source
%patch0 -p0 -b .sav

find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

sed -i 's/\r//' web/docs/package-list
sed -i 's/\r//' web/docs/stylesheet.css
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' README.txt

%build
ant

%install

# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 %{project_name}-%{version}.jar   %{buildroot}%{_javadir}/%{project_name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} \
    %{buildroot}%{_mavenpomdir}/JPP-%{project_name}.pom
%add_maven_depmap JPP-%{project_name}.pom %{project_name}.jar -a "edu.umd.cs.mtc:multithreadedtc-jdk14,com.googlecode.multithreadedtc:multithreadedtc"

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr web/docs/* %{buildroot}%{_javadocdir}/%{name}/
rm -rf web/docs

%files -f .mfiles
%doc LICENSE.txt README.txt
%{_javadir}/*
%{_mavenpomdir}/*

# Workaround for rpm bug, remove in F23
%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.01-alt4_21jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.01-alt3_21jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.01-alt3_20jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.01-alt3_19jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.01-alt3_13jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.01-alt3_12jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.01-alt3_2jpp6
- new jpp relase

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.01-alt3_1jpp5
- fixes for java6 support

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.01-alt2_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.01-alt1_1jpp5
- converted from JPackage by jppimport script

