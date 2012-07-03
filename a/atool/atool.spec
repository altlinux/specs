# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl
# END SourceDeps(oneline)
BuildRequires: perl(Encode.pm)
Name:		atool
Version:	0.37.0
Release:	alt2_3
Summary:	A perl script for managing file archives of various types

Group:		Archiving/Other
License:	GPLv2+
URL:		http://www.nongnu.org/atool/
Source0:	http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
Source44: import.info

%description
atool is a script for managing file archives of various types.

It includes aunpack (to extract archives), apack (to create archives),
als (to list files), acat (to extract files to the standard output),
etc.

atool relies on external programs to handle the archives.
It determines the archive types using file extensions whenever possible,
with a fallback on 'file'.

It includes support for tarballs, gzip, bzip, bzip2, lzop, lzma, pkzip, rar,
ace, arj, rpm, cpio, arc, 7z, alzip.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}
mv NEWS NEWS.old
iconv -f iso-8859-1 -t UTF-8 -o NEWS NEWS.old


%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/*
%doc NEWS README TODO AUTHORS COPYING
%{_mandir}/man1/*

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.37.0-alt2_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.37.0-alt1_3
- update to new release by fcimport

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.37.0-alt1_2
- initial release by fcimport

