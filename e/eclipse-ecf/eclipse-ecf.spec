# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global tag R-Release_HEAD-sdk_feature-77_2012-06-10_19-42-02
%global contextQualifier 201208090744
Name:           eclipse-ecf
Version:        3.5.6
Release:        alt1_3jpp7
Summary:        Eclipse Communication Framework

License:        EPL
URL:            http://www.eclipse.org/ecf/
Source0:        http://git.eclipse.org/c/ecf/org.eclipse.ecf.git/snapshot/%{tag}.tar.bz2

BuildRequires:  jpackage-utils
BuildRequires:  eclipse-pde >= 4.2.0-5

BuildArch:      noarch
Source44: import.info

%description
ECF is a framework for building distributed servers, applications,
 and tools. It provides a modular implementation of the OSGi 4.2
 Remote Services standard, along with support for REST-based and
 SOAP-based remote services, and asynchronous messaging for remote services. 

%package core
Summary:   ECF core bundles
Group:     System/Libraries
Requires:       jpackage-utils

%description core
ECF bundles required by eclipse-platform.

%prep
%setup -q -n %{tag}

#get just the bits we need
mkdir -p ecf/plugins
mkdir -p ecf/features

cp -r releng/features/org.eclipse.ecf.filetransfer{,.httpclient}.feature \
    ecf/features

cp -r framework/bundles/org.eclipse.ecf ecf/plugins
cp -r framework/bundles/org.eclipse.ecf.identity ecf/plugins
cp -r framework/bundles/org.eclipse.ecf.ssl ecf/plugins
cp -r framework/bundles/org.eclipse.ecf.filetransfer ecf/plugins
cp -r providers/bundles/org.eclipse.ecf.provider.filetransfer ecf/plugins
cp -r providers/bundles/org.eclipse.ecf.provider.filetransfer.ssl ecf/plugins
cp -r providers/bundles/org.eclipse.ecf.provider.filetransfer.httpclient ecf/plugins
cp -r providers/bundles/org.eclipse.ecf.provider.filetransfer.httpclient.ssl ecf/plugins

rm -rf `ls | grep -v "ecf"`

find . -type f -name "*.jar" -exec rm {} \;

%build
eclipse-pdebuild -f org.eclipse.ecf.filetransfer.feature -j "-DforceContextQualifier=%{contextQualifier}"
eclipse-pdebuild -f org.eclipse.ecf.filetransfer.httpclient.feature -j "-DforceContextQualifier=%{contextQualifier}"


%install
install -d -m 755 %{buildroot}%{_javadir}/ecf

unzip -q -n -d %{buildroot}%{_javadir}/ecf          build/rpmBuild/org.eclipse.ecf.filetransfer.feature.zip
unzip -q -n -d %{buildroot}%{_javadir}/ecf          build/rpmBuild/org.eclipse.ecf.filetransfer.httpclient.feature.zip

pushd %{buildroot}%{_javadir}/ecf/eclipse/plugins/
rm -rf org.apache*
ln -s %{_javadir}/commons-codec.jar
ln -s %{_javadir}/commons-httpclient.jar
ln -s %{_javadir}/commons-logging.jar
popd
%files core
%{_javadir}/ecf
%doc ecf/features/org.eclipse.ecf.filetransfer.feature/license.html
%doc ecf/features/org.eclipse.ecf.filetransfer.feature/about.html

%changelog
* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 3.5.6-alt1_3jpp7
- new version

