%define Name KeyLaunch
Name: keylaunch
Version: 1.3.9
Release: alt1
Summary: Small utility for binding commands to a hot key.
Summary(uk_UA.CP1251): ћаленька утил≥та дл€ призначенн€ командам "гар€чих клав≥ш"
Summary(ru_RU.CP1251): ћаленька€ утилита дл€ назначени€ командам "гор€чих клавиш"
License: GPL
Group: Graphical desktop/Other
URL: http://www.oroborus.org/
Source: %{name}_%version.tar.bz2

# Automatically added by buildreq on Fri Jun 16 2006
BuildRequires: libSM-devel libX11-devel xorg-cf-files

%description
%Name is a small utility for binding commands to a hot key.

%description -l uk_UA.CP1251
%Name - маленька утил≥та дл€ призначенн€ командам "гар€чих клав≥ш".

%description -l ru_RU.CP1251
%Name - маленька€ утилита дл€ назначени€ командам "гор€чих клавиш".



%prep
%setup -n %name-%version
subst 's/\r//g' README


%build
%configure \
	--with-x
%make_build


%install
%make_install DESTDIR=%buildroot install
rm -rf %buildroot%_docdir/%name
gzip --best --stdout -- debian/changelog > changelog.gz


%files
%doc README docs/example_rc changelog.*
%_bindir/*
%_man1dir/*


%changelog
* Tue Sep 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.9-alt1
- Version 1.3.9

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.3-alt1.qa1
- NMU: rebuilt for updated dependencies.

* Fri Jun 16 2006 Led <led@altlinux.ru> 1.3.3-alt1
- initial build
