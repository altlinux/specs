BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
BuildRequires: rpm-build-java-osgi
%global eclipse_base   %{_libdir}/eclipse
%global install_loc    %{_datadir}/eclipse/dropins/man

Name:           eclipse-manpage
Version:        0.9.0
Release:        alt1_1jpp6
Summary:        Man page viewer

Group:          Development/Java
License:        EPL
URL:            http://www.eclipse.org/linuxtools/projectPages/manpage/
Source0:        http://download.eclipse.org/technology/linuxtools/%{version}-sources/linuxtools-man-parent-%{version}-src.tar.bz2

BuildArch: noarch

BuildRequires: eclipse-pde >= 1:3.4.0
Requires: eclipse-platform >= 3.4.0
Source44: import.info

%description
Plugin providing common interface for displaying a man page in a view or 
fetching its content for embedded display purposes (e.g hover help).

%prep
%setup -q -n linuxtools-man-parent-%{version}-src

%build
%{eclipse_base}/buildscripts/pdebuild

%install
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.eclipse.linuxtools.man.zip 

%files
%{install_loc}
%doc org.eclipse.linuxtools.man/license.html
%doc org.eclipse.linuxtools.man/epl-v10.html

%changelog
* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_1jpp6
- update to new release by jppimport

* Tue Oct 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt5_0.svn24060.1.1jpp6
- update to new release by jppimport

* Thu Oct 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt4_0.svn24060.1.1jpp6
- update to new release by jppimport

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt3_0.svn24060.1.1jpp6
- update to new release by jppimport

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt2_0.svn24060.1.1jpp6
- update to new release by jppimport

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_0.svn24060.1jpp6
- new version

