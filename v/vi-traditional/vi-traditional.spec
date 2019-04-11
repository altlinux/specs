Summary: A port of the traditional ex/vi editors
Name: vi-traditional
Version: 4.1.3
Epoch: 0
Release: alt1
License: BSD
Source: ex-%version.tar.bz2
Group: Editors
#Url: http://ex-vi.sourceforge.net
Url: https://github.com/n-t-roff/heirloom-ex-vi

BuildRequires: libncursesw-devel

%description
This is a port of the traditional ex and vi editor implementation as
found on 2BSD and 4BSD. It was enhanced to support most of the additions
in System V and POSIX.2, and international character sets like UTF-8 and
many East Asian encodings.

%prep
%setup -n ex-%version

%build
./configure
%make_build PREFIX=%prefix

%install
make PREFIX=%buildroot%prefix install


%files
%doc Changes LICENSE README TODO
%_bindir/*
%exclude %_bindir/wvi
%_prefix/libexec/ex*
%_man1dir/*
%exclude %_man1dir/wvi*

%changelog
* Thu Apr 11 2019 Fr. Br. George <george@altlinux.ru> 0:4.1.3-alt1
- New upstream

* Wed Jan 30 2019 Fr. Br. George <george@altlinux.ru> 050325-alt1
- Initial build for ALT (at last!)

