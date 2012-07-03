# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jorbis
Version:        0.0.17
Release:        alt1_6jpp7
Summary:        Pure Java Ogg Vorbis Decoder
URL:            http://www.jcraft.com/jorbis/
License:        LGPLv2+
Group:          System/Libraries
Source0:        http://www.jcraft.com/jorbis/%{name}-%{version}.zip
# Some fixes from the jorbis copy embedded in cortada. I've mailed upstream
# asking them to integrate these, for more info also see:
# https://trac.xiph.org/ticket/1565
# Note that although the original git headers were left in place for reference
# the actual patches have been rebased to 0.0.17 !
Patch0:         jorbis-0.0.17-cortado-fixes.patch
BuildArch:      noarch
BuildRequires:  jpackage-utils
Requires:       jpackage-utils
# We used to also package the comment editor example, but that is not so
# useful to end users (esp. the passing of cmdline args as java defines)
Obsoletes:      %{name}-comment <= 0.0.17-3
Source44: import.info

%description
JOrbis is a pure Java Ogg Vorbis decoder.


%package javadoc
Summary:        Java docs for jorbis
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains the API documentation for jorbis.


%package player
Summary:        Java applet for playing ogg-vorbis files from a browser
License:        GPLv2+
Group:          Sound
Requires:       %{name} = %{version}-%{release}

%description player
This package contains JOrbisPlayer a simple java applet for playing
ogg-vorbis files from a browser.
See %{_docdir}/%{name}-player-%{version}/JOrbisPlayer.html for
an example how to embed and use the applet.


%prep
%setup -q
%patch0 -p1


%build
javac com/jcraft/jogg/*.java com/jcraft/jorbis/*.java player/*.java
jar cf jogg.jar com/jcraft/jogg/*.class
jar cf jorbis.jar com/jcraft/jorbis/*.class
jar cf JOrbisPlayer.jar player/*.class
javadoc -d doc -public com/jcraft/*/*.java


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -a *.jar $RPM_BUILD_ROOT%{_javadir}
cp -a doc $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%doc ChangeLog COPYING.LIB README
%{_javadir}/jogg.jar
%{_javadir}/jorbis.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%files player
%doc player/JOrbisPlayer.html
%{_javadir}/JOrbisPlayer.jar


%changelog
* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.17-alt1_6jpp7
- new version

