Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global svn_rev 1242
Name:           OSGi-bundle-ant-task
Version:        0.2.0
Release:        alt1_0.9.svn1242jpp7
Summary:        A wrapper around Bnd to allow easy bundle creation from ant builds

License:        BSD
URL:            https://opensource.luminis.net/wiki/display/SITE/OSGi+Bundle+Ant+Task
# svn export -r 1242 https://opensource.luminis.net/svn/BUNDLES/releases/build-plugin-0.2.0/  OSGi-bundle-ant-task
# tar -cvzf OSGi-bundle-ant-task.tar.gz OSGi-bundle-ant-task/
Source0:        %{name}.tar.gz
Source1:        %{name}-bsd.txt
Patch0:         %{name}-build-xml.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils
BuildRequires:  aqute-bnd ant

# for jar

Requires:       jpackage-utils
Source44: import.info

%description
A wrapper around Bnd to allow easy bundle creation from ant builds

%prep
%setup -q -n %{name}
%patch0 -p0

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
cp %{SOURCE1} .

%build
export CLASSPATH=$(build-classpath aqute-bnd ant)
ant dist
%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -pa dist/lib/net.luminis.build.plugin-0.2.0.jar  $RPM_BUILD_ROOT%{_javadir}/net.luminis.build.plugin.jar

%files
%doc %{name}-bsd.txt
%{_javadir}/*

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_0.9.svn1242jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_0.8.svn1242jpp7
- new version

