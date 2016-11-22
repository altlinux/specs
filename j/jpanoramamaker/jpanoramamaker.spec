# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global majorv 5
%global minorv 6

Name:           jpanoramamaker
Version:        %{majorv}.%{minorv}
Release:        alt1_5jpp8
Summary:        Tool for stitching photos to panorama in linear curved space
BuildArch:      noarch

#Group:          Applications/Graphics
Group:          Toys
License:        BSD
URL:            http://jpanoramamaker.wz.cz
Source0:        http://jpanoramamaker.wz.cz/fedora/%{name}-%{version}.src.tar.gz
Source1:        %{name}.appdata.xml

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant
BuildRequires:  swing-layout
BuildRequires:  desktop-file-utils

Requires: javapackages-tools rpm-build-java
Requires:       swing-layout
Source44: import.info

%description
Tool for stitching photos to panorama in linear curved space

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.
This tool is unique in number of manual touches you can do to affect final result.
Sometimes simple changing of order of image or lying a bit on position where they meet can do miracles.


%prep
%setup -q -n %{name}-%{majorv}
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

#add swing-layout to classpath
sed -i 's-javac.classpath=\\-javac.classpath=/usr/share/java/swing\-layout.jar\:\\-g'  nbproject/project.properties
#remove copylibraries
sed -i 's/<taskdef/<!--<taskdef/g' nbproject/build-impl.xml
sed -i 's:</copylibs>:</copylibs>-->:g' nbproject/build-impl.xml

%build
ant

#pack manually
pushd  build/classes
jar -cvf ../../dist/%{name}.jar *
popd

%install

#desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications  jpanoramamaker.desktop
cp -p ./jpanoramamaker.png  $RPM_BUILD_ROOT%{_datadir}/pixmaps/jpanoramamaker.png
#end desktop

#launcher
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
cp -p ./jpanoramamaker $RPM_BUILD_ROOT%{_bindir}/jpanoramamaker
#end launcher



# we are in /BUILD/jpanoramamaker-5/
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./dist/%{name}.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar


mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp ./dist/javadoc/  $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{_javadocdir}/%{name} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

#appdata
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml


#####################################

%files
%{_datadir}/pixmaps/jpanoramamaker.png
%{_datadir}/applications/jpanoramamaker.desktop
%attr(755,root,root) %{_bindir}/jpanoramamaker
%{_datadir}/appdata/%{name}.appdata.xml


%{_javadir}/*
%doc license.txt


%files javadoc
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-%{version}


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 5.6-alt1_5jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 5.6-alt1_4jpp8
- new version

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 5.6-alt1_1jpp7
- new version

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 5.4-alt1_3jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 5.4-alt1_2jpp7
- new version

