# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
Name:     tomcatjss
Version:  7.1.0
Release:  alt1_2
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
BuildRequires:    java-devel
BuildRequires:    jpackage-utils >= 0:1.7.5-15
BuildRequires:    jss >= 4.2.6-24
BuildRequires:    tomcat >= 7.0.27

Requires:         java
Requires:         jpackage-utils >= 0:1.7.5-15
Requires:         jss >= 4.2.6-24
Requires:         tomcat >= 7.0.27

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

%build

ant -f build.xml -Djnidir=%{_jnidir}
ant -f build.xml -Djnidir=%{_jnidir} dist

%install

# Unpack the files we just built
cd dist/binary
unzip %{name}-%{version}.zip -d %{buildroot}

# Install our files
cd %{buildroot}%{_javadir}
mv %{name}.jar %{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{name}.jar
mkdir -p %{buildroot}%{_datadir}/doc/%{name}-%{version}

%files
%doc %attr(644,root,root) README LICENSE
%attr(00755,root,root) %{_datadir}/doc/%{name}-%{version}
%{_javadir}/*

%changelog
* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 7.1.0-alt1_2
- new version

