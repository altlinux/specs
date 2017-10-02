%filter_from_requires /^java-headless/d

Name:     tomcatjss
Version:  7.2.4
Release:  alt1%ubt
Summary:  JSSE implementation using JSS for Tomcat
License:  LGPLv2+
Group:    System/Libraries
URL:      http://pki.fedoraproject.org/

Source0:  http://pki.fedoraproject.org/pki/sources/%{name}/%{name}-%{version}.tar.gz

BuildRequires(pre): rpm-macros-java rpm-build-ubt
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
BuildRequires: ant
BuildRequires: apache-commons-lang
BuildRequires: jss >= 4.4.2
BuildRequires: tomcat >= 8.0.18

Conflicts: tomcat-native
BuildArch: noarch

%description
A Java Secure Socket Extension (JSSE) implementation
using Java Security Services (JSS) for Tomcat 7.

NOTE:  The 'tomcatjss' package conflicts with the 'tomcat-native' package
       because it uses an underlying NSS security model rather than the
       OpenSSL security model, so these two packages may not co-exist.

%prep

%setup
chmod -c -x LICENSE README

%build

ant -f build.xml -Djnidir=%{_jnidir}
ant -f build.xml -Djnidir=%{_jnidir} dist

%install

# Unpack the files we just built
cd dist/binary
unzip %{name}-%{version}.zip -d %{buildroot}

%files
%doc README LICENSE
%{_javadir}/*

%changelog
* Fri Sep 22 2017 Stanislav Levin <slev@altlinux.org> 7.2.4-alt1%ubt
- Update to upstream's 7.2.4 version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.4-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.3-alt1_2jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.3-alt1_1jpp8
- new version

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 7.1.0-alt1_2
- new version

