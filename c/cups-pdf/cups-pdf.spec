Name: cups-pdf
Version: 3.0.1
Release: alt1

Summary: Extension for creating pdf-Files with CUPS
Summary(ru_RU.UTF-8): Расширения для создания PDF файлов с помощью CUPS

License: GPLv2+
Group: Publishing
Url: http://www.cups-pdf.de

# Source-url: http://www.cups-pdf.de/src/cups-pdf_%version.tar.gz
Source: %name-%version.tar
Source1: cups-pdf.sh

Patch1: cups-pdf-conf.patch
Patch2: cups-pdf-desktop.patch


Requires(pre): cups
Requires: ghostscript
BuildRequires: perl-MIME-Lite perl-MailTools perl-MIME-tools libcups-devel

BuildRequires: libcups-devel

%description
"cups-pdf" is a backend script for use with CUPS - the "Common UNIX Printing System"
(see more for CUPS under http://www.cups.org/). "cups-pdf" uses the ghostscript pdfwrite
device to produce PDF Files.

%prep
%setup
%patch1 -p0 -b .oldconf
%patch2 -p0 -b .desktop

%build
cc %optflags -D_FILE_OFFSET_BITS=64 -o cups-pdf src/cups-pdf.c -lcups

%install
install -D -m 700 cups-pdf %buildroot%_libexecdir/cups/backend/cups-pdf
install -D -m 644 extra/cups-pdf.conf %buildroot%_sysconfdir/cups/cups-pdf.conf
# Note: also noopt there
install -D -m644 extra/CUPS-PDF_opt.ppd %buildroot%_datadir/cups/model/CUPS-PDF.ppd
#mv contrib/cups-pdf-dispatch-0.1/README README.dispatch
mkdir -p %buildroot%_spooldir/cups-pdf
mkdir -p %buildroot%_spooldir/cups-pdf/SPOOL
install -D -m 755 %SOURCE1 %buildroot%_sysconfdir/firsttime.d/cups-pdf

%post
# First install : create the printer if cupsd is running
if [ "$1" -eq "1" ]
then

    service cups status > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        /usr/sbin/lpadmin -p Cups-PDF -v cups-pdf:/ -m CUPS-PDF.ppd -E || :
    else
        service cups start > /dev/null 2>&1 && /usr/sbin/lpadmin -p Cups-PDF -v cups-pdf:/ -m CUPS-PDF.ppd -E || : && service cups stop > /dev/null 2>&1 || :
    fi
fi

%postun
if [ "$1" -eq "0" ]; then
    # Delete the printer
    /usr/sbin/lpadmin -x Cups-PDF || :
fi

%files
%doc ChangeLog COPYING README
%_sysconfdir/firsttime.d/cups-pdf
%_libexecdir/cups/backend/cups-pdf
%config(noreplace) %_sysconfdir/cups/cups-pdf.conf
%_datadir/cups/model/CUPS-PDF.ppd
%dir %_spooldir/cups-pdf
%dir %_spooldir/cups-pdf/SPOOL

%changelog
* Sat Oct 28 2017 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt1
- new version 3.0.1 (with rpmrb script)
- cleanup spec

* Thu Sep 11 2014 Vitaly Lipatov <lav@altlinux.ru> 2.6.1-alt2
- build with -D_FILE_OFFSET_BITS=64 (ALT bug 30304)

* Thu Sep 27 2012 Andriy Stepanov <stanv@altlinux.ru> 2.6.1-alt1
- New version

* Wed Aug 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.1-alt4
- modify firsttime.d script to add Cups-PDF printer if it does not exist

* Tue Aug 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.1-alt3
- add firsttime.d script to turn Cups-PDF printer into the default
  printer (ALT #26057)

* Thu Aug 11 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.1-alt2
- build for sisyphus (ALT #25918)

* Mon Jul 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.1-alt1
- 2.5.1 with Fedora patches (write PDFs to Desktop)

* Wed Mar 28 2007 Andriy Stepanov <stanv@altlinux.ru> 2.4.5-alt2
- change owner of cups-psd to 700

* Tue Mar 27 2007 Andriy Stepanov <stanv@altlinux.ru> 2.4.5-alt1
- Initial test build

