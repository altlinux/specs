# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jpanoramamaker
Version:        5.4
Release:        alt1_3jpp7
Summary:        Tool for stitching photos to panorama in linear curved space
BuildArch:      noarch

#Group:          Applications/Graphics
Group:          Toys
License:        BSD
URL:            http://jpanoramamaker.wz.cz
Source0:        http://jpanoramamaker.wz.cz/fedora/%{name}-5.4.src.tar.gz

BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  swing-layout
BuildRequires:  desktop-file-utils

Requires:       jpackage-utils
Requires:       swing-layout
Source44: import.info

%description
Tool for stitching photos to panorama in linear curved space

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.



%prep
%setup -q -n %{name}-5


find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
ant

#at this time the only existing test is executing and killing whole app.
#DISPLAY=:0.0
#export DISPLAY
#ant run-test-with-main


cat jpanoramamaker | sed s/jpanoramamaker-5/jpanoramamaker-5.4/g  | sed  "s/run \"\$1\" \"\$2\" \"\$3\" \"\$4\" \"\$5\" \"\$6\" \"\$7\" \"\$8\" \"\$9\"/run \$@/g"> jpanoramamakerSED

%install

#desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications  jpanoramamaker.desktop
cp -p ./jpanoramamaker.png  $RPM_BUILD_ROOT%{_datadir}/pixmaps/jpanoramamaker.png
#end desktop

#launcher
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
cp -p ./jpanoramamakerSED $RPM_BUILD_ROOT%{_bindir}/jpanoramamaker
#end launcher



# we are in /BUILD/jpanoramamaker-5/
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./dist/%{name}.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar


mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp ./dist/javadoc/  $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{_javadocdir}/%{name} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}




#####################################

%files
%{_datadir}/pixmaps/jpanoramamaker.png
%{_datadir}/applications/jpanoramamaker.desktop
%attr(755,root,root) %{_bindir}/jpanoramamaker


%{_javadir}/*
%doc license.txt


%files javadoc
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-%{version}


%changelog
* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 5.4-alt1_3jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 5.4-alt1_2jpp7
- new version

