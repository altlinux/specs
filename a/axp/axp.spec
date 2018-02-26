Name: axp
Version: 0.2.1
Release: alt1

Summary: axp is a modular command line tool extending GNU Arch functionality. 
License: GPL
Group: Development/Other
URL: http://migo.sixbit.org/software/axp/

BuildArch: noarch

Source: %name-%version.tar.bz2


# Automatically added by buildreq on Mon Jan 31 2005 (-bi)
BuildRequires: perl-Arch

%description 
AXP stands for Arch eXtension Platform (or Arch eXtended by Perl).

This is a command line tool with a modular, hierarchical and pluggable
command set, that provides an additional GNU Arch functionality.

%prep
%setup -q

%install
%make install prefix=%_prefix DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%perl_vendor_privlib
mv $RPM_BUILD_ROOT%_datadir/%name/perllib/* $RPM_BUILD_ROOT%perl_vendor_privlib
rmdir $RPM_BUILD_ROOT%_datadir/%name/perllib/
rm -rf $RPM_BUILD_ROOT%perl_vendor_privlib/Arch

%files
%doc AUTHORS README doc ChangeLog NEWS
%_bindir/*
%perl_vendor_privlib/AXP


%changelog
* Tue Oct 11 2005 Alexey Voinov <voins@altlinux.ru> 0.2.1-alt1
- new version (0.2.1)

* Wed Apr 27 2005 Alexey Voinov <voins@altlinux.ru> 0.2.0-alt1
- new version (0.2.0)

* Mon Jan 31 2005 Alexey Voinov <voins@altlinux.ru> 0.1.1-alt1
- initial build
