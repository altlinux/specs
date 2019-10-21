Name: econnman
Version: 1.1
Release: alt5

Summary: Enlightenment Connection Manager
License: BSD
Group: Graphical desktop/Enlightenment
URL: http://www.enlightenment.org/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-base python3-devel
BuildRequires: efl-libs-devel

Requires: connman python3-module-efl


%description
Enlightenment connection manager frontend.

%prep
%setup -q

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '%name-bin*')

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
* Mon Oct 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1-alt5
- python2 -> python3

* Sat Oct 19 2019 Anton Midyukov <antohami@altlinux.org> 1.1-alt4
- rebuild

* Tue Dec 24 2013 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt3
- Depend on python-module-efl.

* Thu Dec 12 2013 Paul Wolneykien <manowar@altlinux.org> 1.1-alt2
- Fix the version pattern in the cronbuild script.

* Wed Dec 11 2013 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt1
- Freshed up to v1.1 with the help of cronbuild and update-source-functions.

* Tue Jan 22 2013 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt2
- Require connman explicitly.

* Thu Jan 17 2013 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt1
- Initial build for ALT Linux Sisyphus.
