
Summary: Enlightenment Connection Manager
Name: econnman
Version: 1.1
Release: alt2
License: BSD
Group: Graphical desktop/Enlightenment
URL: http://www.enlightenment.org/
Source: %name-%version.tar

Requires: connman

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-base python3-devel
BuildRequires: efl-libs-devel

BuildArch: noarch

%description
Enlightenment connection manager frontend.

%prep
%setup -q

%build
%autoreconf
export PYTHON=/usr/bin/python3
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
* Thu Dec 12 2013 Paul Wolneykien <manowar@altlinux.org> 1.1-alt2
- Fix the version pattern in the cronbuild script.

* Wed Dec 11 2013 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt1
- Freshed up to v1.1 with the help of cronbuild and update-source-functions.

* Tue Jan 22 2013 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt2
- Require connman explicitly.

* Thu Jan 17 2013 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt1
- Initial build for ALT Linux Sisyphus.
