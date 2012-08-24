BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           guava
Version:        09
Release:        alt1_2jpp7
Summary:        Google Core Libraries for Java

Group:          Development/Java
License:        ASL 2.0 
URL:            http://code.google.com/p/guava-libraries
#svn export http://guava-libraries.googlecode.com/svn/tags/release05/ guava-r05
#tar jcf guava-r05.tar.bz2 guava-r05/
Source0:        %{name}-r%{version}.tar.bz2
#Remove parent definition which doesn't really to be used
Patch0:        %{name}-pom.patch

BuildArch: noarch

BuildRequires:  maven
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  jpackage-utils
BuildRequires:  jsr-305 >= 0-0.7.20090319svn
BuildRequires:  ant-nodeps

Requires:       jpackage-utils
Source44: import.info

%description
Guava is a suite of core and expanded libraries that include 
utility classes, Google's collections, io classes, and much 
much more.
This project is a complete packaging of all the Guava libraries
into a single jar.  Individual portions of Guava can be used
by downloading the appropriate module and its dependencies.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-r%{version}

rm -r lib/* gwt-*

%patch0 -p1


%build

mvn-rpmbuild install javadoc:aggregate

%install

# jars
install -Dpm 644 target/guava-r%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom


%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "com.google.collections:google-collections"

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :


%files
%doc COPYING README README.maven
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 09-alt1_2jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 09-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

