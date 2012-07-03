Name:          clpbar
Version:       1.10.9
Release:       alt2_5
Summary:       Show information about a data transfer

Group:         File tools
License:       LGPLv2+
URL:           http://clpbar.sourceforge.net/
Source0:       http://downloads.sourceforge.net/%{name}/bar_%{version}.tar.gz
Source1:       clpbar.1.in
Patch0:        bar-1.10.9-clpbar.patch
Patch1:        bar-1.10.9-Makefile.patch


BuildRequires: automake
BuildRequires: autoconf
Source44: import.info

%description
Bar is a simple tool to process a stream of data and print a display for the
user on stderr showing (a) the amount of data passed, (b) the throughput of the
data transfer, and, if the total size of the data stream is known, (c)
estimated time remaining, percent complete, and a progress bar.  Bar was
originally written for the purpose of estimating the amount of time needed to
transfer large amounts (many, many gigabytes) of data across a network.
(Usually in an SSH/tar pipe.)

%prep
%setup -q -n bar-%{version}
%patch0 -p1
%patch1 -p1
cp %{SOURCE1} .
./autogen

%build
%configure
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS COPYING ChangeLog TODO TROUBLESHOOTING
%{_bindir}/clpbar
%{_mandir}/man1/clpbar.1.*

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.10.9-alt2_5
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.10.9-alt1_5
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.10.9-alt1_4
- initial release by fcimport

