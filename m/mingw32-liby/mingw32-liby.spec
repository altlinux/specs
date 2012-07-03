Name: mingw32-liby
Version: 2.4.1
Release: alt1
Summary: A GNU general-purpose parser generator (MinGW static library)

License: GPLv3
Group: System/Libraries
Url: http://www.gnu.org/software/bison/

Packager: Fr. Br. George <george@altlinux.ru>

Source: http://ftp.gnu.org/gnu/bison/bison-%version.tar.bz2
BuildArch: noarch

BuildRequires: rpm-build-mingw32
#BuildRequires: mingw32-gcc
#BuildRequires: mingw32-binutils

# Automatically added by buildreq on Tue Oct 20 2009
BuildRequires: flex mingw32-gettext

%description
A library needed for MinGW cross-compiling Bison and YACC based software

%prep
%setup -q -n bison-%version
rpmquery --queryformat "%%DESCRIPTION\n" bison > README.bison

%build
%_mingw32_configure --enable-static
%make_build -C lib liby.a

%install
install -D lib/liby.a  %buildroot%_mingw32_libdir/liby.a

%files
%doc README.bison
%_mingw32_libdir/liby.a

%changelog
* Wed Oct 21 2009 Fr. Br. George <george@altlinux.ru> 2.4.1-alt1
- Initial build

