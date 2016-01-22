# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: gcc-java gcc-c++ /usr/bin/dos2unix java-1.5.0-gcj
%define gcj_support	1

Name:		pdftk
Version:	2.02
Release:	alt2_2
Summary:	PDF Tool Kit
License:	GPLv2+
Group:		Publishing
URL:		https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/
Source0:	https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/%{name}-%{version}-src.zip
# since the gcj version is hardcoded in this patch, don't forget to updated it
# when gcc is updated, current version is 5.2.1
Patch0:		pdftk-1.44-makefile-fix.patch
Source44: import.info


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
%setup -q -n %{name}-%{version}-dist
%patch0 -p0 -b .makefix

dos2unix changelog.txt pdftk.1.txt

chmod 0644 pdftk.1.html pdftk.1.txt changelog.txt

GCC_VERSION=$(gcc -dumpversion)
sed -i s/'^export VERSUFF=$'/"export VERSUFF=-${GCC_VERSION}"/ pdftk/Makefile.Redhat

%build
pushd pdftk
	GCJFLAGS="%{optflags} -I`pwd`/../java -Wno-all" make -f Makefile.Redhat
popd

%install
install -Dpm 0755 pdftk/pdftk %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 pdftk.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc pdftk.1.html pdftk.1.txt changelog.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
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

