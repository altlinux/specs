# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
BuildRequires: rpm-build-java-osgi
%define eclipse_base   %{_libdir}/eclipse
%define install_loc    %{_libdir}/eclipse/dropins/valgrind
%define qualifier      201111050234

%if 0%{?rhel} >= 6
ExclusiveArch: %{ix86} x86_64
%endif

# Package in %%{_libdir} but no native code so no debuginfo
%global debug_package %{nil}

Name:           eclipse-valgrind
Version:        0.9.0
Release:        alt1_2jpp6
Summary:        Valgrind Tools Integration for Eclipse

Group:          Development/Java
License:        EPL
URL:            http://www.eclipse.org/linuxtools/projectPages/valgrind
# Note that 0.0.1 != 0.7.0 but this is an upstream maven issue
Source0:        http://download.eclipse.org/technology/linuxtools/0.9.0-sources/linuxtools-valgrind-parent-0.9.0-src.tar.bz2

#No CDT on ppc64
ExcludeArch: ppc64

BuildRequires: eclipse-cdt >= 1:7.0.0
BuildRequires: eclipse-linuxprofilingframework >= 0.7.0
BuildRequires: eclipse-birt >= 2.5
BuildRequires: eclipse-pde >= 1:3.6.0
Requires: eclipse-platform >= 1:3.6.0
Requires: eclipse-cdt >= 1:7.0.0
Requires: eclipse-linuxprofilingframework >= 0.7.0
Requires: eclipse-birt >= 2.5
Requires: valgrind >= 3.3.0
Source44: import.info

%description
This package for Eclipse allows users to launch their C/C++ Development Tools
projects using the Valgrind tool suite and presents the results in the IDE. 

%prep
%setup -q -n linuxtools-valgrind-parent-0.9.0-src

%build
%{eclipse_base}/buildscripts/pdebuild \
    -f org.eclipse.linuxtools.valgrind \
    -d "cdt linuxprofilingframework emf rhino birt" \
    -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier}"

%install
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.eclipse.linuxtools.valgrind.zip 

%files
%{install_loc}
%doc org.eclipse.linuxtools.valgrind/epl-v10.html

%changelog
* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_2jpp6
- update to new release by jppimport

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_1jpp6
- update to new release by jppimport

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_1jpp6
- new version

