Name: i8kutils
Version: 1.33
Release: alt1
Summary: Dell laptop SMM BIOS support
License: GPLv2+
Group: Monitoring
Source: http://ftp.debian.org/debian/pool/main/i/i8kutils/%{name}_%version.tar.gz

%description
This package contains a user-space programs for accessing the SMM BIOS
of Dell Inspiron and Latitude laptops. The SMM BIOS is used on many
recent laptops to implement APM functionalities and to access custom
hardware, for example cooling fans and volume buttons.

Also provided is a cool and useful plugin for gkrellm.
Note that you need the "Dell Laptop" option compiled into your kernel
(included in the main kernel tree since 2.4.14-pre8)

%package -n i8kmon
Summary: Dell laptop SMM BIOS monitoring tool
Group: Monitoring

%description -n i8kmon
This package contains a monitoring tool for accessing the SMM BIOS
of Dell Inspiron and Latitude laptops.

%prep
%setup

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%_bindir
%makeinstall_std

%files
%doc README.*
%_bindir/i8kbuttons
%_bindir/i8kctl
%_bindir/i8kfan

%files -n i8kmon
%_bindir/i8kmon

%changelog
* Mon Jul 18 2011 Fr. Br. George <george@altlinux.ru> 1.33-alt1
- Initial build from MDV

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.33-3mdv2011.0
+ Revision: 619494
- the mass rebuild of 2010.0 packages

* Fri Oct 23 2009 Olivier Blin <oblin@mandriva.com> 1.33-2mdv2010.0
+ Revision: 459005
- split out i8kmon in its own package (suggested by i8kutils), not to
  pull tcl/tk and libX11 in minimal installations

* Mon Sep 28 2009 Frederik Himpe <fhimpe@mandriva.org> 1.33-1mdv2010.0
+ Revision: 450631
- update to new version 1.33

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.27-4mdv2010.0
+ Revision: 429484
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.27-3mdv2009.0
+ Revision: 247134
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.27-1mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Adam Williamson <awilliamson@mandriva.org> 1.27-1mdv2008.0
+ Revision: 63867
- rebuild for 2008
- don't package license (not required)
- use makeinstall_std macro
- correct URLs
- use Fedora license policy (GPLv2+)
- requires tcl and tk (fix #31132)
- new release 1.27
- Import i8kutils

* Thu Jan 05 2005 Lenny Cartier <lenny@mandriva.com> 1.25-2mdk
- rebuild

* Tue Aug 24 2004 Erwan Velu <erwan@mandrakesoft.com> 1.25-1mdk
- 1.25
* Tue Oct 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.17-2mdk
- buildrequires
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- quiet setup
- compile with $RPM_OPT_FLAGS
- updated description

* Wed Dec 18 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.17-1mdk
- new
