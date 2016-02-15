Name:		auto-destdir
Version:	1.11
Release:	alt2_10
Summary:	Automate DESTDIR support for "make install"

Group:		Development/Tools
License:	MIT
URL:		http://www.dwheeler.com/auto-destdir
Source0:	http://www.dwheeler.com/auto-destdir/%{name}-%{version}.tgz

BuildArch:	noarch
Source44: import.info

%description
Auto-DESTDIR is a set of programs for POSIX/Unix/Linux systems that helps
automate program installation from source code.  It can be useful for
creating native packages (e.g., RPM or deb), or for installing programs
from source code to be managed by tools like GNU stow.

The Auto-DESTDIR tools (run-redir and make-redir) redirect file installations
so that the installed files are placed inside the the $DESTDIR directory,
even if the provided makefile doesn't support the DESTDIR convention.
In most cases you can simply replace "make install" with
"make-redir DESTDIR=... install".

%prep
%setup -q


%build
%configure --scriptdir="%{_libexecdir}/%{name}"
make


%install
make DESTDIR="%{buildroot}" install
chmod a-x %{buildroot}/%{_mandir}/man1/*


%files
%{_bindir}/*
%{_libexecdir}/%{name}/
%doc %{_mandir}/man1/*
%doc README
%doc COPYING

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_9
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_4
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_3
- rebuild to get rid of #27020

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_3
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_2
- initial release by fcimport

