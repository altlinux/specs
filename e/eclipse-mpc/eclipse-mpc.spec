BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global src_repo_tag   R_1_1_1
%global install_loc    %{_datadir}/eclipse/dropins/mpc

Name:           eclipse-mpc
Version:        1.1.1
Release:        alt1_4jpp7
Summary:        Eclipse Marketplace Client

Group:          Development/Java
License:        EPL
URL:            http://www.eclipse.org/mpc/
Source0:        http://git.eclipse.org/c/mpc/org.eclipse.epp.mpc.git/snapshot/%{src_repo_tag}.tar.bz2

BuildArch: noarch

BuildRequires: eclipse-pde >= 1:3.4.0
BuildRequires: eclipse-p2-discovery >= 1.0.0
Requires: eclipse-platform >= 3.6.0
Requires: eclipse-p2-discovery >= 1.0.0
Source44: import.info

%description
The Eclipse Marketplace Client provides access to extension catalogs.

%prep
%setup -q -n %{src_repo_tag}

%{__chmod} a-x org.eclipse.epp.mpc.feature/license.html

%build
eclipse-pdebuild -f org.eclipse.epp.mpc -d discovery

%install
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.eclipse.epp.mpc.zip 


%files
%{install_loc}
%doc org.eclipse.epp.mpc.feature/epl-v10.html
%doc org.eclipse.epp.mpc.feature/license.html

%changelog
* Tue Jul 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_4jpp7
- update

