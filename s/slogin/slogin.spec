Name: slogin
Version: 1.0
Release: alt1

Summary: Simple login
License: GPL-2.0-or-later
Group: System/Base

URL: https://github.com/legionus/slogin

Source: %name-%version.tar

%define _unpackaged_files_terminate_build 1

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-Authen-PAM
BuildRequires: perl-Curses
BuildRequires: perl-Encode
BuildRequires: perl-devel

%description
Implementation of login in perl. The login utility works a lot with strings. The
main goal of the implementation is to minimize the possibility of memory errors.

%prep
%setup -q
%autopatch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/slogin
%perl_vendor_archlib/LIBC_XS.pm
%perl_vendor_autolib/LIBC_XS/LIBC_XS.so

%changelog
* Sun Aug 13 2023 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- First release.

