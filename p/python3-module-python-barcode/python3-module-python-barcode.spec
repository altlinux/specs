
%define base_name python-barcode
Name: python3-module-%base_name
Version: 0.13.1
Release: alt1
Summary: Library to create Barcodes with Python
License: MIT
Group: Development/Python3
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: https://github.com/WhyNotHugo/python-barcode
Source: https://files.pythonhosted.org/packages/source/p/%base_name/%base_name-%version.tar.gz
BuildRequires: fonts-ttf-dejavu python3-module-pip python3-module-setuptools_scm
BuildRequires: rpm-build-python3 python3-module-setuptools rpm-macros-python3 pyproject-build  python3-module-build
Requires: fonts-ttf-dejavu
BuildArch: noarch

%description
Library to create standard barcodes with Python. No external modules needed (optional PIL support included).

%prep
%setup -n %base_name-%version
# Fix rpmlint warning about too many +x perms when these files get installed later.
find . -type f -exec chmod a-x {} +
# doc buildscripts we don't wanna ship
rm docs/Makefile

%build
%python3_build

%install
%python3_install

#find %buildroot -type f -name "*.ttf" | while read i; do
#	ln -fs "%_datadir/fonts/truetype/${i##*/}" "$i"
#done

#check
#sed -i '/cov/d' setup.cfg
#pytest


%files
%doc docs/*
%python3_sitelibdir/barcode
%python3_sitelibdir/python_barcode-%version-py?.??.egg-info
%_bindir/python-barcode


%changelog
* Thu May 12 2022 Ilya Mashkin <oddity@altlinux.ru> 0.13.1-alt1
- Build for Sisyphus

* Mon Oct 26 2020 Steve Kowalik <steven.kowalik@suse.com>
- Update to 0.13.1:
  * Fix a crash when using the generate shortcut function.
  * Added support for transparent backgrounds. This is done by setting the
    mode option for a writer to RGBA.
  * Removed writer_options from barcode.get. This parameter was not used.
  * Add a with_doctype flag to SVGWriter. Set this to false to avoid including
    a DOCTYPE in the resulting SVG.
  * Add support for Pillow>=8.0.0.
* Wed May 20 2020 Petr Gajdos <pgajdos@suse.com>
- %%python3_only -> %%python_alternative
* Mon Mar 23 2020 Tomáš Chvátal <tchvatal@suse.com>
- Remove tests folder that was installed in sitelib
* Fri Mar 20 2020 pgajdos@suse.com
- version update to 0.11.0
  * Added basic support for multiline text.
  * Dropped lots of older compat-only code and other cleanups.
  * Fixed a bug in the API when combining certain barcodes and writers.
  * Published documentation again and updated all project references.
  * Fix python_barcode.get mixups between options as writer_options. Previously, some writer/barcode combinations worked fine, while others failed. Now all work consistently.
  * The cli tool has been fixed and should now work as expected again.
* Sat May 25 2019 Tomáš Chvátal <tchvatal@suse.com>
- Update to 0.10.0:
  * Various minor fixes and tweaks
  * CI integration fixes
* Sat Apr  6 2019 Jan Engelhardt <jengelh@inai.de>
- Unbundle DejaVu font and reuse the one from the system.
* Thu Apr  4 2019 Tomáš Chvátal <tchvatal@suse.com>
- Provide and obsolete pyBarcode as we are fork of it
* Wed Apr  3 2019 Tomáš Chvátal <tchvatal@suse.com>
- Run the spec-cleaner
* Mon Mar 25 2019 Axel Braun <axel.braun@gmx.de>
- Verion 0.9 of python-barcode (fork of pyBarcode)
  initial OBS build
