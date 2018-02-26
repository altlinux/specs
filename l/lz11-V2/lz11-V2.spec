Summary: Printer Drivers for the Lexmark Z11 and Compaq IJ300 printer

Name: lz11-V2
Version: 1.2
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

License: GPL
Group: Publishing

URL: http://sourceforge.net/projects/lz11/
Source:	http://easynews.dl.sourceforge.net/sourceforge/lz11/lz11-V2-%{version}.tar

%description
A Linux printer driver/filter for the Lexmark Z11 and the Compaq IJ300 printer,
supporting color and b/w printing, variable page size and more.

This package contains CUPS drivers (PPD) for the following printers:

 o Compaq IJ300
 o Lexmark Z11

%prep

%setup -q

%build
make CFLAGS="%optflags"

%install

for i in cZ11-V2 cZ11 cZ11-bit* lz11.[^c]*;do
    %__install -Dpm755 $i %buildroot%_bindir/$i
done
rm -f %buildroot/%_bindir/lz11.{stop,install}

%__install -Dpm644 lz11.conf %{buildroot}/etc/LexmarkZ11/lz11.conf
%__install -d %buildroot%_datadir/cups/model
%__install -m644 *.ppd %buildroot%_datadir/cups/model/


%files
%doc ChangeLog README release-notes-*
%dir %_sysconfdir/LexmarkZ11
%config(noreplace) %_sysconfdir/LexmarkZ11/lz11.conf
%_bindir/*
%_datadir/cups/model/*.ppd*

%changelog
* Wed Nov 07 2007 Stanislav Ievlev <inger@altlinux.org> 1.2-alt1
- Build as a separate package
