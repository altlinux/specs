Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global project_name MultithreadedTC
Name:           multithreadedtc
Version:        1.01
Release:        alt3_13jpp7
Summary:        A framework for testing concurrent Java application

Group:          Development/Java
License:        BSD 
URL:            http://www.cs.umd.edu/projects/PL/multithreadedtc
#http://multithreadedtc.googlecode.com/files/MultithreadedTC-1.01-source.zip
Source0:        %{project_name}-%{version}-source.zip
Source1:        %{name}.pom
Patch0:        %{name}-build.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit
BuildRequires: junit

Requires:       jpackage-utils
Requires:      junit

Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils
Source44: import.info

%description
MultithreadedTC is a framework for testing concurrent applications. 
It features a metronome that is used to provide fine control over
the sequence of activities in multiple threads.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{project_name}-%{version}-source
%patch0 -p0 -b .sav

rm -f *.jar

sed -i 's/\r//' web/docs/package-list
sed -i 's/\r//' web/docs/stylesheet.css
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' README.txt

%build
ant

%install

# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 %{project_name}-%{version}.jar   %{buildroot}%{_javadir}/%{project_name}-%{version}.jar

(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; \
    do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%add_to_maven_depmap edu.umd.cs.mtc multithreadedtc %{version} JPP %{project_name}
%add_to_maven_depmap edu.umd.cs.mtc multithreadedtc-jdk14 %{version} JPP %{project_name}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} \
    %{buildroot}%{_mavenpomdir}/JPP-%{project_name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr web/docs/* %{buildroot}%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
rm -rf web/docs

%files
%doc LICENSE.txt README.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
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

