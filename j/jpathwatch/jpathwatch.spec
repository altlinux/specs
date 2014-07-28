# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

%global site_ver  0-94

Name:             jpathwatch
Version:          0.94
Release:          alt1_7jpp7
Summary:          Java library for monitoring directories for changes
License:          GPLv2
Group:            Development/Java
# http://jpathwatch.wordpress.com/
URL:              http://%{name}.wordpress.com/
# wget http://jpathwatch.svn.sourceforge.net/viewvc/jpathwatch/branches/0-94/jpathwatch/?view=tar -O jpathwatch-0.94.tar.gz
# wget http://%{name}.svn.sourceforge.net/viewvc/%{name}/branches/%{site_ver}/%{name}/?view=tar -O %{name}-%{version}.tar.gz
Source0:          %{name}-%{version}.tar.gz

Patch0:           %{name}-fsf-address.patch

BuildRequires:    jpackage-utils
BuildRequires:    ant

Requires:         jpackage-utils

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
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch:        noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

%patch0 -p1

%build

# native part
cd %{name}-native/prj/linux/%{name}-native-linux
%ifarch x86_64 s390x sparc64 ppc64
  make DEFAULTCONF=Release_x86-64bit %{?_smp_mflags} CXXFLAGS="%{optflags}"
%else
  make DEFAULTCONF=Release_x86-32bit %{?_smp_mflags} CXXFLAGS="%{optflags}"
%endif

# java part
cd ../../../..
ant -Dplatforms.JDK_1.5.home=%{_jvmdir}/java jar

# javadoc target exists but doesn't work - generating
find %{name}-java/src -name '*.java' | xargs javadoc -classpath dist:%{name}-%{site_ver}.jar -d doc

%install

# jars
install -d -m 755 %{buildroot}%{_jnidir}
install -p -m 644 dist/%{name}-%{site_ver}.jar %{buildroot}%{_jnidir}/%{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr doc/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc README.txt LICENSE.txt
%{_jnidir}/%{name}.jar

%files javadoc
%doc LICENSE.txt
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1_7jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1_5jpp7
- new version

