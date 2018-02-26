Name: xemacs-gnus
Version: 1.94
Release: alt1

%define_xemacs_package gnus

Summary: The Gnus Newsreader and Mailreader
License: GPL
Group: Networking/News

%description
The Gnus Newsreader and Mailreader for XEmacs

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.94-alt1
- 1.94

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.93-alt1
- 1.93

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.90-alt1
- 1.90

* Sun Jan 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.89-alt1
- 1.89

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.87-alt1
- 1.87

* Sun Jul  3 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.85-alt1
- 1.85

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.82-alt1
- 1.82

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.80-alt1
- 1.80

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.79-alt1
- 1.79

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.73-alt1
- 1.73

* Sat Jun 07 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.71-alt1
 - 1.71

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.68-alt1
 - 1.68

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.65-alt1
- 1.65

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.64-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.64-alt1
- 1.64

* Thu Oct  3 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.62-alt2
- openssl invocation in nntp.el fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.62-alt1
- first build for %distribution distribution

