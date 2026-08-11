%define _unpackaged_files_terminate_build 1
%define _pkgdocdir %_docdir/%name

Name: beakerlib
Version: 1.33.3
Release: alt1
Summary: BeakerLib is a shell-level integration testing library
License: GPL-2.0
Group: Development/Other
Url: https://github.com/beakerlib/beakerlib
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: perl-podlators
BuildRequires: perl-Pod-Markdown
BuildRequires: python3(sphinx)
BuildRequires: python3-module-myst-parser
BuildRequires: python3-module-sphinx_design
BuildRequires: python3-module-sphinx-togglebutton
BuildRequires: python3(breathe)
BuildRequires: python3(furo)
BuildRequires: python3-module-accessible-pygments
BuildRequires: python3(Pygments)

%description
BeakerLib is a shell-level integration testing library

%prep
%setup -q

%build
%make_build
PYTHONPATH=${PWD} sphinx-build-3 doc html
rm -rf html/.{doctrees,buildinfo}

%install
mkdir -p %buildroot%_prefix
%make_install install DD=%buildroot%_prefix
%python3_fix_shebang %buildroot%_bindir

%files
%doc README.md
%_pkgdocdir/LICENSE
%_pkgdocdir/MAINTENANCE
%_pkgdocdir/README
%_pkgdocdir/VERSION
%_pkgdocdir/testwatcher.txt
%doc html/
%_datadir/%name
%_datadir/vim/vimfiles/after/
%_mandir/man1/beakerlib*.1*
%_pkgdocdir/examples/
%_bindir/%name-*

%changelog
* Tue Aug 11 2026 Pavel Shilov <zerospirit@altlinux.org> 1.33.3-alt1
- Initial build for Sisyphus.
