# vim: set ft=spec: -*- rpm-spec -*-

%define ruby_major 1.8
%define pkgname minitest

Name: ruby%{ruby_major}-%pkgname
Version: 2.0.0
Release: alt2

Summary: Small and fast replacement for ruby's huge and slow test/unit
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/bfts/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Fri Feb 06 2009 (-bi)
BuildRequires: ruby%{ruby_major}-stdlibs rpm-build-ruby ruby-tool-setup

%description
minitest/unit is a small and fast replacement for ruby's huge and slow
test/unit. This is meant to be clean and easy to use both as a regular
test writer and for language implementors that need a minimal set of
methods to bootstrap a working unit test suite.

mini/spec is a functionally complete spec engine.

mini/mock, by Steven Baker, is a beautifully tiny mock object framework.

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
for i in test/*; do
  %ruby_vendor -Ilib "$i"
done

%install
%ruby_install

%files
%doc History.txt README.txt
%ruby_sitelibdir/*

%changelog
* Tue Apr 12 2011 Timur Aitov <timonbl4@altlinux.org> 2.0.0-alt2
- Rebuild for ruby1.8

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 2.0.0-alt1
- [2.0.0]

* Tue Oct 13 2009 Kirill A. Shutemov <kas@altlinux.org> 1.4.2-alt1
- 1.4.2

* Wed May 06 2009 Alexey I. Froloff <raorn@altlinux.org> 1.3.1-alt2
- Rebuilt with ruby 1.9

* Fri Feb 06 2009 Sir Raorn <raorn@altlinux.ru> 1.3.1-alt1
- Built for Sisyphus

