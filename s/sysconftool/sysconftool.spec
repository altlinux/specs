Group: Development/Tools
Summary: Macros for aclocal to install configuration files
Summary(pl):	Makra dla aclocal do instalacji plików konfiguracyjnych
Name: sysconftool
Version: 0.21
Release: alt1
License: GPLv3 with exceptions
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: http://downloads.sourceforge.net/project/courier/sysconftool/%version/%name-%version.tar.bz2
Url: http://www.courier-mta.org/sysconftool/
BuildArch: noarch
BuildRequires: autoconf
BuildRequires: automake
Source44: import.info

%description
sysconftool is a development utility that helps to install application
configuration files. sysconftool allows an existing application to be
upgraded without losing the older version's configuration settings.

%description -l pl
sysconftool jest narzędziem, które pomaga instalować pliki
konfiguracyjne aplikacji. sysconftool pozwala na wymienienie
istniejących aplikacji na nowsze wersje bez straty starszych wersji
plików konfiguracyjnych.

%prep
%setup

%build
autoreconf
%configure

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# make the symlinks relative
ln -sf ../share/sysconftool/sysconftoolcheck $RPM_BUILD_ROOT%_bindir/
ln -sf ../share/sysconftool/sysconftoolize.pl $RPM_BUILD_ROOT%_bindir/sysconftoolize

%check
make check

%files
%doc AUTHORS ChangeLog COPYING *.html NEWS
%_bindir/sysconftoolcheck
%_bindir/sysconftoolize
%_datadir/sysconftool
%_mandir/man1/sysconftool*
%_mandir/man1/sysconftoolcheck.1*
%_mandir/man7/sysconftool.7*
%_datadir/aclocal/sysconftool.m4

%changelog
* Tue Dec 13 2022 Ilya Mashkin <oddity@altlinux.ru> 0.21-alt1
- 0.21

* Wed Aug 03 2022 Ilya Mashkin <oddity@altlinux.ru> 0.19-alt1
- 0.19

* Mon May 31 2021 Ilya Mashkin <oddity@altlinux.ru> 0.18-alt1
- 0.18

* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 0.17-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_2
- update to new release by fcimport

* Tue Nov 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_1
- update to new release by fcimport

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_5
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_4
- update to new release by fcimport

* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_3
- initial fc import

