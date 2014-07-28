# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jtnef
Version:        1.6.0
Release:        alt1_8jpp7
Summary:        Java TNEF package

Group:          Development/Java
License:        GPLv2+
URL:            http://www.freeutils.net/source/jtnef/
Source0:        http://www.freeutils.net/source/jtnef/jtnef-1_6_0.zip
BuildArch:      noarch
ExcludeArch:    ppc64

BuildRequires:  jpackage-utils
BuildRequires:  javamail
BuildRequires:  apache-poi
Requires:       jpackage-utils
Requires:       javamail
Requires:       apache-poi
Source44: import.info

%description
The Java TNEF package is an open source code implementation of a TNEF message
handler, which can be used as a command-line utility or integrated into Java-
based mail applications to extract the original message content. 

Transport-Neutral Encapsulation Format (TNEF) is Microsoft's non-standard
format for encapsulating mail which has any non-plain-text content or
properties (such as rich text, embedded OLE objects, voting buttons, and
sometimes just attachments). Whether or not a given message is encoded using
TNEF is determined by the Outlook default settings, per-recipient setting,
Exchange Server settings, and message type and content.

Once a TNEF message is used, the entire message, including all the original
attachments and properties, is encapsulated in a single attachment of mime
type "application/ms-tnef" added to the message to be sent over the Internet.
This attachment is usually named "WINMAIL.DAT", and when sent to any non-MS
mail client, is useless, and makes access to the original message attachments
impossible.


%package javadoc                                                                                 
Summary:        Javadocs for %{name}                                                             
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch
                                                                                                 
%description javadoc                                                                             
This package contains the API documentation for %{name}.                                         


%prep
%setup -q -c
find -name '*.jar' -delete
sed -i -e 's/\r//' *.txt
mkdir classes


%build
export CLASSPATH=$(build-classpath javamail poi)
javac -d classes `find src -name *.java`
jar -cf %{name}.jar -C classes .

javadoc -quiet -windowtitle "Java TNEF package %version" -use -d javadoc -sourcepath src net.freeutils.tnef


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p %{name}.jar   \
  $RPM_BUILD_ROOT%{_javadir}/

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -rp javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%doc CHANGES.txt LICENSE.txt README.txt
%{_javadir}/%{name}.jar

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_8jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_7jpp7
- new version

