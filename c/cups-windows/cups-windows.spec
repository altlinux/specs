#
# "$Id: cups-windows.spec.in 5 2006-04-19 23:47:43Z mike $"
#
#   RPM "spec" file for the CUPS Windows driver.
#
#   Copyright 2006 by Easy Software Products, all rights reserved.
#
#   These coded instructions, statements, and computer programs are the
#   property of Easy Software Products and are protected by Federal
#   copyright law.  Distribution and use rights are outlined in the file
#   "LICENSE.txt" which should have been included with this file.  If this
#   file is missing or damaged please contact Easy Software Products
#   at:
#
#       Attn: CUPS Licensing Information
#       Easy Software Products
#       44141 Airport View Drive, Suite 204
#       Hollywood, Maryland 20636 USA
#
#       Voice: (301) 373-9600
#       EMail: cups-info@cups.org
#         WWW: http://www.cups.org
#

Summary: Common UNIX Printing System Windows driver for use with Samba.
Name: cups-windows
Version: 6.0
Release: alt1
Epoch: 0
License: GPL
Group: System/Servers
Source: ftp://ftp.easysw.com/pub/cups/windows/cups-windows-6.0-source.tar.bz2
Url: http://www.cups.org/windows/
Packager: Igor Vlasenko <viy@altlinux.ru>

BuildRequires: libcups-devel

# Dependencies...
Requires: cups >= 1.2

%description
The Common UNIX Printing System provides a portable printing
layer for UNIX(R) operating systems. This is the Windows driver
support package for use with Samba.

%prep
%setup
%build
%install
# Make sure the RPM_BUILD_ROOT directory exists.
rm -rf $RPM_BUILD_ROOT

make BUILDROOT=$RPM_BUILD_ROOT install

%files
%dir /usr/share/cups/drivers
/usr/share/cups/drivers/*

%changelog
* Fri Apr 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:6.0-alt1
- first build

#
# End of "$Id: cups-windows.spec.in 5 2006-04-19 23:47:43Z mike $".
#
