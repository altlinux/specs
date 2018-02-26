##
##  shtool.spec -- RPM specification for shtool package
##  Copyright (c) 2000-2002 Ralf S. Engelschall <rse@engelschall.com>
##
##  This file is part of shtool and free software; you can redistribute
##  it and/or modify it under the terms of the GNU General Public
##  License as published by the Free Software Foundation; either version
##  2 of the License, or (at your option) any later version.
##
##  This file is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
##  General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program; if not, write to the Free Software
##  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307,
##  USA, or contact Ralf S. Engelschall <rse@engelschall.com>.
##

#   This is a specification file for the RedHat Package Manager (RPM).
#   It is part of the shtool source tree and this way directly included
#   in shtool distribution tarballs. This way one can use a simple "rpm
#   -tb shtool-1.X.Y.tar.gz" command to build binary RPM packages from a
#   original shtool distribution tarball.

#
# This Spec is adopted for ALT Linux Specific
#
Name: shtool
Version: 2.0.8
Release: alt2
Group: Development/Other

License: GPL

Url: http://www.gnu.org/software/shtool/

Summary: GNU shtool, The GNU Portable Shell Tool

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: ftp://ftp.gnu.org/gnu/shtool/shtool-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jun 19 2005
BuildRequires: termutils perl-podlators

%description
    GNU shtool is a compilation of small but very stable and portable
    shell scripts into a single shell tool. All ingredients were in
    successful use over many years in various free software projects.
    The compiled shtool program is intended to be used inside the
    source tree of other free software packages. There it can overtake
    various (usually non-portable) tasks related to the building and
    installation of such a package. It especially can replace the old
    mkdir.sh, install.sh and related scripts.

%prep
%setup -q

%build
%configure

%make
%make test

%install
%makeinstall

# Install Docs
mkdir -p $RPM_BUILD_ROOT%_docdir/%name-%version
install -p -m644 AUTHORS COPYING ChangeLog INSTALL README THANKS $RPM_BUILD_ROOT%_docdir/%name-%version

%files
%dir %_docdir/%name-%version

%dir %_datadir/%name
%_datadir/%name/*
%_bindir/shtool
%_bindir/shtoolize

%_man1dir/*

%_datadir/aclocal/shtool.m4
%doc AUTHORS  ChangeLog  COPYING  INSTALL  README  THANKS

%changelog
* Fri Dec 23 2010 Ilya Mashkin <oddity@altlinux.ru> 2.0.8-alt2
- fix build

* Fri Jan 09 2009 Ilya Mashkin <oddity@altlinux.ru> 2.0.8-alt1
- 2.0.8

* Sun Jun 19 2005 Serge A. Volkov <vserge at altlinux.ru> 2.0.2-alt1
- Update to new version 2.0.2 (Security FIX)

* Thu Aug 05 2004 Serge A. Volkov <vserge@altlinux.org> 2.0.0-alt1
- Update version to 2.0.0

* Sun Jun 20 2004 Serge A. Volkov <vserge@altlinux.org> 1.6.1-alt2
- Spec cleanup
- Update BuildReq

* Wed Oct 30 2002 Serge A. Volkov <vserge@altlinux.ru> 1.6.1-alt1
- Update for new versions 
- Correct rpm GROUP

* Fri Jun 14 2002 Serge A. Volkov <vserge@altlinux.ru> 1.6.0-alt1
- Initial release for ALT Linux Team
