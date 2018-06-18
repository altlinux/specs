%define  pkgname ed25519

Name:    ruby-%pkgname
Version: 1.2.4
Release: alt1

Summary: Ruby library for the Ed25519 public-key signature system
License: MIT
Group:   Development/Ruby
Url:     https://github.com/crypto-rb/ed25519

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

%filter_from_requires /^ruby(ed25519_jruby)/d

%description
A Ruby binding to the Ed25519 elliptic curve public-key signature system
described in RFC 8032.

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
* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1
- Initial build for Sisyphus
