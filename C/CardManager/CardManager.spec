# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           CardManager
Version:        3
Release:        alt1_7jpp8
Summary:        Java application to allows you to play any, especially collectible, card game

Group:          Games/Other
License:        BSD
URL:            http://cardmanager.wz.cz/
Source0:        http://cardmanager.wz.cz/CardManager_sources%{version}.zip
Source1:        %{name}.appdata.xml
Patch0:         removeManifestEntries.patch
Patch1:         jdk8-javadoc.patch
BuildArch:      noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant
BuildRequires:  desktop-file-utils

Requires: javapackages-tools rpm-build-java
Source44: import.info

%description
This is free, open source multiplatform (java) application which allows you to
 play ANY card game. 
The game is designed especially to play collectible card games like Magic the
 Gathering or Doomtrooper over network.
To play those games you need to own (scanned) images of card, which are not part
 of this package.
Some can be easily downloadable from internet, but be aware of copyrights.
The default deck and background is free of copyright
Also please feel free to add your own backgrounds to 
~/CardManager/data/backgrounds and of course enhance
collection under ~/CardManager/collection

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c CardManager
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
%patch0
%patch1

%build

ant

%install

#desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications  CardManager.desktop
cp -p ./CardManager.png  $RPM_BUILD_ROOT%{_datadir}/pixmaps/
#end desktop

#launcher
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
cp -p ./FedoraLauncher.sh $RPM_BUILD_ROOT%{_bindir}/CardManager
#end launcher


#appdata
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/
cp -r data $RPM_BUILD_ROOT/%{_datadir}/%{name}/
cp -r collection $RPM_BUILD_ROOT/%{_datadir}/%{name}/

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -r dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_datadir}/pixmaps/CardManager.png
%{_datadir}/applications/CardManager.desktop
%{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/CardManager
%{_javadir}/*
%doc license.txt
%{_datadir}/appdata/%{name}.appdata.xml

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3-alt1_7jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3-alt1_6jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3-alt1_3jpp7
- new release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 3-alt1_1jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1-alt1_2jpp7
- new version

