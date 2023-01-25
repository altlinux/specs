# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name:    universal-ctags
Version: 6.0.0
Release: alt1
Epoch:   1

Summary: Universal Ctags generates an index of language objects found in source
License: GPL-2.0-only
Group:   Development/Other
Url:     https://ctags.io/
Vcs:     https://github.com/universal-ctags/ctags.git
# Docs:  https://docs.ctags.io
Conflicts: ctags < %EVR
Provides:  ctags = %EVR

Source: %name-%version.tar
BuildRequires: libjansson-devel
BuildRequires: libseccomp-devel
BuildRequires: libxml2-devel
BuildRequires: libyaml-devel
BuildRequires: python3-module-docutils

%description
Universal Ctags generates an index (or tag) file of language objects
found in source files for many popular programming languages. This index
makes it easy for text editors and other tools to locate the indexed
items. Universal Ctags improves on traditional ctags because of its
multilanguage support, its ability for the user to define new languages
searched by regular expressions, and its ability to generate emacs-style
TAGS files.

universal-ctags has the objective of continuing the development from
what existed in the Sourceforge area. Github exuberant-ctags repository
was started by Reza Jelveh and was later moved to the universal-ctags
organization.

The goal of the project is preparing and maintaining common/unified
working space where people interested in making ctags better can work
together.

%prep
%setup
# Seems, developer-only test requiring git.
sed -i '/check:/s/check-genfile//' makefiles/testing.mak

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%define _customdocdir %_docdir/%name

%check
./ctags --version
%make_build check

%files
%doc COPYING README.md docs/*.rst docs/*.svg
%_bindir/ctags
%_bindir/readtags
%_bindir/optscript
%_man1dir/ctags.1*
%_man1dir/readtags.1*
%_man5dir/tags.5*
%_man5dir/ctags-json-output.5*
%_man7dir/ctags-*.7*

%changelog
* Thu Jan 26 2023 Vitaly Chikunov <vt@altlinux.org> 1:6.0.0-alt1
- Update to v6.0.0 (2022-12-16).

* Thu Oct 21 2021 Vitaly Chikunov <vt@altlinux.org> 1:5.9.20211017.0-alt1
- Update to p5.9.20211017.0.

* Tue Oct 12 2021 Vitaly Chikunov <vt@altlinux.org> 1:5.9.20211010.0-alt1
- Update to p5.9.20211010.0. (Also fixes seccomp rules for glibc-2.34).

* Fri Nov 20 2020 Vitaly Chikunov <vt@altlinux.org> p5.9.20201115.0-alt2
- Add conflict with ctags.

* Thu Nov 19 2020 Vitaly Chikunov <vt@altlinux.org> p5.9.20201115.0-alt1
- Initial import of p5.9.20201115.0 (updates: 39176).
