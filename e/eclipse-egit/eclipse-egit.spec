BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
# required for install
BuildRequires: unzip
%global eclipse_base     %{_libdir}/eclipse
%global install_loc      %{_datadir}/eclipse/dropins/egit

Summary:          Eclipse Git Integration
Name:             eclipse-egit
Version:          1.1.0
Release:          alt1_1jpp6
License:          EPL
URL:              http://www.eclipse.org/egit
Group:            Development/Java

# retrieved from http://egit.eclipse.org/w/?p=egit.git;a=snapshot;h=v1.1.0.201109151100-r;sf=tbz2
Source0:          egit-v1.1.0.201109151100-r.tar.bz2

BuildRequires:    eclipse-pde
BuildRequires:    eclipse-jgit >= 1.1.0
BuildRequires:    jpackage-utils >= 0:1.5
Requires:         eclipse-platform >= 1:3.5.0
Requires:         eclipse-jgit >= 1.1.0

BuildArch:        noarch
Source44: import.info

%description
The eclipse-egit package contains Eclipse plugins for
interacting with Git repositories.

%prep
%setup -n eclipse-egit -q -c
NR=$((`wc -l egit/org.eclipse.egit.ui/src/org/eclipse/egit/ui/internal/clone/GitCloneWizard.java | \
            cut -d' ' -f1` - 1))
       tail -n$NR egit/org.eclipse.egit.ui/src/org/eclipse/egit/ui/internal/clone/GitCloneWizard.java > part2.java
echo "/*******************************************************************************" > part1.java
cat part1.java part2.java > egit/org.eclipse.egit.ui/src/org/eclipse/egit/ui/internal/clone/GitCloneWizard.java

%build
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.egit -d jgit mylyn

%install
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}

# egit main feature
unzip -q -d $RPM_BUILD_ROOT%{install_loc}/ build/rpmBuild/org.eclipse.egit.zip

%files
%{install_loc}
%doc egit/LICENSE
%doc egit/README

%changelog
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

