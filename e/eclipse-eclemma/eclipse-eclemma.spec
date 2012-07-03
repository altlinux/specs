BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
# required for install
BuildRequires: unzip
%global eclipse_base %{_libdir}/eclipse
%global install_loc  %{_datadir}/eclipse/dropins/eclemma

Name:      eclipse-eclemma
Version:   1.5.3
Release:   alt1_1jpp6
Summary:   Java code coverage tool plugin for Eclipse
Group:     Development/Java
License:   EPL and ASL 2.0
URL:       http://www.eclemma.org

# Source tarball and script used to generate it
# $ sh ./get-eclemma.sh
Source0:   eclemma-%{version}.tar.xz
Source1:   get-eclemma.sh
# Unpack the emma-including plugin so we can symlink to our JAR
Patch0:    %{name}-unjar.patch
Patch1:    %{name}-unjar-2.patch

BuildArch:        noarch
BuildRequires:    jpackage-utils
BuildRequires:    eclipse-pde >= 1:3.4.1
BuildRequires:    emma
Requires:         jpackage-utils
Requires:         eclipse-jdt >= 1:3.4.1
Requires:         emma
Provides:         eclemma = %{version}-%{release}
Source44: import.info

%description
EclEmma is a Java code coverage tool for Eclipse based on the EMMA Java
code coverage tool.  Features include launching from within the IDE,
coverage analysis summaries, and highlighting in Java source code
editors.

%prep
%setup -q -n eclemma-%{version}
%patch0

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

pushd com.mountainminds.eclemma.core
%patch1
popd
build-jar-repository -s -p com.mountainminds.eclemma.core emma.jar

%build
%{eclipse_base}/buildscripts/pdebuild

%install
install -d -m 755 %{buildroot}/%{install_loc}
unzip -q -o -d %{buildroot}/%{install_loc} \
  build/rpmBuild/com.mountainminds.eclemma.feature.zip
pushd %{buildroot}/%{install_loc}/eclipse/plugins
#build-jar-repository -s -p com.mountainminds.eclemma.core_%{version} emma.jar
rm com.mountainminds.eclemma.core_%{version}/emma.jar
ln -s ../../../../../../java/emma.jar com.mountainminds.eclemma.core_%{version}
popd

%files
%doc com.mountainminds.eclemma.doc/pages/faq.html
%doc com.mountainminds.eclemma.doc/pages/license.html
%doc com.mountainminds.eclemma.core/about.html
%{install_loc}

%changelog
* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_1jpp6
- update to new release by jppimport

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2jpp6
- new version

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1_1jpp6
- new version

