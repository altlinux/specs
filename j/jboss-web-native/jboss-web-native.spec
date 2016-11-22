# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ perl(DynaLoader.pm) perl(Exporter.pm) perl(Fcntl.pm) perl(IO/File.pm) perl(find.pl)
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-web-native
%define version 2.0.10
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

# The version of tomcat native that this package is based on:
%global tcn_version 1.1.22

Name:             jboss-web-native
Version:          2.0.10
Release:          alt1_9jpp8
Summary:          JBoss Web Native
Group:            Development/Other
License:          LGPLv2+ and ASL 2.0
URL:              http://www.jboss.org/

Source0:          http://downloads.jboss.org/jbossnative/%{namedversion}/jboss-native-%{version}-src-ssl.tar.gz

# In order to avoid a conflict with the tomcat-native package it is necessary
# to rename the library from libtcnative to libjbnative:
Patch0: %{name}-rename-so-to-jbnative.patch

BuildRequires:    libapr1-devel
BuildRequires:    autoconf-common
BuildRequires:    automake-common
BuildRequires:    gcc-common
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    make
BuildRequires:    libssl-devel
Source44: import.info

%description
This package contains support for Apache Portable Runtime (APR) in JBoss AS.

%package devel
Group: Development/Other
Summary: JBoss Web Native development files
Requires: jboss-web-native = %{version}
Requires: libapr1-devel
Requires: libssl-devel

%description devel
This package provides the support files which can be used to
build applications using the JBoss Web native library.

%prep
%setup -q -n jboss-native-%{version}-src-ssl/srclib/tomcat-native-%{tcn_version}
%patch0 -p1

%build

# In order to rename the output library we need to modify the configure.in file
# (with patch 0) and then regenerate the configure script:
autoreconf --force

# Now we can run the modified configure script:
%configure \
--with-apr=%{_bindir}/apr-1-config \
--with-java-home=%{java_home} \
--with-java-platform=2

# And build:
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/libjbnative-1.so.*

%files devel
%{_libdir}/libjbnative-1.so
%{_libdir}/pkgconfig/jbnative-1.pc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_8jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_4jpp7
- new release

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_3jpp7
- new version

