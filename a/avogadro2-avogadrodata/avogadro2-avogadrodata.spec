%define _unpackaged_files_terminate_build 1

Name: avogadro2-avogadrodata
Version: 2.1.0
Release: alt1

Summary: Test data files for Avogadro2 libraries
Group: Sciences/Chemistry
License: BSD-3-Clause
URL: https://avogadro.cc/
VCS: https://github.com/OpenChemistry/avogadrodata

Source: %name-%version.tar
BuildArch: noarch

%description
This package contains data and test files used by the upstream Avogadro2
unit tests: reference molecules, valid and invalid file format samples,
and baseline files. It is required at build time of avogadro2-libs when
tests are enabled.

# Test and data helper scripts are inputs for the upstream test suite,
# not runnable dependencies of this package.
%add_findreq_skiplist %_datadir/avogadro2/avogadrodata/*
%add_findprov_skiplist %_datadir/avogadro2/avogadrodata/*

%prep
%setup

%install
mkdir -p %buildroot%_datadir/avogadro2/avogadrodata
cp -a .avogadro.data README.md baselines data tests \
  %buildroot%_datadir/avogadro2/avogadrodata/

%files
%_datadir/avogadro2/avogadrodata

%changelog
* Wed Nov 11 2026 Valentin Sokolov <sova@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus.
