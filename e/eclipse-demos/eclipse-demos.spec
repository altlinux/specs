Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
Name:           eclipse-demos
Version:        0.0.1
Release:        alt2_4jpp6
Summary:        Eclipse demonstration screencasts

Group:          Development/Java
License:        Open Publication
URL:            http://sources.redhat.com/eclipse
Source0:        http://overholt.fedorapeople.org/%{name}-%{version}.tar.bz2
BuildArch:      noarch

%description
Screencasts demonstrating various features of Eclipse.

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}-%{version}
cp -p * $RPM_BUILD_ROOT/%{_datadir}/%{name}-%{version}

%files
%dir %{_datadir}/%{name}-%{version}
%doc %{_datadir}/%{name}-%{version}/openpub.html
%{_datadir}/%{name}-%{version}/*.ogg

%changelog
* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt2_4jpp6
- build for new eclipse version

* Thu Jul 31 2008 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt2_2jpp6
- rebuild with eclipse 3.3.2

* Tue Dec 04 2007 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_2jpp5.0
- converted from JPackage by jppimport script

