# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
Name:     tomcatjss
Version:  7.1.3
Release:  alt1_2jpp8
Summary:  JSSE implementation using JSS for Tomcat
URL:      http://pki.fedoraproject.org/
License:  LGPLv2+
Group:    System/Libraries

BuildArch:      noarch

Source0:  http://pki.fedoraproject.org/pki/sources/%{name}/%{name}-%{version}.tar.gz

# jpackage-utils requires versioning to meet both build and runtime requirements
# jss requires versioning to meet both build and runtime requirements
# tomcat requires versioning to meet both build and runtime requirements
BuildRequires:    ant
BuildRequires:    apache-commons-lang
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    jss >= 4.2.6
%if 0%{?fedora} >= 23
BuildRequires:    tomcat >= 8.0.18
%else
BuildRequires:    tomcat >= 7.0.40
%endif

Requires:         apache-commons-lang
%if 0%{?fedora} >= 21
%else
%endif
Requires: javapackages-tools rpm-build-java
Requires:         jss >= 4.2.6
%if 0%{?fedora} >= 23
Requires:         tomcat >= 8.0.18
%else
Requires:         tomcat >= 7.0.40
%endif

# The 'tomcatjss' package conflicts with the 'tomcat-native' package
# because it uses an underlying NSS security model rather than the
# OpenSSL security model, so these two packages may not co-exist.
# (see Bugzilla Bug #441974 for details)
Conflicts:        tomcat-native

%if 0%{?rhel}
# For EPEL, override the '_sharedstatedir' macro on RHEL
%define           _sharedstatedir    /var/lib
%endif
Source44: import.info

%description
A Java Secure Socket Extension (JSSE) implementation
using Java Security Services (JSS) for Tomcat 7.

NOTE:  The 'tomcatjss' package conflicts with the 'tomcat-native' package
       because it uses an underlying NSS security model rather than the
       OpenSSL security model, so these two packages may not co-exist.

%prep

%setup -q
chmod -c -x LICENSE README

%build

ant -f build.xml -Djnidir=%{_jnidir}
ant -f build.xml -Djnidir=%{_jnidir} dist

%install

# Unpack the files we just built
cd dist/binary
unzip %{name}-%{version}.zip -d %{buildroot}

# Install our files
cd %{buildroot}%{_javadir}
%if 0%{?rhel} || 0%{?fedora} < 21
mv %{name}.jar %{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{name}.jar
%endif

%files
%doc README LICENSE
%{_javadir}/*

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.3-alt1_2jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.3-alt1_1jpp8
- new version

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 7.1.0-alt1_2
- new version

