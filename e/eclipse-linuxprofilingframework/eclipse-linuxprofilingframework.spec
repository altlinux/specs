# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
BuildRequires: rpm-build-java-osgi
%define eclipse_base   %{_libdir}/eclipse
%define install_loc    %{_libdir}/eclipse/dropins/linuxprofilingframework
%define qualifier      201111050234

# Package in %%{_libdir} but no native code so no debuginfo
%global debug_package %{nil}

Name:           eclipse-linuxprofilingframework
Version:        0.9.0
Release:        alt1_2jpp6
Summary:        Eclipse Linux Tools Profiling Framework

Group:          Development/Java
License:        EPL
URL:            http://eclipse.org/linuxtools
Source0:        http://download.eclipse.org/technology/linuxtools/%{version}-sources/linuxtools-profiling-parent-%{version}-src.tar.bz2

# No CDT on ppc64
ExcludeArch: ppc64

BuildRequires: eclipse-pde >= 1:3.6.0
BuildRequires: eclipse-cdt >= 1:7.0.0
BuildRequires: eclipse-birt >= 3.7.0-3
Requires: eclipse-platform >= 1:3.6.0
Requires: eclipse-cdt >= 1:7.0.0
Requires: eclipse-birt >= 3.7.0-3

%if 0%{?rhel} >= 6
ExclusiveArch: %{ix86} x86_64
%endif
Source44: import.info

%description
Plugins common to Eclipse Linux Tools profiling tools.

%prep
%setup -q -n linuxtools-profiling-parent-%{version}-src

%build
%{eclipse_base}/buildscripts/pdebuild -v -d "cdt birt emf gef rse dtp-connectivity" \
 -a "-DjavacSource=1.6 -DjavacTarget=1.6 -DforceContextQualifier=%{qualifier}" \
 -j -DJ2SE-1.6=%{_jvmdir}/java/jre/lib/rt.jar \
 -f org.eclipse.linuxtools.profiling

%install
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}

unzip -q -d $RPM_BUILD_ROOT%{install_loc} \
     build/rpmBuild/org.eclipse.linuxtools.profiling.zip

%files
%doc org.eclipse.linuxtools.profiling/epl-v10.html
%{install_loc}

%changelog
* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_2jpp6
- update to new release by jppimport

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_0.1.20110706git02ddf6ebc7jpp6
- update to new release by jppimport

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_1jpp6
- new version

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_2jpp6
- new version

