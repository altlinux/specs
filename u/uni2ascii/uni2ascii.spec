Name: uni2ascii
Version: 4.18
Release: alt1

Summary: Convert between UTF-8 Unicode and 7-bit ASCII equivalents
License: GPLv3
Group: File tools

Url: http://www.billposer.org/Software/uni2ascii.html
Source: http://billposer.org/Software/Downloads/uni2ascii-%version.tar.bz2

# Automatically added by buildreq on Fri Feb 29 2008 (-bi)
BuildRequires: tk

%description
uni2ascii and ascii2uni convert between UTF-8 Unicode and more than a dozen
7-bit ASCII equivalents including: hexadecimal and decimal HTML numeric
character references, \u-escapes, standard hexadecimal, raw hexadecimal, and
RFC2396 URI format. Such ASCII equivalents are encountered in a variety of
circumstances, such as when Unicode text is included in program source, when
entering text into Web programs that can handle the Unicode character set but
are not 8-bit safe, and when debugging.

%package -n u2a
Summary: A graphical interface to uni2ascii and ascii2uni
Group: File tools
Requires: uni2ascii = %version-%release
# tklib needed for tablelist library, buildreq not detected this dep:
Requires: tklib

BuildArch: noarch

%description -n u2a
A graphical interface to uni2ascii and ascii2uni. uni2ascii and ascii2uni
convert between UTF-8 Unicode and more than a dozen 7-bit ASCII equivalents.

%prep
%setup

%build
%configure
%make_build CFLAGS="%optflags"

%install
%makeinstall_std

%files
%_bindir/uni2ascii
%_bindir/ascii2uni
%_man1dir/*

%files -n u2a
%_bindir/u2a

%changelog
* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 4.18-alt1
- 4.18

* Fri Mar 04 2011 Victor Forsiuk <force@altlinux.org> 4.17-alt1
- 4.17

* Tue Dec 14 2010 Victor Forsiuk <force@altlinux.org> 4.16-alt1
- 4.16

* Mon Aug 30 2010 Victor Forsiuk <force@altlinux.org> 4.15-alt1
- 4.15

* Wed Sep 30 2009 Victor Forsyuk <force@altlinux.org> 4.14-alt1
- 4.14

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 4.11-alt1
- 4.11

* Mon Sep 15 2008 Victor Forsyuk <force@altlinux.org> 4.10-alt1
- 4.10

* Tue Aug 26 2008 Victor Forsyuk <force@altlinux.org> 4.9-alt1
- 4.9

* Fri Apr 04 2008 Victor Forsyuk <force@altlinux.org> 4.6-alt1
- 4.6

* Mon Mar 24 2008 Victor Forsyuk <force@altlinux.org> 4.5-alt1
- 4.5

* Fri Feb 29 2008 Victor Forsyuk <force@altlinux.org> 4.4-alt2
- Add package with GUI to uni2ascii and ascii2uni - u2a.

* Mon Feb 25 2008 Victor Forsyuk <force@altlinux.org> 4.4-alt1
- Initial build.
