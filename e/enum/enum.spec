Name: enum
Version: 1.0.3
Release: alt1_1
Summary: Seq- and jot-like enumerator

Group:   File tools
License: BSD
URL:     https://fedorahosted.org/enum
Source0: https://fedorahosted.org/releases/e/n/enum/%{name}-%{version}.tar.bz2
Source44: import.info

%description
Utility enum enumerates values (numbers) between two values, possibly
further adjusted by a step and/or a count, all given on the command line.
Before printing, values are passed through a formatter. Very fine control
over input interpretation and output is possible.


%prep
%setup -q


%build
%configure --disable-doc-rebuild
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%check
make check

%files
%doc COPYING ChangeLog
%_mandir/man1/enum.1*
%_bindir/enum


%changelog
* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_1
- initial release by fcimport

