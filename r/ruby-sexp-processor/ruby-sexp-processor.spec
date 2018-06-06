%define  pkgname sexp_processor

Name:    ruby-sexp-processor
Version: 4.11.0
Release: alt1

Provides: ruby-%pkgname = %EVR

Summary: sexp_processor branches from ParseTree bringing all the generic sexp processing tools with it
License: MIT
Group:   Development/Ruby
Url:     https://github.com/seattlerb/sexp_processor

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
sexp_processor branches from ParseTree bringing all the generic sexp
processing tools with it. Sexp, SexpProcessor, Environment, etc... all for
your language processing pleasure.

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

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 4.11.0-alt1
- Initial build for Sisyphus
