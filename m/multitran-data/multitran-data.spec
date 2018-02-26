Name: multitran-data
Version: 0.3
Release: alt2

Summary: Multitran dictionary data
License: GPL
Group: System/Internationalization
Url: http://www.multitran.ru

Buildarch: noarch

Source: %name.tar.bz2
Source1: mt.conf

Requires: multitran-dict-en-ru

%define mtname multitran
%define mtdatadir %_datadir/multitran

%description
multitran dictionary data, this package only for backward 
compatibility with libmt

%package -n %mtname-dict-en-ru
Summary: english-russian Multitran dictionary
Group: System/Internationalization
Provides: %mtname-dict
Requires: %mtname-data-en, %mtname-data-ru

%description -n %mtname-dict-en-ru
english-russian Multitran dictionary

%package -n %mtname-data-en
Summary: english language data for Multitran
Group: System/Internationalization

%description -n %mtname-data-en
english language data for Multitran

%package -n %mtname-data-ru
Summary: russian language data for Multitran
Group: System/Internationalization

%description -n %mtname-data-ru
russian language data for Multitran

%package -n %mtname-data-common
Summary: common data for Multitran
Group: System/Internationalization

%description -n %mtname-data-common
common data for Multitran

%prep
%setup -q -n %name

%build

%install
%__install -pD %SOURCE1 -m644  $RPM_BUILD_ROOT%_sysconfdir/mt.conf
%makeinstall DESTDIR=$RPM_BUILD_ROOT

%files
%_sysconfdir/*
%mtdatadir/usertra*

%files -n %mtname-dict-en-ru
%mtdatadir/eng_rus/*

%files -n %mtname-data-en
%mtdatadir/english/*

%files -n %mtname-data-ru
%mtdatadir/russian/*

%files -n %mtname-data-common
%mtdatadir/*.txt

%changelog
* Fri Mar 10 2006 Stanislav Ievlev <inger@altlinux.ru> 0.3-alt2
- update subjects

* Fri Nov 12 2004 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- 0.3, accomodations for new libmt generation

* Wed Sep 22 2004 Stanislav Ievlev <inger@altlinux.org> 0.02-alt1.1
- rebuild in hasher

* Tue Feb 18 2003 Peter A. Novodvorsky <nidd@altlinux.com> 0.02-alt2
- new upstream

* Thu Feb 08 2003 Peter A. Novodvorsky <nidd@altlinux.com> 0.01-alt1
- Initial revision.
