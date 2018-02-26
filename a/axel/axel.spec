Name:		axel		
Version:	2.4
Release:	alt2_6
Summary:	Accelerated download client

Group:		Networking/Other
License:	GPLv2+
URL:		http://axel.alioth.debian.org/
Source0:	http://alioth.debian.org/frs/download.php/3015/%{name}-%{version}.tar.gz
BuildRequires:	gettext
Source44: import.info



%description
Axel tries to accelerate HTTP/FTP downloading process by using 
multiple connections for one file. It can use multiple mirrors for a 
download. Axel has no dependencies and is lightweight, so it might 
be useful as a wget clone on byte-critical systems.

%prep
%setup -q

%build
export CFLAGS=" %{optflags}"
export CXXFLAGS=" %{optflags}"
./configure --prefix=%{_prefix} --strip=0
make %{?_smp_mflags}


%install
make install \
	DESTDIR=%{buildroot}

install -m 755 -p %{name} %{buildroot}%{_bindir}

%find_lang	%{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%doc CHANGES CREDITS API README COPYING
%config(noreplace) %{_sysconfdir}/axelrc
%{_mandir}/man1/axel.1*
%{_mandir}/zh_CN/man1/axel.1*

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_6
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_5
- initial release by fcimport

