%define _unpackaged_files_terminate_build 1

Summary: CUPS driver for Brother P-touch label printers

%define orig_name ptouch-driver

Name: printer-driver-ptouch
Version: 1.7
Release: alt1

Provides: %orig_name = %version
Obsoletes: %orig_name

Group: Publishing
License: GPL

URL: https://github.com/philpem/printer-driver-ptouch
#Source: https://github.com/philpem/printer-driver-ptouch/archive/refs/tags/v%version.tar.gz
Source: %orig_name-%version.tar

Requires: cups

# Automatically added by buildreq on Wed Nov 07 2007
BuildRequires: libcups-devel libpng-devel perl-XML-LibXML

%description
This is a CUPS raster filter for Brother P-touch label printers.  It is
meant to be used by the PostScript Description files of the drivers from
the foomatic package.

%prep
%setup -q -n %orig_name-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall libdir=%buildroot%_prefix/lib
# those files conflicts with foomatic-db
rm -rf %buildroot%_datadir/foomatic/db/source/printer/

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_datadir/foomatic/db/source/driver/*.xml
%_datadir/foomatic/db/source/opt/*.xml
%_prefix/lib/cups/filter/*

%changelog
* Mon Apr 22 2024 Oleg Solovyov <mcpain@altlinux.org> 1.7-alt1
- New version 1.7

* Tue Sep 28 2021 Oleg Solovyov <mcpain@altlinux.org> 1.6-alt1
- New version 1.6

* Mon Feb 08 2021 Oleg Solovyov <mcpain@altlinux.org> 1.4.2-alt3
- fix build

* Mon Jul 17 2018 Oleg Solovyov <mcpain@altlinux.org> 1.4.2-alt2
- fix files (conflicts with foomatic-db)

* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 1.4.2-alt1
- Build version 1.4.2

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Sep 30 2009 Stanislav Ievlev <inger@altlinux.org> 1.3-alt1
- 1.3

* Fri Nov 21 2008 Stanislav Ievlev <inger@altlinux.org> 1.2-alt2
- fix build with gcc-4.3
- rename package to printer-driver-ptouch

* Wed Nov 07 2007 Stanislav Ievlev <inger@altlinux.org> 1.2-alt1
- Initial build
