# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
BuildRequires: rpm-build-java-osgi
%global eclipse_base        %{_libdir}/eclipse
%global install_loc         %{_datadir}/eclipse/dropins
%global qualifier           201108151400

Name:           eclipse-rpm-editor
Version:        0.9.0
Release:        alt1_1jpp6
Summary:        RPM Specfile editor for Eclipse
Group:          Development/Java
License:        EPL
URL:            http://www.eclipse.org/linuxtools/
Source0:       http://download.eclipse.org/technology/linuxtools/%{version}-sources/linuxtools-rpm-parent-%{version}-src.tar.bz2

BuildRequires: eclipse-pde >= 1:3.7.0
BuildRequires: eclipse-changelog >= 2.5.1
Requires: eclipse-platform >= 3.7.0
Requires: eclipse-changelog >= 2.5.1
Requires: rpmlint >= 0.81
Requires: rpmdevtools

# These plugins are really noarch but the changelog plugin need cdt which
# we only build on these architectures.
ExclusiveArch: %{ix86} x86_64 ppc ia64
%global debug_package %{nil}
Source44: import.info
BuildArch: noarch

%description
The Eclipse Specfile Editor package contains Eclipse plugins that are
useful for maintenance of RPM specfiles within the Eclipse IDE.

%prep
%setup -q -n linuxtools-rpm-parent-0.9.0-src

%build
%{eclipse_base}/buildscripts/pdebuild -a "-DforceContextQualifier=%{qualifier} -DjavacSource=1.5 -DjavacTarget=1.5" \
 -f  org.eclipse.linuxtools.rpm
%{eclipse_base}/buildscripts/pdebuild -a "-DforceContextQualifier=%{qualifier} -DjavacSource=1.5 -DjavacTarget=1.5" \
 -f  org.eclipse.linuxtools.rpm.ui.editor.feature -d changelog ;

%install
installDir=%{buildroot}%{install_loc}/rpm-editor
install -d -m 755 $installDir
unzip -q -d $installDir \
 build/rpmBuild/org.eclipse.linuxtools.rpm.ui.editor.feature.zip
unzip -q -d $installDir \
 build/rpmBuild/org.eclipse.linuxtools.rpm.zip

%files
%doc org.eclipse.linuxtools.rpm.ui.editor.feature/*.html
%{install_loc}/rpm-editor

%changelog
* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_1jpp6
- update to new release by jppimport

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_0.2.20110815git2168cacbjpp6
- update to new release by jppimport

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_1jpp6
- new version

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_1jpp6
- new version

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 0.4.3-alt1_2jpp6
- new version

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 0.4.3-alt1_1jpp6
- build for new eclipse version

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_5jpp6
- new version

* Mon Jul 28 2008 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_3jpp6
- eclipse 3.3.2

* Tue Dec 11 2007 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2_10jpp5.0
- fixed dependencies

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_10jpp5.0
- converted from JPackage by jppimport script

