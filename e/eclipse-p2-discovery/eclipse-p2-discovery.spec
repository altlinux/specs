BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global src_repo_tag   R4_2_1
%global eclipse_base   %{_libdir}/eclipse
%global install_loc    %{_datadir}/eclipse/dropins/discovery

Name:           eclipse-p2-discovery
Version:        4.2.1
Release:        alt1_2jpp7
Summary:        Equinox p2 Discovery

Group:          Development/Java
License:        EPL
URL:            http://www.eclipse.org/equinox/p2
Source0:        %{name}-fetched-src-%{src_repo_tag}.tar.xz
Source1:        %{name}-fetch-src.sh
Patch0:         remove-license-feature.patch

BuildArch: noarch

BuildRequires: eclipse-pde >= 1:4.2.0
Requires: eclipse-platform >= 4.2.0
Source44: import.info

%description
All of the bundles that comprise the Equinox p2 discovery component.

%prep
%setup -q -n %{name}-%{src_repo_tag}
%patch0

%build
eclipse-pdebuild -f org.eclipse.equinox.p2.discovery.feature

%install
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.eclipse.equinox.p2.discovery.feature.zip 

%files
%{install_loc}

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1_2jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1_2jpp7
- new version

