
Summary: Enlightenment Connection Manager
Name: econnman
Version: 1.0.0
Release: alt1
License: BSD
Group: Graphical desktop/Enlightenment
URL: http://www.enlightenment.org/
Source: %name-%version.tar

BuildRequires: python-module-elementary-devel, python-module-edbus-devel edje libedje-devel embryo_cc

BuildArch: noarch

%description
Enlightenment connection manager frontend.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build V=1


%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING README
%_bindir/*
%_datadir/applications/%{name}*.desktop
%_datadir/%name

%changelog

* Thu Jan 17 2013 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt1
- Initial build for ALT Linux Sisyphus.
