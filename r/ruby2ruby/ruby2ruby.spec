Name:    ruby2ruby
Version: 2.4.1
Release: alt1

Summary: ruby2ruby provides a means of generating pure ruby code easily from RubyParser compatible Sexps
License: MIT
Group:   Development/Ruby
Url:     https://github.com/seattlerb/ruby2ruby

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
# For tests
BuildRequires: ruby-sexp-processor
BuildRequires: ruby-parser

%description
ruby2ruby provides a means of generating pure ruby code easily from
RubyParser compatible Sexps. This makes making dynamic language
processors in ruby easier than ever!

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %name-%version
%update_setup_rb

%build
%ruby_config
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
%_bindir/r2r_show
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1
- Initial build for Sisyphus
