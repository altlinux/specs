BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
# required for install
BuildRequires: unzip
%global install_loc  %{_datadir}/eclipse/dropins
%global eclipse_base %{_libdir}/eclipse

%global pkgname      eclox

Name:           eclipse-%{pkgname}
Version:        0.8.0
Release:        alt1_6.20100810svnjpp6
Summary:        Eclipse-based doxygen plugin

Group:          System/Libraries
License:        GPLv2+
URL:            http://eclox.eu/

Source0:        org.gna.%{pkgname}_%{version}.tar.gz
# Source1 is used to download Source0
Source1:        eclipse-%{pkgname}-download.sh

# These excludes are pulled as %%docs instead
Patch0:         eclipse-eclox-bin_excludes.patch
Patch1:         eclipse-eclox-help_excludes.patch


BuildRequires:  eclipse-pde

Requires:       doxygen
Requires:       eclipse-platform

BuildArch:      noarch
ExcludeArch:    ppc64
Source44: import.info

%description
Eclox is a doxygen frontend plug-in for eclipse.
It aims to provide a slim and sleek integration of the
code documentation process into eclipse.

%prep
%setup -q -n org.gna.%{pkgname}_%{version}

find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

# Remove unneccessary files
%patch0 -p0 -b .exclude
%patch1 -p0 -b .exclude

%build
# build the main feature
%{eclipse_base}/buildscripts/pdebuild -f org.gna.%{pkgname}

%install

install -d -m 755 %{buildroot}%{install_loc}

unzip -d %{buildroot}%{install_loc} -q build/rpmBuild/org.gna.%{pkgname}.zip


%files
%doc %{pkgname}.feature/{AUTHORS,CHANGES,COPYING,MANUAL,README,TODO}
%{install_loc}/*

%changelog
* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_6.20100810svnjpp6
- update to new release by jppimport

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_4.20090616svnjpp6
- new version

