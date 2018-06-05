%define  pkgname ISO8601

Name:    ruby-iso8601
Version: 0.10.1
Release: alt1

Summary: Ruby parser to work with ISO8601 dateTimes and durations (http://en.wikipedia.org/wiki/ISO_8601)
License: MIT
Group:   Development/Ruby
Url:     https://github.com/arnau/ISO8601

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

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

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.10.1-alt1
- Initial build for Sisyphus
