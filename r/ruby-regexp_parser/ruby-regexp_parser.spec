%define  pkgname regexp_parser

Name:    ruby-%pkgname
Version: 1.2.0
Release: alt1

Summary: A regular expression parser library for Ruby
License: MIT
Group:   Development/Ruby
Url:     https://github.com/ammar/regexp_parser.git

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
%summary

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
mv %buildroot%_bindir/console %buildroot%_bindir/regexp-parser-console
mv %buildroot%_bindir/test %buildroot%_bindir/regexp-parser-test

%check
#%ruby_test_unit -Ilib:test test

%files
%doc README*
%_bindir/*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Oct 30 2018 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
