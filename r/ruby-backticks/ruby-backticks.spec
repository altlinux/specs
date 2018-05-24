%define  pkgname backticks

Name:    ruby-%pkgname
Version: 1.0.2
Release: alt1

Summary: Intuitive OOP wrapper for command-line processes; uses PTY to avoid buffering.
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/xeger/backticks

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
* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
