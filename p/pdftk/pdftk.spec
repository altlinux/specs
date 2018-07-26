Name:		pdftk
Version:	2.02.java
Release:	alt1
Summary:	PDF Tool Kit
License:	GPLv2+
Group:		Publishing
#URL:		https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/
URL:		https://gitlab.com/pdftk-java/pdftk
Source0:	%{name}-%{version}.tar
BuildArch:	noarch
BuildRequires(pre): rpm-macros-java
BuildRequires:	rpm-build-java java-devel-default /proc
BuildRequires:  gradle ant ant-junit ivy-local bouncycastle apache-ivy apache-commons-lang3

Requires:	bouncycastle apache-commons-lang3

%description
Pdftk is a simple tool for doing everyday things with PDF documents.
Keep one in the top drawer of your desktop and use it to:
- Merge PDF Documents
- Split PDF Pages into a New Document
- Decrypt Input as Necessary (Password Required)
- Encrypt Output as Desired
- Fill PDF Forms with FDF Data and/or Flatten Forms
- Apply a Background Watermark
- Report on PDF Metrics, including Metadata and Bookmarks
- Update PDF Metadata
- Attach Files to PDF Pages or the PDF Document
- Unpack PDF Attachments
- Burst a PDF Document into Single Pages
- Uncompress and Re-Compress Page Streams
- Repair Corrupted PDF (Where Possible)

%prep
%setup -q

%build
mkdir lib
build-jar-repository lib bcprov commons-lang3
%ant jar

%install
#install -Dpm 0755 pdftk/pdftk %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 pdftk.1 %{buildroot}%{_man1dir}/%{name}.1
install -Dpm 0644 build/jar/pdftk.jar %{buildroot}%{_javadir}/pdftk.jar

%jpackage_script com.gitlab.pdftk_java.pdftk "" "" bcprov:commons-lang3:pdftk pdftk true

%files
%{_bindir}/%{name}
%{_man1dir}/%{name}.1*
%{_javadir}/pdftk.jar

%changelog
* Thu Jul 26 2018 Igor Vlasenko <viy@altlinux.ru> 2.02.java-alt1
- new pure java fork from gitlab.com/pdftk-java (closes: #35156)
- bogus version because there is no official release yet
- closes

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.02-alt2_4
- converted for ALT Linux by srpmconvert tools

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.02-alt2_2
- rebuild

* Tue Oct 27 2015 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1_2
- new version (closes: #31407)

* Thu Nov 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.44-alt2_11jpp7
- new version

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.44-alt2_10jpp7
- new fc release

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.44-alt2_6jpp6
- build with itext instead of itext2

* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1_6jpp6
- update to new release by jppimport

* Tue Sep 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1_5jpp6
- update to new release by jppimport

* Wed May 27 2009 Igor Vlasenko <viy@altlinux.ru> 1.41-alt1_18jpp5
- Sisyphus build (request by Kirill)

