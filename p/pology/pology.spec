Name:           pology
Version:        0.10
Release:        alt1
Summary:        Pology is a Python library and collection of command-line tools for in-depth processing of PO files

License:        GPLv3+
Group:          Development/Tools
URL:            http://pology.nedohodnik.net/

Packager:       Andrey Cherepanov <cas@altlinux.org>

Source0:        http://pology.nedohodnik.net//release/%{name}-%{version}.tar.bz2

BuildRequires(pre): cmake
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  libxml2-devel
BuildRequires:  python-devel
BuildRequires:  python-module-distribute
BuildRequires:  python-module-epydoc
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

%build
%cmake -DPYTHON2_PACKAGES_DIR:PATH=%{python_sitelibdir}

%install
pushd BUILD
%makeinstall_std
popd

%find_lang %name

%files -f %name.lang
%doc NEWS README TODO
%doc %_datadir/doc/%name
%_bindir/*
%_datadir/%name
%python_sitelibdir/%name

%changelog
* Fri Mar 16 2012 Andrey Cherepanov <cas@altlinux.org> 0.10-alt1
- Initial build in Sisyphus

