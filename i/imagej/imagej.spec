# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           imagej
Version:        1.50
Release:        alt1_1.hjpp8
Summary:        Image Processing and Analysis in Java

Group:          Engineering
License:        Public Domain
URL:            http://rsbweb.nih.gov/ij/index.html
Source0:        http://rsbweb.nih.gov/ij/download/src/ij150h-src.zip
Source1:        %{name}.desktop
Source2:        http://rsbweb.nih.gov/ij/macros/macros.zip
Source3:        http://rsb.info.nih.gov/ij/download/linux/unix-script.txt
Source4:        imagej.png

# don't copy .class files 
patch0:         %{name}-%{version}-patch0.patch
# modify imagej.sh for fedora compatibility
patch1:         %{name}-%{version}-patch1.patch
BuildArch:      noarch


BuildRequires:  jpackage-utils
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  ant
BuildRequires:  desktop-file-utils


Requires:       jpackage-utils
Source44: import.info
# java-devel not java for plugins build

%description
ImageJ is a public domain Java image processing program. It can display,        
edit, analyze a wide variety of image data, including image sequences. Imagej   
can be used for quantitative analysis of engineering and scientific image data.

%package javadoc
Group: Development/Documentation
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c -n "%{name}-%{version}" 
# patch build.xml
%patch0 -p0 -b .patch0
# unzip macros.zip
unzip -qq -u %{SOURCE2} 
# erase binary and useless files 
rm -rf macros/.FBC*
rm macros/build.xml
rm -rf __MACOSX
#get and patch unix-script.txt
cp %{SOURCE3} ./imagej.sh
%patch1 -p1 -b .patch1

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
cd source
ant build javadocs
cd ..

%install

# install jar
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p source/ij.jar   \
$RPM_BUILD_ROOT%{_javadir}/%{name}.jar


# install javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp api  \
$RPM_BUILD_ROOT%{_javadocdir}/%{name}

# install icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/pixmaps

# install data files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -p source/build/about.jpg $RPM_BUILD_ROOT%{_datadir}/%{name}/about.jpg
cp -p source/build/IJ_Props.txt $RPM_BUILD_ROOT%{_datadir}/%{name}/IJ_Props.txt

#install macros
chmod 644 macros/About\ Startup\ Macros 
find ./macros -name \*.txt -type f -exec chmod 644 {} \;
find ./macros -type d -exec chmod 755 {} \;
cp -rp macros $RPM_BUILD_ROOT%{_datadir}/%{name}


#install luts
mkdir $RPM_BUILD_ROOT%{_datadir}/%{name}/luts 

# install script
mkdir -p $RPM_BUILD_ROOT%{_bindir}
chmod +x imagej.sh
cp -p imagej.sh $RPM_BUILD_ROOT%{_bindir}/%{name}

# directory for plugins
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins
#cp source/plugins/JavaScriptEvaluator.source $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/JavaScriptEvaluator.java

# desktop file
desktop-file-install --vendor=""                     \
       --dir=%{buildroot}%{_datadir}/applications/   \
       %{SOURCE1}

%files
%{_javadir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/imagej.png
%{_bindir}/%{name}
%doc source/aREADME.txt source/release-notes.html source/applet.html

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.50-alt1_1.hjpp8
- new version

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.48-alt1_7.ejpp8
- java 8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.48-alt1_1.ejpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1_2.djpp7
- new version

