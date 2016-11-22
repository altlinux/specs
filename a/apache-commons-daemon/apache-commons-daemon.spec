Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat

%global base_name   daemon
%global short_name  commons-%{base_name}

Name:           apache-%{short_name}
Version:        1.0.15
Release:        alt1_11jpp8
Summary:        Defines API to support an alternative invocation mechanism
License:        ASL 2.0
Group:          System/Base
URL:            http://commons.apache.org/%{base_name}
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch1:         apache-commons-daemon-JAVA_OS.patch
# backport from https://fisheye6.atlassian.com/changelog/commons?cs=1458896
Patch2:         apache-commons-daemon-secondary.patch
# backport from http://svn.apache.org/viewvc?view=revision&revision=1533345
# https://issues.apache.org/jira/browse/DAEMON-308
Patch3:         apache-commons-daemon-aarch64.patch
BuildRequires:  maven-local
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  apache-commons-parent
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  xmlto
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
Group:          System/Base
Provides:       jsvc = 1:%{version}-%{release}

%description    jsvc
%{summary}.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch:      noarch

%description    javadoc
%{summary}.


%prep
%setup -q -n %{short_name}-%{version}-src
%patch1 -p1 -b .java_os
%patch2 -p1 -b .secondary
%patch3 -p1 -b .aarch64

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
%mvn_file  : %{short_name} %{name}
%mvn_alias : org.apache.commons:%{short_name}
%mvn_build


%install
# install native jsvc
install -Dpm 755 src/native/unix/jsvc $RPM_BUILD_ROOT%{_bindir}/jsvc
install -Dpm 644 src/native/unix/jsvc.1 $RPM_BUILD_ROOT%{_mandir}/man1/jsvc.1

%mvn_install


%files -f .mfiles
%doc LICENSE.txt PROPOSAL.html NOTICE.txt RELEASE-NOTES.txt src/samples
%doc src/docs/*


%files jsvc
%doc LICENSE.txt NOTICE.txt
%{_bindir}/jsvc
%{_mandir}/man1/jsvc.1*


%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.15-alt1_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.15-alt1_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.15-alt1_4jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.13-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.11-alt2_1jpp7
- rebuild with maven-local

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0.11-alt1_1jpp7
- fc update

* Mon Oct 08 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.10-alt1_4jpp7
- new version

* Sat Jan 01 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_0.r831676.4jpp6
- new version

