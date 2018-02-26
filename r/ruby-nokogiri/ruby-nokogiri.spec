# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname nokogiri

Name: ruby-%pkgname
Version: 1.4.4.2
Release: alt2

Summary: HTML, XML, SAX, and Reader parser
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/nokogiri/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch1: ruby-nokogiri-1.4.4.2-alt-Drop-FFI-support.patch
Patch2: ruby-nokogiri-1.4.4.2-alt-Fix_encoding_issues.patch
Patch3: ruby-nokogiri-1.4.4.2-alt-rubygems.patch
Patch4: ruby-nokogiri-1.4.4.2-alt-libxml.patch

# Automatically added by buildreq on Sun Jun 28 2009 (-bi)
BuildRequires: libruby-devel libxslt-devel ruby-racc-runtime ruby-test-unit ruby-tool-setup
BuildRequires: ruby-minitest
BuildRequires: ruby-racc
BuildRequires: ruby-rexical
BuildRequires: libxml-ruby

%description
Nokogiri parses and searches XML/HTML very quickly, and also has
correctly implemented CSS3 selector support as well as XPath support.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
# Not needed.
rm -r lib/nokogiri/ffi
%update_setup_rb

%build
%ruby_config
%ruby_build

# XXX@stanv: next lines are taken from Rakefile:
racc -l -o lib/nokogiri/css/generated_parser.rb lib/nokogiri/css/parser.y
rex --independent -o lib/nokogiri/css/generated_tokenizer.rb lib/nokogiri/css/tokenizer.rex

###ruby_test_unit -I. -Ilib:ext:test test
%ruby_vendor -Ilib:ext:test setup.rb test


%install
%ruby_install
%rdoc lib/

%files
%doc README.rdoc
%_bindir/*
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%files doc
%ruby_ri_sitedir/Nokogiri*

%changelog
* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.4.4.2-alt2
- Fix build

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.4.4.2-alt1
- [1.4.4.2]

* Wed Mar 17 2010 Timur Batyrshin <erthad@altlinux.org> 1.4.0-alt1
- [1.4.0]

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.3.2-alt1
- [1.3.2]

* Thu Sep 25 2008 Grigory Batalov <bga@altlinux.ru> 1.1.0-alt1
- Initial build for ALT Linux.

