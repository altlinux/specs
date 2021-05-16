Name: python3-module-sphinxcontrib-aafig
Version: 1.2.0
Release: alt1
License: ALT-Public-Domain
Source: sphinxcontrib-aafig-%version.tar.gz
Group: Development/Python3
BuildArch: noarch
Summary: Aafigure support for sphinx

%description
This package contains the aafigure Sphinx extension.

aafigure is a program and a reStructuredText directive to allow embeded
ASCII art figures to be rendered as nice images in various image
formats. The aafigure directive needs a hardcoded image format, so it
doesn't goes well with Sphinx multi-format support.

This extension adds the aafig directive that automatically selects the
image format to use acording to the Sphinx writer used to generate the
documentation.

%prep
%setup -n sphinxcontrib-aafig-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/sphinxcontrib/*
%python3_sitelibdir_noarch/sphinxcontrib_*

%changelog
* Sun May 16 2021 Fr. Br. George <george@altlinux.ru> 1.2.0-alt1
- Autobuild version bump to 1.2.0

* Sun May 16 2021 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Initial build foir ALT
