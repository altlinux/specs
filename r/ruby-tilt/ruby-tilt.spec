%define  pkgname tilt

Name: 	 ruby-%pkgname
Version: 2.0.7 
Release: alt1

Summary: Generic interface to multiple Ruby template engines
License: MIT
Group:   Development/Ruby
Url:     http://github.com/rtomayko/tilt

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(\(asciidoctor\|erubi\|erubis\|haml\|less\|sass\|builder\|liquid\|rdiscount\|redcarpet\|bluecloth\|kramdown\|pandoc-ruby\|rdoc.*\|maruku\|commonmarker\|redcloth\|radius\|markaby\|nokogiri\|coffee_script\|livescript\|typescript-node\|creole\|wikicloth\|yajl\|fastercsv\|prawn\|babel\/transpiler\))/d

%description
Tilt is a thin interface over a bunch of different Ruby template engines in an
attempt to make their usage as generic as possible. This is useful for web
frameworks, static site generators, and other systems that support multiple
template engines but don't want to code for each of them individually.

The following features are supported for all template engines (assuming the
feature is relevant to the engine):
* Custom template evaluation scopes / bindings
* Ability to pass locals to template evaluation
* Support for passing a block to template evaluation for "yield"
* Backtraces with correct filenames and line numbers
* Template file caching and reloading
* Fast, method-based template source compilation

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

# Move man page to appropriate place
mkdir -p %buildroot%_man1dir
mv %buildroot%_mandir/%pkgname.1.ronn %buildroot%_man1dir/%pkgname.1
rm -f %buildroot%_mandir/index.txt

%check
%ruby_test_unit -Ilib:test test

%files
%doc *.md
%_bindir/%pkgname
%ruby_sitelibdir/*
%_man1dir/%pkgname.1*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Jun 14 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.7-alt1
- Initial build for Sisyphus
