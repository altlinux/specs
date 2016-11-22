# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:		vldocking
Version:	2.1.5
Release:	alt1_10jpp8
Summary:	A Java a.. docking system for JFC Swing applications
Group:		Development/Java
License:	CeCILL
URL:		http://www.vlsolutions.com/en/download/
# the zip file can be downloaded from the redirect 
# from  http://www.vlsolutions.com/en/download/downloader2_0.php
 
Source0:	vldocking_%{version}.zip
Patch1:		vldocking-build.patch

BuildArch:	noarch

BuildRequires: javapackages-tools rpm-build-java ant

Requires: javapackages-tools rpm-build-java
Source44: import.info


%description 
Docking windows allow the user to reorganize the application's workspace
according to his needs:

	* Drag and Drop parts of the application ("Dockables")
	* Hide the dockables not often used to save screen space
	* Detach some dockables and have them floating outside the window
	* Easily switch between different workspaces
	* And much more... 

%package	javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}
Requires: javapackages-tools rpm-build-java
BuildArch: noarch
%description	javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}_%{version}

find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

%build

ant jar
ant javadoc

%install

install -D jar/%{name}_%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc Licence_CeCILL-V1_VF.pdf Licence_CeCILL-V1.1_VA.pdf
%{_javadir}/*

%files javadoc
%{_javadocdir}/*

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.5-alt1_10jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.5-alt1_9jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.5-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.5-alt1_5jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.5-alt1_4jpp7
- new version

