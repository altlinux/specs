%define ver_major 0.5

Name: eperiodique
Version: %ver_major
Release: alt1

Summary: A Periodic Table of Elements for Enlightenment
License: BSD
Group: Sciences/Chemistry
Url: http://%name.sourceforge.net

Source: http://sourceforge.net/projects/%name/files/%version/%name-%version.tar.bz2

BuildRequires: intltool libelementary-devel >= 1.8.0

%description
ePeriodique is a graphical application that display the periodic table
of the elements. It shows basic data for each element, pictures, Bohr
models and lattice structures.

%prep
%setup

%build
%autoreconf
%configure

%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/applications/*
%_datadir/%name/
%_iconsdir/%name.png
%_man1dir/%name.1*
%doc AUTHORS ChangeLog COPYING README TODO

%changelog
* Wed Jan 29 2014 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- first build for Sisyphus

