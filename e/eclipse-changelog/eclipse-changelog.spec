# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
BuildRequires: rpm-build-java-osgi
%define qualifier      201106060936
%define eclipse_base   %{_libdir}/eclipse

Epoch: 1

Name:           eclipse-changelog
Version:        2.7.0
Release:        alt1_2jpp6
Summary:        Eclipse ChangeLog plug-in

Group:          Development/Java
License:        EPL
URL:            http://sources.redhat.com/eclipse

Obsoletes:      eclipse-changelog-cdt < %{epoch}:%{version}-%{release}
Obsoletes:      eclipse-changelog-jdt < %{epoch}:%{version}-%{release}

Provides:       eclipse-changelog-cdt = %{epoch}:%{version}-%{release}
Provides:       eclipse-changelog-jdt = %{epoch}:%{version}-%{release}

# Note that 0.9.0 is the linuxtools release, not individual features
Source0:        http://download.eclipse.org/technology/linuxtools/0.9.0-sources/linuxtools-changelog-parent-0.9.0-src.tar.bz2


BuildRequires:          eclipse-pde >= 1:3.7.0
# CParser requires at least CDT 7.0.0
BuildRequires:          eclipse-cdt >= 1:7.0.0

# These plugins are really noarch but they need cdt which
# we only build on these architectures.
%if 0%{?rhel} >= 6
ExclusiveArch: %{ix86} x86_64
%else
ExclusiveArch: %{ix86} x86_64 ppc ia64
%endif
%define debug_package %{nil}

Requires:               eclipse-platform >= 1:3.7.0
Source44: import.info

%description
The Eclipse ChangeLog package contains Eclipse features and plugins that are
useful for ChangeLog maintenance within the Eclipse IDE.  It includes
fragments for parsing C, C++, and Java source files to create more detailed
entries containing function or method names.

%prep
%setup -q -c -n linuxtools-changelog-parent-0.9.0-src

%build
%{eclipse_base}/buildscripts/pdebuild -d cdt \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -f org.eclipse.linuxtools.changelog


%install
installDir=$RPM_BUILD_ROOT/%{eclipse_base}/dropins/changelog
install -d -m 755 $installDir
unzip -q -d $installDir \
 build/rpmBuild/org.eclipse.linuxtools.changelog.zip

%files
%doc linuxtools-changelog-parent-0.9.0-src/org.eclipse.linuxtools.changelog/epl-v10.html
%{eclipse_base}/dropins/changelog

%changelog
* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.7.0-alt1_2jpp6
- update to new release by jppimport

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 1:2.7.0-alt1_1jpp6
- update to new release by jppimport

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 1:2.6.7-alt1_3jpp6
- new version

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 1:2.6.3-alt1_2jpp6
- new version

* Thu Jul 31 2008 Igor Vlasenko <viy@altlinux.ru> 1:2.6.2-alt1_1jpp6
- new version

* Mon Jul 28 2008 Igor Vlasenko <viy@altlinux.ru> 1:2.6.1-alt1_3jpp6
- eclipse 3.3.2

* Tue Dec 04 2007 Igor Vlasenko <viy@altlinux.ru> 1:2.5.1-alt2_2jpp5.0
- set noarch

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 1:2.5.1-alt1_2jpp5.0
- converted from JPackage by jppimport script

