%define  srcname svglib

#def_disable check

Name:    python3-module-%srcname
Version: 1.1.0
Release: alt1

Summary: Read SVG files and convert them to other formats
License: LGPL-3.0-or-later
Group:   Development/Python3
URL:     https://github.com/deeplook/svglib

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools

%if_disabled check
%else
BuildRequires: python3-module-pytest
BuildRequires: python3-module-Reportlab
BuildRequires: python3-module-cssselect2
BuildRequires: python3-module-lxml
%endif

BuildArch: noarch

# Source-url: https://github.com/deeplook/svglib/archive/refs/tags/v%version.tar.gz
Source: %srcname-%version.tar

%description
Svglib is a pure-Python library for reading SVG files and converting
them (to a reasonable degree) to other formats using the ReportLab
Open Source toolkit.

Used as a package you can read existing SVG files and convert them
into ReportLab Drawing objects that can be used in a variety of
contexts, e.g. as ReportLab Platypus Flowable objects or in RML.
As a command-line tool it converts SVG files into PDF ones (but
adding other output formats like bitmap or EPS is really easy
and will be better supported, soon).

Tests include a huge W3C SVG test suite plus ca. 200 flags from
Wikipedia and some selected symbols from Wikipedia (with
increasingly less pointing to missing features).

%package -n svg2pdf
Summary: Convert svg to pdf
Group: File tools
BuildArch: noarch

%description -n svg2pdf
Convert svg to pdf.
This part %name.

%prep
%setup -n %srcname-%version

%build
%python3_build

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -v -k "not TestWikipediaFlags and not TestW3CSVG"

%install
%python3_install

%files
%python3_sitelibdir/*
%doc *.rst *.txt

%files -n svg2pdf
%_bindir/svg2pdf
%_man1dir/*.1.*

%changelog
* Fri Jul 30 2021 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
