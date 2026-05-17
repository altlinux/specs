Name:           pology
Version:        0.13
Release:        alt1.77c0872.1
Summary:        Pology is a Python library and collection of command-line tools for in-depth processing of PO files

License:        GPL-3.0-or-later
Group:          Development/Tools
URL:            https://invent.kde.org/sdk/pology 
VCS:            https://github.com/KDE/pology
Source0:        %name-%version.tar

BuildRequires(pre): cmake
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  libxml2-devel
BuildRequires:  python3-devel
BuildRequires:  xmllint
BuildRequires:  xsltproc

%description
Pology is a Python library and collection of command-line tools for
in-depth processing of PO files, the translation file format of the
GNU Gettext software translation system. Pology functionality ranges
from precision operations on individual PO messages, to cross-file
operations on large collections of PO files.

%prep
%setup -q
# Set correct python2 executable in shebang
#subst 's|#!.*python$|#!%__python3|' $(grep -Rl '#!.*python$' *.py)

%build
%cmake -DPYTHON3_PACKAGES_DIR:PATH=%{python3_sitelibdir}
%cmake_build -j1

%install
%cmake_install

%find_lang %name

%files -f %name.lang
%doc NEWS README.rst TODO
%doc %_datadir/doc/%name
%_bindir/*
%_datadir/%name
%python3_sitelibdir/%name

%changelog
* Sun May 17 2026 Anton Midyukov <antohami@altlinux.org> 0.13-alt1.77c0872.1
- New snapshot with python3 support (Closes: 59224).

* Sat Jul 24 2021 Grigory Ustinov <grenka@altlinux.org> 0.12-alt2.2
- NMU: fixed BuildRequires.

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 0.12-alt2.1
- NMU: spec: adapted to new cmake macros.

* Tue Apr 14 2020 Andrey Cherepanov <cas@altlinux.org> 0.12-alt2
- Set correct python2 executable in shebang.

* Tue Nov 29 2016 Andrey Cherepanov <cas@altlinux.org> 0.12-alt1
- New version

* Fri Mar 16 2012 Andrey Cherepanov <cas@altlinux.org> 0.10-alt1
- Initial build in Sisyphus

