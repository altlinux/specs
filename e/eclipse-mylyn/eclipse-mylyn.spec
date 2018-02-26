# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
BuildRequires: rpm-build-java-osgi
%global eclipse_base        %{_libdir}/eclipse
%global install_loc         %{_datadir}/eclipse/dropins
# Taken from update site so we match upstream
#  http://download.eclipse.org/mylyn/archive/3.6.3/v20110608-1400/
%global qualifier           v20110908-0706
Name: eclipse-mylyn
Summary: Eclipse Mylyn main feature.
Version: 3.6.4
Release: alt1_2jpp6
License: EPL
URL: http://www.eclipse.org/mylyn

# bash fetch-eclipse-mylyn.sh
Source0: eclipse-mylyn-R_3_6_4-fetched-src.tar.bz2
Source1: fetch-eclipse-mylyn.sh

BuildArch: noarch
%if 0%{?rhel} >= 6
ExclusiveArch: %{ix86} x86_64
%endif

BuildRequires: eclipse-platform >= 1:3.5.0
BuildRequires: eclipse-pde >= 1:3.5.0
BuildRequires: eclipse-mylyn-commons >= 3.6.0
BuildRequires: rome
BuildRequires: jdom

Requires: eclipse-platform >= 1:3.5.0
Requires: eclipse-mylyn-commons >= 3.6.0
Requires: rome
Requires: jdom

Group: Development/Java
Source44: import.info

%description
Mylyn integrates task support into Eclipse. It supports offline editing
for certain task repositories and monitors work activity to hide
information that is not relevant to the current task.

%prep
%setup -q -n eclipse-mylyn-R_3_6_4-fetched-src
rm -rf orbitDeps
mkdir orbitDeps
pushd orbitDeps
ln -s %{_javadir}/jdom.jar
ln -s %{_javadir}/rome*.jar
popd

%build
%{eclipse_base}/buildscripts/pdebuild \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -d "mylyn-commons" -o `pwd`/orbitDeps

%install
install -d -m 755 %{buildroot}%{_datadir}/eclipse
install -d -m 755 %{buildroot}%{install_loc}/mylyn

unzip -q -o -d %{buildroot}%{install_loc}/mylyn \
 build/rpmBuild/org.eclipse.mylyn_feature.zip


%files
%{install_loc}/mylyn
%doc org.eclipse.mylyn-feature/epl-v10.html
%doc org.eclipse.mylyn-feature/license.html

%changelog
* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 3.6.4-alt1_2jpp6
- update to new release by jppimport

* Tue Oct 11 2011 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_1jpp6
- update to new release by jppimport

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 3.6.0-alt1_3jpp6
- update to new release by jppimport

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 3.4.0-alt1_4jpp6
- new version

* Wed Dec 15 2010 Igor Vlasenko <viy@altlinux.ru> 3.3.2-alt2_2jpp6
- fixed build

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 3.3.2-alt1_2jpp6
- new version

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_2jpp6
- converted from JPackage by jppimport script

* Sat Mar 21 2009 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_3jpp6
- new version

* Mon Jan 12 2009 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_3jpp6
- new version

* Mon Jul 28 2008 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_6jpp6
- eclipse 3.3.2

* Thu Feb 28 2008 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_9jpp5.0
- fixed buildreq: lucene1

* Tue Dec 04 2007 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_9jpp5.0
- converted from JPackage by jppimport script

