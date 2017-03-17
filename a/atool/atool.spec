# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl perl(Encode.pm)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		atool
Version:	0.39.0
Release:	alt1_8
Summary:	A perl script for managing file archives of various types

Group:		Archiving/Other
License:	GPLv2+
URL:		http://www.nongnu.org/atool/
Source0:	http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	rpm-build-perl

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

# Convert to UTF-8 while keeping the original timestamp
iconv -f iso8859-1 -t utf-8 NEWS -o tmp
touch -r NEWS tmp
mv -f tmp NEWS
chmod 0644 NEWS


%build
%configure
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/*
%doc NEWS README TODO AUTHORS COPYING
%{_mandir}/man1/*

%changelog
* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.39.0-alt1_8
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.39.0-alt1_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.39.0-alt1_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.39.0-alt1_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.39.0-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.39.0-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.39.0-alt1_2
- update to new release by fcimport

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.39.0-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.37.0-alt2_4
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.37.0-alt2_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.37.0-alt1_3
- update to new release by fcimport

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.37.0-alt1_2
- initial release by fcimport

