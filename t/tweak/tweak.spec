Name:		tweak
Version:	3.01
Release:	alt2
Summary:	An efficient hex editor
License:	MIT/X11
Group:		Development/Other
Source:		%name-%version.tar.gz
URL:		http://www.chiark.greenend.org.uk/~sgtatham/tweak/

# Automatically added by buildreq on Mon Aug 23 2010
BuildRequires: halibut libncurses-devel

%description
Tweak is a hex editor. It allows you to edit a file at very low level, letting
you see the full and exact binary contents of the file. It can be useful for
modifying binary files such as executables, editing disk or CD images,
debugging programs that generate binary file formats incorrectly, and many
other things.

%prep
%setup

%build
rm -f %name.1 btree.html
%make_build

%install
%makeinstall BINDIR=%buildroot%_bindir MANDIR=%buildroot%_man1dir

%files
%doc btree.html
%_bindir/*
%_man1dir/*


%changelog
* Wed Sep 01 2010 Fr. Br. George <george@altlinux.ru> 3.01-alt2
- Homepage URL added

* Mon Aug 23 2010 Fr. Br. George <george@altlinux.ru> 3.01-alt1
- Initial build for ALT

