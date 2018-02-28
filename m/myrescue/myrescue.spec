# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global debug_package %{nil}

Name:           myrescue
Version:        0.9.4
Release:        alt1_7.1
Summary:        Rescue the still-readable data from a damaged harddisk
License:        GPL-2.0+
Group:          File tools
URL:            http://myrescue.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source44: import.info

%description
myrescue is a program to rescue the still-readable data from a
damaged harddisk. It is similar in purpose to dd_rescue, but it
tries to quickly get out of damaged areas to first handle the not
yet damaged part of the disk and return later.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%make_build -C src

%install
install -Dpm 0755 src/myrescue %{buildroot}%{_bindir}/myrescue
install -Dpm 0644 doc/myrescue.1 %{buildroot}%{_mandir}/man1/myrescue.1
gzip -9f %{buildroot}%{_mandir}/man1/myrescue.1
install -Dpm 0644 doc/myrescue.de.1 %{buildroot}%{_mandir}/de/man1/myrescue.1
gzip -9f %{buildroot}%{_mandir}/de/man1/myrescue.1

%files
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/myrescue
%doc %{_mandir}/man1/myrescue.1.*
%doc %{_mandir}/de/man1/myrescue.1.*

%changelog
* Wed Feb 28 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_7.1
- converted for ALT Linux by srpmconvert tools

