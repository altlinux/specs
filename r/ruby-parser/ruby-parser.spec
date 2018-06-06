Name:    ruby-parser
Version: 3.11.0
Release: alt1

Summary: ruby_parser (RP) is a ruby parser written in pure ruby
License: MIT
Group:   Development/Ruby
Url:     https://github.com/seattlerb/ruby_parser

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  ruby_parser-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: ruby-hoe
BuildRequires: ruby-racc
BuildRequires: ruby-sexp-processor
BuildRequires: unifdef

%description
ruby_parser (RP) is a ruby parser written in pure ruby (utilizing
racc-which does by default use a C extension). RP's output is the same
as ParseTree's output: s-expressions using ruby's arrays and base types.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n ruby_parser-%version
%update_setup_rb

%build
%ruby_config
rake repackage
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%_bindir/*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.0-alt1
- Initial build for Sisyphus
