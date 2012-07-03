Name: mingw32-libfl
Version: 2.5.35
Release: alt1
Summary: A fast lexical analyzer generator (MinGW static library and header)

License: BSD-style
Group: System/Libraries
Url: http://flex.sourceforge.net/
Packager: Fr. Br. George <george@altlinux.ru>

Source: http://prdownloads.sourceforge.net/flex/flex-%version.tar.gz
BuildArch: noarch

BuildRequires: rpm-build-mingw32
#BuildRequires: mingw32-gcc
#BuildRequires: mingw32-binutils

# Automatically added by buildreq on Tue Oct 20 2009
BuildRequires: flex mingw32-gettext

%description
Libraries ane header file needed for MinGW cross-compiling flex based software

%prep
%setup -q -n flex-%version
rpmquery --queryformat "%%DESCRIPTION\n" flex > README.flex

%build
%_mingw32_configure --enable-static
%make_build libfl.a libfl_pic.a

%install
install -D libfl.a  %buildroot%_mingw32_libdir/libfl.a
install -D libfl_pic.a  %buildroot%_mingw32_libdir/libfl_pic.a
ln -s libfl.a %buildroot%_mingw32_libdir/libl.a
install -D FlexLexer.h %buildroot%_mingw32_includedir/FlexLexer.h

%files
%doc README.flex
%_mingw32_libdir/lib*.a
%_mingw32_includedir/FlexLexer.h


%changelog
* Wed Oct 21 2009 Fr. Br. George <george@altlinux.ru> 2.5.35-alt1
- Initial build 

