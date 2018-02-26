# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
BuildRequires: rpm-build-java-osgi
%global eclipse_base   %{_libdir}/eclipse
%global install_loc    %{_datadir}/eclipse/dropins/cmakeed

Name:           eclipse-cmakeed
Version:        1.1.6
Release:        alt1_1jpp6
Summary:        CMake Editor plug-in for Eclipse

Group:          Development/Java
License:        CPL
URL:            http://cmakeed.sourceforge.net
#svn export https://cmakeed.svn.sourceforge.net/svnroot/cmakeed/tags/1_1_6/ eclipse-cmakeed-1.1.6
#rm -fr eclipse-cmakeed-1.1.6/com.cthing.cmakeed.site/
# tar caf eclipse-cmakeed-1.1.6.tar.xz eclipse-cmakeed-1.1.6/
Source0: eclipse-cmakeed-1.1.6.tar.xz

BuildArch: noarch

BuildRequires: eclipse-pde >= 1:3.4.0
Requires: eclipse-platform >= 3.4.0
Source44: import.info

%description
The CMakeEd plug-in provides an editor for CMake files. The plug-in registers
an editor for files named CMakeLists.txt and *.cmake.

%prep
%setup -q
#remove jar files
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

%build
%{eclipse_base}/buildscripts/pdebuild

%install
%{__install} -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/com.cthing.cmakeed.feature.zip

%files
%{install_loc}
%doc com.cthing.cmakeed.feature/License.html

%changelog
* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1_1jpp6
- update to new release by jppimport

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt1_2jpp6
- update to new release by jppimport

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt1_1jpp6
- new version

