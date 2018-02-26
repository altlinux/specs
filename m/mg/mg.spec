Name:		mg
Version:	20110905
Release:	alt2_2
Summary:	Tiny Emacs-like editor

Group:		Editors
License:	BSD and ISC and MirOS
URL:		http://homepage.boetes.org/software/mg/
Source0:	http://homepage.boetes.org/software/mg/%{name}-%{version}.tar.gz

BuildRequires:	libncurses-devel
Source44: import.info

%description
mg is a tiny, mostly public-domain Emacs-like editor included in the base 
OpenBSD system. It is compatible with Emacs because there shouldn't be any 
reason to learn more editor types than Emacs or vi.

%prep
%setup -q

%build
# configure takes no arguments and will fail if you give it any, therefore we
# do not use the configure macro here
./configure
make %{?_smp_mflags} CFLAGS="%{optflags}" LDFLAGS="%{optflags} -lncurses" libdir="%{_libdir}"

%install
make install DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} \
     INSTALL='install -p'

%files
%doc README tutorial
%{_bindir}/mg
%{_mandir}/man1/mg.1.*

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20110905-alt2_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20110905-alt1_2
- update to new release by fcimport

* Thu Oct 06 2011 Igor Vlasenko <viy@altlinux.ru> 20110905-alt1_1
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 20110120-alt1_1
- initial release by fcimport

