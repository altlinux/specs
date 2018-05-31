%define  pkgname paint

Name:    ruby-%pkgname
Version: 2.0.1
Release: alt1

Summary: Ruby gem for ANSI terminal colors
License: MIT
Group:   Development/Ruby
Url:     https://github.com/janlelis/paint

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Paint creates terminal colors and effects for you. It combines the
strengths of term-ansicolor, rainbow, and similar projects into a simple
to use, however still flexible terminal colors gem with no core
extensions by default.

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
%_datadir/rgb_colors.marshal.gz

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus
