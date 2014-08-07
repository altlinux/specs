Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

%global base_name   daemon
%global short_name  commons-%{base_name}

Name:           apache-%{short_name}
Version:        1.0.11
Release:        alt2_1jpp7
Summary:        Defines API to support an alternative invocation mechanism
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/%{base_name}
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:         0001-execve-path-warning.patch
Patch1:         apache-commons-daemon-JAVA_OS.patch
Patch2:         apache-commons-daemon-s390x.patch
Patch3:         apache-commons-daemon-ppc64.patch
BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  apache-commons-parent
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  xmlto

Requires:         jpackage-utils


# This should go away with F-17
Provides:       jakarta-%{short_name} = 1:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} <= 1:1.0.1
Source44: import.info


%description
The scope of this package is to define an API in line with the current
Java Platform APIs to support an alternative invocation mechanism
which could be used instead of the public static void main(String[])
method.  This specification covers the behavior and life cycle of what
we define as Java daemons, or, in other words, non interactive
Java applications.

%package        jsvc
Summary:        Java daemon launcher
Group:          Development/Java
Provides:       jsvc = 1:%{version}-%{release}

Provides:       jakarta-%{short_name}-jsvc = 1:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-jsvc <= 1:1.0.1

%description    jsvc
%{summary}.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch:      noarch

Obsoletes:      jakarta-%{short_name}-javadoc <= 1:1.0.1

%description    javadoc
%{summary}.


%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1 -b .execve
%patch1 -p1 -b .java_os
%patch2 -p1 -b .s390x
%patch3 -p1 -b .ppc64

# remove java binaries from sources
rm -rf src/samples/build/

chmod 644 src/samples/*
cd src/native/unix
xmlto man man/jsvc.1.xml


%build

# build native jsvc
pushd src/native/unix
%configure --with-java=%{java_home}
# this is here because 1.0.2 archive contains old *.o
make clean
make %{?_smp_mflags}
popd

# build jars
mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  install javadoc:javadoc



%install

# install native jsvc
install -Dpm 755 src/native/unix/jsvc $RPM_BUILD_ROOT%{_bindir}/jsvc
install -Dpm 644 src/native/unix/jsvc.1 $RPM_BUILD_ROOT%{_mandir}/man1/jsvc.1

# jars
install -Dpm 644 target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar


# pom
install -Dpm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.apache.commons:%{short_name}"


# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :


%files
%doc LICENSE.txt PROPOSAL.html NOTICE.txt RELEASE-NOTES.txt src/samples
%doc src/docs/*
%{_javadir}/%{name}.jar
%{_javadir}/%{short_name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}


%files jsvc
%doc LICENSE.txt
%{_bindir}/jsvc
%{_mandir}/man1/jsvc.1*


%files javadoc
%doc %{_javadocdir}/%{name}
%doc LICENSE.txt


%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.11-alt2_1jpp7
- rebuild with maven-local

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0.11-alt1_1jpp7
- fc update

* Mon Oct 08 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.10-alt1_4jpp7
- new version

* Sat Jan 01 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_0.r831676.4jpp6
- new version

