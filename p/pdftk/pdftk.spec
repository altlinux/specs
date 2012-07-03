# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: gcc-c++
BuildRequires: /proc
BuildRequires: jpackage-compat
%global itextvers 2.1.7

Summary:        The PDF Tool Kit
Name:           pdftk
Version:        1.44
Release:        alt2_6jpp6
License:        GPLv2+
URL:            http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/
Source0:        http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/%{name}-%{version}-src.zip
Patch0:         pdftk-use-internal-itext.patch
# Solves ".afm files not found" error. RHBZ#494785:
Patch4:         pdftk-classpath.patch
Group:          Publishing
BuildRequires:  gcc-java
BuildRequires:  libgcj-devel

BuildRequires:  itext >= %{itextvers}

Requires:       itext >= 2.1.7-6

%{?filter_setup:
%filter_from_requires /\.jar\.so/d
%filter_setup
}
Source44: import.info

%description
If PDF is electronic paper, then pdftk is an electronic staple-remover,
hole-punch, binder, secret-decoder-ring, and X-Ray-glasses. Pdftk is a simple
tool for doing everyday things with PDF documents. Keep one in the top drawer
of your desktop and use it to:

   * Merge PDF Documents
   * Split PDF Pages into a New Document
   * Decrypt Input as Necessary (Password Required)
   * Encrypt Output as Desired
   * Burst a PDF Document into Single Pages
   * Report on PDF Metrics, including Metadata and Bookmarks
   * Uncompress and Re-Compress Page Streams
   * Repair Corrupted PDF (Where Possible)

Pdftk is also an example of how to use a library of Java classes in a
stand-alone C++ program. Specifically, it demonstrates how GCJ and CNI allow
C++ code to use iText's (itext-paulo) Java classes.

%prep
%setup -q -n %{name}-%{version}-dist
%patch0 -p1
%patch4 -p0 -b .classpath

# Remove bundled libraries from the source tree
rm -rf java

# Fix EOL encoding
for file in *.txt license_gpl_pdftk//*.txt; do
    sed 's|\r||' $file > $file.tmp
    touch -r $file $file.tmp
    mv $file.tmp $file
done

%build
# Requires as a workaround for gcc BZ #39380
export CFLAGS="${RPM_OPT_FLAGS}"
jar tf %{_javadir}/itext-%{itextvers}.jar | grep '\.class$' | sed 's/\.class//' | sed 's|/|\.|g' > classes
    gjavah -d java -cni -classpath=%{_javadir}/itext-%{itextvers}.jar \
       `cat classes`
    cd pdftk
    make -f Makefile.Redhat LIBDIR=%{_libdir} %{?_smp_mflags} ITEXTVERS="%{itextvers}" 

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 0755 pdftk/pdftk $RPM_BUILD_ROOT/%{_bindir}/pdftk
install -m 0644 pdftk.1 $RPM_BUILD_ROOT/%{_mandir}/man1/pdftk.1

%files
%doc changelog.html changelog.notes changelog.txt
%doc pdftk.1.html pdftk.1.notes pdftk.1.txt
%doc license_gpl_pdftk/pdftk_gpl_license.txt license_gpl_pdftk/readme.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

%changelog
* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.44-alt2_6jpp6
- build with itext instead of itext2

* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1_6jpp6
- update to new release by jppimport

* Tue Sep 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1_5jpp6
- update to new release by jppimport

* Wed May 27 2009 Igor Vlasenko <viy@altlinux.ru> 1.41-alt1_18jpp5
- Sisyphus build (request by Kirill)

