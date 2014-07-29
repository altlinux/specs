# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global install_loc    %{_datadir}/eclipse/dropins/testframework
%global tag            R4_2

%global easymockVerQual 2.4.0.v20090202-0900

Name:           eclipse-testframework
Version:        4.2.0
Release:        alt1_3jpp7
Summary:        Eclipse Test Framework

Group:          Development/Java
License:        EPL
URL:            http://eclipse.org
## sh %{name}-fetch-src.sh %{tag}
Source0:        %{name}-fetched-src-%{tag}.tar.bz2
Source1:        %{name}-fetch-src.sh
# Remove win32 fragment from test feature
Patch0:         %{name}-nowin32testfragment.patch
# Some fixes for library.xml
# FIXME:  submit parts of this upstream to make tests pwd-agnostic
Patch1:         %{name}-libraryXml.patch
# Fedora doesn't ship the shared license feature
Patch2:         %{name}-nosharedlicense.patch
# Fedora doesn't have a .source bundle for easymock
Patch3:         %{name}-noeasymocksource.patch

BuildArch: noarch

BuildRequires: eclipse-pde >= 4.2.0-6
BuildRequires: easymock2
Requires: eclipse-platform >= 4.2.0-6
Requires: easymock2
Requires: eclipse-jdt
Source44: import.info

%description
Eclipse Test Framework. Used in conjunction with Eclipse JUnit tests.

%prep
%setup -q -n %{name}-fetched-src-%{tag}
%patch0
%patch1
%patch2
%patch3
sed -i "s:/usr/lib/eclipse:%{_eclipse_base}:" org.eclipse.test/library.xml

mkdir orbitDeps
pushd orbitDeps
ln -s %{_javadir}/easymock2.jar org.easymock_%{easymockVerQual}.jar
popd

%build
eclipse-pdebuild -f org.eclipse.test -o `pwd`/orbitDeps

%install
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.eclipse.test.zip

pushd $RPM_BUILD_ROOT%{install_loc}/eclipse/plugins
rm -fr org.junit*
rm org.easymock_%{easymockVerQual}.jar
ln -s ../../../../../java/easymock2.jar org.easymock_%{easymockVerQual}.jar
rm -fr org.hamcrest.core_*
ln -s /usr/share/java/hamcrest/core.jar
popd

%files
%{install_loc}
%doc org.eclipse.test/about.html
%doc org.eclipse.test-feature/rootfiles/notice.html

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1_3jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1_2jpp7
- new version

