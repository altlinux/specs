Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version_maj 1
%define version_min 1
%define version_rev 0
%define version_tag GA
%define version_full %{version_maj}.%{version_min}.%{version_rev}.%{version_tag}

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/jbpm/bpel/%{version_full}
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

 
Summary:        JBoss JBPM BPEL
Name:           jboss-jbpm-bpel
Version:        %{version_maj}.%{version_min}.%{version_rev}
Release:        alt1_2jpp5
Epoch:          0
License:        LGPLv2+
Group:          Development/Java
URL:            http://jbpm.org/
Source0:        %{name}-%{version_full}-tp.tar.gz
BuildArch:      noarch

%description
Web services orchestration platform.

%if %{with_repolib}
%package repolib
Summary:	 Artifacts to be uploaded to a repository library
Group:	         Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n jbpm

%build
# FIXME: One day this should actually... you know, build something.

%install

install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -p -m 0644 bpel/%{version_full}/lib/*.?ar $RPM_BUILD_ROOT%{_javadir}/%{name}

%if %{with_repolib}
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
cp -p bpel/%{version_full}/lib/* $RPM_BUILD_ROOT%{repodirlib}
# FIXME: (dwalluck): We need to install our own component-info.xml so that the version is correct
install -m 644 bpel/%{version_full}/component-info.xml $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
%endif

%files
%{_javadir}/%{name}

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_2jpp5
- new version

