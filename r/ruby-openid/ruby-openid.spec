Name:    ruby-openid
Version: 2.8.0
Release: alt1

Summary: OpenID library for Ruby
License: MIT/Ruby and Apache 2.0
Group:   Development/Ruby
Url:     https://github.com/openid/ruby-openid

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
# For tests
BuildRequires: ruby-bundler

%filter_from_requires /^ruby(hmac-sha/d

%description
A Ruby library for verifying and serving OpenID identities.

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
LANG=en_US.UTF-8 %ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- Initial build for Sisyphus
