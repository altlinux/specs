# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global install_loc      %{_datadir}/eclipse/dropins/egit
%global version_suffix 201212191850-r

Summary:          Eclipse Git Integration
Name:             eclipse-egit
Version:          2.2.0
Release:          alt1_1jpp7
License:          EPL
URL:              http://www.eclipse.org/egit
Group:            Development/Java
Source0:          http://git.eclipse.org/c/egit/egit.git/snapshot/egit-%{version}.%{version_suffix}.tar.bz2

BuildRequires:    eclipse-pde
BuildRequires:    eclipse-jgit >= 2.2.0
BuildRequires:    jpackage-utils >= 0:1.5
Requires:         eclipse-platform >= 1:3.5.0
Requires:         eclipse-jgit >= 2.2.0

BuildArch:        noarch
Source44: import.info

%description
The eclipse-egit package contains Eclipse plugins for
interacting with Git repositories.

%prep
%setup -n egit-%{version}.%{version_suffix} -q

%build
%{_bindir}/eclipse-pdebuild -f org.eclipse.egit -d "jgit"

%install
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}

# egit main feature
unzip -q -d $RPM_BUILD_ROOT%{install_loc}/ build/rpmBuild/org.eclipse.egit.zip

%files
%{install_loc}
%doc LICENSE README.md

%changelog
* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_1jpp7
- fc update

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_2jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_1jpp6
- fixed build

* Thu Oct 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1jpp6
- update to new release by jppimport

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp6
- update to new release by jppimport

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_1jpp6
- new version

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_2jpp6
- new version

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_0.1.git20091029jpp6
- new version

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.3.1.20081022-alt1_3jpp6
- new version

* Mon Jul 28 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_0jpp6
- eclipse 3.3.2

* Tue Dec 11 2007 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2_2jpp5.0
- fixed dependencies

* Tue Dec 04 2007 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_2jpp5.0
- converted from JPackage by jppimport script

