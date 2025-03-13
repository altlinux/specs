%define srcname ocrmypdf
%def_without docs

Name: ocrmypdf
Version: 16.10.0
Release: alt1

Summary: Add an OCR text layer to scanned PDF files

License: MPL-2.0 AND Zlib
Group: Office
Url: https://github.com/ocrmypdf/OCRmyPDF

# Source-url: %__pypi_url %srcname
Source: %name-%version.tar

# We drop pi-heif for now, as it is optional.
Patch1: 0001-Remove-unnecessary-dependencies.patch

BuildArch: noarch

#ExcludeArch: %ix86

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs


BuildRequires: ghostscript >= 9.50
BuildRequires: %_bindir/pdftotext
BuildRequires: pngquant >= 2.0.0
BuildRequires: tesseract >= 4.1.1
BuildRequires: tesseract-langpack-osd
#BuildRequires: tesseract-langpack-deu
BuildRequires: unpaper >= 6.1
BuildRequires: python3-devel

Requires: ghostscript >= 9.15
#Recommends:     pngquant >= 2.0.0
Requires: tesseract >= 4.1.1
Requires:     unpaper >= 6.1

%description
OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be
searched or copy-pasted.

%package doc
Summary: ocrmypdf documentation
License: CC-BY-SA-4.0
Group: Development/Documentation

%description doc
Documentation for ocrmypdf

%prep
%setup
%patch1 -p1

subst 's|/usr/bin/env python$|/usr/bin/env python3|' misc/webservice.py

# Cleanup shebang and executable bits.
for f in src/%srcname/*.py src/%srcname/*/*.py; do
    sed -e '1{\@^#!%_bindir/env python@d}' $f > $f.new &&
    touch -r $f $f.new &&
    mv $f.new $f
    chmod -x $f
done

%build
%pyproject_build

%if_with docs
# generate html docs
PYTHONPATH="$PWD/build/lib" OCRMYPDF_VERSION="%version" sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rfv html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

# Install completion files.
install -Dpm 0644 misc/completion/ocrmypdf.bash %buildroot%_datadir/bash-completion/completions/ocrmypdf
install -Dpm 0644 misc/completion/ocrmypdf.fish %buildroot%_datadir/fish/vendor_completions.d/ocrmypdf.fish

# Install optional programs.
install -Dpm 0755 misc/watcher.py %buildroot%_bindir/%srcname-watcher
install -Dpm 0755 misc/webservice.py %buildroot%_bindir/%srcname-webservice

%check
k="${k-}${k+ and }not test_tesseract_config_invalid"

#pytest -ra -n auto --runslow -k "${k-}"

%files
%doc README.md LICENSE
%_bindir/ocrmypdf
%_bindir/ocrmypdf-watcher
%_bindir/ocrmypdf-webservice
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-%version.dist-info/
%_datadir/bash-completion/completions/ocrmypdf
%dir %_datadir/fish
%dir %_datadir/fish/vendor_completions.d
%_datadir/fish/vendor_completions.d/ocrmypdf.fish

%if_with docs
%files doc
%doc html
%doc LICENSE
%endif

%changelog
* Wed Mar 12 2025 Vitaly Lipatov <lav@altlinux.ru> 16.10.0-alt1
- new version 16.10.0 (with rpmrb script)

* Sun Dec 22 2024 Vitaly Lipatov <lav@altlinux.ru> 16.7.0-alt1
- initial build for ALT Sisyphus
