Name: histring
Version: 1.1.0
Release: alt1
License: GPL2
Group: Text tools
Url: git://git.grml.org/histring.git
Summary: highlight strings using ANSI terminal escape sequences
Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: %name-%version.tar

%description
highlight strings using ANSI terminal escape sequences
histring simply highlights strings using ANSI terminal escape codes.
It is very useful for example for parsing output of grep and diff.ess4.engr.uvic.ca

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
mkdir -p %buildroot%_man1dir
install -m644 debian/histring.1 %buildroot%_man1dir

%files
%_bindir/histring
%_man1dir/histring.1*
%doc README

%changelog
* Sat Sep 26 2009 Ildar Mulyukov <ildar@altlinux.ru> 1.1.0-alt1
- 1st version for Sisyphus
