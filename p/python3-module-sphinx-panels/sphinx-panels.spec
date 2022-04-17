Name: python3-module-sphinx-panels
Version: 0.6.0
Release: alt1
License: MIT
Source: sphinx-panels-%version.tar.gz
Group: Development/Python3
BuildArch: noarch
Summary: A sphinx extension for creating document components optimised for HTML+CSS

# Automatically added by buildreq on Sun Apr 17 2022
# optimized out: libgpg-error python3 python3-base python3-dev python3-module-packaging python3-module-pep517 python3-module-pkg_resources python3-module-pyparsing python3-module-tomli sh4
BuildRequires: python3-module-build python3-module-flit python3-module-setuptools python3-module-wheel

%description
A sphinx extension for creating document components optimised for HTML+CSS.
 *  The panels directive creates panels of content in a grid layout,
    utilising both the Bootstrap 4 grid system, and cards layout.
 *  The link-button directive creates a click-able button, linking to
    a URL or reference, and can also be used to make an entire panel
    click-able.
 *  The dropdown directive creates toggle-able content.
 *  The tabbed directive creates tabbed content.
 *  opticon and fa (fontawesome) roles allow for inline icons to be added.

%prep
%setup -n sphinx-panels-%version

%build
python3 -m build -w -n

%install
pip3 install --no-deps --root=%buildroot -I dist/sphinx_panels*%{version}*.whl

%files
%python3_sitelibdir_noarch/*

%changelog
* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 0.6.0-alt1
- Autobuild version bump to 0.6.0

* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 0.5.2-alt2
- Initial release for ALT
