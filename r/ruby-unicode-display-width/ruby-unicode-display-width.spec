%define  pkgname unicode-display_width

Name:    ruby-unicode-display-width
Version: 1.4.0
Release: alt1

Summary: Monospace Unicode character width in Ruby
License: MIT
Group:   Development/Ruby
Url:     https://github.com/janlelis/unicode-display_width

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar
Patch:   alt-fix-datadir.patch

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
%patch -p1
%update_setup_rb

%build
%ruby_config --datadir=%_datadir/%name
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%files
%doc README*
%ruby_sitelibdir/*
%_datadir/%name

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
