%global rel r9153

Name:		agedu
Version:	0
Release:	alt2_3.r9153
Summary:	An utility for tracking down wasted disk space
Group:		File tools
License:	MIT
URL:		http://www.chiark.greenend.org.uk/~sgtatham/agedu/
# Upstream tarball is regenerated nightly, so md5sums will differ.
Source0:	http://www.chiark.greenend.org.uk/~sgtatham/agedu/agedu-%{rel}.tar.gz
Source44: import.info

%description
Agedu is a program that helps you to track down wasted disk space by creating
a graphical representation of last access times and occupied disk space of
files and directories.

%prep
%setup -q -n %{name}-%{rel}


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"


%files
%doc LICENCE TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt2_3.r9153
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt1_3.r9153
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0-alt1_2.r9153
- initial release by fcimport

