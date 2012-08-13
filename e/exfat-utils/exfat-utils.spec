Summary:    Utilities for exFAT file system
Summary(ru):Утилиты для файловой системы exFAT
Name:       exfat-utils
Version:    0.9.7
Release:    alt1_1

License:    GPLv3+
Group:      System/Base
Source0:    http://exfat.googlecode.com/files/exfat-utils-%{version}.tar.gz
Source100:  README.RFRemix
URL:        http://code.google.com/p/exfat/

BuildRequires:  scons
BuildRequires:  gzip
BuildRequires:  libfuse-devel
Source44: import.info


%description
A set of utilities for creating, checking, dumping and labelling exFAT file
system.

%description -l ru
Набор утилит для создания, проверки, дампа и назначения метки для
файловой системы exFAT.


%prep
%setup -q


%build
scons
cp %{SOURCE100} .


%install
scons install DESTDIR=$RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8/
gzip -9 -c dump/dumpexfat.8 > $RPM_BUILD_ROOT%{_mandir}/man8/dumpexfat.8.gz
gzip -9 -c fsck/exfatfsck.8 > $RPM_BUILD_ROOT%{_mandir}/man8/exfatfsck.8.gz
gzip -9 -c mkfs/mkexfatfs.8 > $RPM_BUILD_ROOT%{_mandir}/man8/mkexfatfs.8.gz
gzip -9 -c label/exfatlabel.8 > $RPM_BUILD_ROOT%{_mandir}/man8/exfatlabel.8.gz


%files
%{_sbindir}/dumpexfat
%{_sbindir}/exfatfsck
%doc README.RFRemix
%attr(755,root,root) %{_sbindir}/fsck.exfat
%{_sbindir}/mkexfatfs
%attr(755,root,root) %{_sbindir}/mkfs.exfat
%{_sbindir}/exfatlabel
%attr(644,root,root) %{_mandir}/man8/dumpexfat.8.gz
%attr(644,root,root) %{_mandir}/man8/exfatfsck.8.gz
%attr(644,root,root) %{_mandir}/man8/mkexfatfs.8.gz
%attr(644,root,root) %{_mandir}/man8/exfatlabel.8.gz


%changelog
* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1_1
- new release

