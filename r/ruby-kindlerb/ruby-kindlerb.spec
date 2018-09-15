%define  pkgname kindlerb

Name:    ruby-%pkgname
Version: 1.2.0
Release: alt1

Summary: Kindle periodical format ebook generation tool
License: MIT
Group:   Development/Ruby
Url:     https://github.com/danchoi/kindlerb

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
kindlerb is a Ruby Kindle periodical-format ebook generator. This tool
was initially extracted from kindlefeeder.com. Kindlefodder was also
built on top of kindlerb. kindlerb converts a file tree of sections,
articles, images, and metadata into a MOBI periodical-formatted document
for the Kindle. It is a wrapper around the kindlegen program from Amazon
that hides the details for templating OPF and NCX files.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%update_setup_rb
echo "gemspec" >> Gemfile

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
%_bindir/setupkindlerb
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
