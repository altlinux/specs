BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global eclipse_base   %{_libdir}/eclipse
%global install_loc    %{_datadir}/eclipse/dropins/jgit

Name:           eclipse-jgit
Version:        1.1.0
Release:        alt1_1jpp6
Summary:        Eclipse JGit

Group:          Development/Java
License:        BSD
URL:            http://www.eclipse.org/egit/
#Fetched from http://egit.eclipse.org/w/?p=jgit.git;a=snapshot;h=v1.1.0.201109151100-r;sf=tbz2
Source0:        jgit-v1.1.0.201109151100-r.tar.bz2

BuildArch: noarch

BuildRequires: eclipse-pde >= 1:3.5.0
Requires: eclipse-platform >= 3.5.0
Source44: import.info

%description
A pure Java implementation of the Git version control system.

%prep
%setup -n eclipse-jgit -q -c

%build
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.jgit

%install
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.eclipse.jgit.zip 

%files
%doc jgit/LICENSE 
%doc jgit/README
%{install_loc}

%changelog
* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1jpp6
- update to new release by jppimport

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp6
- update to new release by jppimport

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_1jpp6
- new version

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_1jpp6
- new version

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_0.1.git20091029jpp6
- new version

