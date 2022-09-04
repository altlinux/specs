Name:     codetest_sl
Version:  1.6
Release:  alt1

Summary:  Steam locomotive
License:  ALT-Public-Domain
Group:    Games/Other

Url:      https://github.com/lambriggerbrian/codetest_sl.git
Source:   %name-%version.tar

BuildRequires: gcc-c++ libncurses-devel

%description
SL (Steam Locomotive) runs across your terminal when you type "sl" as you meant
to type "ls". It's just a joke command, and not useful at all.

%prep
%setup
subst 's|/opt/|/usr/share/|' ascii.cpp

%build
%make_build

%install
install -Dm 0755 sl %buildroot%_bindir/sl
install -Dm 0755 sl.1 %buildroot%_man1dir/sl.1
mkdir -p %buildroot%_datadir/sl/art
install -m 0755 art/* %buildroot%_datadir/sl/art

%files
%doc *.md LICENSE
%_bindir/*
%_man1dir/*
%_datadir/sl

%changelog
* Sat Sep 03 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.6-alt1
- Initial build for ALT.

