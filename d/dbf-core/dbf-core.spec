Name: dbf-core
Version: 0.9.0
Release: alt1

Summary: Program to read and convert dBASE files
License: BSD-like
Group: Databases
Url: http://dbf.berlios.de/

Source0: %name-%version.tar.bz2

Packager: Igor Zubkov <icesik@altlinux.org>

Obsoletes: dbf
Provides: dbf

# Automatically added by buildreq on Wed Feb 21 2007
#BuildRequires: gcc-c++ gcc-fortran libdbf-devel linux-libc-headers packages-info-i18n-common perl-XML-Parser
BuildRequires: gcc-c++ libdbf-devel perl-XML-Parser

%description
dbf is an easy-to-use command line tool to show and convert the content
of dBASE III, IV, and 5.0 files. It reads dBASE databases and prints the
content to the screen or converts it to comma-separated (*.csv) files
which can be opened in Excel, StarOffice, and most other spread sheets.

It can also be used to show some statistics about the content.

%prep
%setup -q -n %name

%build
chmod +x configure
chmod +x install-sh
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang dbf

%files -f dbf.lang
%doc AUTHORS BUGS CREDITS ChangeLog FAQ NEWS README
%_bindir/dbf

%changelog
* Wed Feb 21 2007 Igor Zubkov <icesik@altlinux.org> 0.9.0-alt1
- build for Sisyphus


