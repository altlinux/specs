Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           qdox16-poms
Version:        1.0
Release:	alt2_0jpp5
Epoch:          0
Summary:        pom files for qdox
License:        BSD
URL:            http://repo1.maven.org/maven2
Group:          Development/Java
Source1:        qdox-1.6.pom
Source2:        qdox-1.6-SNAPSHOT.pom

Buildarch:      noarch

%description
%summary.
Temporary package until qdox will be upgraded to 1.9/1.10.

%prep

%build

%install
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.qdox.pom
%add_to_maven_depmap com.thoughtworks.qdox qdox 1.6.3 JPP qdox

%files
%{_datadir}/maven2/*
%{_mavendepmapfragdir}/*

%changelog
* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0jpp5
- temporary release to finish qdox upgrade

* Thu Mar 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0jpp5
- temporary package until qdox upgrade to 1.9
