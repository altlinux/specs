BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
# required for install
BuildRequires: unzip
%define eclipse_base        %{_libdir}/eclipse
%define install_loc         %{_datadir}/eclipse/dropins
%define upstream_name       QuickREx
%define cvs_tag             %{upstream_name}_3_5_0
%define oro_jar             jakarta-oro-2.0.8.jar
%define regexp_jar          jakarta-regexp-1.4.jar

Name:           eclipse-quickrex
Version:        3.5.0
Release:        alt1_14jpp6
Summary:        %{upstream_name} is a regular-expression test Eclipse Plug-In

Group:          Development/Java
License:        EPL
URL:            http://www.bastian-bergerhoff.com/eclipse/features/web/QuickREx/toc.html
# This tarball was made using the included script, like so:
#   sh ./fetch-quickrex.sh %{cvs_tag}
Source0:        quickrex-fetched-src-%{cvs_tag}.tar.bz2
Source1:        fetch-quickrex.sh
# build.properties and feature.xml was create to easily build this plugin with
# the awesome Fedora way, these files are licensed under the same license as
# the package.
Source2:        build.properties
Source3:        feature.xml
Patch0:         quickrex-disable-jregex-capability.patch

BuildArch: noarch

BuildRequires: eclipse-pde >= 1:3.2.0
Requires: eclipse-platform >= 3.2.1
BuildRequires: jakarta-oro
Requires: jakarta-oro
BuildRequires: regexp
Requires: regexp
Provides: eclipse-%{upstream_name} = %{version}-%{release}
Source44: import.info

%description
%{upstream_name} provides an Eclipse view in which you can enter
test-texts and try regular expressions.

# Note: This version of QuickREx disables jregex support due to
# the fact that there isn't a Fedora package of it.

%prep
%setup -q -n quickrex-fetched-src-%{cvs_tag}

mkdir quickrex-features
# create the feature plugin
cp -p %{SOURCE2} %{SOURCE3} quickrex-features

pushd Plug-In
%patch0 -p0
pushd lib
ln -s %{_javadir}/jakarta-oro.jar %{oro_jar}
ln -s %{_javadir}/regexp.jar %{regexp_jar}
popd
popd

%build
%{eclipse_base}/buildscripts/pdebuild

%install
installDir=%{buildroot}%{install_loc}/quickrex
install -d -m 755 $installDir
unzip -q -d $installDir \
 build/rpmBuild/de.babe.eclipse.plugins.QuickREx.zip

# Re-symlink
pushd  $installDir/eclipse/plugins/de.babe.eclipse.plugins.QuickREx_%{version}/lib
rm %{oro_jar}
rm %{regexp_jar}
ln -s %{_javadir}/jakarta-oro.jar %{oro_jar}
ln -s %{_javadir}/regexp.jar %{regexp_jar}
popd

%files
%doc Plug-In/html
%{install_loc}/quickrex

%changelog
* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 3.5.0-alt1_14jpp6
- update to new release by jppimport

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 3.5.0-alt1_12jpp6
- build for new eclipse version

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 3.5.0-alt1_9jpp6
- new version

* Mon Jul 28 2008 Igor Vlasenko <viy@altlinux.ru> 3.5.0-alt1_7jpp6
- eclipse 3.3.2

* Wed Dec 05 2007 Igor Vlasenko <viy@altlinux.ru> 3.5.0-alt1_5jpp5.0
- converted from JPackage by jppimport script

