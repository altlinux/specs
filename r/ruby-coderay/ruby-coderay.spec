# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname coderay

Name: ruby-%pkgname
Version: 0.9.2
Release: alt2

Summary: Fast syntax highlighter engine
Group: Development/Ruby
License: LGPL
Url: http://rubyforge.org/projects/coderay/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version-trunk.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Wed Jul 29 2009 (-bi)
BuildRequires: libdb4-devel rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup ruby-json

%description
CodeRay is a Ruby library for syntax highlighting.
I try to make CodeRay easy to use and intuitive, but at the same time
fully featured, complete, fast and efficient.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
export nocolor=1
%ruby_config
%ruby_build
%ruby_test_unit sample/suite.rb
%ruby_test_unit test/functional/suite.rb
ruby test/scanners/suite.rb

%install
%ruby_install
%rdoc lib/

%files
%doc TODO
%_bindir/*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/CodeRay*

%changelog
* Mon Nov 29 2010 Alexey I. Froloff <raorn@altlinux.org> 0.9.2-alt2
- Fix build with Ruby 1.9.2

* Tue Apr 13 2010 Alexey I. Froloff <raorn@altlinux.org> 0.9.2-alt1
- [0.9.2]

* Sun Nov 08 2009 Alexey I. Froloff <raorn@altlinux.org> 0.9.0-alt0.r394.1
- Updated to r394 AKA 0.9.0rc2

* Wed Jul 29 2009 Alexey I. Froloff <raorn@altlinux.org> 0.9.0-alt0.r355.1
- Built for Sisyphus

