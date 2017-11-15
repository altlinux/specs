Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-java
BuildRequires: gcc-c++ rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global site_ver  0-95

Name:             jpathwatch
Version:          0.95
Release:          alt1_12jpp8
Summary:          Java library for monitoring directories for changes
License:          GPLv2
# http://jpathwatch.wordpress.com/
URL:              http://%{name}.wordpress.com/
# wget http://jpathwatch.svn.sourceforge.net/viewvc/jpathwatch/branches/0-94/jpathwatch/?view=tar -O jpathwatch-0.94.tar.gz
# wget http://%{name}.svn.sourceforge.net/viewvc/%{name}/branches/%{site_ver}/%{name}/?view=tar -O %{name}-%{version}.tar.gz
Source0:          %{name}-%{version}.tar.gz
Source1:          https://repo1.maven.org/maven2/net/sf/%{name}/%{name}/%{version}/%{name}-%{version}.pom

Patch0:           %{name}-fsf-address.patch

BuildRequires:    ant
BuildRequires:    javapackages-local

# can't debug .so in jars
%global debug_package %{nil}
Source44: import.info

%description
jpatchwatch is a Java library for monitoring directories
for changes. It uses the host platforma.'s native OS functions
to achieve this to avoid polling.

The following events on a directory can be monitored:

  - File creation and deletion
  - File modification
  - File renaming
  - Changes in subdirectories (recursive monitoring)
  - Invalidation (a watched directory becomes unavailable)


%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch:        noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

%patch0 -p1

%build

# native part
cd %{name}-native/prj/linux/%{name}-native-linux
%if 0%{?__isa_bits} == 64
  make DEFAULTCONF=Release_x86-64bit %{?_smp_mflags} CXXFLAGS="%{optflags}"
%else
  make DEFAULTCONF=Release_x86-32bit %{?_smp_mflags} CXXFLAGS="%{optflags}"
%endif

# java part
cd ../../../..
ant -Dplatforms.JDK_1.5.home=%{_jvmdir}/java jar

# javadoc target exists but doesn't work - generating
find %{name}-java/src -name '*.java' | xargs javadoc -Xdoclint:none -classpath dist:%{name}-%{site_ver}.jar -d doc

%install
%mvn_artifact %{SOURCE1} dist/%{name}-%{site_ver}.jar
%mvn_file : %{name}
%mvn_install -J doc

%files -f .mfiles
%doc README.txt LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.95-alt1_12jpp8
- fc update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.95-alt1_10jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.95-alt1_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.95-alt1_7jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.95-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1_7jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1_5jpp7
- new version

